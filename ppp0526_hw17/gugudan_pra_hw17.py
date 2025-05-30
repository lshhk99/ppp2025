import random
import tkinter as tk
from tkinter import  simpledialog
import rich

window = tk.Tk()
window.withdraw()

def gui_input(text: str) -> str:
    return simpledialog.askstring(title = "test", prompt = text)

def problem(num):
    dan = random.randint(2,9)
    mul = random.randint(1, 9)
    try:
        result = int(input(f"{dan} * {mul} = "))
    except ValueError:
        return False

    if result == dan * mul:
        print("참입니다.")
        return True
    print("틀렸습니다.")
    return False

def main():
    correct = 0
    total_problem = int(input("몇 문제를 풀지 정하시오!!"))

    for n in range(total_problem):
        is_correct = problem(n)
        if is_correct == True:
            correct += 1
        score = correct / total_problem * 100
    print(f"{correct}, {score}")

    if score >= 80:
        rich.print("훌륭합니다 :thumbs_up:")
    elif 50 <= score < 80:
        rich.print("노력하세요 :grinning_face:")
    else:
        rich.print("...:sleeping_face:")

if __name__=="__main__":
    main()