l10n-misc-scripts
=================

Several scripts for l10n basic tasks:

po2pot
  script for converting a Gettext PO file in a Gettext POT file by blanking all the msgstr fields in all entries, and generating a fresh header.

invert_msgid_and_msgstr_in_one_file
  script for inverting the msgid and msgstr fields in all entries in a Gettext PO file.

create_po_from_two_non_english_source_files
  script for creating a Gettext PO file from two Gettext PO files having each of them a source language which is not English. This can be used for creating a PO file with english in the msgid and translations for another language in the msgstr for a project that, for example, uses French in the msgid fields.


License
-------
This software is licensed under the GNU General Public License 3.0 (http://www.gnu.org/licenses/gpl-3.0.txt), a copy of which can be found in the LICENSE file.

