import time

def count_down(count): # 타이머를 분과 초로 나누기
    while count >= 0:
        min = count // 60
        sec = count % 60
        print(f"{min:02}:{sec:02}", end = "\r")
        time.sleep(1)
        count -= 1
    print("")
    print("Bomb!!")

def main():
    timer = int(input("원하는 시간을 입력하세요."))
    count_down(timer)

if __name__=="__main__":
    main()