 import astroid
from pylint.checkers import BaseChecker
from pylint.interfaces import IAstroidChecker

class CustomRequestsRule(BaseChecker):
    __implements__ = IAstroidChecker

    name = 'custom-requests-rule'
    priority = -1

    def visit_import(self, node):
        """
        This method is called when an import statement is encountered.
        We'll check if 'requests' or 'urllib.request' is imported and issue a warning.
        """
        if 'requests' in node.names or ('urllib' in node.names and 'request' in node.names):
            self.add_message('custom-requests-warning', node=node)

def register(linter):
    linter.register_checker(CustomRequestsRule(linter))
