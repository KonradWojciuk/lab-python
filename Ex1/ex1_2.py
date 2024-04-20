age = input("Enter your age: ")
money = input("Enter your money: ")

if int(age) >= 18 and int(money) > 20:
    print("You can buy a vodka")
elif int(age) >= 18 and int(money) < 20:
    print("You have not enough money but your age is ok")
elif int(age) < 18 and int(money) > 20:
    print("You have not enough age but your money is ok")
elif int(age) < 18 and int(money) < 20:
    print("You have not enough age and money")