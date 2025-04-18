spisok =[]
zagadali = random.choice(spisok) 
inputnie = []
print('Это игра поле чудес. Начинай отгадать слово') 
bykvslov = input('Введите букву или слово')
while True:
    if len(bykvslov) == 1:
        If bykvslov in zagadali:
            for i in range zagadali:
                if i == bykvslov:
                    print(bykvslov, end='') 
                else:
                    print('*', end=''

    else:
        if bykvslov == zagadali:
            print('Это правильное слово!') 
        else:
            print('Это  не правильное слово.')
    bykvslov = input('Введите букву или слово')
