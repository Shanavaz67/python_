Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #concatenation
>>> a="code"
>>> b="gnan"
>>> print(a+b)
codegnan
>>> a="python"
>>> b="course"
>>> print(a+" "+b)
python course
>>> a="shannu"
>>> fname="shannu"
>>> lname="shaik"
>>> print(fname+" "+lname)
shannu shaik
>>> print(fname.title+" "+lname.tittle)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    print(fname.title+" "+lname.tittle)
TypeError: unsupported operand type(s) for +: 'builtin_function_or_method' and 'str'
>>> print(fname.title()+" "+lname.title())
Shannu Shaik
>>> print((fname+" "+lname).title())
Shannu Shaik
