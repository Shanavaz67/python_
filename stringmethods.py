Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a="wait until you succeed"
a.replace("wait","work")
'work until you succeed'
b="python java"
b.replace("java","c")
'python c'

#upper()
a="python"
>>> a.upper()
'PYTHON'
>>> b="CODE"
>>> b.lower()
'code'
>>> c="java"
>>> c.captialize()
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    c.captialize()
AttributeError: 'str' object has no attribute 'captialize'. Did you mean: 'capitalize'?
>>> c.capitalize()
'Java'
>>> d="i am shanavaz"
>>> d.title()
'I Am Shanavaz'
>>> a="hello world"
>>> a.startswith("h")
True
>>> a.endswith("d")
True
>>> b="helloworld"
>>> b.isalpha()
True
>>> c="1234"
>>> c.isdigit()
True
>>> c.isalnum()
True
>>> d="java"
>>> d.isalnum()
True
>>> e="shannu123"
>>> e.isalnum"
SyntaxError: unterminated string literal (detected at line 1)
>>> e.isalnum()
True
>>> #strip
>>> #lstrip(),rstrip()
>>> a="       shannu    "
>>> a.strip()
'shannu'
>>> a.lstrip()
'shannu    '
>>> a.rstrip()
'       shannu'
