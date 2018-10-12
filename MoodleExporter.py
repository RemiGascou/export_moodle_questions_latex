# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET

class MoodleExporter(object):
    """docstring for MoodleExporter."""
    def __init__(self, config:MoodleExporterConfig):
        super(MoodleExporter, self).__init__()
        self.config = config

    def export(self):
        bd = self.config.get_latex_mainheader()
        bd += """\n\n\n\\begin{document}\n\t\\maketitle\n"""
        if self.config.has_latex_tableofcontents():
            bd += """\n\t\\tableofcontents\n\\newpage\n\n"""
        for file in self.config.get_source_files():
            bd += moodle_exporter(file)
            if self.config.each_file_newpage():
                bd += """\n\\newpage\n\n"""
        return bd

    def export_to_file(self, pathtofilename="moodle_exported.latex":str):
        #Writing file
        f = open(path+filename,'w')
        f.write(self.export())
        f.close()

    def moodle_exporter(pathtofilename:str):
        mqb = MoodleQuestionBankData()
        tree = ET.parse(pathtofilename)
        quiz = tree.getroot()
        for question in quiz:
            if question.attrib['type'] == 'multichoice':
                question_name = question.find('name').find('text').text
                question_text = question.find('questiontext').find('text').text
                question_feedback = question.find('generalfeedback').find('text').text
                correct_answers = [a.find('text').text for a in question.findall('answer') if a.attrib['fraction'] != "0"]
                wrong_answers = [a.find('text').text for a in question.findall('answer') if a.attrib['fraction'] == "0"]
                mqb.add_multichoice_question(
                    question.attrib['type'],
                    question_name,
                    question_text,
                    correct_answers,
                    wrong_answers,
                    question_feedback
                )
            elif question.attrib['type'] == 'matching':
                question_name = question.find('name').find('text').text
                question_text = question.find('questiontext').find('text').text
                question_feedback = question.find('generalfeedback').find('text').text
                subquestions = [a.find('text').text for a in question.findall('subquestions') if a.attrib['fraction'] != "0"]
                subquestions_answers = [a.find('answer').find('text').text for a in question.findall('subquestions') if a.attrib['fraction'] == "0"]
                mqb.add_matching_question(
                    question.attrib['type'],
                    question_name,
                    question_text,
                    subquestions,
                    subquestions_answers,
                    question_feedback
                )
            elif question.attrib['type'] == 'category':
                mqb.set_name(question.find('category').find('text').text.replace("$course$/", ""))
            else :
                print(question.find('name').find('text').text)
        return mqb.export_to_latex_str()

if __name__ == '__main__':
    pass
