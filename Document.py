"""
.. module:: Document

Document
******

:Description: Document

    Document for the quiz

:Authors:
    javier

:Version: 

:Date:  30/07/2014
"""

__author__ = 'javier'

class Document:

    def __init__(self, config, quiz):
        self._config = config
        self._quiz = quiz

    def save(self, name, choices, permans=False, permchoices=False, solutions=False, stdname=None):
        """
        Saves the document

        :param path:
        :param name:
        :return:
        """


        path = self._config._output
        dfile = open(path + '/test/' + name + '.tex', 'w')
        if solutions:
            dsfile = open(path + '/solution/' + name + '-sol.tex', 'w')
        else:
            dsfile = None

        # Writes the header/configuration of the latex file
        ltxpreamble = open('latex/preamble', 'r')
        for line in ltxpreamble:
            dfile.write(line)
        if solutions:
            ltxpreamble = open('latex/preamble-sol', 'r')
            for line in ltxpreamble:
                dsfile.write(line)

        self._preamble(dfile, stdname=stdname)
        if solutions:
            self._preamble(dsfile, stdname=stdname)

        for i in range(self._quiz.size()):
            q = self._quiz.get_i_question(i)
            q.latex_question(dfile, choices, 'q'+str(i), permans=permans,
                             permchoices=permchoices, sfile=dsfile, solutions=solutions)

        self._closing(dfile)
        if solutions:
            self._closing(dsfile)

        dfile.close()

    def save_collection(self, name):
        """
        Generates a document with all the positive and negative questions
        :return:
        """
        path = self._config._output
        pfile = open(path + '/' + name + '-all.tex', 'w')

        # Writes the header/configuration of the latex file
        ltxpreamble = open('latex/preamble-sol', 'r')
        for line in ltxpreamble:
            pfile.write(line)

        self._preamble(pfile)

        for i in range(self._quiz.size()):
            q = self._quiz.get_i_question(i)
            q.latex_complete_question(pfile, 'q'+str(i))

        self._closing(pfile)

        pfile.close()

    def _preamble(self, wfile, stdname=None):
        wfile.write('\\begin{document}\n')
        wfile.write('\\noindent\n')
        wfile.write('%s \\hfill %s \\hfill %s \\\\\n' % (self._config._course, self._config._title, self._config._date))
        wfile.write('%s \\hfill %s \\\\\n\n' % (self._config._term, self._config._curricula))
        wfile.write('\\hrulefill\n\n')
        wfile.write('\\vspace*{1cm}\n\n')

        if stdname is not None:
             wfile.write('\\noindent \\textbf{Name:} '+ stdname +'\n')
        else:
            wfile.write('\\noindent \\textbf{Name:} \\textField '+
                        '[\\BC{0 0 1}\\BG{0.98 0.92 0.73}'+
                        '\\textColor{1 0 0 rg}'+
                        ']{myText}{3.5in}{12bp}\n')
        wfile.write('\\bigskip\n')
        wfile.write('\\section*{Instructions}\n')
        instructions = self._config._instructions.split('#')
        for ins in instructions:
            wfile.write(ins+'\n\n')
        wfile.write('\\bigskip\n')
        wfile.write('\\hspace*{1cm}\\hrulefill\\hspace*{1cm}\n\n')
        wfile.write('\\bigskip\n\n')
        wfile.write('\\begin{quiz}{a}\n\n')
        wfile.write('%s\n\n' % self._config._quiztitle)
        wfile.write('\\bigskip\n\n')
        wfile.write('\\begin{questions}\n')

    def _closing(self, wfile):
        wfile.write('\n\\end{questions}\n')
        wfile.write('\n\\end{quiz}\\quad\n')
        wfile.write('\\end{document}\n')
