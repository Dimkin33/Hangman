from random import randint
nouns = [
    "компьютер", "программист", "инженер", "машина", 
    "облако", "телефон", "планшет", "алгоритм", 
    "инструкция", "технология", "путеводитель", "автомобиль"
]

hangman = {
'hangman':[
'-----',
'|   |',
'|'    ,
'|'    ,
'|'    ,
'|'    ,
'------'],
'men': [
'|   O'  ,
'|   |'  ,
'|  /|'  ,
'|  /|\\',
'|  /',
'|  / \\',
]}
word = nouns[randint(0, len(nouns)-1)]

#print(*ris_full, sep = '\n')
def hangman_print(attempt):
    print(*hangman['hangman'][0:2], sep = '\n')
    match attempt:
        case 0:
            print(*hangman['hangman'][2:], sep = '\n')
        case 1:
            print(hangman['men'][0], sep = '\n')
            print(*hangman['hangman'][3:], sep = '\n')
        case 2:
            print(*hangman['men'][0:2], sep = '\n')
            print(*hangman['hangman'][4:], sep = '\n')           
        case 3:
            print(hangman['men'][0], sep = '\n')     
            print(hangman['men'][2], sep = '\n')
            print(*hangman['hangman'][4:], sep = '\n') 
        case 4:
            print(hangman['men'][0], sep = '\n')     
            print(hangman['men'][3], sep = '\n')
            print(*hangman['hangman'][4:], sep = '\n') 
        case 5:
            print(hangman['men'][0], sep = '\n')     
            print(hangman['men'][3], sep = '\n')
            print(hangman['men'][4], sep = '\n')
            print(*hangman['hangman'][5:], sep = '\n') 
        case 6:
            print(hangman['men'][0], sep = '\n')     
            print(hangman['men'][3], sep = '\n')
            print(hangman['men'][5], sep = '\n')
            print(*hangman['hangman'][5:], sep = '\n') 
#class Hangman:
hangman_print(0)

letters = set()
attempt = 0
while attempt < 7:
    t = 0
    char = input('Введите букву: ')
    if char == '':
        break
    if not char in word:
        attempt += 1
    letters.add(char)
    print('осталось попыток ',6 - attempt)
    print('буквы: ', letters)
    hangman_print(attempt)
    print("На данный момент слово выглядит так:")
    for char in word:
        if char in letters:
            print(char, end = '')
        else:
            print('_', end = '')
            t += 1
            
    if t == 0:
        print('')
        print('Victory')
    if attempt == 7:
        print('')
        print(f'Right word was {word}')
        print('GG')
