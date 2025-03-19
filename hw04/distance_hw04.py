x_1=int(input("x_1의 좌표는?"))
y_1=int(input("y_1의 좌표는?"))
if x_1>0 and y_1>0:
    print("입력한 좌표는 1사분면입니다.")
elif x_1<0 and y_1>0:
    print("입력한 좌표는 2사분면입니다.")
elif x_1<0 and y_1<0:
    print("입력한 좌표는 3사분면입니다.")
elif x_1>0 and y_1<0:
    print("입력한 좌표는 4사분면입니다.")
else:
    print("원점입니다.")
