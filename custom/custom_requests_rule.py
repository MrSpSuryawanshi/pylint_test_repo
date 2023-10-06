import astroid
from pylint.checkers import BaseChecker
from pylint.interfaces import IAstroidChecker

class CustomRequestsRule(BaseChecker):
    __implements__ = IAstroidChecker

    name = 'custom-requests-rule'
    priority = -1

def register(linter):
    linter.register_checker(CustomRequestsRule(linter))
