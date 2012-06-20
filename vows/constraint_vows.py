__author__ = 'Doug Woos'

from pyvows import Vows, expect

import os
import sys
sys.path.append(os.path.abspath('{0}/../../'.format(__file__)))

from hackery.version_hack import Constraint

class FalseContext(Vows.Context):
    def should_be_false(self, topic):
        expect(topic).to_be_false()

class TrueContext(Vows.Context):
    def should_be_true(self, topic):
        expect(topic).to_be_true()



@Vows.batch
class ConstraintContext(Vows.Context):

    class ExistenceConstraint(Vows.Context):
        def topic(self):
            return Constraint('android', '', '')

        class WhenKeyExists(TrueContext):
            def topic(self, constraint):
                return constraint({'android': 2})

        class WhenKeyDoesNotExist(FalseContext):
            def topic(self, constraint):
                return constraint({})

    class EqualsConstraint(Vows.Context):
        def topic(self):
            return Constraint('android', '==', '2')

        class WhenKeyEquals(TrueContext):
            def topic(self, constraint):
                return constraint({'android': 2})

        class WhenKeyDoesNotEqual(FalseContext):
            def topic(self, constraint):
                return constraint({})

    class LessThanConstraint(Vows.Context):
        def topic(self):
            return Constraint('android', '<', '2')

        class WhenKeyLessThan(TrueContext):
            def topic(self, constraint):
                return constraint({'android': 1})

        class WhenKeyEquals(FalseContext):
            def topic(self, constraint):
                return constraint({'android': 2})

        class WhenKeyGreaterThan(FalseContext):
            def topic(self, constraint):
                return constraint({'android': 3})

    class GreaterThanConstraint(Vows.Context):
        def topic(self):
            return Constraint('android', '>', '2')

        class WhenKeyLessThan(FalseContext):
            def topic(self, constraint):
                return constraint({'android': 1})

        class WhenKeyEquals(FalseContext):
            def topic(self, constraint):
                return constraint({'android': 2})

        class WhenKeyGreaterThan(TrueContext):
            def topic(self, constraint):
                return constraint({'android': 3})

    class LessThanOrEqualConstraint(Vows.Context):
        def topic(self):
            return Constraint('android', '<=', '2')

        class WhenKeyLessThan(TrueContext):
            def topic(self, constraint):
                return constraint({'android': 1})

        class WhenKeyEquals(TrueContext):
            def topic(self, constraint):
                return constraint({'android': 2})

        class WhenKeyGreaterThan(FalseContext):
            def topic(self, constraint):
                return constraint({'android': 3})

    class GreaterThanOrEqualConstraint(Vows.Context):
        def topic(self):
            return Constraint('android', '>=', '2')

        class WhenKeyLessThan(FalseContext):
            def topic(self, constraint):
                return constraint({'android': 1})

        class WhenKeyEquals(TrueContext):
            def topic(self, constraint):
                return constraint({'android': 2})

        class WhenKeyGreaterThan(TrueContext):
            def topic(self, constraint):
                return constraint({'android': 3})
