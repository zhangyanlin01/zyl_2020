# a_1 = [55,65,75,80,85,95,100,101]
#
# for a in a_1 :
#     if (a >= 0 and a <= 59):
#         print("不合格")
#     elif (a >= 60 and a <= 70):
#         print("及格")
#     elif(a in range(70,81)):
#         print("良好")
#     elif(a in range(80,101)):
#         print("优秀")
#     else:
#         print("请输入正确的成绩")
#
# q = 1
# for w in range(10,0,-1):
#     q *= w
#     print(q)
#
# for q in range(1,101):
#     if(q % 3 != 0 ):
#         continue
#     print(q)

# def jieguo(a,b):
#     if (b == 0):
#         return None
#     else:
#         return(a // b,a % b)
# c = jieguo(10,5)
# if c is None:
#     print(c)
#     print("参数错误")
# else:
#     print("商数：",c[0],"，余数：",c[1])

# def qiuhe(a,b):
#     return a+b
# print(qiuhe(6,6))

# class calc():
#     a=None
#     b=None
#     res=None
#     def iuput(self,a,b):
#         self.a=a
#         self.b=b
#     def sum(self):
#         self.res=self.a+self.b
#     def div(self):
#         self.res=self.a/self.b
#     def get_result(self):
#         print(self.res)
#
# c=calc()
#
# c.iuput(10,20)
# c.sum()
# c.get_result().
# c.div()
# c.get_result()
#
# for q in range(1,10):
#     for w in range(1,q+1):
#         print(q,"x",w,"=",q*w,end="\t")
#     print()


# q = [1,58,23,4468,46,148,36,6,4,5682,4654,154,0]
# length = len(q)
# for w in range(length-1,0,-1):
#     for e in range(0,w):
#         if q[e] > q[e+1]:
#             q[e],q[e + 1] = q[e + 1],q[e]
# print(q)
#
# class Qqq():
#     w = 100000
#     e = '好多钱'
#     def __init__(self,a):
#         self.a = a
#     def Rrr_r(self):
#         print("嗯")
# class Yyy(Qqq):
#     ai_hao = "chpd"
#     def __init__(self,a):
#         super().__init__(a)
#
# t = Yyy(123)
# print(t.e)
# print(t.w)
# print(t.ai_hao)
# t.Rrr_r
# print(t.a)

# q = open("qqq.txt","w")
# q.write("ye")
# q.close()

# for q in range(1,10):
#     for w in range(1,q+1):
#         print("{} x {} = {}".format(w,q,q*w),end="\t")
#     print()

# q = {"姓名":"小明","年龄":"18"}
# print(q)
# q.update({"性别":"男"})
# print(q)

