'''
Script for building help documentation
Created 13 Mar 2022

    - Build steps
        - Construct each content file in the output directory
        - Make the tags file in the output directory
        - Make the index file index.hld in the output directory
            - Done now by makeindex.c, but move it to a python script that
              also does tags processing
    - Directory structure
        - content:  location of help files
        - doc:  documentation on help system
        - tools:  scripts, etc.
        - output:  deployment of build's files

'''
if 1:  
    # Copyright, license
        # These "trigger strings" can be managed with trigger.py
        #∞copyright∞# Copyright (C) 2022 Don Peterson #∞copyright∞#
        #∞contact∞# gmail.com@someonesdad1 #∞contact∞#
        #∞license∞#
        #   Licensed under the Open Software License version 3.0.
        #   See http://opensource.org/licenses/OSL-3.0.
        #∞license∞#
        #∞what∞#
        # Build help files
        #∞what∞#
        #∞test∞# #∞test∞#
    # Standard imports
        import os
        from pathlib import Path as P
        import re
        import sys
        from pdb import set_trace as xx
    # Custom imports
        from wrap import wrap, dedent
        from f import flt
        from clr import Clr
        from columnize import Columnize
        if len(sys.argv) > 1:
            import debug
            debug.SetDebugger()
    # Global variables
        c = Clr()
        class g: pass
        g.output = P("output")
        g.content = P("content")
        g.help = P("hldhelp.vim")
        g.suffix = ".hld"
        g.index = "index" + g.suffix
        c.err = c("lred")
if 1:   # Help
    def Help():
        print(dedent(f'''
        This script constructs 'help' files in '{g.output}' with extensions
        {g.suffix} that are intended to be opened by vim.  These *{g.suffix}
        files are copies of those in '{g.content}', so you can (accidentally)
        edit them without changing the original content.

        You can read these files in any editor, but using vim is preferred
        because it will syntax highlight the topics.

        To use these files with vim, you'll need to utilize the '{g.help}'
        file.  This is the relevant command I use in my vimrc file:

            autocmd BufRead *.hld source $MYVIMFILES/syntax/hldhelp.vim

        I also use the following:

            autocmd BufRead *.hld noremap q :q!<cr>:unmap q
            " How to return from a tag jump in a help file
            autocmd BufRead *.hld noremap t ^T

        The first lets me exit the help file by pressing the 'q' key.  The
        second lets me return from a tags jump (^]) by pressing the 't' key.

        These help files are formatted to fit in an 80 column wide terminal
        window.  You can reformat them as needed if you use a different width.
        '''))
        exit(0)
