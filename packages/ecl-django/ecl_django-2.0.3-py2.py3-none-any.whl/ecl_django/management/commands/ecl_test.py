import sys

from django.core.management.base import BaseCommand
from django.conf import settings

_temp = __import__("app", globals(), locals(), ["tests"], -1)
tests = _temp.tests


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        results = []
        succeeded = 0
        total = 0

        for flow in tests.flows:
            for result in flow().get_results():
                if not result.passed:
                    passed = False

                results.append(result)
                succeeded += result.succeeded
                total += result.total
                print(result)

        print("%d/%d tests passed." % (succeeded, total))

        if succeeded == total:
            sys.exit(0)
        else:
            sys.exit(1)

