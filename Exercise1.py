number_of_milk = 9
number_of_egg = 99
money = 20000
milk_price = 3000
egg_price = 2000
total_eggs = 0

print(f'My money is {money}')
print(f'milk price is {milk_price}')
print(f'egg price is {egg_price}')

if number_of_milk > 0:
    money_left = money - milk_price
    if money_left > 0:
        print(f'money is enough to buy 1 milk, money left is {money_left}')

    if number_of_egg > total_eggs:
        for i in range(number_of_egg):
            money_left = money_left - egg_price
            total_eggs += 1
            if money_left < egg_price:
                break

        if money_left > 0:
            print(f'money is enough to buy {total_eggs} eggs')
        print(f'So, I bought 1 milk and {total_eggs} eggs, money left is {money_left}')
    else:
        print('buy 1 milk only')