if 1:   # Core functionality
    def GetContentFiles():
        'Get list of files in the content directory'
        files = '''

            arduino asciidoc astronomical awk bash basic bibtex biology c
            chemistry constants cpp cvs darcs electrical engineering find
            flex g gdb git go hg hp3488 hp42s hp49 html korn make_ markdown
            materials math mathematica matplotlib mpmath numpy office
            pandoc pcl5 perl4 perl5 physics ps pygame python rst scipy
            scons sed shop shop.densities simpy sizes snippets sql
            statistics stl subversion svn sympy thermal_cond tmux
            uncertainties units utilities yaml

        '''.split()
        return files
    def CopyContentFiles(content_files):
        '''In the output directory, create copies of the content files.
        We make copies instead of hard links because a user in an editor
        might make a change to them.  Note these copies will have the 
        suffix '.hld' so that the custom syntax file for vim will color
        highlight them.
 
        Since this is something that can be done is less than a second, I
        just copy all the files every time.
        '''
        bytecount = 0
        for file in content_files:
            frm = g.content/file
            to = (g.output/file).with_suffix(g.suffix)
            try:
                s = open(frm).read()
                bytecount += len(s)
                open(to, "w").write(s)
            except UnicodeDecodeError as e:
                print(f"Error reading '{file}'")
                print(f"  {e}")
                exit(1)
        n = flt(bytecount/1e6)
        n.n = 2
        print(f"{len(content_files)} file copies in '{g.output.absolute()}' constructed "
              f"({n!s} MB)")
    def CopyLaunchScript():
        '''Copies the h script to the output directory.  There's really no
        need for this, as the script can be put anywhere and aliased, but 
        this is what I use, as it lets the output directly be copied
        anywhere.
        '''
        cwd = os.getcwd()
        file = P("h")
        assert(file.exists())
        to = g.output/file
        open(to, "w").write(open(file).read())
        to.chmod(0o774)
    def BuildTagsFile():
        '''Construct a tags file for the output directory.  For vim's help
        files, this is done by searching for text between two asterisk
        characters and extracting the tag.  This is written to the tags
        file in the form 
            symbol\tsymbol.hld\t/*symbol*
        and the file is sorted on these lines.  The first line of the file
        must be 'help-tags\ttags\t1'.
        '''
        cwd = os.getcwd()
        r = re.compile(f"\*([A-Za-z_][A-Za-z0-9_]*?)\*")
        tags = ["help-tags\ttags\t1"]
        # Change to the output directory since vim will be editing the
        # index.hld file in this directory.  Therefore we want no
        # directory names in the file's name.
        os.chdir(g.output)
        for file in P(".").glob(f"*{g.suffix}"):
            for line in open(file).readlines():
                mo = r.search(line)
                if mo:
                    gr = mo.groups()
                    if len(gr) > 1:
                        continue
                    tag = gr[0]
                    t = f"{tag}\t{file}\t/*{tag}*"
                    tags.append(t)
        # Get rid of duplicates
        tags = list(sorted(list(set(tags))))
        n = len(tags) - 1
        # Write the tags file
        t = P("tags")
        with open(t, "w") as f:
            f.write('\n'.join(tags))
        print(f"{n} tags constructed in {t.absolute()}")
        # Go to the directory we started from
        os.chdir(cwd)
    def MakeIndexFile():
        '''This is the file that we start the vim editor from; the links
        all go to other *.hld files.
        '''
        # Grouped by (topic, num_columns, column_width)
        groups = (('''
                    python
                    git
                    uncertainties
                    shop
                    bash
                    C
                    g
                    matplotlib
                    numpy
                    sympy
                    Cpp
                    gdb
                    scipy
                    mpmath
                    make_
                    Utilities
            ''', 3, 20),
            ('''
                Electrical
                Physics
                Math
                Engineering
                Astronomy
                Units
                Statistics
                constants
                Biology
                Chemistry
                Office
            ''', 3, 20),
            ('''
                arduino
                asciidoc
                awk
                basic
                bibtex
                csvkit
                cvs
                darcs
                find
                fld
                flex
                hg
                hp3488
                HP42s
                HTML
                Korn_Shell
                markdown
                Mathematica
                mortgage
                mysql
                NSF
                pandoc
                PCL5
                perl4
                perl5
                PostScript
                pygame
                rst
                sed
                Snippets
                STL
                Subversion
                tmux
                Windows
                yaml
            ''', 0, 0),
        )
        cwd = os.getcwd()
        os.chdir(g.output)
        index = P(g.index)
        count = 0
        with open(index, "w") as f:
            for group, n, w in groups:
                G = group.split()
                count += len(G)
                lines = Columnize(G, columns=n, col_width=w)
                for line in lines:
                    print(line, file=f)
                print("", file=f)
        print(f"Index file {index.absolute()} constructed ({count} topics)")
        os.chdir(cwd)
if __name__ == "__main__": 
    if len(sys.argv) > 1:
        Help()
    g.content_files = GetContentFiles()
    CopyContentFiles(g.content_files)
    BuildTagsFile()
    MakeIndexFile()
    print(dedent(f'''

    Include an argument for an explanation of the script.
    See doc/readme.pdf for documentation.
    '''))
