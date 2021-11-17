# l1=("hi","hello","How r u?")

# print(l1[:-1])

# l2=["I","am","fine"]
# print(l1.insert(3,"no thanks"))
# print (l1)
 
# l2.pop(0)
# print(l2)

# a=bin(5)
# b=bin(6)
# c=bin(4)
# print (a,b,c)
# print(5&6)

# print(20*"nid \n" )

# d2={"Ha":{"B":"roti","L":"Fish"},"Ni":[12,2,3]}
# print(d2["Ha"]["B"])
# print(d2["Ni"][0])

#------------------------------dictionary--------------------------------------#
# myDic={"apple":"the firut.","brinjal":"a vegetable"}

# _input_=input("Enter a word whose meaning you want to know:")

# print(myDic[_input_])
# Dict={"name":"nidhi", 1:[21,3,5,6]}
# Dict['value_set']=2,3,4
# print(Dict)

#------------------------------function--------------------------------------#

# def sum(num1, num2):
#     print(num1+num2)

# sum(234,45)
# sum(54,89)
# print(__name__)

#-------------------------------------function---------------------------------#


# def main():
#     print("hi")

# main()

# str="""nidhi    hi"""
# print(ascii('°C'))

# print(ord("a"))

# print('\xb0C')

#-------------------------------------break, continue---------------------------------#

# i=0
# while True:
#     if i<5:
#         i=i+1
#         continue
#     print(i, end=" ")
#     if(i==20):
#         break
#     i=i+1

#_______________________________even and odd------------------------------------

# num=int(input("enter a number:"))

# if(num%2==0):
#     print("number is even")
# else:
#     print("number is odd")

# --------------------------file reading----------------------------------

# f=open("test/nidhi.txt","rt")
# content=f.read()
# print(content)

# --------------------------file writing----------------------------------

# f=open("nidhi2.txt","w")
# f.write("nidhi is too good")
# f.close()
# # print(content)

# with open("nidhi2.txt") as f:
#     a=f.read(2)
#     print(a)
#     # print(f.readline())

# e=open("nidhi2.txt")

# print(e.read())

# --------------------------pattern writing----------------------------------

# n=int(input("enter number of rows you want "))

# b=bool(input("write t if you want seedha pyramid else write f"))

# if b==True:
#     for i in range(0,n):
#         for j in range(0,i+1):
#          print("*",end="")
#         print("\n")    
  
# elif b==False:
#     for i in range(0,n):
#         for j in range(i,n):
#             print("*",end="")
#         print("\n")    
    
# --------------------------factorial---------------------------------

# def factorial(n):
#     if(n==0 or n==1):
#         return 1
#     else:
#         return n * factorial(n-1)

# print(factorial(5))

# --------------------------sort---------------------------------

# def fun(e):
#     return len(e)


# l=["hi","hello","how","r","u"]
# l.sort(reverse=True, key=fun)
# print(l)


# -------------------------compound interest---------------------------------

# amount=pow(2,4)
# # print(amount)

# p=float(input("enter principal"))

# r=float(input("enter rate"))


# t=float(input("enter time"))

# amount=p * pow ( 1 + r/100 , t)

# amount=p * ( 1 + r/100) ** t
# #  Amount = principle * (pow((1 + rate / 100), time))

# print(amount)
# -------------------------kwargs and args---------------------------------

# def fun(n,*args, **kargs):
#     print(n)
#     print(f"args value {args[0]}")
#     print(f"args value {kargs.keys()}")
# b=["nidhi","atishay","ankush","sagar"]
# a={"nidhi":"programmer","atishay":"student","ankush":"Engineer","sagar":"Businessman"}

# fun("hi",*b, **a)
#-----------------------------------------
# def length1(*b):

#     print(len(b))

# length1(2,3,3,4,3)

# -------------------------time module---------------------------------

# import time as t
# print(t.localtime())
# print(f" {t.localtime().tm_year} / {t.localtime().tm_mon} / {t.localtime().tm_mday}")


# print(t.asctime())

# -------------------------import sys---------------------------------

# import sys
# print(sys.path)

# -------------------------enumerate function---------------------------------

# lis=["a","b","c","d","e","f"]

# for index1,item in enumerate(lis):
#     print(index1, item)

# -------------------------sound / play mp3 file---------------------------------

# from pygame import mixer

# # def musiconloop(file, stopper):
# #     mixer.init()
# #     mixer.music.load(file)
# #     b=True
# #     while b:
# #         mixer.music.play()
# #         a=input()
# #         if a == stopper:
# #             mixer.music.stop()
# #             break

# # if __name__ == '__main__':
# #     # musiconloop("my learning/Healthy Programmer/mp3 files/drink.mp3","stop")
# #     # musiconloop("test/drink.mp3","stop")
# #      musiconloop("test/hitm.mp3","stop")


# mixer.init()
# mixer.music.load("test/waterfall.mp3")
# mixer.music.play()
# a=input()
# if a == "a":
#     mixer.music.stop()
    
# -------------------------decorators--------------------------------

# def function1():
#     print("hi")

# fun2=function1
# del function1
# fun2()

# def fun1(fun):

#     fun(2)

# def fun2(a):
#     print(a+a)

# fun1(fun2)


# -------------------------OOPS (class)--------------------------------
# class Calculation:
#     def __init__(self,num1,num2):
#         self.num1=num1
#         self.num2=num2

#     def add(self):
#         return self.num1+self.num2
    
#     def mul(self):
#         return self.num1*self.num2


# n1=int(input("enter the first number: "))
# n2=int(input("enter the second number: "))
# a1=Calculation(n1,n2)
# resultAdd=a1.add()
# resultMul=a1.mul()
# print(f"Addtition of your number {resultAdd} \nMultiplication of your number {resultMul}")

# -------------------------OOPS (class method)--------------------------------

class Employee:
    no_of_leaves=10
    
    @classmethod
    def changeLeave( c,newLeaves):
        c.no_of_leaves=newLeaves



e1=Employee()
e1.changeLeave(34)
print(Employee.no_of_leaves)



