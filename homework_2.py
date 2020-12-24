user = []

first_name = input("Isminizi giriniz: ")
last_name = input("Soyisminizi giriniz: ")
age = int(input("Yasinizi giriniz: "))
date_of_birth = input("Dogum tarihinizi giriniz: ")

user.append(first_name)
user.append(last_name)
user.append(age)
user.append(date_of_birth)

for i in user:
    print(i)
    if type(i)==type(1) and i < 18:
        print("You can't go out because it's too dangerous")
    elif type(i)==type(1) and i > 18:
        print("You can go out to the street")   