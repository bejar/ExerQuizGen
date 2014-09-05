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

    def save(self, name, choices, permans=False, permchoices=False, solutions=False):
        """
        Saves the document

        :param path:
        :param name:
        :return:
        """

        def preamble(wfile):
            wfile.write('\\begin{document}\n')
            wfile.write('\\noindent\n')
            wfile.write('%s \\hfill %s \\hfill %s \\\\\n' % (self._config._course, self._config._title, self._config._date))
            wfile.write('%s \\hfill %s \\\\\n\n' % (self._config._term, self._config._curricula))
            wfile.write('\\vspace*{1cm}\n\n')
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
            wfile.write('\\begin{questions}\n')

        def closing(wfile):
            wfile.write('\n\\end{questions}\n')
            wfile.write('\n\\end{quiz}\\quad\n')
            wfile.write('\\end{document}\n')

        path = self._config._output
        dfile = open(path + '/' + name + '.tex', 'w')
        if solutions:
            dsfile = open(path + '/' + name + '-sol.tex', 'w')

        # Writes the header/configuration of the latex file
        ltxpreamble = open('latex/preamble', 'r')
        for line in ltxpreamble:
            dfile.write(line)
        if solutions:
            ltxpreamble = open('latex/preamble-sol', 'r')
            for line in ltxpreamble:
                dsfile.write(line)

        preamble(dfile)
        if solutions:
            preamble(dsfile)

        for i in range(self._quiz.size()):
            q = self._quiz.get_i_question(i)
            q.latex_question(dfile, choices, 'q'+str(i), permans=permans, permchoices=permchoices)

        closing(dfile)
        if solutions:
            closing(dsfile)

        dfile.close()