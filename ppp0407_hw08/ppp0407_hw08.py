def average(nums):
    for num in nums:
        total = sum(nums)
        aver =  total / len(nums)
    return aver

def minmax(nums):
    return min(nums), max(nums)

def median(nums):
    sorted_list = sorted(nums)
    return sorted_list[len(sorted_list)//2]

def read_text(filename):
    text =""
    with open(filename) as f:
        lines = f.readlines()
        for line in lines:
            print(f"!{text.strip()}!")
            text +=" " + line.strip()
    return text

def read_numbers(filename):
    nums = []
    with open(filename) as f:
        lines = f.readlines()
        for line in lines:
            nums.append(int(line.strip()))
    return nums

def main():
    line = sorted(read_numbers("numbers2.txt"))
    mn, mx = minmax(line)
    print(line)
    print(f"총 숫자의 개수는 {len(line)}개 입니다.")
    print(f"평균값은 {average(line)}입니다.")
    print(f"최댓값은 {mx} 입니다")
    print(f"최솟값은 {mn} 입니다")
    print(f"중앙값은 {median(line)}입니다.")

if __name__=="__main__":
    main()