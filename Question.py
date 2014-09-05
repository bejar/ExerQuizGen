"""
.. module:: Question

Question
******

:Description: Question

    Class for tst questions

:Authors:
    javier

:Version: 

:Date:  30/07/2014
"""

__author__ = 'javier'

import random

class Question:
    """
    Test questions with single/multiple choice answers + solutions
    Assumes that all questions hve positive/negative answers and a solution

    """

    def __init__(self):
        self._qtext = None
        self._qchoices = []

    def get_qtext(self):
        """
        Gets the text of the question
        :return:
        """
        return self._qtext

    def set_qtext(self,value):
        """
        Sets the text of the question
        :param value:
        :return:
        """
        self._qtext = value

    def append_qchoice(self, choice):
        """
        Adds a new choice to the questions
        as a dictionary that can have the keys:
            pos - Positive answer
            neg - Negative answer
            negsol - Solution to the negative answer

        :param tchoice:
        :param fchoice:
        :return:
        """
        self._qchoices.append(choice)

    def get_i_qchoice(self, index):
        """
        Gets the i-th choice of the question
        :param index:
        :return:
        """
        if index < (len(self._qchoices)):
            return self._qchoices[index]
        else:
            return None

    def len_qchoices(self):
        """
        Gets the number of choices of the question
        :return:
        """
        return len(self._qchoices)

    def generate_questions(self, nans, seed=None):
        """
        Generates a list of random questions from the answers of the questions
        Each question has nans answers
        :param nans:
        :param seed:
        :return:
        """

        if seed is not None:
            random.seed(seed)

        ch = range(len(self._qchoices))
        random.shuffle(ch)
        nq = len(self._qchoices)/nans
        lq = []
        for i in range(0,nq):
            qu = Question()
            qu.set_qtext(self.get_qtext())
            for j in range(nans):
                qu.append_qchoice(self.get_i_qchoice(ch[i*nans+j]))
            lq.append(qu)

        return lq

    def latex_question(self, dfile, nchoices, label, permans=False, permchoices=False):
        """
        Writes a question with nchoices correct answers on a file in latex qexam format
        It can permutate the answers and the correct answers
        :param dfile:
        :param choices:
        :param permans:
        :param permchoices:
        :return:
        """

        if nchoices == 1:
            dfile.write('\\item %s:\n\n' % self.get_qtext())
        else:
            dfile.write('\\item %s (multiple answer):\n\n' % self.get_qtext())

        if nchoices == 1:
            dfile.write('\\begin{answers}[*]{1}\n')
        else:
            dfile.write('\\begin{manswers}[*]{1}\n')
            dfile.write('\\bChoices\n')

        pnans = []
        for i in range(nchoices):
            pnans.append(1)
        for i in range(len(self._qchoices)-nchoices):
            pnans.append(0)
        random.shuffle(pnans)

        order = range(len(self._qchoices))
        if permans:
            random.shuffle(order)

        for p,a in zip(order,pnans):
            qchoices = self.get_i_qchoice(p)
            if a == 0:
                qtn = qchoices['neg']
            else:
                qtn = qchoices['pos']
            if nchoices == 1:
                dfile.write('\\Ans%d \\label{%s} %s\n' % (a, label+str(p), qtn))
            else:
                dfile.write('\\Ans%d \\label{%s} %s\eAns\n' % (a, label+str(p), qtn))


        if nchoices == 1:
            dfile.write('\\end{answers}\n')
        else:
            dfile.write('\\eChoices\n')
            dfile.write('\\end{manswers}\n')


        dfile.write('\\begin{solution}\n\n')
        solpos = []
        for p,a in zip(order,pnans):
            if a == 1:
                solpos.append(label + str(p))

        if nchoices == 1:
            dfile.write('The correct answer is (\\ref{%s}).\n\n' % solpos[0])
        else:
            dfile.write('The correct answers are ')
            dfile.write('\\ref{%s})' % solpos[0])
            for i in range(1,len(solpos)):
                dfile.write(' and {\\ref{%s})' %solpos[i])
            dfile.write('\n')

        for p,a in zip(order,pnans):
            qchoices = self.get_i_qchoice(p)
            qtn = qchoices['negsol']
            if a == 0:
                dfile.write('The answer (\\ref{%s}) is not correct because %s.\n\n' % (label + str(p), qtn) )


        dfile.write('\\end{solution}')

        dfile.write('\n\n')


