fruit_eat={"한라봉":int(input("한라봉을 얼마나 먹었습니다까?")),
            "딸기":int(input("딸기를 얼마나 먹었습니다까?")),
            "바나나":int(input("바나나를 얼마나 먹었습니다까?")),
            "파인애플":int(input("파인애플을 얼마나 먹었습니다까?")),
            "토마토":int(input("토마토를 얼마나 먹었습니다까?"))}
kcal={"한라봉":50/100, "딸기":34/100, "바나나":77/100, "파인애플":53/100, "토마토":19/100}
fruit_eat_list=["한라봉", "딸기", "바나나", "파인애플","토마토"]
total=0
for item in fruit_eat_list:
    total += fruit_eat[item] * kcal[item]
    print(f"{item},{fruit_eat[item]}g을 먹으면 {kcal[item]} * {fruit_eat[item]} ")
print(f"먹은 과일의 총 칼로리는 {total}㎉입니다.")


