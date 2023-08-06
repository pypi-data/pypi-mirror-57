import re

from pycsp3.classes.auxiliary.types import TypeVar
from pycsp3.classes.main.domains import Domain


class NotVariable:
    def __init__(self, variable):
        self.variable = variable


class NegVariable:
    def __init__(self, variable):
        self.variable = variable


class Variable:
    name2obj = dict()  # Dictionary (keys: names of variables - values: variable objects)

    @staticmethod
    def build_names_array(name, sizes, mins, indexes=[]):
        if sizes:
            t = []
            for i in range(sizes[0]):
                indexes.append(i + mins[len(indexes)])
                t.append(Variable.build_names_array(name, sizes[1:], mins, indexes))
                indexes.pop()
            return t
        return name + "[" + "][".join(str(i) for i in indexes) + "]"

    @staticmethod
    def build_domain(name, domain, when, indexes):
        if domain is None:
            return None
        if when and not when(*indexes):
            return None
        if isinstance(domain, Domain):
            return domain
        if isinstance(domain, list) and all(isinstance(v, int) for v in domain):  # possible, even if using a set is recommended
            return Domain(set(domain))
        if isinstance(domain, list):  # meaning a specific domain for each variable
            for i in indexes:
                assert i < len(domain), ("The number of domains is less than the specified index " + str(name) + " - " + str(domain)
                                         + "\nUse a set instead of a list if you want the same domain for all variables.")
                domain = domain[i]
        elif isinstance(domain, type(lambda: 0)):
            domain = domain(*indexes)
            if domain is None:
                return None
        if isinstance(domain, Domain):
            return domain
        if isinstance(domain, list) and all(isinstance(ele, int) for ele in domain):
            return Domain(set(domain))
        assert isinstance(domain, (range, set)), type(domain)
        return Domain(domain)

    @staticmethod
    def build_variable(name, domain, when, indexes):  # name, domain):
        dom = Variable.build_domain(name, domain, when, indexes)
        if dom is None:
            return None
        var = VariableInteger(name, dom) if dom.get_type() == TypeVar.INTEGER else VariableSymbolic(name, dom)
        Variable.name2obj[name] = var
        return var

    @staticmethod
    def build_variables_array(name, sizes, domain, when=None, indexes=[]):
        if isinstance(name, list):
            # it means that several variables are declared with a single line
            assert len(sizes) == 1, "When using several declarations, only one-dimensional arrays are allowed."
            return [Variable.build_variable(var_name.strip(), domain, when, indexes) for var_name in name]
        if sizes:
            t = []
            for i in range(sizes[0]):
                indexes.append(i)
                t.append(Variable.build_variables_array(name, sizes[1:], domain, when, indexes))
                indexes.pop()
            return t
        var_name = name + "[" + "][".join(str(i) for i in indexes) + "]"
        return Variable.build_variable(var_name, domain, when, indexes)

    def __init__(self, name, dom):
        self.id = name
        self.dom = dom
        pos = self.id.find("[")
        if pos == -1:
            self.indexes = None
        else:
            self.prefix, self.suffix = self.id[:pos], self.id[pos:]
            self.indexes = [int(v) for v in re.split("\]\[", self.suffix[1:-1])]

    # def tag(self, tag):
    #     VarEntities.varToEVar[self].tag(tag)

    def __invert__(self):
        return NotVariable(self)

    def __neg__(self):
        return NegVariable(self)

    def __hash__(self, *args, **kwargs):
        return object.__hash__(self, *args, **kwargs)

    def __repr__(self):
        return self.id


class VariableInteger(Variable):
    def __init__(self, name, dom):
        super().__init__(name, dom)


class VariableSymbolic(Variable):
    def __init__(self, name, dom):
        super().__init__(name, dom)
