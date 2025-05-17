from ppp0331.ppp0331_hw07.average_hw07 import average


def str2int(text:str, default_value:int=None) -> int:
    try:
        return int(text)

    except ValueError:
        return default_value

def main():
    numbers = []
    while True:
        number = input("원하는 숫자를 입력하시오!")
        num = str2int(number)
        if num is None:
            print("정수가 아닙니다.")
        elif num == -1:
            break
        elif num > 0:
            numbers.append(num)
            continue
        else:
            print("이 숫자는 자연수가 아닙니다.")

    if numbers:
        print(f"입력된 값은 {numbers}입니다. 총 {len(numbers)}개의 자연수가 입력되었고, 평균은 {average(numbers):.2f}입니다 ")
    else:
        print("리스트 안에 숫자가 없습니다")

if __name__=="__main__":
    main()