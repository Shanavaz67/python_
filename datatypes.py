Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#datatypes
a=7
type(a)
<class 'int'>
b=6.7
type(b)
<class 'float'>
c='python'
type(c)
<class 'str'>
d="shannu"
type(d)
<class 'str'>
e='''codegnan'''
type(e)
<class 'str'>
f=2+7j
type(f)
<class 'complex'>
h=9j
type(h)
<class 'complex'>
g=4j+2
type(g)
<class 'complex'>
x=9+7i
SyntaxError: invalid decimal literal
z=Ture
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    z=Ture
NameError: name 'Ture' is not defined
type(z)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    type(z)
NameError: name 'z' is not defined
z=True
type(z)
<class 'bool'>
y=False
type(y)
<class 'bool'>
#
#
#int
int(6)
6
int(3.2)
3
int("shannu")
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    int("shannu")
ValueError: invalid literal for int() with base 10: 'shannu'
int(5+8j)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    int(5+8j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
int("True")
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    int("True")
ValueError: invalid literal for int() with base 10: 'True'
int(True)
1
int(False)
0
#
#
#float
float(5)
5.0
float(8.3)
8.3
float("python")
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    float("python")
ValueError: could not convert string to float: 'python'
float("7+6k")
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    float("7+6k")
ValueError: could not convert string to float: '7+6k'
float(True)
1.0
float(False)
0.0
#
#
#str
str(4)
'4'
str(2.3)
'2.3'
str("shannu")
'shannu'
str(2+9j)
'(2+9j)'
str(True)
'True'
str(False)
'False'
#
>>> #
>>> #complex
>>> complex(7)
(7+0j)
>>> complex(4.3)
(4.3+0j)
>>> cpmplex("python")
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    cpmplex("python")
NameError: name 'cpmplex' is not defined. Did you mean: 'complex'?
>>> cpmplex(2+6k)
SyntaxError: invalid decimal literal
>>> complex(2+3j)
(2+3j)
>>> complex(8+7k)
SyntaxError: invalid decimal literal
>>> complex(True)
(1+0j)
>>> cpmplex(false)
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    cpmplex(false)
NameError: name 'cpmplex' is not defined. Did you mean: 'complex'?
>>> complex(false)
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    complex(false)
NameError: name 'false' is not defined. Did you mean: 'False'?
>>> complex(False)
0j
>>> #
>>> #
>>> #boolean
>>> bool(5)
True
>>> bool(5.2)
True
>>> bool("java")
True
>>> bool(5+9j)
True
>>> bool(True)
True
>>> bool(False)
False
