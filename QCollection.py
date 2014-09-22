"""
.. module:: QCollection

QCollection
******

:Description: QCollection

    Collection of questions

:Authors:
    javier

:Version: 

:Date:  30/07/2014
"""

__author__ = 'javier'
from Question import Question
import json
import random
from Quiz import Quiz

class QCollection:
    """
    Collection of multiple choice questions
    """
    def __init__(self):
        self._questions = []
        self.decoder = json.JSONDecoder()

    def append_question(self, question):
        """
        Adds a new question to the collection
        :param question:
        :return:
        """
        if isinstance(question, Question):
            self._questions.append(question)

    def get_i_question(self, index):
        """
        gets the i-th question from the collection
        :param index:
        :return:
        """
        if index < (len(self._questions)):
            return self._questions[index]
        else:
            return None

    def size(self):
        """
        Size of the collection
        :return:
        """
        return len(self._questions)

    def _loads(self, s):
        """A generator reading a sequence of JSON values from a string."""
        res = []
        while s:
            s = s.strip()
            obj, pos = self.decoder.raw_decode(s)
            if pos:
                res.append(obj)
                s = s[pos:]
        return res

    def load_qcollection(self, path, nfile):
        """
        Load a collection of questions from a json file
        :param path:
        :param nfile:
        :return:
        """
        fp = open(path + '/' + nfile + '.json', 'r')

        lquestions = self._loads(fp.read())

        for question in lquestions:
            q = Question()
            for sec in question:
                if sec == 'text':
                    q.set_qtext(question[sec])
                if sec == 'choices':
                    for ch in question[sec]:
                        o = {}
                        for op in ch:
                            o[op] = ch[op]
                        q.append_qchoice(o)

            self.append_question(q)

    def pprint(self):
        print '------------------'
        for q in self._questions:
            print q.get_qtext()
            for i in range(q.len_qchoices()):
                ch = q.get_i_qchoice(i)
                if 'pos' in ch:
                    print i, ch['pos']
                if 'neg' in ch:
                    print i, ch['neg']
            print '------------------'

    def generate_quiz(self, nquest, nans, seed=None):
        """
        Generate a quiz with a number of questions, a number of answers per question
         and a number of true choices
        :param nquest:
        :param nans:
        :param seed:
        :return:
        """

        if seed is not None:
            random.seed(seed)

        order = range(len(self._questions))
        random.shuffle(order)
        i=0
        nq = 0
        qz = Quiz()
        while i < len(order) and nq < nquest:
            q = self.get_i_question(order[i])
            lq = q.generate_questions(nans)
            for q in lq:
                if nq < nquest:
                    qz.add_question(q)
                nq += 1
            i += 1


        return qz

    def generate_collection(self):
        """
        Generates a quiz that contains all the questions in the collection
        :return:
        """
        qz = Quiz()
        for i in range(self.size()):
            q = self.get_i_question(i)
            qz.add_question(q.generate_all_questions())

        return qz