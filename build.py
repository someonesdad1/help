'''
To change index file order, edit MakeIndexFile()

    Script for building help documentation
    Created 13 Mar 2022
    
    - To add a new topic
        - Create a file in ./content directory
            - Make sure there are suitable objects to be tagged like 
              '*mswindows*'
        - Add this file to files in GetContentFiles()
        - Run this script (build.py)
    
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
if 1:  # Header
    _pgminfo = '''
        <oo gist ∞ Script for building help documentation oo>
        <oo desc ∞ oo>
        <oo copy ∞ Copyright © 2022 Don Peterson oo>
        <oo lic ∞ MIT License
            Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
            The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
            THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
        oo>
        <oo ind ∞ 8 indent oo>
        <oo cat ∞ utility oo>
        <oo test ∞ notest oo>
        <oo todo ∞ 

            - On 4 Feb 2026 I added the WinMerge help file and added 'winmerge' to
              index.hld, but it didn't show up when I typed 'hh'.  Thus, I need to see
              more details of how the build works.  To do this, I'll add a Dbg command
              that is used when -d is on the command line, as it will show all the
              details of the build.

        oo>
    '''
    if 1:  # Standard imports
        from pathlib import Path as P
        import getopt
        import os
        import re
        import sys
    if 1:  # Custom imports
        from color import t
        from f import flt
        from wrap import dedent
        if 0:
            import debug
            debug.SetDebugger()
    if 1:  # Global variables
        ii = isinstance
        W = int(os.environ.get("COLUMNS", "80")) - 1
        L = int(os.environ.get("LINES", "50"))
        class G:
            pass
        g = G()     # Instance whose attributes hold global variables
        g.dbg = False
        g.output = P("output")
        g.content = P("content")
        g.help = P("hldhelp.vim")
        g.suffix = ".hld"
        g.index = "index" + g.suffix
if 1:   # Utility
    def GetColors():
        t.err = t.redl
        t.help = t.lill
        t.concern = t.ornl if g.dbg else ""
        t.dbg = t.sky if g.dbg else ""
        t.N = t.n if g.dbg else ""
    def Dbg(*p, **kw):
        if g.dbg:
            print(f"{t.dbg}", end="")
            print(*p, **kw)
            print(f"{t.n}", end="")
    def Error(*msg, status=1):
        print(*msg, file=sys.stderr)
        exit(status)
    def Usage(status=0):
        print(dedent(f'''
        Usage:  {sys.argv[0]} [options] 
          Build my vim help files.
        Options:
          --debug   Drop into debugger on exception
          -d    Turn on debug mode
          -H    Print instructions
          -v    Don't output details at end
        '''))
        exit(status)
    def ParseCommandLine(d):
        d["-d"] = False     # Debug mode
        d["-v"] = True      # Verbose output
        try:
            opts, args = getopt.getopt(sys.argv[1:], "dHhv", 
                    ["help", "debug"])
        except getopt.GetoptError as e:
            print(str(e))
            exit(1)
        for o, a in opts:
            if o[1] in list("dv"):
                d[o] = not d[o]
            elif o == "-H":
                GetColors()
                Help()
            elif o in ("-h", "--help"):
                Usage()
                exit(0)
            elif o in ("--debug",):
                # Set up a handler to drop us into the debugger on an
                # unhandled exception
                import debug
                debug.SetDebugger()
        if d["-d"]:
            g.dbg = True
        GetColors()
        if d["-d"]:
            Dbg(f"Command line: {t.ornl}{sys.argv}")
            Dbg("Option settings:")
            for i in d:
                Dbg(f"  {i}    {t.ornl}{d[i]}")
        return args
if 1:   # Help
    def Help():
        print(dedent(f'''
        
        This script constructs 'help' files in the directory '{g.output}' with
        extensions '{g.suffix}' that are intended to be opened by vim.  These
        *{g.suffix} files are copies of those in '{g.content}', so you can
        (accidentally) edit them without changing the original content.
        
        You can read these files in any editor, but using vim is preferred because it
        will syntax highlight the topics.
        
        To use these files with vim, you'll need to utilize the '{g.help}' file.  This
        is the relevant command I use in my vimrc file:
        
            autocmd BufRead *.hld source $MYVIMFILES/syntax/hldhelp.vim
        
        I also use the following in my .vimrc file:
        
            autocmd BufRead *.hld noremap q :q!<cr>:unmap q
            " How to return from a tag jump in a help file
            autocmd BufRead *.hld noremap t ^T
        
        The first lets me exit the help file by pressing the 'q' key.  The second lets
        me return from a tags jump (^]) by pressing the 't' key.
        
        These help files are formatted to fit in an 80 column wide terminal window.  You
        can reformat them as needed if you use a different width. {t.help}

        - To add a new topic
            - Create a file in the ./content directory
                - Make sure there are suitable objects to be tagged like
                  '*this_is_a_tag*'
            - Add this file to files in build.py:GetContentFiles(){t.yel}
            - Edit build.py:MakeIndexFile() to create new index.hld file (you won't see
              your changes in the hh command if you don't do this){t.help}
            - Run this script (build.py){t.n}
        
        - Build steps
            - Construct each content file in the output directory
            - Make the tags file in the output directory
            - Make the index file index.hld in the output directory
                - Done now by makeindex.c, but move it to a python script that also does
                  tags processing
        - Directory structure
            - content:  location of help files
            - output:  deployment of build's files
        
        {t.help}See doc/readme.pdf for documentation.{t.n}
        '''))
        exit(0)
if 1:   # Core functionality
    def GetContentFiles():
        'Get list of files in the content directory'
        files = '''
        
            arduino asciidoc astronomical awk bash basic bibtex biology btop c chemistry
            conda constants cpp cvs darcs electrical engineering find flex g gdb git go hg
            hp3488 hp42s hp49 html json korn latex lua make_ markdown materials math
            mathematica matplotlib mpmath mswindows numpy office pandoc pcl5 perl4 perl5
            physics pil ps pygame python rst scipy scons sed shop simpy sizes snippets
            sql statistics_python statistics_tables stl subversion svn sympy
            thermal_cond tmux uncertainties units utilities vim winmerge yaml
        
        '''.split()
        # The following is used to detect when a file might have been left
        # off the list.
        curdir = os.getcwd()
        tgtdir = "/help/content"
        Dbg(f"Inspecting {tgtdir}")
        os.chdir(tgtdir)
        p = P(".")
        ignore = "a bash.ex.sh mk shop.densities tags .todo .vi z .z".split()
        Dbg(f"Ignoring {ignore}")
        for i in p.glob("*"):
            # Remove files we ignore
            if i.suffix == ".py" or str(i) in ignore:
                continue
            if i.suffix == ".swp":
                continue
            if str(i) not in files:
                t.print(f"{t.concern}Warning:  {i!s} not in GetContentFiles()")
                continue
        os.chdir(curdir)
        return files
    def CopyContentFiles(content_files):
        '''In the output directory, create copies of the content files.
        We make copies instead of hard links because a user in an editor
        might make a change to them.  Note these copies will have the 
        suffix '.hld' so that the custom syntax file for vim will color
        highlight them.
 
        Since this is something that can be done is less than a second, I
        just copy all the files every time this script is run.
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
        if d["-v"]:
            print(f"{len(content_files)} file copies in '{g.output.absolute()}' constructed "
                f"({n!s} MB)")
    def CopyLaunchScript():
        '''Copies the h script to the output directory.  There's really no
        need for this, as the script can be put anywhere and aliased, but 
        this is what I use, as it lets the output directly be copied
        anywhere.
        '''
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
        # This regex finds tags of the form '*abc1*'
        r = re.compile(r"\*([A-Za-z_][A-Za-z0-9_]*?)\*")
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
        if d["-v"]:
            print(f"{n} tags constructed in {t.absolute()}")
        # Go to the directory we started from
        os.chdir(cwd)
    def MakeIndexFile():
        '''This is the file that we start the vim editor from; the links
        all point to other *.hld files.
        '''
        # This file used to be made by the script, but now I prefer to be 
        # able to manually determine its structure here.
        data = dedent('''

        python numpy scipy
        arduino shop winmerge
        git markdown
        
        Science∇ (∇ means it's not a link)
            Physics Electrical Engineering Astronomy units constants Biology Chemistry
        Math
            mpmath matplotlib sympy StatisticsTables StatisticsPython Mathematica
        Prog∇
            bash vim conda C Cpp gdb g make_ PIL basic flex pygame Snippets STL perl4 perl5
            json uncertainties PCL5 yaml Korn_Shell lua
        VCS∇
            git hg darcs cvs Subversion
        Utilities 
            find awk sed tmux
        Doc∇
            markdown html pandoc rst latex Office bibtex asciidoc PostScript mswindows
        Hardware∇
            hp3488 HP42s 

        ''')
        cwd = os.getcwd()
        os.chdir(g.output)
        index = P(g.index)
        with open(index, "w") as f:
            print(data.rstrip(), file=f)
        os.chdir(cwd)
        Dbg("New index file:")
        for line in data.split("\n"):
            Dbg(f"{t.trql}  {line}")
        print("Successful build")
if __name__ == "__main__": 
    d = {}      # Options dictionary
    args = ParseCommandLine(d)
    g.content_files = GetContentFiles()
    CopyContentFiles(g.content_files)
    BuildTagsFile()
    MakeIndexFile()
