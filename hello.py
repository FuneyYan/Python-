import math
'''
name=input('please enter you username:')
print(name)

a=100
if a>=1:
	print(0)
else:
	print(1)

print(10.0/3.0)
	
print('i\' am \"ok\"!')
#字符串原样输出 \\r\\
print(r'\\r\\')
#占位符
s1=72
s2=85
r=(s2-s1)/100
print('hello,{0}成绩提升了{1:.1f}%'.format('james',r))
#占位符
print('hello,%s的成绩是%.1f' % ('james',11.22));
# 打印 Apple  python  lisa
list=[
	["Apple","Google","Microsoft"],
	["java","python","ruby","php"],
	['Adam', 'Bart', 'Lisa']
]
print(list[0][0])
print(list[1][1])
print(list[2][2])

#判断语句,注意缩进
age=20
if age>=18:
	print('age is ',age)
	print("is adult")
else:
	print("is not adult")

# elif 是else if的缩写
age=5
if age>=18:
	print("is adult")
elif age<=6:
	print("is kid")
else:
	print("is teenager")

#在python中1是true,0是false
x=1
if x:
	print("true")
#input函数接受的是字符串,需要将输入的内容强制转换成int,注意强转是int()
birth=input("birth:")
birth=int(birth)
if birth <2000:
	print("夕阳红")
else:
	print("00后")

#计算BMI
weight=82
height=1.7
bmi=weight/(height*height)
#print(int(math.floor(bmi)))#需要在第一行import math
bmi=int(bmi)
print(bmi)
if bmi<18:
	print("过轻")
elif bmi>18 and bmi<25:
	print("正常")
elif bmi>25 and bmi<32:
	print("肥胖")
else:
	print("超重")

#for in循环注意缩进
names = ["james","tom","jack"]
for name in names:
	print(name)

#计算1-10的整数之和,注意,没有大括号,会将缩进的都看做循环体,另外也要注意冒号不能少
sum=0
for i in [1,2,3,4,5,6,7]:
	sum+=i
print(sum)

#使用for+range函数计算1+100
sum=0
for i in range(101):
	sum+=i
print(sum)

#while循环计算1+100
sum=0
n=1
while n<=100:
	sum+=n
	n+=1
print(sum)

#利用循环打印人名
L = ['Bart', 'Lisa', 'Adam']
for name in L:
	print(name)

i=0
while i<len(L) :
	print(L[i])
	i+=1
	
#continue结束本次循环
n=0
while n<10:
	n+=1
	if n%2==0:
		continue
	print(n)

#break退出循环
n=0
while n<100:
		print(n)
		if(n==10):
			break
		n+=1
print("end...")

#dict字典,键值对,类似map,字典是无序的
score={"james":89,"tom":88,"bosh":90,"bosh":99}#如果两个键一样,后面覆盖前面的
#print(score["james"])
score["james"]=99
print(score["james"])
print(score)
#判断键是否在dic中,有则返回True;或者使用get(),找不到的话为None
#print("james" in score)#True
#print(score.get("jame"))#结果是None
#删除指定键的值
#score.pop("james")
#print(score)#dic的键只能是不可变的值,比如字符串,整数;但不能是list
#直接往字典中添加数据
score={}
print(score)
score["james"]=90
print(score)


#用字典做电话本
dic={"james":"111"}
name=input("请输入联系人姓名")
if name in dic:
	print("联系人已存在")
else:
	phone=input("请输入联系人电话")
	dic[name]=phone
	print(dic)

#除了用name in dic找外还可以get()...
dic={"james":11}
if dic.get("jame"):
	print("find james")


#set,存储一组键,不存值
s=set([1,2,3,4,5])
print(s)
s.add(6)#添加元素
s.add(7)
s.remove(7)#删除元素
print(s)

#set的创建方法有很多:s=({1,2,3})   s={1,2,3}  s={(1,2,3)}
s1=set([1,2,3])
s2=set([2,3,4])
#两个set做交集
print(s1 & s2)
#两个set做并集
print(s1|s2)
#关于set类型的坑

s={}
print(type (s))  #dict
s={1}
print(type (s))  #set
s={1:2}
print(type (s))  #dict
s={1,2}
print(type (s))  #set


#函数
#求绝对值
print(abs(-10))
print(abs(11.23))
#求最大值(可以接收多个参数)
print(max(1,5,34,99,4))
print(max(1,54,4,9))

#数据类型转换
print(int("123"))
print(float("12.22"))
print(str(True))
print(bool(1))#True
print(bool(''))#False

#函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量(相当于js中的函数表达式)
a=abs
print(a(-1))

n1=255
print("十六进制转换%s"%(hex(n1)))

#定义函数
def myAbs(x):
	if x>=0:
		return x
	else:
		return -x

print(myAbs(-10))

a=myAbs;
print(a(-109))

#如果函数没有写return,默认会return None
def myfun():
	print("myFun")
	
result=myfun()
print(result)#None

#利用函数,dic做电话本
phoneDic={"james":120}
phoneDic["tom"]=110

#获取所有key
#print(phoneDic.keys())
#for dict_key in phoneDic.keys():
#	print(dict_key)
	
def startup():
	print("1.save")
	print("2.find")
	index=int(input("chose:"))
	if index==1:
		save()
	elif index==2:
		find()
	else:
		startup()
		
def save():
	name=input("please enter name : ")
	if name in phoneDic:
		print("person exists!")
	else:
		phone=input("please enter phone : ")
		phoneDic[name]=phone
		print("save success!")
	startup()
def find():
	name=input("please enter name : ")
	result=phoneDic.get(name)
	if result:
		print(result)
	else:
		print("not exists")
	
	startup()

startup()

#from cellPhone import startup  #导入文件的方法(来自XX文件导入XX方法)
#startup()#调用方法

#空函数
def nop():
	pass #pass表示占位符,在if中也可以使用pass,空函数如果不谢pass会报错


#参数类型判断
def myAbs(x):
	if not isinstance(x,(int,float)):#如果X不是int,也不是float的话
		#print("参数类型不正确")
		#return
		raise TypeError("参数类型不正确")
	if x>=0:
		print(x)
	else:
		print(-x)
myAbs("A")

#python函数可以返回多个值,最终多个值组成元组
def fun():
	return "A","B"

result=fun()
print(result)

A,B=fun()#拿两个变量分别接受
print(A,B)

#函数默认参数
def mypower(x,n=2):#n=2是函数的默认参数,必选参数在前，默认参数在后
	result=1
	for i in range(1,n+1):
		result*=x
	return result
print(mypower(2))

def mypower(x,n=2):#n=2是函数的默认参数,必选参数在前，默认参数在后;默认参数必须指向不变对象！ 
	result=1
	for i in range(1,n+1):
		result*=x
	return result
print(mypower(2,n=5))

def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
print(power(5,3))

def add_end(L=[]):
    L.append('END')
    return L
print(add_end())
print(add_end())
print(add_end())

def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L
    

print(add_end())
print(add_end())
print(add_end())

#可变参数(不定项参数)
def calc(*numbers):#如果是可变参数,参数前加*,自动组装成tuple
	sum=0
	for i in numbers:
		sum+=i*i
	print(sum)
#calc((1,2,3))#可以传list和tuple,如果是可变参数则不可用
#calc(1,2,3)
#如果非要将一个list或者tuple传递到可变参数中可以:
list=[1,2,3]
calc(*list)

#关键字参数(自动组装成dict)
def person(name,age,**kw):
	print(name,age,kw)

person("james",22,city="jz")#可以不填kw
person("tom",22,gender="man")
#和list一样,先组装一个dict,然后传到函数中
myDic={"city":"beijing","job":"manager"}
person("james",22,**myDic)

#命名关键字参数(限制关键字参数的名字)
def person(name,age,*,city,job):#*后面的都会被视为关键字参数,传递时候必须   参数名="XXX"
	print(name,age,city,job)
person("james",22,city="beijing",job="manager")
#如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了：
def person(name,age,*arg,city,job):#*后面的都会被视为关键字参数,关键字参数也是可以有默认值的
	print(name,age,arg,city,job)
person("james",22,city="beijing",job="manager")

#▲参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
def f1(a,b,c=0,*arg,**kw):
	print(a,b,c,arg,kw)
def f2(a,b,c=0,*,d,**kw):
	print(a,b,c,d,kw)

f1(1,2)#1,2,0,(),{}
f1(1,2,3)#1,2,3,(),{}
f1(1, 2, 3, 'a', 'b')#1,2,3,(a,b),{}
f1(1, 2, 3, 'a', 'b', x=99)#1 2 3 ('a', 'b') {'x': 99}
f2(1, 2, d=99, ext=None)#1 2 0 99 {'ext': None}

args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*args,**kw)#1 2 3 (4,) {'d': 99, 'x': '#'}

args = (1, 2, 3)
kw = {'d': 88, 'x': '#'}
f2(*args, **kw)#1 2 3 88 {'x': '#'}

#递归函数
#▲在函数内部，可以调用其他函数。如果一个函数在内部调用自身本身，这个函数就是递归函数。
#递归计算阶乘
def fact(n):
	if n==1:
		return 1
	return n*fact(n-1)
print(fact(1000))
#尾递归
def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)
print(fact(1000))

#切片(比如取出列表中的前N个元素)
list=["james","tom","jack","paul"]
print(list[0:3])#取出前三个(从0开始,到3为止)
print(list[:3])
print(list[-2:])#jack,paul


list=list(range(100))#0-99
print(list[90:])#从90取到最后
print(list[:11])
print(list[10:21])
print(list[-10:])#后10个数字
print(list[:10:2])#前10个数,每两个取一个
print(list[::5])#每5个取一个
print(list[:])#原样输出

#利用切片去除字符串首尾空格(字符串也可以切片)
def trim(s):
	while(s[:1]==' '):
		s=s[1:]
	while(s[-1:]==' '):
		s=s[:-1]
	return s
print(len(trim("abcd   ")))

#迭代
#同时迭代K,V
dic={"a":"a1","b":"b1"}
for k,v in dic.items():
	print(k,v)
#当我们使用for循环时，只要作用于一个可迭代对象，for循环就可以正常运行

#判断对象是否是可迭代的对象
from collections import Iterable#导入
print(isinstance("abc",Iterable))#True
print(isinstance([1,2,3],Iterable))#True
print(isinstance(123,Iterable))#False

#索引迭代
for i,value in enumerate(["A","B","C"]):
	print(i,value)

list=["A","B","C"]
for i,value in enumerate(list):
	print(list[i])

for x,y in[(1,2),(3,4),(5,6)]:
	print(x,y)

#请使用迭代查找一个list中最小和最大值，并返回一个tuple：
list=[10,9,8,56,4,0,99,1];

def findMaxAndMin(list):
	if list==[]:
		return(None,None)
	max=list[0]
	min=list[0]
	print(max,min)
	for i in list:
		if max<i:
			max=i
		if min>i:
			min=i
	return (max,min)
print(findMaxAndMin(list))

#列表生成式
list=[1,2,3,4,5]#等价于list(range(1, 11))
print(list)

#生成[1*1,2*2,3*3...10*10]
list=[]
for i in range(1,11):
	list.append(i*i)
print(list)
#简化
print([x*x for x in range(1,11)])

#偶数平方
print([x*x for x in range(1,11) if x%2==0])

#列表生成式两个变量生成list
dic={"X":"A","Y":"B","Z":"C"}
print([k+"="+v for k,v in dic.items()])

#列表生成式将list中的字母变小写
list=["James","Tom","JACK"]
print([s.lower() for s in list])

#列表生成式将list中的字母变小写(注意如果包含数字该如何处理)
list=["James","Tom",12,"JACK"]
print([s.lower() if isinstance(s,str) else s for s in list]  )

print(type([x*x for x in range(1,11)]))#list


#生成器(generator)
#把一个列表生成式的[]改成()，就创建了一个generator
g=(x*x for x in range(1,11))#创建生成器
print(g)
#通过next()函数获得generator的下一个返回值
print(next(g))
#generator是可迭代对象
for n in g:
	print(n)

#斐波拉契数列（Fibonacci），除第一个和第二个数外，任意一个数都可由前两个数相加得到
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'
fib(6)#1,1,2,3,5,8

#赋值语句
n,a,b=0,0,1
print(n,a,b)#0,0,1

a, b = b, a + b#相当于
t = (b, a + b) # t是一个tuple
a = t[0]
b = t[1]



#迭代器
#用isinstance()判断一个对象是否是Iterable(可迭代)对象
from collections import Iterable
print(isinstance([],Iterable))#True
print(isinstance({},Iterable))#True
print(isinstance("abc",Iterable))#True
print(isinstance((x for x in range(10)),Iterable))#生成器也是可迭代对象,True
print(isinstance(100,Iterable))#False

#可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。
from collections import Iterator
print(isinstance([],Iterator))#False
print(isinstance({},Iterator))#False
print(isinstance("abc",Iterator))#False
print(isinstance((x for x in range(10)),Iterator))#生成器可以用next(),True
print(isinstance(100,Iterator))#False

#▲生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator
#把list、dict、str等Iterable变成Iterator可以使用iter()函数
from collections import Iterator
print(isinstance(iter([]),Iterator))#True
print(isinstance(iter({}),Iterator))#True
#凡是可作用于for循环的对象都是Iterable类型；
#凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；


#▲函数式编程
#高阶函数
#print(abs)#直接输出内置函数:abs(10)是调用函数,而abs是函数本身
#函数赋值
f=abs
result=f(-10)
print(result)

#▲函数名其实就是指向函数的变量,比如
abs=10
abs(10)#报错TypeError: 'int' object is not callable

#将绝对值函数作为参数传递过去
def add(a,b,f):
	return f(a)+f(b)
result=add(-1,-2,abs)
print(result)


#map/reduce
#map()函数接收两个参数，一个是函数，一个是Iterable(可迭代对象)
#map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator(迭代器对象)返回
#计算1-10的每个数的平方
def f(x):
	return x*x
result=map(f,range(1,11))#结果是一个map对象
print(list(result))#强制转换为list对象

#将list中的每个值转换为字符串
print(list(map(str,[1,2,3,4,5,6,7,8,9,10])))

#reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，
#这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，
#其效果就是：reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
#将[1,2,3,4,5]转换为12345
from functools import reduce
def f(x,y):
	return x*10+y
print(reduce(f,range(1,6)))

#将str转换为int
from functools import reduce

def charToint(s):
	digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
	return digits[s]
def fn(x,y):
	return x*10+y
result=reduce(fn,map(charToint,"12345"))
print(type(result))#int

#利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
#输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']
def normalize(name):
	name=name[0].upper()+name[1:].lower()
	return name
r=list(map(normalize,['adam', 'LISA', 'barT']))
print(r)

#prod()函数，可以接受一个list并利用reduce()求积：
from functools import reduce
def fn(x,y):
	return x*y
result=reduce(fn,[3, 5, 7, 9])
print(result)

#将字符串转换为整数,并求出最大值
dic={'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def fn(x):
	return dic[x] 
result=map(fn,"123645")
from functools import reduce
def jisuan(x,y):
	return x if x>y else y#三元表达式
print(reduce(jisuan,result))


#▲filter(过滤序列)把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
#filter()函数返回的是一个Iterator(惰性序列)
#删除序列中的偶数(只要奇数)
def is_odd(x):
	return x%2==1
print(list(filter(is_odd,[1,2,3,4,5,6])))#[1,3,5]

#把一个序列中的空字符串删掉
def mytrim(s):
	return s!=" "
print("".join((filter(mytrim," a s d "))))#asd;  "".join(list)将list转为字符串

#排序算法
#print(sorted([3,12,6,4]))
#print(sorted([-1,2,-22,4,-6],key=abs))#key指定的函数将作用于list的每一个元素上
#字符串排序
#print(sorted(["C","D","a","Cat"]))#['C', 'Cat', 'D', 'a']
#print(sorted(["C","D","a","Cat"],key=str.lower))#['a', 'C', 'Cat', 'D']

#降序排序
#print(sorted([1,2,99,6],reverse=True))#[99, 6, 2, 1]

#分别按名字排序,再按成绩降序排列
l = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def  byName(t):
	return t[0].lower()
def byScore(t):
	return t[1]
print(sorted(l,key=byName))
print(sorted(l,key=byScore,reverse=True))


#返回函数(函数作为返回值)
def f(*x):
	def sum():
		s=0
		for i in x:
			s+=i
		return s
	return sum;#将函数返回出去
result=f(1,2,3,4,5)()#调用函数
print(result)


def count():
	fs=[]
	for i in range(1,4):
		def f():
			return i*i
		fs.append(f)
	return fs
f1,f2,f3=count()
print(f1())#9
print(f2())#9
print(f3())#9


def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs
f1,f2,f3=count()
print(f1())#1
print(f2())#4
print(f3())#9

#用过滤器筛选list中的偶数(lambda表达式)
def is_odd(n):
	return n%2==0
print(list(filter(lambda n:n%2==0,[1,2,3,4,5,6])))



#装饰器
#由于函数也是一个对象，而且函数对象可以被赋值给变量，所以，通过变量也能调用该函数。
def now():
	print("2018-1-30")
f=now
f()

#函数对象有一个__name__属性，可以拿到函数的原始名字：
#print(abs.__name__)#abs
#在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。
def log2(func):
	def wrapper(*args,**kw):
		print("call %s():"%func.__name__)
		return func(*args,**kw)
	return wrapper

@log2#相当于now = log2(now)
def now():
	print("2018-1-30")
now()#call now:  2018-1-30

#自定义log文本的装饰器
import functools
def log(text):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args,**kw):
			print("%s %s():"%(text,func.__name__))
			return func(*args,**kw)
		return wrapper
	return decorator

@log("自定义的文本")#now = log('execute')(now)
def now():
	print("2018-1-30")
now()#自定义的文本 now():      2018-1-30
print(now.__name__)#@functools.wraps(func),为了避免那些依赖函数签名的代码出现错误,可以使用functools.wraps,就变成now了

#设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间：


import time
def log(func):
	def wrapper(*args,**kw):
		print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
		return func(*args,**kw)
	return wrapper
@log
def fn():
	print("...")
fn()




#偏函数
print(int("12345"))
print(int("1234",base=16))#4660    十六进制
print(int("1234",8))#668    八进制

def int2(x, base=2):
    return int(x, base)
print(int2("1000000"))#64

#functools.partial就是帮助我们创建一个偏函数的，不需要我们自己定义int2()
import functools
int2=functools.partial(int,base=2)
print(int2("1000000"))#64


#模块(在Python中，一个.py文件就称之为一个模块（Module）)
#▲使用模块还可以避免函数名和变量名冲突。相同名字的函数和变量完全可以分别存在不同的模块中
#https://docs.python.org/3/library/functions.html     Python的所有内置函数。
#为了避免模块名冲突，Python又引入了按目录来组织模块的方法，称为包（Package）。
#每一个包目录下面都会有一个__init__.py的文件，这个文件是必须存在的，否则，Python就把这个目录当成普通目录，而不是一个包
#__init__.py可以是空文件，也可以有Python代码，因为__init__.py本身就是一个模块，而它的模块名就是mycompany。
#▲自己创建模块时要注意命名，不能和Python自带的模块名称冲突。例如，系统自带了sys模块，自己的模块就不可命名为sys.py，否则将无法导入系统自带的sys模块。 

#使用模块
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"a test module"#表示模块的文档注释，任何模块代码的第一个字符串都被视为模块的文档注释；
__author__="james"#作者名
import sys#导入模块

def test():
	args=sys.argv#用list存储了命令行的所有参数,argv至少有一个元素，因为第一个参数永远是该.py文件的名称
	if len(args)==1:
		print("Hello world "+args[0])#Hello world hello.py
	elif len(args)==2:
		print("Hello %s" % args[1])#运行python hello.py james   结果是:Hello james
	else:
		print("no argument")
if __name__=="__main__":#在命令行运行hello模块文件时，Python解释器把一个特殊变量__name__置为__main__,而如果在其他地方导入该hello模块时，if判断将失败
	test()


#第1行和第2行是标准注释，第1行注释可以让这个hello.py文件直接在Unix/Linux/Mac上运行，
#第2行注释表示.py文件本身使用标准UTF-8编码；



#作用域
#函数和变量我们希望仅仅在模块内部使用。在Python中，是通过_前缀来实现的
#类似_xxx和__xxx这样的函数或变量就是非公开的（private），不应该被直接引用

def _private_1(name):
	return "hello %s"%name

def _private_2(name):
	return "hi %s"%name

def getting(name):
	if len(name)>3:
		return _private_1(name)
	else:
		return _private_2(name)

print(getting("james"))#hello james
#外部不需要引用的函数全部定义成private，只有外部需要引用的函数才定义为public。


#第三方库
#https://pypi.python.org/pypi
#要安装一个第三方库，必须先知道该库的名称，可以在官网或者pypi上搜索，
#比如Pillow的名称叫Pillow，因此，安装Pillow的命令就是：pip install Pillow
#用pip一个一个安装费时费力，还需要考虑兼容性。我们推荐直接使用Anaconda,内置了许多非常有用的第三方库
#下载GUI安装包  https://www.anaconda.com/download/#download
#国内镜像:https://pan.baidu.com/s/1kU5OCOB#list/path=%2Fpub%2Fpython
#安装好Anaconda后，重新打开命令行窗口，输入python   尝试直接import numpy等已安装的第三方模块。
#如果我们要添加自己的搜索目录，有两种方法：
#一是直接修改sys.path，添加要搜索的目录：import sys   sys.path.append('src')  运行时有效
#第二种方法是设置环境变量PYTHONPATH
import sys
print(sys.path)



#面向对象编程
class Student(object):#(object)表示继承自object
	def __init__(self,name,score):#通过定义一个特殊的__init__方法，在创建实例的时候，就把name，score等属性绑上去：
		self.name=name
		self.score=score
	def printScore(self):
		print("%s  %s"%(self.name,self.score))
james=Student("james",66)#创建对象
bart=Student("bart",96)
james.printScore()
bart.printScore()


#类和实例

class Student():
	pass
james=Student()
james.name="james"  #可以自由地给一个实例变量绑定属性
print(james.name)

#▲__init__方法的第一个参数永远是self，表示创建的实例本身(self就指向创建的实例本身。)
#有了__init__方法，在创建实例的时候，就不能传入空的参数了，必须传入与__init__方法匹配的参数
#要定义一个方法，除了第一个参数是self外，其他和普通函数一样



#访问限制
#▲如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__
class Student(object):
	def __init__(self,name,age):
		self.__name=name#外部访问不到
		self.__age=age
james=Student("james",22)
print(james.name)#'Student' object has no attribute 'name'


#setXXX和getXXX方法
class Student(object):
	def __init__(self,name,age):
		self.__name=name
		self.__age=age
	def setName(self,name):
		self.__name=name
	def getName(self):
		return self.__name
	def setAge(self,age):
		self.__age=age
	def getAge(self):
		return self.__age

james=Student("james",22)
print(james.getName())
print(james.getAge())
print(james._Student__name)#james

#在Python中，以双下划线开头，并且以双下划线结尾的
#是特殊变量，特殊变量是可以直接访问的，不是private变量，所以，不能用__name__、__score__这样的变量名。

#以一个下划线开头的实例变量名，比如_name，这样的实例变量外部是可以访问的
#但是，按照约定俗成的规定，当你看到这样的变量时，意思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”。

#Python解释器对外把__name变量改成了_Student__name，所以，仍然可以通过_Student__name来访问__name变量：



#继承和多态
class Animal(object):
	def run(self):
		print("animal run...")
class Dog(Animal):
	pass
class Cat(Animal):
	pass
dog=Dog()
dog.run()
cat=Cat()
cat.run()


class Animal():#不写,默认继承自object
	def run(self):
		print("animal run ...")
class Dog(Animal):
	def run(self):
		print("dog run ...")
dog=Dog()
dog.run()#dog run ...


#多态
class Animal():
	pass
class Cat(Animal):
	pass
cat=Cat()
print(isinstance(cat,Cat))#True
print(isinstance(cat,Animal))#True
#在继承关系中，如果一个实例的数据类型是某个子类，那它的数据类型也可以被看做是父类。但是，反过来就不行：
animal=Animal()
print(isinstance(animal,Cat))#False

class Animal():
	def __init__(self,name):
		self.name=name
class Dog(Animal):
	pass
dog=Dog("d")
print(dog.name)#d



#获取对象信息
#判断对象类型，使用type()函数,基本类型都可以用type()判断：
print(type(123))#<class 'int'>
print(type("str"))#<class 'str'>
print(type(None))#<class 'NoneType'>
#如果一个变量指向函数或者类，也可以用type()判断
print(type(abs))#<class 'builtin_function_or_method'>

#type()返回的是Class类型
print(type(123)==type(345))#True
print(type(123)==int)#True
print(type('abc')==type('123'))#True
print(type('abc')==str)#True
print(type('abc')==type(123))#False

#如果要判断一个对象是否是函数可以使用types模块中定义的常量：
import types
def fn():
	pass
print(type(fn)==types.FunctionType)#True
print(type(abs)==types.BuiltinFunctionType)#True,判断是否是内置函数
print(type(lambda x: x)==types.LambdaType)#True,判断是否是lambda表达式
print(type((x for x in range(10)))==types.GeneratorType)#True,判断是否是生成器


#判断class的类型，可以使用isinstance()函数。
class Animal():
	pass
class Dog(Animal):
	pass
class Hasky(Dog):
	pass
a=Animal()
d=Dog()
h=Hasky()
print(isinstance(a,Animal))#True
print(isinstance(d,Dog))#True
print(isinstance(h,Hasky))#True
print(isinstance(h,Dog))#True
print(isinstance(h,Animal))#True

#能用type()判断的基本类型也可以用isinstance()判断：
print(isinstance('a', str))#True
print(isinstance(123, int))#True
print(isinstance(b'a', bytes))#True

#判断一个变量是否是某些类型中的一种
print(isinstance([1, 2, 3], (list, tuple)))#True
print(isinstance((1, 2, 3), (list, tuple)))#True


#dir获得一个对象的所有属性和方法,它返回一个包含字符串的list
print(dir("abc"))#['__add__', '__class__', '__contains__'......]

#类似__xxx__的属性和方法在Python中都是有特殊用途的，比如__len__方法返回长度。
#在Python中，如果你调用len()函数试图获取一个对象的长度，
#实际上，在len()函数内部，它自动去调用该对象的__len__()方法，所以，下面的代码是等价的：
print(len("abc"))#3
print("abc".__len__())#3
#我们自己写的类，如果也想用len(myObj)的话，就自己写一个__len__()方法：
class MyClass():
	def __len__(self):
		return 100
print(MyClass().__len__())#100



#实例属性和类属性
#给实例绑定属性的方法是通过实例变量，或者通过self变量：
class Student():
	def __init__(self,name):
		self.name=name
s=Student("james")
print(s.name)

#如果Student类本身需要绑定一个属性,这种属性是类属性，归Student类所有(相当于java中的静态变量)：

class Student():
	name="Student"
s=Student()
print(Student.name)#Student
print(s.name)#Student
s.name="jack"
print(s.name)#jack
del s.name#删除实例的属性
print(s.name)#Student
'''