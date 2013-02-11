#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# Copyright 2012 Leandro Regueiro
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

#TODO fix for passing the files and options as parameters in command line
lang = "gl"
proxecto = "foofind"
clave_vale_como_msgctxt = True
inicio = 17 # Número de liña no que remata a cabeceira do .po

dic = {}

enf = open(proxecto + ".en.po", "r")
glf = open(proxecto + "." + lang + ".po", "r")
resul = open(proxecto + "_FINAL." + lang + ".po", "w")
lines = enf.readlines()
enf.close()


i = 0

msgid = ""
msgstr = ""

msgid_atopado = False
msgstr_atopado = False
listo_para_escribir_entrada = False
ainda_non_pasou_a_cabeceira = True


for l in lines:# Iterate first over the source translation file (usually the english one)
    i = i + 1
    
    if i > inicio:
        # TODO fix for getting it working with plurals
        if l.startswith("msgid \""):
            msgid_atopado = True
        elif l.startswith("msgstr \""):
            msgid_atopado = False
            msgstr_atopado = True
        elif l == "\n":
            msgid_atopado = False
            msgstr_atopado = False
            listo_para_escribir_entrada = True
        
        if msgid_atopado:
            msgid += l
        elif msgstr_atopado:
            msgstr += l
        elif listo_para_escribir_entrada:
            # Write the whole entry at once
            listo_para_escribir_entrada = False
            msgstr = msgstr.replace("msgstr ", "msgid ", 1)
            dic[msgid] = msgstr
            msgid = ""
            msgstr = ""


linesgl = glf.readlines()
glf.close()

i = 0
msgid = ""
msgstr = ""
cache = ""# For caching the lines in each entry before the msgid (the comments)

msgid_atopado = False
msgstr_atopado = False
listo_para_escribir_entrada = False
ainda_non_pasou_a_cabeceira = True


for l in linesgl:# Iterate first over the target translation file
    i = i + 1
    
    if ainda_non_pasou_a_cabeceira:
        resul.write(l)
        if l.startswith("msgstr \""):
            ainda_non_pasou_a_cabeceira = False
    else:
        # TODO fix for getting it working with plurals
        if l.startswith("msgid \""):
            msgid_atopado = True
        elif l.startswith("msgstr \""):
            msgid_atopado = False
            msgstr_atopado = True
        elif l == "\n":
            msgid_atopado = False
            msgstr_atopado = False
            listo_para_escribir_entrada = True
        
        if msgid_atopado:
            msgid += l
        elif msgstr_atopado:
            msgstr += l
        elif listo_para_escribir_entrada:
            # Write the whole entry at once
            listo_para_escribir_entrada = False
            resul.write(cache)
            if clave_vale_como_msgctxt:
                resul.write(msgid.replace("msgid ", "msgctxt ", 1))
            resul.write(dic[msgid]) 
            resul.write(msgstr)
            resul.write(l)
            #try:
            #    resul.write(cache)
            #    resul.write(dic[msgid]) 
            #    resul.write(msgstr)
            #    resul.write(l)
            #except KeyError:
            #    pass
            msgid = ""
            msgstr = ""
            cache = ""
        else:
            cache += l

resul.close()



