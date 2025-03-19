x_1=int(input("x_1의 좌표는?"))
y_1=int(input("y_1의 좌표는?"))
x_2=int(input("x_2의 좌표는?"))
y_2=int(input("y_2의 좌표는?"))
import math
distance_x = abs(x_2-x_1)
distance_y = abs(y_2-y_1)
distance_l = math.sqrt(math.pow(distance_x,2)+math.pow(distance_y,2))
print("좌표({}, {})와 좌표({}, {})의 거리는 {}이다".format(x_1, y_1, x_2, y_2, distance_l))