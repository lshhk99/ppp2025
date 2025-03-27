def gugudan(dan):
    for i in range(1, 10):
        total=dan*i
        print(f"{dan}*{i}={total}")
def main():
    dan = int(input("원하는 숫자를 입력하시오."))
    gugudan(dan)
if __name__ == "__main__":
    main()