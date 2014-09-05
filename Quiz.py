"""
.. module:: Quiz

Quiz
******

:Description: Quiz

    Generates a quiz from a collection of questions

:Authors:
    javier

:Version: 

:Date:  30/07/2014
"""

__author__ = 'javier'

class Quiz:
    def __init__(self):
        self._questions = []

    def add_question(self, question):
        """
        Adds a question to que quiz
        :param question:
        :return:
        """
        self._questions.append(question)

    def get_i_question(self, index):
        """
        Gets the i-th question of the quiz
        :param index:
        :return:
        """
        return self._questions[index]

    def size(self):
        """
        length of the quiz
        :return:
        """
        return len(self._questions)