"""
.. module:: GenerateTests

GenerateTests
*************

:Description: GenerateTests

    

:Authors: bejar
    

:Version: 

:Created on: 05/09/2014 12:00 

"""

__author__ = 'bejar'


from QCollection import QCollection
from Question import Question
from QConfiguration import QConfiguration
from Document import Document
from Quiz import Quiz

cfpath = '/home/bejar/Documentos/Docencia/aaac/Preguntas'

cnf = QConfiguration()
cnf.get_configuration(cfpath, 'testpreprocess.cfg')

col = QCollection()
col.load_qcollection(cnf.get_questions_path(), cnf.get_questions_collection())

for i in range(3):
    qz = col.generate_quiz(cnf.get_exam_num_questions(), cnf.get_exam_num_answers())
    d = Document(cnf, qz)
    d.save(cnf.get_exam_file_name()+str(i), cnf.get_exam_num_choices())
