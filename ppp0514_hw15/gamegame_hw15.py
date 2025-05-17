import random

chosung = ["ㄱ", "ㄲ", "ㄴ", "ㄷ", "ㄸ", "ㄹ", "ㅁ", "ㅂ", "ㅃ"
           , "ㅅ", "ㅆ", "ㅇ", "ㅈ", "ㅉ", "ㅊ", "ㅋ", "ㅌ", "ㅍ", "ㅎ"]

def to_chosung_ch(ch):
    if '가' <= ch <= '힣':
        index = ((ord(ch) - ord("가")) //588)
        return chosung[index]
    else:
        return ch



def to_chosung(text):
    full_text = []
    for ch in text:
        full_text.append(to_chosung_ch(ch))
    return "".join(full_text)

def main():
    print("초성게임을 시작하겠습니다!")
    problems = ["바나나", "딸기", "토마토", "복숭아"]
    solution = problems[random.randrange(len(problems))]
    is_correct = False

    for i in range(3):
        answer = input(f"{to_chosung(solution)}")
        if answer == solution:
            print("정답입니다!")
            is_correct = True
            break
        else:
            print("오답입니다.")

    if is_correct:
        print("잘하셨습니다.")
    else:
        print("다시하세요.")



if __name__== "__main__":
    main()