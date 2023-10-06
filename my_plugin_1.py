from astroid import nodes
from pylint.checkers import BaseChecker

class UnusedVariableChecker(BaseChecker):
    name = "unused-variable"

    msgs = {
        "W0001": (
            "Unused variable '%s'",
            "unused-variable",
            "A warning message for unused variables",
        )
    }

    @check_messages("unused-variable")
    def visit_Assign(self, node):
        for target in node.targets:
            if not isinstance(target, nodes.Name):
                continue

            if not self.is_variable_used(target):
                self.add_message("unused-variable", node=target)

    def is_variable_used(self, node):
        # TODO: Implement this method to check if the variable is used anywhere in the code.

        return True

def register(linter):
    linter.register_checker(UnusedVariableChecker(linter))
