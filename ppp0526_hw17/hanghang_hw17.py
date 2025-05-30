import random
import tkinter as tk
from tkinter import  simpledialog
import rich

window = tk.Tk()
window.withdraw()

def gui_input(text: str) -> str:
    return simpledialog.askstring(title = "test", prompt = text)

def check(soultion, answer, input_ch):
    is_correct = False
    for i in range(len(soultion)):
        if soultion[i] == input_ch:
            answer[i] = soultion[i]
            is_correct = True
    return is_correct



def main():
    problems = ["banana", "apple"]
    solution = problems[random.randrange(len(problems))]
    lives = 5

    answer = ["_" for n in solution]

    while True:
            input_ch = input(f"{''.join(answer)}?")

            if check(solution, answer, input_ch):
                rich.print(f"[green]{input_ch}[green]가 포함되어 있습니다.")
            else:
                rich.print(f"[red]{input_ch}[red]는 없습니다.")
                lives -= 1

            if "_" not in answer:
                rich.print(f"{solution} 정답입니다!!:thumbs_up:")
                break
            if lives <= 0:
                print(f"실패했습니다. 정답은 {solution} 입니다. 다시 도전하세요")
                break



if __name__=="__main__":
    main()