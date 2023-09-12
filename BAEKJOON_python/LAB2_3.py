name = input("Enter the name: ")
age = int(input(f"Enter the {name}'s age: "))

generation = (f'{age // 10 * 10}대')

if  age < 50:
    print(f'{name}은 {generation}이다')
else:
    print(f'{name}은 50대 이상이다')