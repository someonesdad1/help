# help
Collection of plain text help files (use with vim for fast navigation)

To use:  run the build.py script.  This will populate the 'output'
directory with the help files.  Run build.py with an argument and it will
tell you how to set things up to use with vim.  When things are set up
properly, open the output/index.hlp file.  Position the cursor on a word
and press ^] to jump to the associated help file.

I used python 3.7.12 to test the scripts in this repository.

# Notes

1. See [plib](https://github.com/someonesdad1/plib) for the needed modules
   to run the python scripts in this repository.  In the python scripts,
   these are imported in the section labeled "Custom imports".
1. The contents/math_.py script may not work for you if you don't have a
   Unicode-capable terminal.  If you don't, change the uni global variable
   to False.

# History

I've been collecting various forms of information most of my adult life.
In the 1970's when inexpensive computers started appearing, it became
feasible to start collecting and storing this information in digital form.  
You're forced to do such things as a research engineer/scientist because
1) you need that information to help with decisions and 2) you need to
attribute your sources.  This stuff is a mish-mash of varying quality and
it could benefit from a careful editor.  But I don't want to invest any
time with it, so it has been static for quite a while.  However, when I
learn a new tool, I'll often make up a new help subdocument for it,
particularly if I plan on using that tool on a regular basis.  Since I do
most of my work in terminal windows on my Windows/Mac/Linux boxes, this is
a good form for the data, as it is quickly accessed using vim.

Repository created 14 Mar 2022

The material in this repository is released under the OSL 3.0 license.
