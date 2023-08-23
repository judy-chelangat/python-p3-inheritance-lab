#!/usr/bin/env python

from user import User

import random

class Teacher(User):
    def __init__(self, first_name, last_name, knowledge):
        super().__init__(first_name, last_name)  # Call the parent class constructor
        self.knowledge = knowledge
        
    def teach(self):
        if self.knowledge:
            random_index = random.randint(0, len(self.knowledge) - 1)
            return self.knowledge[random_index]
        else:
            return "No knowledge available."
knowledge = [
    "str is a data type in Python",
    "programming is hard, but it's worth it",
    "JavaScript async web request",
    "Python function call definition",
    "object-oriented teacher instance",
    "programming computers hacking learning terminal",
    "pipenv install pipenv shell",
    "pytest -x flag to fail fast",
]

my_teacher = Teacher("John", "Doe", knowledge)
