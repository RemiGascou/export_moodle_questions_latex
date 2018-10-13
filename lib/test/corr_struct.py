# -*- coding: utf-8 -*-

def gen_corr_struct(correct_answers:list, wrong_answers:list):
    out = """\\medskip\n\n\\begin{itemize}\n"""
    for ca in correct_answers:
        out += """\t\\item \\fbox{\\parbox{15cm}{\\textbf{""" + ca.replace("\n", "") + """}}}\n"""
    for cw in wrong_answers:
        out += """\t\\item """ + cw.replace("\n", "") + """\n"""
    out += """\\end{itemize}\n"""
    return out

if __name__ == '__main__':
    print(gen_corr_struct(["TrueA", "TrueB"], ["WrongA","WrongB", "WrongC"]))
