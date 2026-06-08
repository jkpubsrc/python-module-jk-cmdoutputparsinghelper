#!/usr/bin/python3




from jk_cmdoutputparsinghelper import *





t = TextData("foo\nbar\n")

print("repr(t.text)")
print("->", repr(t.text))
print()

print("repr(t.lines))")
print("->", repr(t.lines))
print()

print("repr(t))")
print("->", repr(t))
print()

print("t.lines.removeTrailingEmptyLines()")
t.lines.removeTrailingEmptyLines()
print()

print("repr(t))")
print("->", repr(t))
print()



