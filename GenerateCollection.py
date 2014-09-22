"""
.. module:: GenerateCollection

GenerateCollection
*************

:Description: GenerateCollection

    

:Authors: bejar
    

:Version: 

:Created on: 22/09/2014 11:54 

"""

__author__ = 'bejar'



from QCollection import QCollection
from Question import Question
from QConfiguration import QConfiguration
from Document import Document
from Quiz import Quiz
import string


def stripNl(val):
    return (string.lstrip(string.rstrip(val[:len(val)-1])))

cfpath = '/home/bejar/Documentos/Docencia/aaac/Preguntas'

cnf = QConfiguration()
cnf.get_configuration(cfpath, 'testpreprocess.cfg')

col = QCollection()
col.load_qcollection(cnf.get_questions_path(), cnf.get_questions_collection())

qz = col.generate_collection()
d = Document(cnf, qz)
d.save_collection(cnf.get_exam_file_name())
