import random
import tkinter as tk
from tkinter import  simpledialog
import rich

window = tk.Tk()
window.withdraw()

def gui_input(text: str) -> str:
    return simpledialog.askstring(title = "test", prompt = text)

def get_lotto():
    lotto_list = []
    while True:
        n = random.randint(1, 45)
        if n not in lotto_list:
            lotto_list.append(n)
        if len(lotto_list) == 6:
            break
    return sorted(lotto_list)

def main():
    for n in range(5):
        lotto_num = get_lotto()
        rich.print(f"[yellow]{lotto_num}[yellow]")


if __name__=="__main__":
    main()
