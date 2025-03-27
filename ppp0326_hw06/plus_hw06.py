n=int(input("원하는 숫자를 입력하시오."))
def sum_n(n):
    total=0
    for i in range(1,n+1):
        total+=i
    return total
def main():
    plus=sum_n(n)
    print(f"{n}부터 1까지의 합은 {plus}입니다.")

if __name__ == "__main__":
    main()