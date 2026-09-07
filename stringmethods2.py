Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> a=2
>>> b=4
>>> print("the sum is {} {}" .format(a,b))
the sum is 2 4
>>> c=a+b
>>> print("the sum is {}".format(c))
the sum is 6
>>> print(f"the sum is {a+b}")
the sum is 6
>>> print(the sum of {}",format(a+b)
...       
SyntaxError: unterminated string literal (detected at line 1)
>>> print("the sum of {}",format(a+b))
...       
the sum of {} 6
