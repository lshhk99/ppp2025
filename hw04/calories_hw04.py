#eat_fruit_1=int(input("한라봉을 몇 g먹었어?"))
#eat_fruit_2=int(input("딸기를 몇 g먹었어?"))
#eat_fruit_3=int(input("바나나를 몇 g먹었어?"))
#eat_fruit_4=int(input("파인애플을 몇 g먹었어?"))
#eat_fruit_5=int(input("토마토를 몇 g먹었어?"))
#kcal={"한라봉":50/100, "딸기":34/100, "바나나":77/100, "파인애플":53/100, "토마토":19/100}
#total_kcal=kcal["한라봉"]*eat_fruit_1+kcal["딸기"]*eat_fruit_2+kcal["바나나"]*eat_fruit_3+kcal["파인애플"]*eat_fruit_4+kcal["토마토"]*eat_fruit_5
#print(f"한라봉 {eat_fruit_1}g, 딸기 {eat_fruit_2}g, 바나나 {eat_fruit_3}g, 파인애플 {eat_fruit_4}g, 토마토{eat_fruit_5}g를 먹으면 {total_kcal}㎉를 먹은 거야")
print("="*30)
eat_fruit_1=int(input("한라봉을 몇 g먹었어?"))
eat_fruit_2=int(input("딸기를 몇 g먹었어?"))
eat_fruit_3=int(input("바나나를 몇 g먹었어?"))
eat_fruit_4=int(input("파인애플을 몇 g먹었어?"))
eat_fruit_5=int(input("토마토를 몇 g먹었어?"))
kcal=[50/100, 34/100, 77/100, 53/100, 19/100] #한라봉, 딸기, 바나나, 파인애플, 토마토
total_kcal=kcal[0]*eat_fruit_1+kcal[1]*eat_fruit_2+kcal[2]*eat_fruit_3+kcal[3]*eat_fruit_4+kcal[4]*eat_fruit_5
print(f"한라봉 {eat_fruit_1}g, 딸기 {eat_fruit_2}g, 바나나 {eat_fruit_3}g, 파인애플 {eat_fruit_4}g, 토마토{eat_fruit_5}g를 먹으면 {total_kcal}㎉를 먹은 거야")