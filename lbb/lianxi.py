#!/usr/bin/python
#-*-coding:utf8-*-



# for i in range (1,10):
#     for j in range(1,i+1):
#         print('%d*%d=%d'%(j,i,j*i),end=' ')
#     print(' ')

# a=1
# while a<=9:
#     b=1
#     while b<=a:
#         print('%d*%d=%d'%(b,a,a*b),end=' ')
#         b+=1
#     a+=1
#     print(' ')


# import requests
# import re
# a='https://www.65ws.com/a/22/22450/7027756.html'
# b=requests.get(a)
# c=b.content.decode('gbk')
# d=re.compile('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(.*?)https://www.65ws.com/a/22/22450/7027756.html')
# e=d.findall(c)
# print(e)



# class Pai():
#     def tongji(self):
#         a='asdfsdfqs'
#         for i in a:




# a='asdasda'
# b,c,d=a.count('a'),a.count('s'),a.count('d')
# print(b,c,d)





# import pymysql
# con=pymysql.connect(host='192.168.2.124',port=3306,user='root',passwd='123456')
# yb=con.cursor()
# yb.execute('show databases;')
# print(yb.fetchall())







# a=[12,41,10,35,27]
# for i  in range (len(a)):
#     for j in range(len(a)):
#         for z in range (j+1,len(a)):
#             if a[j]>a[z]:
#                 a[j],a[z]=a[z],a[j]
# print(a)

# for i in range(100,1000):
#     a=i//100
#     b=i//10%10
#     c=i%10
#     if a**3+b**3+c**3==i:
#         print(i)


# import  xlrd
# import pymysql
# xl=xlrd.open_workbook('a.xls')
# sheet=xl.sheets()[0]
# hangshu=sheet.nrows
# con=pymysql.connect(host='192.168.2.134',port=3306,user='root',passwd='123456')
# yb=con.cursor()
# yb.execute('use lbb;')
# yb.cursor('create table biao ()')
# for i in range(hangshu):
#     shuju=sheet.row_values(i)



# for i in range(100,1000):
#     a=i//100
#     b=i//10%10
#     c=i%10
#     if a**3+b**3+c**3==i:
#         print(i)


# import requests
# a='https://03imgmini.eastday.com/mobile/20191012/2019101215_4345bd64180e4d4d925475b1fdb55d15_7004_wmk.png'
# b=requests.get(a)
# c=b.content
# print(c)
# with open ('1.png','wb') as f:
#     f.write(c)


# import requests
# a='https://video.pearvideo.com/mp4/adshort/20191015/cont-1612297-14485233_adpkg-ad_hd.mp4'
# b=requests.get(a)
# c=b.content
# print(c)
# with open('a.mp4','wb')as f:
#     f.write(c)


import requests
import re
class  PaChong():
    def __init__(self,url,bianma,guolv):
        self.url=url
        self.bianma=bianma
        self.guolv=guolv
    def qingqiu(self):
        a=requests.get(self.url)
        geshi=a.content.decode(self.bianma)
        # print(geshi)
        return geshi
    def neirong(self):
        c=re.compile(self.guolv)
        d=c.findall(self.qingqiu())
        # print(d)
        for i in d:
            i=i.replace('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp','')
            i=i.replace('\r<br />\r<br />','')
            print(i)
            return i
    def xieru(self):
        with open('1.txt','w',encoding='UTF-8')as f:
            f.write(self.neirong()+'\n')
aa=PaChong('https://www.65ws.com/a/109/109011/36810028.html','gbk','&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(.*?)https://www.65ws.com/a/109/109011/36810028.html')
aa.xieru()