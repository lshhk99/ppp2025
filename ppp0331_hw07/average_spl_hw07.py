def average(nums):
    for num in nums:
        total = sum(nums)
        aver =  total / len(nums)
        return aver
def main():
    number_text = "5, 3, 8, 9, 7, 14, 13"
    nums = number_text.split(",")
    numbers = []
    for num in nums:
        numbers.append(int(num))
    print(average(numbers))

    # numbers_text = "5, 3, 8, 9, 7, 14, 13"
    # numbers =[int(x)for x in numbers_text.split(",") ]
    # print(f"{average(numbers):.3f}")

if __name__ == "__main__":
    main()