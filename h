#!/bin/bash

# Help launcher
 
# This script is used to launch my help files, viewing them in vim.  With no arguments, open
# output/index.hld in vim to allow access to all the help files 
 
# With one argument, make it lowercase and append .hld; if it matches a file in
# output/, open this file.  Otherwise, the argument is a case-sensitive regex; open all the *.hld
# files that contain it.

set -u      # Error on unset variables
 
Initialize()    
{
    # Get our variables and cd to the /help/output directory:
        # ext:          Extension of our help files
        # helpdir:      Location of the *.hld files we'll search
        # index_file    Core index file for the help files 
        # filelist      List of *.hld files in $helpdir
 
    # Extension of the help files.  In my .vimrc, this is accomanied by 
    #   'autocmd BufRead *.hld source $dpvim/syntax/donhelp.vim'
    # which provides syntax coloring.  I also use 
    #   'autocmd BufRead *.hld noremap q :q!<cr>:unmap q'
    # to allow me to quit using the 'q' key.  Also,
    #   'autocmd BufRead *.hld noremap t ^T' 
    # lets me use the 't' key to return from a jump to a tag.
    ext=hld
 
    # Location of the help *.hld files
    helpdir=/help/output
 
    # Core index file for all the help files.  This file is viewed in vim by default with the tags
    # highlighted.
    index_file=index.hld
 
    # Get a list of the *.hld files in $helpdir
    cd "$helpdir" || { echo "Could not cd to '$helpdir'" ; exit 1 ; }
    filelist=""
    for file in *.$ext ; do
        filelist="$filelist $file"
    done
 
    # Make variables readonly
    readonly helpdir ext index_file filelist
}
GetFilesToOpen()
{
    # Echo a list of the files to open.  Note the search is always case-sensitive because I like to
    # use vim's ability to open on the searched-for regex and there's no way to make this case
    # insensitive.
    "$dpub"/grep -lE --color=never "$1" *."$ext"
}
main()
{
    Initialize      # Get our variables
    # Note we are now in /help/output
 
    # I open the python help file the most, so if the first argument is 'xxpython', do so
    [ "${1-}" = "xxpython" ] && exec "$EDITOR" +4 python.hld
    # With no arguments, open $index_file
    [ -z "${1-}" ] && exec "$EDITOR" "$index_file"
 
    # $1 is a regex to search for.  First, see if it matches one of the help *.hld files.
    [ -r "${1}.$ext" ] && exec "$EDITOR" "${1}.$ext"
 
    # No, it's not an index file, so find all *.hld files that contain the regex and open them
    local regex
    regex="${1?Need a regex}"
    files=$(GetFilesToOpen "$regex")
    if [ "$files" ] ; then
        # Had one or more matches to regex.  Note we can't use the handy '+/"$regex"' vim option to
        # position on the regex because, in general, the search was case-insensitive and vim
        # doesn't have a command line option to do this.
        exec "$EDITOR" -p +/"$regex" $files
    else
        # regex didn't match in any of the files
        exec $EDITOR $index_file
    fi
}
main "$@"
