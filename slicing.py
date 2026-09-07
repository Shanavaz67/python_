Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a="codegnan"
a=[0:3]
SyntaxError: invalid syntax
a[0:3]
'cod'
a=[0:4]
SyntaxError: invalid syntax
a[0:4]
'code'
a[4:8]
'gnan'
a="work until you succeed"
a[0:4]
'work'
a[6:10]
'ntil'
a[5:10]
'until'
>>> a[14:20]
' succe'
>>> b="happy teachers day"
>>> b[-12:-17]
''
>>> b[-18:-13]
'happy'
>>> b[-3]
'd'
>>> b[0:-4]
'happy teachers'
>>> b[-4]
' '
>>> b[-4:]
' day'
>>> b[-4:-15]
''
>>> b[-12:-4]
'teachers'
>>> a="data science'
SyntaxError: unterminated string literal (detected at line 1)
>>> s="cloud computing"
>>> s[2:13:3]
'o mt'
>>> s[4:14:5}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
>>> s[4:14:5]
'dp'
>>> s[3:12:6]
'up'
>>>        s[4:14:5]
...        
SyntaxError: unexpected indent
>>> k="python course"
>>> k[-2:-12:-4]
'sch'
>>> 
...     
>>> a=
SyntaxError: invalid syntax
>>> "python course"
'python course'
>>> a="python course"
>>> a[-4:-13:-5]
'uo'
