#원의 면적 구하기 pi*r^2
import math
pi=math.pi
r=int(input("반지름이 얼마인가요?"))
width=pi*math.pow(r,2)
print("반지름이 {}인 원의 면적은{}이다".format(r,width))



#사다리꼴 면적 구하기 (윗변+아랫변)*높이*1/2
upper = int(input("윗변의 길이가 얼마인가요?"))
lower = int(input("아랫변의 길이가 얼마인가요?"))
height = int(input("높이의 길이가 얼마인가요?"))
width=(upper + lower)/2*height
print("{}".format(width))
