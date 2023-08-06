import sqlite3
import re

from django.test.client import Client
from django.db import connections, DEFAULT_DB_ALIAS
from django.core import management

class TestResult(object):
    def __init__(self, path, succeeded, total):
        self.path = " > ".join(path)
        self.succeeded = succeeded
        self.total = total

    def __repr__(self):
        return "<TestResult %s: %d/%d>" % (self.path, self.succeeded, self.total)

    def __str__(self):
        return "%s: %d/%d" % (self.path, self.succeeded, self.total)

    @property
    def passed(self):
        return self.succeeded == self.total


class TestSet(tuple):
    def __rshift__(self, test_obj):
        return self.run(test_obj)

    def get_results(self):
        for test in self:
            if test.completed:
                result = TestResult(test.path, test.succeeded, test.total)
            else:
                test_cases = test.test_cases()
                test_case = next(test_cases)
                while True:
                    succeeded = test.succeeded + test.tmp_succeeded
                    total = test.total + test.tmp_total
                    result = TestResult(test.path, succeeded, total)
                    yield result
                    test.reset()

                    try:
                        test_case = next(test_cases)
                    except StopIteration:
                        break

    def __call__(self):
        test_set = []
        for test in self:
            if test.completed:
                result = TestResult(test.path, test.succeeded, test.total)
            else:
                test_cases = test.test_cases()
                test_case = next(test_cases)
                while True:
                    succeeded = test.succeeded + test.tmp_succeeded
                    total = test.total + test.tmp_total
                    client = test.client

                    wrapper = connections.all()[0]
                    schema = "".join(line for line in wrapper.connection.iterdump())

                    params = {
                            'client': client,
                            'succeeded': succeeded,
                            'total': total,
                            'path': test.path[:-1],
                            'schema': schema }

                    if not client:
                        params['completed'] = True

                    result = test.__class__(**params)
                    test_set.append(result)
                    test.reset()

                    try:
                        test_case = next(test_cases)
                    except StopIteration:
                        break

        return TestSet(test_set)

    def run(self, test_obj):
        results = []
        for test in self:
            if test.completed:
                results.append(test)
            else:
                for result in test >> test_obj:
                    results.append(result)

        return TestSet(results)


class Test(object):
    def __init__(self, client=None, succeeded=0, total=0, path=[],
            schema=None, completed=False, **kwargs):
        self.client = client
        self.succeeded = succeeded
        self.total = total
        self.tmp_total = 0
        self.tmp_succeeded = 0
        self.path = path[:]
        self.completed = completed
        self.schema = schema
        if not completed:
            self.path.append(self.name)

    def __rshift__(self, test_obj):
        if self.completed:
            return TestSet([self])
        else:
            results = []

            if not self.schema:
                connection = sqlite3.connect(":memory:")
                wrapper = connections.all()[0]
                wrapper.connection = connection
                wrapper.creation.create_test_db(verbosity=0)

            if not self.client:
                self.client = Client()

            test_cases = self.test_cases()
            test_case = next(test_cases)
            while True:
                succeeded = self.succeeded + self.tmp_succeeded
                total = self.total + self.tmp_total

                wrapper = connections.all()[0]
                schema = "".join(line for line in wrapper.connection.iterdump())
                client = self.client

                params = {
                        'client': client,
                        'succeeded': succeeded,
                        'total': total,
                        'path': self.path,
                        'schema': schema }

                if not client:
                    params['completed'] = True
                    test_obj = self.__class__

                result = test_obj(**params)
                results.append(result)
                self.reset()

                try:
                    # Run the next test.
                    test_case = next(test_cases)
                except StopIteration:
                    break

            return TestSet(results)

    def reset(self):
        self.tmp_total = 0
        self.tmp_succeeded = 0
        self.client = Client()
        connection = sqlite3.connect(":memory:")
        if self.schema:
            connection.executescript(self.schema)

        wrapper = connections.all()[0]
        wrapper.connection = connection

        if not self.schema:
            wrapper.creation.create_test_db(verbosity=0)

    def assertion(self, conditional, message=""):
        self.tmp_total += 1

        if conditional:
            self.tmp_succeeded += 1

    @property
    def name(self):
        name = self.__class__.__name__
        s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

    def __str__(self):
        return "%s: %d/%d" % (self.name, self.succeeded, self.total)

    def __repr__(self):
        return "<Test %s: %d/%d>" % (self.name, self.succeeded, self.total)


