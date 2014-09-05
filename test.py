"""
.. module:: test

test
******

:Description: test

    Different Auxiliary functions used for different purposes

:Authors:
    javier

:Version: 

:Date:  30/07/2014
"""

__author__ = 'javier'

from QCollection import QCollection
from Question import Question
from QConfiguration import QConfiguration
from Document import Document
from Quiz import Quiz
import json
import StringIO


def test1():
    a = Question()

    a.set_qtext('aaaaaaa')

    a.append_qchoices('aaa', 'bbb')
    a.append_qchoices('ccc', 'ddd')

    print a.get_qtext()

    for i in range(a.len_qchoices()):
        print a.get_i_qchoices(i)

def test2():
    cnf = QConfiguration()

    cnf.get_configuration('.','exam.cfg')

    print cnf._title
    print cnf._course
    print cnf._date

    doc = Document(cnf)

    doc.save('/home/javier/tmp', 'test')

def test3():
    col = QCollection()
    col.load_qcollection('.', 'questions')
    quiz = Quiz()
    col.pprint()


col = QCollection()
col.load_qcollection('.', 'questions')
qz = col.generate_quiz(3, 3)

# for i in range(qz.size()):
#     qu = qz.get_i_question(i)
#     print qu.get_qtext(), qu.len_qchoices()
#     for j in range(qu.len_qchoices()):
#         print qu.get_i_qchoice(j)


cnf = QConfiguration()
cnf.get_configuration('.', 'exam.cfg')

print cnf._instructions.split('#')

d = Document(cnf, qz)

d.save('test', 2)



