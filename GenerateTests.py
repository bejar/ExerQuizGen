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
import string
import os


def stripNl(val):
    return string.lstrip(string.rstrip(val[:len(val)-1]))

cfpath = '/home/bejar/Documentos/Docencia/aaac/Preguntas'
dnipath = '/home/bejar/Documentos/Docencia/aaac/C1617'

cnf = QConfiguration()
cnf.get_configuration(cfpath, 'testarulesstruct.cfg')

col = QCollection()
col.load_qcollection(cnf.get_questions_path(), cnf.get_questions_collection())

dnifile = open(dnipath + '/' + 'DNI1617' + '.txt', 'r')
if not os.path.exists(cnf.get_output_path()):
    os.mkdir(cnf.get_output_path())
    os.mkdir(cnf.get_output_path() + '/test')
    os.mkdir(cnf.get_output_path() + '/solution')

os.system(' rm -fr ' + cnf.get_output_path() + '/test/*')
os.system(' rm -fr ' + cnf.get_output_path() + '/solution/*')

for values in dnifile:
    dni, famname, firstname  = values.split(',')
    qz = col.generate_quiz(cnf.get_exam_num_questions(), cnf.get_exam_num_answers(), seed=int(dni))
    d = Document(cnf, qz)
#    d.save(cnf.get_exam_file_name()+'-'+stripNl(dni), cnf.get_exam_num_choices(),solutions=True, stdname=firstname.upper() + " " + famname.upper())
    d.save(cnf.get_exam_file_name()+'-'+dni, cnf.get_exam_num_choices(),solutions=True)
    os.system('pdflatex -output-directory '+ cnf.get_output_path() +
              '/test/ '+ cnf.get_output_path() + '/test/' + cnf.get_exam_file_name() + '-' + dni + '.tex')
    os.system('pdflatex -output-directory '+ cnf.get_output_path() +
              '/solution/ ' + cnf.get_exam_file_name() + '-' + dni + '-sol.tex')
    os.system('pdflatex -output-directory '+ cnf.get_output_path() +
              '/solution/ ' + cnf.get_exam_file_name() + '-' + dni + '-sol.tex')
ext = ['log','aux', 'out', 'qsl', 'sol', 'cut', 'djs']
for e in ext:
    os.system(' rm -fr ' + cnf.get_output_path() + '/test/*.' + e)
    os.system(' rm -fr ' + cnf.get_output_path() + '/solution/*.' + e)

os.system('cd '+ cnf.get_output_path() + '/test/' +'; zip ' + cnf.get_exam_file_name() + '.zip *.pdf')
os.system('cd '+ cnf.get_output_path() + '/solution/' +'; zip ' + cnf.get_exam_file_name() + '-sol.zip *.pdf')
