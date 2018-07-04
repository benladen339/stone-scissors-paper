import random
print("---Игра---")
print("Камень, Ножницы, Бумага")

opp=random.randint(1,3)
if opp==1:
    gg="Камень"
elif opp==2:
    gg="Ножницы"
elif opp==3:
    gg="Бумага"

print("1) Камень")
print("2) Ножницы")
print("3) Бумага")

try:
    x=int(input("Напишите ваш выбор\n>"))
    if x==1:
        print("\nВаш выбор: Камень")
    elif x==2:
        print("\nВаш выбор: Ножницы")
    elif x==3:
        print("\nВаш выбор: Бумага")
    else:
        print("Вашего выбора не сущетсвует")
        exit()
    print("Выбор противника: "+str(gg))

except:
    print("Ошибка! Введите число!")

if opp == x:
    print("Ничья")
elif opp > x and opp != 3:
    print("Победа")
elif opp == 1 and x == 3:
    print("Победа")
else:
    print("Поражение")
