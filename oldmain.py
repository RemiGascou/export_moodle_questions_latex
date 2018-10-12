# -*- coding: utf-8 -*-

#https://docs.python.org/2/library/xml.etree.elementtree.html

from lxml import etree

def latexbuild(data):
    out = ""
    for e in data:
        out += ''.join(e)
        out += "\\medskip\n\n\n"
    return out

def update(buffdata, data):
    for k in range(len(buffdata)):
        buffdata[k] = buffdata[k].replace("<br>", "")
        buffdata[k] = buffdata[k].replace("<p>", "")
        buffdata[k] = buffdata[k].replace("</p>", "")
        buffdata[k] = buffdata[k].replace("$", "\\$")
        buffdata[k] = buffdata[k].replace("_", "\\_")
        data[k].append(buffdata[k])
    buffdata.clear()

data = []
buffdata = []
separator_q = """%--------------------------------------------------------------------------------------"""

corr_struct = """
\\medskip

\\begin{itemize}
    \\item \\fbox{\\parbox{15cm}{...}}
    \\item ..
\\end{itemize}


\\subsubsection*{Corrigé}

\\textbf{}
"""

path =r'/home/administrateur/Téléchargements/qcm/'
tree = etree.parse(path + "quizz_SPOC_cas3.xml")

#NAMES
for qn in tree.xpath("/quiz/question/name/text"):
    s = separator_q + "\n" + "\\subsection{" + qn.text + "}\n"
    data.append([s])

#QUESTION TEXT
for c in tree.xpath("/quiz/question/questiontext/text"):
    s = c.text.replace("\n", "") + "\n"
    buffdata.append(s)

update(buffdata,data)

update([corr_struct]*len(data),data)

print(latexbuild(data))