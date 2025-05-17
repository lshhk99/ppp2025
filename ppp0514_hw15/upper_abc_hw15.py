def to_upper(ch):
    if 97 <= ord(ch) <= 122:   
        return chr(ord(ch)-32)
    elif 65<= ord(ch) <= 90:
        return chr(ord(ch)+32)
    else:
        return ch


def main():
    text = (input("원하는 문자열을 입력하시오"))
    result = ""
    for ch in text:
        result += to_upper(ch)
    print(result)



if __name__=="__main__":
    main()