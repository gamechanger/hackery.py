import re
import operator
from pkg_resources import parse_version
from hack import Hack


class Constraint(object):
    version_names = {'android': '~va', 'ios': '~v'}

    constraint_regex=r'(\w+)\s*(?:(<|>|==|<=|>=)\s*([\-\.1-9]+))?'

    operators = {'<': operator.lt,
                 '>': operator.gt,
                 '==': operator.eq,
                 '<=': operator.le,
                 '>=': operator.ge}

    def __init__(self, device, op, target):
        self.version_name = self.version_names[device]
        self.op = self.operators[op] if op else None
        self.target = parse_version(target) if target else None

    @classmethod
    def constraints_from_string(cls, constraint_string):
        return [cls(*match) for match in
                re.findall(cls.constraint_regex, constraint_string)]

    def __call__(self, obj):
        version = obj.get(self.version_name)
        version_passes = True
        if version and self.op:
            version_passes = self.op(parse_version(str(version)),
                                     self.target)
        return version and version_passes

class VersionHack(Hack):

    def __init__(self, name, constraints, obj, *args, **kwargs):
        super(VersionHack, self).__init__(name, *args, **kwargs)
        self.obj = obj
        self.constraints = Constraint.constraints_from_string(constraints)

    def _should_fire(self):
        return any(constraint(self.obj) for constraint in self.constraints)
