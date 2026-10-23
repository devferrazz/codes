a = ""
B = False
c = 0
d = ""
num = input("Enter a binary number: ")
while B == False:
    if len(num) % 3 != 0: # como o maximo de carcter no input vai ser 5
        a = "0" + num    # podemos fazer o resto de 2 em vez de 3
        for count in range(len(num)):
            for dig in num:
                print(f"Dig: {dig}")
        
        print(f"Count: {count}")