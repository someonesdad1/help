#!/bin/bash
# Demonstrate the output of various tests

clear
P()
{
    local cmd="$1"
    local status="$2"
    local expl="$3"
    printf "%-20s    %-6s    %s\n"  "$cmd"  "$status" "$expl"
}
E() 
{
    local cmd="$1"
    local expl="$2"
    eval $cmd
    P "$cmd" $? "$expl"
}
echo "Examples of tests (0 is true, 1 is false)"
fmt="%-20s    %-6s    %s\n"
printf "$fmt" "Test"  "Status" "Explanation"
printf "$fmt" "----"  "------" "-----------"

E '[ ]'             "Unset string"
E 'test'            "Ditto"
E '[ "" ]'          "Empty string"
E 'test ""'         "Ditto"
E '[ " " ]'         "String with single space character"
E 'test " "'        "Ditto"
echo "These show 'test' and '[' ... ']' are equivalent"
E '[ "a" ]'         "String with single character"
E '[ a ]'           "Ditto"
E '[ 0 ]'           "Ditto"
E '[ 1 ]'           "Ditto"
E '[ - ]'           "Ditto"
E '[ " " -a "" ]'   "AND of true string and empty string"
E '[ " " -a " " ]'  "AND of two true strings"
E '[ "" -o "" ]'    "OR of two false strings"
E '[ " " -o "" ]'   "OR of true string and empty string"
echo
echo '[[ ]]            syntax error'
E '[[ " " ]]'
E '[[ "a" ]]'
E '[[ 0 ]]'
E '[[ 1 ]]'
E '[[ - ]]'
echo
E '((4 > 5))'
E '((4 > 3))'
E '((4 == 3))'
E '((4 != 3))'
