# -*- coding: utf-8 -*-

#https://docs.python.org/2/library/xml.etree.elementtree.html

import xml.etree.ElementTree as ET

def moodle_exporter(filename_in, path_in="", filename_out="", path_out=""):
    mqb = MoodleQuestionBankData()
    tree = ET.parse(path + filename_in)
    quiz = tree.getroot()
    for question in quiz:
        if question.attrib['type'] == 'multichoice':
            question_name = question.find('name').find('text').text
            question_text = question.find('questiontext').find('text').text
            question_feedback = question.find('generalfeedback').find('text').text
            correct_answers = [a.find('text').text for a in question.findall('answer') if a.attrib['fraction'] != "0"]
            wrong_answers = [a.find('text').text for a in question.findall('answer') if a.attrib['fraction'] == "0"]
            mqb.add_question(
                question.attrib['type'],
                question_name,
                question_text,
                correct_answers,
                wrong_answers,
                question_feedback
            )
        elif question.attrib['type'] == 'category':
            mqb.set_name(question.find('category').find('text').text.replace("$course$/", ""))
        else :
            print(question.find('name').find('text').text)
    #mqb.export_to_latex_str(filename_out, path_out)
    return mqb.export_to_latex_str()

if __name__ == '__main__':
    path = r'/home/administrateur/Bureau/export_moodle_questions_latex/test/'
    filename_out = 'exported.latex'
    
    bd = """"""
    bd += moodle_exporter('quizz_SPOC_cas1.xml', path_in=path) + """\n\\newpage\n\n"""
    bd += moodle_exporter('quizz_SPOC_cas2.xml', path_in=path) + """\n\\newpage\n\n"""
    bd += moodle_exporter('quizz_SPOC_cas3.xml', path_in=path)
    
    f = open(r'/home/administrateur/Bureau/export_moodle_questions_latex/' + filename_out,'w')
    f.write(bd)
    f.close()
