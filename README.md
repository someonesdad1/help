# help
Collection of plain text help files (use with vim for fast navigation).

**To use**:  run the `build.py` script (you will need some of the modules
from /plib (see below)).  This will populate the `output` directory with
the help files.  Run `build.py -h` to see how to set things up to use with
vim.  When things are set up properly, open the `output/index.hlp` file in
vim.  Position the cursor on a word and press ^] to jump to the associated
help file.

This should build with python 3.7 or later.

# Notes

1. See [plib](https://github.com/someonesdad1/plib) for the needed modules
   to run the python scripts in this repository.  In the python scripts,
   these are imported in the section labeled "Custom imports".
1. The `contents/math_.py` script may not work for you if you don't have a
   Unicode-capable terminal.  If you don't, change the `uni` global variable
   to False.

# History

I've been collecting various forms of information most of my adult life.
In the 1970's when inexpensive computers started appearing, it became
feasible to start collecting and storing this information in digital form.
When I learn a new tool, I'll often make up a new help subdocument for it,
particularly if I plan on using that tool on a regular basis.  Since I do
most of my work in terminal windows, this is a good form for the data, as
it is quickly accessed using vim.

Repository created 14 Mar 2022

The material in this repository is released under the OSL 3.0 license.
