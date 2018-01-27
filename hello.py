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
'''











