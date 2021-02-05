def books():
    if __name__ == '__main__':
        print('I like to read books')
    else:
        print('this is a module')
-------------------------------------------------------
>>> books()
I like to read books
>>> a = books
>>> a()
I like to read books
>>> import sys
>>> sys.path
['C:\\Python\\examples', 'C:\\Python\\Lib\\idlelib', 'C:\\Python\\python36.zip', 'C:\\Python\\DLLs', 'C:\\Python\\lib', 'C:\\Python', 'C:\\Python\\lib\\site-packages']
>>> import nameeqaulsmain
>>> nameeqaulsmain.books()
this is a module
>>> books()
I like to read books

---------------------------------------------------------
直接调用函数名，__name__ == '__main__'
通过module名字调用函数，则是else情况

