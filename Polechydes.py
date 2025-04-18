spisok =['ножницы', 'бактерия', 'ромашка', 'абрикос', 'чемодан', 'студент', 'дегенерация', 'шестерёнки', 'запятая', 'склонение', 'одушевлённость', 'висилица', 'кувшинка', 'рассвет', 'пингвин']
zagadali = random.choice(spisok) 
inputnie = []
nadosp = []
nadosp.append(zagadali) 
zagadalisp = ['*'] * len(zagadali) 
count = 0
print('Это игра поле чудес. Начинай отгадать слово') 
bykvslov = input('Введите букву или слово')


while True:
    if bykvslov not in inputnie:
        if len(bykvslov) == 1:
            if zagadalisp != nadosp:
               for i in range(len(zagadali)):
                  if zagadali[i] == bykvslov:        
                     zagadalisp[i] = bykvslov:
            for j in zagadalisp:
            print(j, end='') 

        else:
            if bykvslov == zagadali:
                print('Это правильное слово!')
                break
            else:
                print('Это  не правильное слово.')
        inputnie.add(bykvslov) 
        count += 1
    else:
        print('Это уже было введено') 

