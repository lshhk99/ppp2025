def average(nums):
    for num in nums:
        total = sum(nums)
        aver =  total / len(nums)
        return aver
def main():
    numbers = [3, 5, 4 ,8 ,9, 11 ,25]
    print(f"{average(numbers):.3f}")

if __name__ == "__main__":
    main()