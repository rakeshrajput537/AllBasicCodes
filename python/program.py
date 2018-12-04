#PRINT FUNCTION
# print("hello, Rakesh Rajput")
# print(5)
# print("that is five="+str(5))
# print("that is five= " , 5) 
# print("c:\desktop\newprogram")
# print(r"c:/desktop/newprogram")


#VARIABLE

# name = 'Rakesh rajput'
# print(name)
# x = 5
# print(x)
# print(type(x))
# b = True
# print(type(b))

#OPERATORS

# print(5+3)
# print(6%3)
# print(6/3)
# print(10//3)

# text = 'this is a text'
# print(text)
# print(text[0:4])
# print(text[1])
# print(text[-1])


#LIST

# list1=["aalu", "Gobhi","tomato"]
# list2=[1,4,33.34,43]
# list2.append(6)
# print(list1)
# print(list2)
# list2.insert(0,12)
# print(list2)
# list2.pop()
# print(list2)
# list2.remove(4)
# print(list2)
# list3=list1+list2
# print(list3)

# name = input("Enter your name:") #enter name in cottation
# print(name)
# age = input("enter your age")
# if age>18:
# 	print("go for bear")
# else:
#   print("you are child")	

# name = input("enter your name")
# if name=="rakesh":
# 	print("hello Rakesh")

# elif name=="avni":
#   print("hi avni")
# else:
#   print("who are you")


#LOOP

# i=1
# while i<10:
# 	print(str(i), "HI Raj Avni")
# 	# print(i)
# 	i=i+1


# for i in xrange(1,10):
# 	print(i)

# list1=[1,4,6,83,3,2]
# for i in list1:
#   if i==6:
# 	continue
#   print(i)


#FUNCTION

# def show():
# 	print("show called")
# show()

# def argu(b):
# 		print(b)	
# argu(6)


#FOR MANY ARGUMENT
# def add(* args):
# 	total = 0
# 	for a in args:
# 		total = total+a
# 	print("total is ",total)
# add(34,43)	
# add(334,3332,353)

# list1={1,1,2232,34,32,23,23} #Not print repeating number
# print(list1)
# class_mates = {'name':'Rakesh', 'rollno':43}	
# print(class_mates['name'])
# import math
# value = math.pow(2,10)
# print(value)

#IPORT A SELF CREATED MODULE
# import mymodule # or write //from mymodule import add//
# ans = mymodule.add(23,2,32)
# print(ans)
# f= open("new.txt","w")

# f.writelines("rakesh kumar")
# f.close()
# f=open("new.txt","r")
# print(f.read())

#CLASS
# class Player:
# 	life = 3
# 	def __init__(self): #JUST LIKE CONSTRUCTOR
# 		print("object created")

# 	# def attack(self):
# 	# 	self.life = self.life -1

# 	def getlife(self):
# 		print("life left: "+str(self.life))

# p1 = Player()
# p1.getlife()

# class Girl:
# 	gender = 'female'             #class variable
# 	def __init__(self,name):
# 		self.name = name          #instance variable
# 	def getGender(self):
# 		print(self.gender)
				
# G1 = Girl("Avni")
# G2 = Girl("karishma")
# G1.getGender()
# print(gi.gender)

#INHERITANCE

# class Parent():
# 	eyes = 'black'
# 	def get_last_name(self):
# 		return ("Rajput")
# class child(Parent ):
# 	def get_name(self):
# 		return ("Rakesh")
# R = child();
# print(R.eyes)
# print(R.get_name()+ " "+R.get_last_name())
	
#INHERITANCE OVERRIDIING 

# class Base():
# 	def show(self):
# 		print("base class show called")

# class Sub(Base):
# 	def show(self):
# 		print("sub class show called")

# s = Sub()
# s.show()  # SUB CLASS SHOW IS CALLED		
# s.super.show()

#THREADING

# import threading 

# class Messenger(threading.Thread):
# 	def run(self): #PREDEFINE FUNCTION
# 		for i in range(10):
# 			print(threading.currentThread().getName())

# x = Messenger(name="sending message")
# y = Messenger(name="Recieveing message")
# x.start()
# y.start()			
	

#LAMDA EXPRESSION

# answer = lambda x: x*7
# print(answer(5))

#BITWISE OPERATOR

# a=50         #110010
# b=25         #011001
# c = a & b    #010000(16)
# print(c)
# d= a | b    #111011(59)
# print(d)

# x=240  #11110000
# y=x>>2 #00111100  2 bit shifted in right
# print(y)


#***********ADVANCE PYTHON *********

#IMPORT RANDOM

# import random
# def lottery():
# 	for i in range(6):
# 		#return 6 number bw 1 to 40
# 		yield random.randint(1,40)
# 	yield random.randint(1,15)
	
# for i in lottery():
# 	print("random  number is %d " %(i))



#SWAP TO NUMBER

# a=1
# b=2
# a,b= b,a
# print(a,b)
	
	
#FIBANACCI SERIES

# def fib():
# 	a,b=1,1
# 	while 1:
# 		yield a
# 		a,b = b,a+b
# import types
# if type(fib()) == types.GeneratorType:
#     print("Good, The fib function is a generator.")

#     counter = 0
#     for n in fib():
#         print(n)
#         counter += 1
#         if counter == 10:
#             break

# LIST COMPREHENSIONS(IMP AND MAST)

# sentence ="the quick brown fox jumps over the lazy dog"	
# words = sentence.split()
# print(sentence)
# print(words)
# words_length =[len(words)]
# each_words_length=[]

# print(words_length)
# for i in words:
# 	if i!='the':
# 		each_words_length.append(len(i))
# print(each_words_length)

#SORTOUT THE POSSITIVE NUMBER FROM A LIST

# list = [12,23,32,-21,22,-2242,-242,222]
# possitive_list =[]
# for i in list:
# 	if i>0:
# 		possitive_list.append(i)
# print(possitive_list)


#MULTIPLE FUNCTION ARGUMENT

# def fun(first,second,*more):
# 	print("first arg is %s "%first)
# 	print("first arg is %s "%second)
# 	print("rest arg is  %s "%list(more))
# fun(1,2,3,4,5,5)	

#FUNCTION ARGUMENT

# def fun(first,second,**options):
# 	if options.get("action")=="sum":
# 		print("the sum is %d "% (first+second))
# 	if options.get("number")=="first":
# 		return first
# fun(1,3,action="sum")

#SETS USE:-"intersection" ,"symmetric_difference","difference",union

# a=set(["rakesh","ankur","rajveer","shailendra"])
# b=set(["rakesh","manish","ankur"])
# print(a.intersection(b))
# print(a.symmetric_difference(b))
# print(a.difference(b))
	


		