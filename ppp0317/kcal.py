#fruit_1는 한라봉, fruit_2는 딸기, fruit_3는 바나나, fruit_4는 파인애플, fruit_5는 토마토
fruit_1=int(input("한라봉을 몇 g먹었어?"))
fruit_2=int(input("딸기를 몇 g먹었어?"))
fruit_3=int(input("바나나를 몇 g먹었어?"))
fruit_4=int(input("파인애플을 몇 g먹었어?"))
fruit_5=int(input("토마토를 몇 g먹었어?"))
kcal_1=fruit_1*50/100
kcal_2=fruit_2*34/100
kcal_3=fruit_3*77/100
kcal_4=fruit_4*53/100
kcal_5=fruit_5*19/100
kcal_l=kcal_1+kcal_2+kcal_3+kcal_4+kcal_5
print("한라봉 {}g, 딸기 {}g, 바나나 {}g, 파인애플 {}g, 토마토{}g를 먹으면 {}㎉를 먹은 거야".format(fruit_1, fruit_2, fruit_3, fruit_4, fruit_5, kcal_l))