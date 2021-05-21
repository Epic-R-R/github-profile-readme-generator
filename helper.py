import platform
import os
from PyInquirer import prompt

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
