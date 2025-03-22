weight=int(input("몸무게가 얼마인가요?=>"))
height=int(input("키가 얼마인가요?=>"))
import math
height_m = height/100
BMI=weight/math.pow(height_m,2)
if BMI>=35:
    print("3단계 비만입니다.")
elif BMI>=30 and BMI<=34.9:
    print("2단계 비만입니다")
elif BMI>=25 and BMI<=29.9:
    print("1단계 비만입니다")
elif BMI>=23 and BMI<=24.9:
    print("비만 전단계입니다")
elif BMI>=18.5 and BMI<=22.9:
    print("정상 체중입니다")
else:
    print("저체중입니다")
print(f"{weight}kg, {height}cm, {BMI:.1f}㎏/㎡")