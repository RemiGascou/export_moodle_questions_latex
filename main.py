# -*- coding: utf-8 -*-

from lib import *

if __name__ == '__main__':
    mtle_c = MoodleToLatexExporterConfig()
    mtle_c.add_source_file("lib/testdata/moodle.xml")

    mtle = MoodleToLatexExporter(mtle_c)
    mtle.export_to_file("lib/testdata/output.latex")
