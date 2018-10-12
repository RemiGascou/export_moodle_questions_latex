# -*- coding: utf-8 -*-

import re #regex

class MoodleQuestionBankData(object):
    """docstring for MoodleQuestionBankData."""
    def __init__(self):
        super(MoodleQuestionBankData, self).__init__()
        self.name = ""
        self.questions = []

    #GENERAL FUNCTIONS ---------------------------------------------------------
    def add_multichoice_question(self, type, question_name:str, question_text:str, correct_answers:list, wrong_answers:list, question_feedback:str):
        if type == "multichoice" :
            question_data = {
                'type' : type,
                'question_name' : self.cleanup(question_name),
                'question_text' : self.cleanup(question_text),
                'correct_answers' : self.cleanup(correct_answers),
                'wrong_answers' : self.cleanup(wrong_answers),
                'question_feedback' : self.cleanup(question_feedback),
            }
            self.questions.append(question_data)
            return 0
        else :
            return -1

    def add_matching_question(self, type, question_name:str, question_text:str, subquestions:list, subquestions_answers:list, question_feedback:str):
        if type == "matching" :
            question_data = {
                'type' : type,
                'question_name' : self.cleanup(question_name),
                'question_text' : self.cleanup(question_text),
                'subquestions' : self.cleanup(subquestions),
                'subquestions_answers' : self.cleanup(subquestions_answers),
                'question_feedback' : self.cleanup(question_feedback),
            }
            self.questions.append(question_data)
            return 0
        else :
            return -1

    def cleanup(self,e):
        def _handle(s):
            #Charset handles
            out = s.replace("\n", "")
            out = out.replace("$", "\\$")
            out = out.replace("_", "\\_")
            #Styles handles
            out = out.replace("<b>", "\\textbf{")
            out = out.replace("</b>", "}")
            #HTML Handles
            out = out.replace("<br>", "")
            out = out.replace("<p>", "")
            out = out.replace("</p>", "")
            out = re.sub('<span .*?>.*?</span>','',out, flags=re.DOTALL)
            out = re.sub('<form .*?>.*?</form>','',out, flags=re.DOTALL)
            return out
        if e is None:
            e = ""
        elif type(e) == str:
            if e.replace(" ","") == "":
                return ""
            else :
                e = _handle(e)
        elif type(e) == list:
            for k in range(len(e)):
                e[k] = _handle(e[k])
        return e

    def gen_question_struct(self, question):
        out = """"""
        if type == "multichoice":
            out += """\\medskip\n\n\\begin{itemize}\n"""
            for ca in question['correct_answers']:
                out += """\t\\item \\fbox{\\parbox{15cm}{\\textbf{""" + ca.replace("\n", "") + """}}}\n"""
            for cw in question['wrong_answers']:
                out += """\t\\item """ + cw.replace("\n", "") + """\n"""
            out += """\\end{itemize}\n"""
        elif type == "matching":
            out += """\\medskip\n\n\\begin{itemize}\n"""
            for k in range(len(question['subquestions'])):
                out += """\t\\item """ + question['subquestions'][k].replace("\n", "") + """\n\t\\begin{itemize}\n\t\t\\item[$\bullet$] """ + question['subquestions_answers'][k].replace("\n", "") + """\n\t\\end{itemize}\n"""
            out += """\\end{itemize}\n"""
        return out

    def export_to_latex_file(self, filename="moodle_exported.latex", path=""):
        #Writing file
        f = open(path+filename,'w')
        f.write(self.export_to_latex_str())
        f.close()

    def export_to_latex_str(self):
        questions_separator = """%-------------------------------------------------------------------------------"""
        out_latex = """\\section{""" + self.name + """}\n\\hrule\n\\bigskip\n\n"""
        for q in self.questions:
            out_latex += questions_separator + """\n\\subsection{""" + q['question_name'] + """}\n"""
            out_latex += """""" + q['question_text'] + """\n"""
            out_latex += self.gen_corr_struct(q['correct_answers'], q['wrong_answers']) + """\n"""
            out_latex += """\\subsubsection*{Corrigé}\n""" + q['question_feedback'] + """\n\\medskip\n\n"""
        return out_latex

    #GET SET -------------------------------------------------------------------
    #NAME
    def get_name (self):
        return self.name

    def set_name (self, name:str):
        self.name = name



if __name__ == '__main__':
    d = MoodleQuestionBankData()
    d.set_name("MQB 1")
