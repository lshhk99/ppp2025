def caesar_encode_ch(ch, shift):
    if 97 <= ord(ch) <= 122: # 소문자를 암호화
        return chr((ord(ch)-ord('a')+shift) % 26 + ord('a'))
    elif 65<= ord(ch) <= 90: # 대문자를 암호화
        return chr((ord(ch)-ord('A')+shift) % 26 + ord('A'))
    else: # 알파벳이 아니면 그대로 출력
        return ch




def caesar_encode(text: str, shift: int = 3):
    full_text = []
    if text:
        for ch in text:
            encoded_ch = caesar_encode_ch(ch, shift)
            full_text.append(encoded_ch)

    return "".join(full_text)

def caesar_decode(text: str, shift: int = -3):
    return caesar_encode(text, shift)


def main():
    print(caesar_encode("HELLO, WORLD"))
    print(caesar_decode("KHOOR, ZRUOG"))
    print(caesar_encode("hello, world"))
    print(caesar_decode("khoor, zruog"))

if __name__=="__main__":
    main()