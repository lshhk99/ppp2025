#BMI=몸무게(kg)/키(M)^2
weight=int(input("몸무게가 얼마인가요?=>"))
height=int(input("키가 얼마인가요?=>"))
import math
height_m = height/100
BMI=weight/math.pow(height_m,2)
print("{}kg, {}cm, {}".format(weight, height, BMI))
print("BMI({}) = {} / {}*{}".format(BMI, weight, height_m, height_m))