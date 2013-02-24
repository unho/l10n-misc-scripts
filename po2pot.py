#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# Copyright 2012, 2013 Leandro Regueiro
# 
# This code is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
# 
# This code is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE.  See the GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License along with
# this code.  If not, see <http://www.gnu.org/licenses/>.

import sys
import optparse

def write_fresh_header(outputfile):
    outputfile.write("""# SOME DESCRIPTIVE TITLE.
# Copyright (C) YEAR THE PACKAGE'S COPYRIGHT HOLDER
# This file is distributed under the same license as the PACKAGE package.
# FIRST AUTHOR <EMAIL@ADDRESS>, YEAR.
#
#, fuzzy
msgid \"\"
msgstr \"\"
\"Project-Id-Version: PACKAGE VERSION\\n\"
\"Report-Msgid-Bugs-To: \\n\"
\"POT-Creation-Date: 2012-12-02 15:39+0100\\n\"
\"PO-Revision-Date: YEAR-MO-DA HO:MI+ZONE\\n\"
\"Last-Translator: FULL NAME <EMAIL@ADDRESS>\\n\"
\"Language-Team: LANGUAGE <LL@li.org>\\n\"
\"MIME-Version: 1.0\\n\"
\"Content-Type: text/plain; charset=CHARSET\\n\"
\"Content-Transfer-Encoding: 8bit\\n\"
\"Plural-Forms: nplurals=INTEGER; plural=EXPRESSION;\\n\"

""")

if __name__ == '__main__':
    parser = optparse.OptionParser()
    parser.add_option("-i", "--input", dest="inputfilename",
                      help="read from INPUT in po format", metavar="INPUT")
    parser.add_option("-o", "--output", dest="outputfilename",
                      help="write to OUTPUT in pot format", metavar="OUTPUT")
    (options, args) = parser.parse_args()

    # If no input filename is provided.
    if options.inputfilename == None:
        parser.print_help()
        sys.exit(1)

    try:
        inputfile = open(options.inputfilename, "r")
        inputlines = inputfile.readlines()
        inputfile.close()
    except IOError:
        print("\nError: the input file \"%s\" couldn't be opened.\n" %
              options.inputfilename)
        sys.exit(1)

    if options.outputfilename == None:
        outputfile = sys.stdout
    else:
        try:
            outputfile = open(options.outputfilename, "w")
        except IOError:
            print("\nError: the output file \"%s\" couldn't be opened.\n" %
                  options.outputfilename)
            sys.exit(1)

    header_not_yet_finished = True
    msgstr_found = False
    plural_found = False

    # Write a fresh header for the POT file.
    write_fresh_header(outputfile)

    for line in inputlines:
        if header_not_yet_finished:
            if line == "\n":
                header_not_yet_finished = False
        else:
            if line.startswith("msgstr \""):
                # Because msgstr entries can expand to several lines.
                msgstr_found = True
            elif line.startswith("msgstr[0] \""):
                # Because plural entries can expand to several lines.
                plural_found = True
            elif line == "\n":
                # Write the msgstr or msgstr[n] blank entries.
                if msgstr_found:
                    msgstr_found = False
                    outputfile.write("msgstr \"\"\n\n")
                elif plural_found:
                    plural_found = False
                    outputfile.write("msgstr[0] \"\"\nmsgstr[1] \"\"\n\n")
            elif line.startswith("#, fuzzy"):
                # If another flag is present then just remove the fuzzy flag,
                # but if no other flag is present then remove the entire line.
                if not line == "#, fuzzy":
                    outputfile.write(line.replace(", fuzzy", ""))
            elif not (line.startswith("#~ ") or line.startswith("# ") or
                      line.startswith("#| ") or msgstr_found or plural_found):
                # Write the read line in case that it doesn't match any of this
                # particular cases: obsolete strings, translator comments,
                # previous untranslated strings, the current line is within a
                # msgstr or msgstr[n].
                outputfile.write(line)

    outputfile.close()



