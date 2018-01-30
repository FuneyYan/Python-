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
	if not isinstance(x,(int,float)):
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
'''















