import re
import operator
from pkg_resources import parse_version
from hack import Hack


class Constraint(object):
    constraint_regex=r'(\w+)\s*(?:(<|>|==|<=|>=)\s*([\-\.0-9a-z]+))?'

    operators = {'<': operator.lt,
                 '>': operator.gt,
                 '==': operator.eq,
                 '<=': operator.le,
                 '>=': operator.ge}

    def __init__(self, version_name, op, target):
        self.version_name = version_name
        self.op = self.operators[op] if op else None
        self.target = parse_version(target) if target else None

    @classmethod
    def constraints_from_string(cls, constraint_string):
        return [cls(*match) for match in
                re.findall(cls.constraint_regex, constraint_string)]

    def __call__(self, version_obj):
        version = version_obj.get(self.version_name)
        version_passes = True
        if version and self.op:
            version_passes = self.op(parse_version(str(version)),
                                     self.target)
        return version and version_passes

class VersionHack(Hack):

    def __init__(self, name, constraints, version, *args, **kwargs):
        """
        version should look like {<device>: <version>}
        """
        super(VersionHack, self).__init__(name, *args, **kwargs)
        self.version = version
        self.constraints = Constraint.constraints_from_string(constraints)

    def _should_fire(self):
        return any(constraint(self.version) for constraint in self.constraints)
