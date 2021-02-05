>>> from io import StringIO
>>> f = StringIO('abdscf')  #初始化字符串
>>> f.tell()                #指针指向0位置
0
>>> f.write('123')          #write为从指针位置开始写入 覆盖之前的数据
3
>>> f.getvalue()
'123scf'
>>> f.tell()                #此时指针指向第四个位置
3
>>> f.readline()
'scf'
>>> f.seek(0)               #返回初始位置
0
>>> f.readline()
'123scf'

>>> t = StringIO('1\n2\n3\n')
>>> t.getvalue()
'1\n2\n3\n'
>>> t.readline()
'1\n'
>>> print(t.getvalue())
1
2
3

>>> t.tell()
2
>>> t.getvalue()   #getvalue不会改变指针位置
'1\n2\n3\n'
>>> t.tell()
2
>>> t.readline()  #readline可以改变指针位置
'2\n'
>>> t.tell()
4
>>> t.readline()
'3\n'
>>> t.tell()
6
> t.write('4\n5\n6')
5

>>> while True:
	s = t.readline()
	if s == '':
		break
	print(s.strip())     #指针在最后 读取为空

	
>>> 
>>> t.seek(0)
0
>>> while True:
	s = t.readline()
	if s == '':
		break
	print(s.strip())
1
2
3
4
5
6
