#원주는 2*pi*r 원의 넓이는 pi*r^2
import math
pi=math.pi
r=int(input("반지름이 얼마인가요?"))
width=pi*r**2
circumference=2*pi*r
print(f"반지름이 {r}인 원의 원주는{circumference:.1f}이고 면적은{width:.2f}이다")