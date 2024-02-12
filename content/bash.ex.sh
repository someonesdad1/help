#!/bin/bash
# Demonstrate the output of various tests

set -u

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
TestExamples()
{
    echo "Examples of tests (0 is true, 1 is false) (output of bash.ex.sh script)"
    fmt="%-20s    %-6s    %s\n"
    printf "$fmt" "Test"  "Status" "Explanation"
    printf "$fmt" "----"  "------" "-----------"

    E '[ ]'             "Unset string"
    E 'test'            "Ditto"
    E '[ "" ]'          "Empty string"
    E 'test ""'         "Ditto"
    E '[ " " ]'         "Space character"
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
    P '[[ ]]' "--"      "Syntax error"
    E '[[ "" ]]'        "Empty string"
    E '[[ " " ]]'       "Space character"
    E '[[ "a" ]]'       "String with single character"
    E '[[ a ]]'         "String with single character"
    E '[[ 0 ]]'         "Ditto"
    E '[[ 1 ]]'         "Ditto"
    E '[[ - ]]'         "Ditto"
    echo
    echo "Arithmetic expressions (double quotes are removed from expression)"
    echo "  Status is 0 if expression value != 0, 1 otherwise (opposite from [...])"
    E '(( ))'           "Null string"
    E '(( "" ))'        "Empty string (quotes removed, so same as previous)"
    E '(( " " ))'       "Non-empty string, (quotes removed, so same as previous)"
    E '(( 0 ))'         "Expr value is 0, so return 1"
    E '(( 1 ))'         "Expr value is != 0, so return 0"
    E '(( 1 - 1 ))'     "Expr value is 0, so return 1"
    E '(( 1 + 1 ))'     "Expr value is 1, so return 0"
    E '(( 1/1 ))'       "Expr value is 1, so return 0"
    E '(( 1/2 ))'       "Expr value is 0, so return 1"
    E '((4 > 5))'       "Integer comparison"
    E '((4 > 3))'       "Integer comparison"
    E '((4 == 3))'      "Integer comparison"
    E '((4 != 3))'      "Integer comparison"
    unset a
    E '(( a ))'         "a is an empty string"
    echo "Define a to be '7'"
    a="7"
    E '(( a ))'         "a is '7', interpreted as an integer"
    echo "Define a to be '7.2'"
    a="7.2"
    P '(( a ))' "--"    "Syntax error"
}
VariableExpansion()
{
    w="yy"
    unset v; echo "x${v-}x"
    unset v; echo "x${v:-}x"
    unset v; echo "x${v-w}x"
    unset v; echo "x${v-$w}x"
    unset v; echo "x${v:-w}x"
    unset v; echo "x${v:-$w}x"
    return

    unset v; echo "x${v=w}x"
    unset v; echo "x${v=$w}x"

    unset v; echo "x${v+w}x"
}
#TestExamples
VariableExpansion
