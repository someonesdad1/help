#!/bin/sh
#
# Help launcher
#
# 19 Jun 2014:  updated to run on Linux.

set +x

main()
{
    Initialize "$@"
    candidates=$(GetCandidates "$1")

    [ "$1" = "xxpython" ] && exec $EDITOR +4 python.hld

    if [ "$candidates" ] ; then
        exec $EDITOR +/"$search_for" $candidates
    else
        exec $EDITOR $index_file
    fi
}

Initialize()
{
    ext=hld
    # Location of the help files has changed over the years
    #dir=$DPBIN/bat/help_system
    #dir=/help/help_system
    dir=/help/output
    cd $dir
    index_file=index.hld
    for file in *.hld ; do
        filelist="$filelist $file"
    done

    if [ $# -eq 0 ] ; then
        exec $EDITOR $index_file
    fi

    # If the -i flag was on the command line, make the grep search
    # case sensitive.

    if [ "$1" = "-i" ] ; then 
        grep_flags="-l"
        shift
    else
        grep_flags=-il
    fi
    search_for="$1"
}

GetCandidates()
{
    for f in $(grep $grep_flags $search_for $filelist) ; do
        files="$files $f"
    done
    echo "$files"
}

#----------------------------------------------------------------------
pgmname=$(basename $0)
main "$@"
