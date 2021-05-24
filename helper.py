import platform
import os
from PyInquirer import prompt, ValidationError, Validator
from style import style
import sys


# create class for check Empty Field in input
class EmptyValidator(Validator):
    def validate(self, value):
        if len(value.text):
            return True
        else:
            raise ValidationError(
                message="You can't leave this blank", cursor_position=len(value.text)
            )

def screencls():
    if platform.system() == "Linux" or platform.system() == "Darwin":
        os.system("clear")
    if platform.system() == "Windows":
        os.system("cls")


def back():
    question = [
        {
            "type": "list",
            "name": "back",
            "message": "choose",
            "choices": ["Back"]
        }
    ]
    ans = prompt(question, style=style)
    if ans["back"] == "Back":
        return True

def exit():
    questions = [
        {
            'type': 'confirm',
            'message': 'Do you want to exit?',
            'name': 'exit',
            'default': False,
        }
    ]
    answer = prompt(questions, style=style)
    return answer['exit']