def get_range_list(n):
    numbers = []
    for i in range(1, n + 1):
        numbers.append(i)
    return (numbers)

def main():
    n=(int(input("원하는 숫자를 입력하시오.")))
    print(get_range_list(n))

if __name__=="__main__":
    main()