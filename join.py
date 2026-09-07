Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> b="vij","hyd","vig"
>>> "".join(b)
'vijhydvig'
>>> " ".join(b)
'vij hyd vig'
>>> "K".join()
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    "K".join()
TypeError: str.join() takes exactly one argument (0 given)
>>> "k".join()
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    "k".join()
TypeError: str.join() takes exactly one argument (0 given)
>>> c="hello"
>>> "m" .join(c)
'hmemlmlmo'
>>> "k".join(b)
'vijkhydkvig'
