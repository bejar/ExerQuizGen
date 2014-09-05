"""
.. module:: QConfiguration

QConfiguration
******

:Description: QConfiguration

    Configuration of the Quiz

:Authors:
    javier

:Version: 

:Date:  30/07/2014
"""

__author__ = 'javier'


from ConfigParser import SafeConfigParser

class QConfiguration:

    def __init__(self):
        self._course = None
        self._date = None
        self._term = None
        self._curricula = None
        self._title = None
        self._quiztitle = None
        self._instructions = None
        self._output = None
        self._qpath = None
        self._qname = None
        self._nchoices = None
        self._nquestions = None
        self._nanswers = None
        self._fname = None

    def get_configuration(self, path, nfile):
        """
        Reads the configuration from a file
        :param path:
        :return:
        """

        cnf = SafeConfigParser()

        cnf.read(path + '/' + nfile)
        self._course = cnf.get('Header', 'Course')
        self._date = cnf.get('Header', 'Date')
        self._term = cnf.get('Header', 'Term')
        self._curricula = cnf.get('Header', 'Curricula')
        self._title = cnf.get('Header', 'Title')
        self._quiztitle = cnf.get('Header', 'QuizTitle')

        self._instructions = cnf.get('Exam', 'Instructions')
        self._qpath = cnf.get('Exam', 'Path')
        self._qname = cnf.get('Exam', 'Questions')
        self._nchoices = int(cnf.get('Exam', 'Choices'))
        self._nquestions = int(cnf.get('Exam', 'NQuestions'))
        self._nanswers = int(cnf.get('Exam', 'NAnswers'))

        self._output = cnf.get('Output', 'Path')
        self._fname = cnf.get('Output', 'FName')

    def get_output_path(self):
        return self._output

    def get_questions_collection(self):
        return self._qname

    def get_questions_path(self):
        return self._qpath

    def get_exam_num_choices(self):
        return self._nchoices

    def get_exam_num_questions(self):
        return self._nquestions

    def get_exam_num_answers(self):
        return self._nanswers

    def get_exam_file_name(self):
        return self._fname

