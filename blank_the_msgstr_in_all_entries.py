#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# Copyright 2012 Leandro Regueiro
# 
# This code is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This code is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this code.  If not, see <http://www.gnu.org/licenses/>.

#TODO fix for passing the files and options as parameters in command line
lang = "gl"

fich = open("DJL." + lang + ".po", "r")
lines = fich.readlines()
fich.close()
resul = open("DJL_FINAL." + lang + ".po", "w")

i = 0
msgstr_atopado = False
listo_para_escribir_entrada = False
ainda_non_pasou_a_cabeceira = True


for l in lines:
    i = i + 1
    
    if ainda_non_pasou_a_cabeceira:
        resul.write(l)
        if l.startswith("msgstr \""):
            ainda_non_pasou_a_cabeceira = False
    else:
        # TODO fix for getting it working with plurals
        if l.startswith("msgstr \""):
            msgstr_atopado = True
        elif l == "\n":
            msgstr_atopado = False
            listo_para_escribir_entrada = True
        
        
        if msgstr_atopado:
            pass
        elif listo_para_escribir_entrada:
            # Write the whole entry at once
            listo_para_escribir_entrada = False
            resul.write("msgstr \"\"\n\n")
        else:
            resul.write(l)

resul.close()



