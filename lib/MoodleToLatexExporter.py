# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET
from lib.MoodleToLatexExporterConfig import *
from lib.MoodleQuestionBankData import *


class MoodleToLatexExporter(object):
    """docstring for MoodleToLatexExporter."""
    def __init__(self, config:MoodleToLatexExporterConfig):
        super(MoodleToLatexExporter, self).__init__()
        self.config = config

    def export(self):
        if len(self.config.get_source_files()) != 0:
            bd = self.config.get_latex_mainheader()
            bd += ("""\n\n\n\\begin{document}\n\t\\maketitle\n""").encode("utf-8")
            if self.config.has_latex_tableofcontents():
                bd += ("""\n\t\\tableofcontents\n\\newpage\n\n""").encode("utf-8")
            for file in self.config.get_source_files():
                bd += self.export_worker(file)
                if self.config.each_file_newpage():
                    bd += ("""\n\\newpage\n\n""").encode("utf-8")
            bd += ("""\n\\end{document}\n""").encode("utf-8")
            return bd
        else :
            return None

    def export_to_file(self, pathtofilename="moodle_exported.latex"):
        if len(self.config.get_source_files()) != 0:
            #Writing file
            f = open(pathtofilename,'wb')
            f.write(self.export())
            f.close()
            return 0
        else :
            return -1

    def export_worker(self, pathtofilename_in:str):
        mqb = MoodleQuestionBankData()
        tree = ET.parse(pathtofilename_in)
        quiz = tree.getroot()
        for question in quiz:
            if   question.attrib['type'] == 'multichoice':
                question_name = question.find('name').find('text').text
                question_text = question.find('questiontext').find('text').text
                question_feedback = question.find('generalfeedback').find('text').text
                correct_answers = [a.find('text').text for a in question.findall('answer') if a.attrib['fraction'] != "0"]
                wrong_answers = [a.find('text').text for a in question.findall('answer') if a.attrib['fraction'] == "0"]
                mqb.add_multichoice_question(question.attrib['type'], question_name, question_text, correct_answers, wrong_answers, question_feedback)
            elif question.attrib['type'] == 'matching':
                question_name = question.find('name').find('text').text
                question_text = question.find('questiontext').find('text').text
                question_feedback = question.find('generalfeedback').find('text').text
                subquestions = [a.find('text').text for a in question.findall('subquestions') if a.attrib['fraction'] != "0"]
                subquestions_answers = [a.find('answer').find('text').text for a in question.findall('subquestions') if a.attrib['fraction'] == "0"]
                mqb.add_matching_question(question.attrib['type'], question_name, question_text, subquestions, subquestions_answers, question_feedback)
            elif question.attrib['type'] == 'truefalse':
                question_name = question.find('name').find('text').text
                question_text = question.find('questiontext').find('text').text
                question_feedback = question.find('generalfeedback').find('text').text
                if question.find('answer').find('text').text and question.find('answer').attrib['fraction'] == "100":
                    answer = False
                else :
                    answer = False
                mqb.add_truefalse_question(question.attrib['type'], question_name, question_text, answer, question_feedback)
            elif question.attrib['type'] == 'category':
                mqb.set_name(question.find('category').find('text').text.split("/")[-1])
            else :
                print("[Not recognized : type == " + question.attrib['type'] + "] " + question.find('name').find('text').text)
        return mqb.export_to_latex_bstr()

if __name__ == '__main__':
    pass
