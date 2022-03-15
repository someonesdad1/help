# Show some PurePath examples
import pathlib as P
import re
r = re.compile(r"'(.*)'")
def Typ(x):
    mo = r.search(str(type(x)))
    return mo.groups()[0]
i = " "*2
print(f'''PurePath for path manipulations (see purepath.py)
{i}import pathlib as P''')
s = '''p = P.PurePath("/home/Don")'''
exec(s)
print(f"{i}{s} --> '{p}'") 
s = '''p/"work/me.tar.gz"'''
exec(f"p = {s}")
print(f"{i}{s} --> '{p}'  # How to append")
items = "parts drive root anchor parents parent name suffix suffixes stem"
for item in items.split():
    s = eval(f"p.{item}")
    print(f"{i}p.{item} --> '{s}'     [{Typ(s)}]")
s = 'q = P.PureWindowsPath("c:/foo/bar/setup.py")'
exec(s)
r, o = "P.Path(p.stem).stem", "other"
print(f'''
{i}drive is only for WindowsPath.
{i}anchor is concatenation of drive and root.
{i}parents:
{i*2}{s}
{i*2}str(q.parents[0])  --> {q.parents[0]!s}
{i*2}repr(q.parents[0]) --> {q.parents[0]!r}
{i*2}str(q.parents[1])  --> {q.parents[1]!s}
{i*2}repr(q.parents[1]) --> {q.parents[1]!r}
{i*2}etc.
{i}is_absolute()
{i}is_reserved()   Only relevant under Windows
{i}joinpath(*other)
{i*2}p = {p}
{i*2}r = P.Path(p.stem).stem --> {eval(r)}
{i*2}p.parent.joinpath(r, "{o}") --> {p.parent.joinpath(eval(r), o)}
{i}match(glob_pattern)
{i}relative_to(*other)
{i*2}p = {p}
{i*2}p.relative_to("/home") --> {p.relative_to("/home")}
{i}with_name(name)
{i*2}p = {p}
{i*2}p.with_name("lib.zip") --> {p.with_name("lib.zip")}
{i}with_suffix(suffix)      Remove original if suffix is ''
{i*2}p = {p}
{i*2}p.with_suffix(".bz2") --> {p.with_suffix(".bz2")}
{i*2}p.with_suffix("") --> {p.with_suffix("")}
'''.rstrip())
