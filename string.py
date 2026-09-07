Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#string methods
#len()
a="python"
len(a)
6
>>> b="python course"
>>> len(b)
13
>>> c=""
>>> len(c)
0
>>> d=" "
>>> len(d)
1
>>> #count
>>> a="twinkle twinkle little star"
>>> count(a)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    count(a)
NameError: name 'count' is not defined. Did you mean: 'round'?
>>> a.count("twinkle")
2
>>> a.count("t")
5
>>> a.count("l")
4
>>> a,count("k")
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    a,count("k")
NameError: name 'count' is not defined. Did you mean: 'round'?
>>> a.count("k")
2
>>> #find a string
>>> a="python"
>>> a[1]
'y'
>>> a.find("y")
1
>>> a.find("o")
4
>>> b=("hello")
>>> b.find("1")
-1
>>> b="hello"
>>> b.find("1")
-1
>>> b.find("l")
2
