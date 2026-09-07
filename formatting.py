Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#formatting
a=5
b=7
print(a+b)
12
print("the sum of",a+b)
the sum of 12
print("the sum is",a+b)
the sum is 12
print("the sum is,a+b)
      
SyntaxError: unterminated string literal (detected at line 1)
>>> print("the sum is,a+b")
...       
the sum is,a+b
>>> city="vijayawada"
...       
>>> print("city is",city)
...       
city is vijayawada
>>> 
>>> 
>>> a="motu"
...       
>>> b="pathlu"
...       
>>> print("hello {}{}".format(a,b))
...       
hello motupathlu
>>> print("hello {} {}".format(a,b))
...       
hello motu pathlu
>>> print("hello {} hello {}".format(a,b))
...       
hello motu hello pathlu
>>> 
>>> 
>>> #fstring()
...       
>>> a="ms"
...       
>>> b="dhoni"
...       
>>> print(f"hello {a} {b})
...       
SyntaxError: unterminated f-string literal (detected at line 1)
>>> print(f"hello {a}{b})
...       
SyntaxError: unterminated f-string literal (detected at line 1)
>>> print(f"hello {a}{b}")
...       
hello msdhoni
>>> print(f"hello {a} {b}")
...       
hello ms dhoni
>>> print(f"hello {a} hello {b}")
...       
hello ms hello dhoni
