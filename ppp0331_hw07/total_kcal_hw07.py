def total_calorie(fruits, fruit_calorie_dic):
    total_kcal = 0
    for item in fruits:
        total_kcal+=fruits[item]*fruit_calorie_dic[item]
    return total_kcal


def main():
    fruit_eat={"한라봉":int(input("한라봉을 얼마나 먹었습니다까?")),
               "딸기":int(input("한라봉을 얼마나 먹었습니다까?")),
               "바나나":int(input("한라봉을 얼마나 먹었습니다까?")),
               "파인애플":int(input("한라봉을 얼마나 먹었습니다까?")),
               "토마토":int(input("한라봉을 얼마나 먹었습니다까?"))}
    kcal={"한라봉":50/100, "딸기":34/100, "바나나":77/100, "파인애플":53/100, "토마토":19/100}
    print(f"먹은 과일의 총 칼로리는 {total_calorie(fruit_eat, kcal)}㎉입니다.")

if __name__=="__main__":
    main()

# for item in fruit_eat.keys():
#     total+=fruit_eat[item]*kcal[item]
#     # print(item, kcal[item], fruit_eat[item], kcal[item]*fruit_eat[item] )
# print(f"총 칼로리는 {total}㎉입니다.")