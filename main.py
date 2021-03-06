import sys
from PyInquirer import prompt
from pprint import pprint
from style import style
from pyfiglet import Figlet
from colorama import init, Fore
from helper import screencls, exit, back, EmptyValidator


def generateREADME():
    questions = [
        {
            "type": "input",
            "name": "title",
            "message": "Hi š, I'm (name)",
            "validate": EmptyValidator,
        },
        {
            "type": "input",
            "name": "subtitle",
            "message": "Subtitle(ex: A passionate backend developer from US):",
        },
        {
            "type": "input",
            "name": "work",
            "message": "Iām currently working on(project name):"
        },
        {
            "type": "input",
            "name": "worklink",
            "message": "Project link:",
        },
        {
            "type": "input",
            "name": "collaborate",
            "message": "šÆ Iām looking to collaborate on(project name):"
        },
        {
            "type": "input",
            "name": "collaboratelink",
            "message": "Project link:"
        },
        {
            "type": "input",
            "name": "helping",
            "message": "š¤ Iām looking for help with(project name):"
        },
        {
            "type": "input",
            "name": "helpinglink",
            "message": "Project link:"
        },
        {
            "type": "input",
            "name": "learn",
            "message": "š± Iām currently learning(Frameworks, courses and etc):"
        },
        {
            "type": "input",
            "name": "about",
            "message": "š¬ Ask me about(python, django and vue):"
        },
        {
            "type": "input",
            "name": "reach",
            "message": "š« How to reach me(example@gmail.com):"
        },
        {
            "type": "input",
            "name": "projects",
            "message": "šØāš» All of my projects are available at(portfolio link):"
        },
        {
            "type": "input",
            "name": "articles",
            "message": "š I regularly write articles on(blog link):"
        },
        {
            "type": "input",
            "name": "resume",
            "message": "š Know about my experiences(resume link):"
        },
        {
            "type": "input",
            "name": "fact",
            "message": "ā” Fun fact(I think I am Funny):"
        }
    ]
    answers = prompt(questions, style=style)
    pprint(answers)

def main():
    screencls()
    ssd = Figlet(font="slant")
    print(f"{Fore.BLUE}{ssd.renderText('README Gen')}")
    questions = [
        {
            "type": "list",
            "name": "main",
            "message": "What do you want to do?",
            "choices": ["Generate README", "Support", "Contributing", "Exit"],
        }
    ]
    answer = prompt(questions, style=style)
    if answer["main"] == "Generate README":
        generateREADME()
    elif answer["main"] == "Support":
        pass
    elif answer["main"] == "Contributing":
        pass
    elif answer["main"] == "Exit":
        if exit():
            sys.exit()
        else:
            main()


if __name__ == "__main__":
    init(autoreset=True)
    main()
