spisok =[]
zagadali = random.choice(spisok) 
inputnie = []
zagadalisp = []
count = 0
zagadalisp.append(zagadali) 
print('Это игра поле чудес. Начинай отгадать слово') 
bykvslov = input('Введите букву или слово')


while True:
    if len(bykvslov) == 1:
       for i in range(len(zagadalisp)):
           if zagadalisp[i] == bykvslov:        
               zagadalisp[i] = bykvslov:


    else:
        if bykvslov == zagadali:
            print('Это правильное слово!')  
        else:
            print('Это  не правильное слово.')
    inputnie.add(bykvslov) 
    count += 1

