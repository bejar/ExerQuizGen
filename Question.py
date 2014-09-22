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
    Assumes that all questions have positive/negative answers and a solution

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

    def generate_all_questions(self):
        """
        Generates a list of all questions
        :return:
        """
        qu = Question()
        qu.set_qtext(self.get_qtext())
        for i in range(self.len_qchoices()):
            qu.append_qchoice(self.get_i_qchoice(i))
        return qu



    def latex_question(self, dfile, nchoices, label, permans=False, permchoices=False, sfile=None, solutions=False):
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
            if solutions:
                sfile.write('\\item %s:\n\n' % self.get_qtext())
        else:
            dfile.write('\\item %s (multiple answer):\n\n' % self.get_qtext())
            if solutions:
                sfile.write('\\item %s (multiple answer):\n\n' % self.get_qtext())

        if nchoices == 1:
            dfile.write('\\begin{answers}{1}\n')
            if solutions:
                sfile.write('\\begin{answers}[*]{1}\n')
        else:
            dfile.write('\\begin{manswers}{1}\n')
            dfile.write('\\bChoices\n')
            if solutions:
                sfile.write('\\begin{manswers}[*]{1}\n')
                sfile.write('\\bChoices\n')

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
                if solutions:
                    sfile.write('\\Ans%d \\label{%s} %s\n' % (a, label+str(p), qtn))
            else:
                dfile.write('\\Ans%d \\label{%s} %s\eAns\n' % (a, label+str(p), qtn))
                if solutions:
                    sfile.write('\\Ans%d \\label{%s} %s\eAns\n' % (a, label+str(p), qtn))


        if nchoices == 1:
            dfile.write('\\end{answers}\n')
            if solutions:
                sfile.write('\\end{answers}\n')
        else:
            dfile.write('\\eChoices\n')
            dfile.write('\\end{manswers}\n')
            if solutions:
                sfile.write('\\eChoices\n')
                sfile.write('\\end{manswers}\n')


        if solutions:
            sfile.write('\\begin{solution}\n\n')
            solpos = []
            for p,a in zip(order,pnans):
                if a == 1:
                    solpos.append(label + str(p))

            if nchoices == 1:
                sfile.write('The correct answer is (\\ref{%s}).\n\n' % solpos[0])
            else:
                sfile.write('The correct answers are ')
                sfile.write('(\\ref{%s})' % solpos[0])
                for i in range(1,len(solpos)):
                    sfile.write(' and (\\ref{%s})' %solpos[i])
                sfile.write('.\n\n')

            for p,a in zip(order,pnans):
                qchoices = self.get_i_qchoice(p)
                qtn = qchoices['negsol']
                if a == 0:
                    sfile.write('The answer (\\ref{%s}) is not correct because %s.\n\n' % (label + str(p), qtn) )


        dfile.write('\n\n')
        if solutions:
            sfile.write('\\end{solution}')
            sfile.write('\n\n')


    def latex_complete_question(self, dfile, label):
        """
        Generates a latex question with all the positive and negative answers
        :param dfile:
        :param label:
        :return:
        """

        dfile.write('\\item %s (positive answer):\n\n' % self.get_qtext())
        pnans = []
        for i in range(len(self._qchoices)):
            pnans.append(1)
        dfile.write('\\begin{manswers}[*]{1}\n')
        dfile.write('\\bChoices\n')

        order = range(len(self._qchoices))

        for p,a in zip(order,pnans):
            qchoices = self.get_i_qchoice(p)
            qtn = qchoices['pos']
            dfile.write('\\Ans%d \\label{%s} %s\eAns\n' % (a, label+str(p)+str(a), qtn))
        dfile.write('\\eChoices\n')
        dfile.write('\\end{manswers}\n')
        dfile.write('\\begin{solution}\n\n')

        solpos = []
        for p,a in zip(order,pnans):
            if a == 1:
                solpos.append(label + str(p)+str(a))
        dfile.write('The correct answers are ')
        dfile.write('(\\ref{%s})' % solpos[0])
        for i in range(1,len(solpos)):
            dfile.write(' and (\\ref{%s})' % solpos[i])
        dfile.write('.\n\n')

        dfile.write('\\end{solution}')
        dfile.write('\n\n')

        dfile.write('\\item %s (negative answer):\n\n' % self.get_qtext())
        pnans = []

        for i in range(len(self._qchoices)):
            pnans.append(0)

        dfile.write('\\begin{manswers}[*]{1}\n')
        dfile.write('\\bChoices\n')


        for p,a in zip(order,pnans):
            qchoices = self.get_i_qchoice(p)
            qtn = qchoices['neg']
            dfile.write('\\Ans%d \\label{%s} %s\eAns\n' % (a, label+str(p)+str(a), qtn))
        dfile.write('\\eChoices\n')
        dfile.write('\\end{manswers}\n')
        dfile.write('\\begin{solution}\n\n')
        solpos = []

        for p,a in zip(order,pnans):
            qchoices = self.get_i_qchoice(p)
            qtn = qchoices['negsol']
            if a == 0:
                dfile.write('The answer (\\ref{%s}) is not correct because %s.\n\n' % (label + str(p) + str(a), qtn))


        dfile.write('\\end{solution}')
        dfile.write('\n\n')
