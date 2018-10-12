# -*- coding: utf-8 -*-

class MoodleExporterConfig(object):
    """docstring for MoodleExporterConfig."""
    def __init__(self):
        super(MoodleExporterConfig, self).__init__()
        self.files = []
        self.latex_title = ""
        self.latex_author = "MoodleExporter"
        #Booleans
        self.latex_tableofcontents_b = True
        self.latex_each_file_newpage_b = True
        #LaTeX Header
        self.latex_mainheader = """
            \\documentclass[a4paper, 11pt]{article}
            \\usepackage[utf8]{inputenc}
            \\usepackage[T1]{fontenc}
            \\usepackage{xcolor,colortbl}
            \\usepackage{pgf,tikz}
            \\usetikzlibrary{calc,positioning,shapes.geometric,shapes.symbols,shapes.misc, fit, shapes, arrows, arrows.meta, fadings,through}
            \\usepackage{eurosym}
            \\usepackage[top=2cm, bottom=2cm, left=2cm, right=2cm]{geometry}
            \\usepackage{hyperref}
            \\usepackage[francais]{babel}

            \\newcommand\\tab[1][0.6cm]{\\hspace*{#1}} %Create and define tab

            \\RequirePackage{fancyhdr}
            \\pagestyle{fancy}
            \\renewcommand{\\headrule}{}
            \\lhead{Corrigés QCMs}
            \\chead{}
            \\rhead{MoodleExporter}
            \\lfoot{}
            \\cfoot{\\thepage}
            \\rfoot{}
        """

    #UTILS ---------------------------------------------------------------------

    def add_source_file(self, path_to_file:str):
        self.files.append(path_to_file)

    def clear_source_files(self):
        self.files.clear()

    def get_source_files(self):
        return self.files

    #GET SET -------------------------------------------------------------------
    def get_author (self):
        return self.latex_author

    def set_author (self, author):
        self.latex_author = author

    def get_title (self):
        return self.latex_title

    def set_title (self, title):
        self.latex_title = title

    def get_latex_mainheader (self):
        return self.latex_mainheader + """\n\n\n\\title{""" + self.latex_title + """}\n\\author{""" + self.latex_author + """}\n\\date{\\today}"""

    def set_latex_mainheader (self, latex_mainheader):
        self.latex_mainheader = latex_mainheader



    #Options -------------------------------------------------------------------
    def has_latex_tableofcontents(self):
        return self.latex_tableofcontents_b

    def each_file_newpage(self):
        return self.latex_each_file_newpage_b




if __name__ == '__main__':
    pass
