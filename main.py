# ;)
#: {<J>}
#! author: Julio C. Moreira
# todo mutativo -> 3 chance -> e aleatoriza um num de 0 a 50 (aumenta) e outro de 0 a 9 -> com tempo comeca em 1 hora e vai abaixando de 5 a 5 ate 5 min -> e aceita as op de + - * / ** radiciacao binario p decimal decimal p binario (equacao) area e perimetro de triangulo quadrado retangulo lozango 

#^ LIBS ->
from random import randint, shuffle
from time import sleep
from pack import hed,cont
from math import ceil,sqrt

#^ EASY - MEDIUM - HARD ->
def game(difcult):
    global cont
    global responses
    num_big = randint(1,51)
    num_small = randint(1,10)
    op = ['x','/','+','-','p','r','bd','db']
    if difcult == 'e':
        operator = op[randint(0,3)]
        div = 10
    if difcult == 'm':
        operator = op[randint(0,5)]
        div = 5
    if difcult == 'd':
        operator = op[randint(0,7)]
        div = 2
    #/////////////////////////////#
    if cont % div == 0:
        print(f'\033[33mcongratulations! you are in the level {cont}\nnow the numbers are little long\ngod luck ;)\n\n')
        sleep(1)
        num_big = randint(cont+11,60+cont)
    elif cont == 1:
        print('\n\n\033[32;1m3')
        sleep(1)
        print('\n\n\033[33;1m2')
        sleep(1)
        print('\n\n\033[31;1m1')
        sleep(1)
        print('\n\033[34m0 go!\n\n')
        sleep(0.5)
    #//////////////////////////////#
    if operator == 'x':
        res = [num_big*num_small,num_small*num_big*2+8-10,num_big-1*num_small+8]
        shuffle(res)
        print(f'\033[31;1m{num_big} x {num_small} = ?\n',str(res).replace(',',' ').replace("'",'').replace('[','').replace(']',''))
        resp = int(input('\033[31m: '))
        #/////////////////////////////#
        if resp == (num_big*num_small):
            print('\n\n\033[32myou WIN!\n\n')
            responses.append([f' the cont: {num_big} x {num_small} (= {num_big*num_small})       the options: {res[2]} {res[1]} {res[0]}     my response: {resp}'])
            return True
        #/////////////////////////////#
        else:
            print(f'\n\n\033[31myou lose! in \033[31;1m{cont}\033[31m tentactives\n\n')
            sleep(2)
            print('\n\n\nthe your results are here: (share with your friends!)\n\n')
            for c in responses:
                print(str(c).replace('[','').replace(']','').replace("'",'').replace(',',''))
            print(f'\nbut i lost at level {cont} and the account was: {num_big} x {num_small}, my answer was: {resp}')
            return False 
    #//////////////////////////////#
    if operator == '/':
        res = [ceil(num_big/num_small),ceil(num_small/num_big+1-2*2+5-10),ceil(num_big+3/num_small+1+10)]
        shuffle(res)
        print(f'\033[31;1m{num_big} / {num_small} = ?\n',str(res).replace(',',' ').replace("'",'').replace('[','').replace(']',''))
        resp = float(input('\033[31m: '))
        #/////////////////////////////#
        if resp == (ceil(num_big/num_small)):
            print('\n\n\033[32myou WIN!\n\n')
            responses.append([f'the cont: {num_big} / {num_small} (= {ceil(num_big/num_small)})     the options: {res[2]} {res[1]} {res[0]}     my response: {resp}'])
            return True
        #/////////////////////////////#
        else:
            print(f'\n\n\033[31myou lose! in \033[31;1m{cont}\033[31m tentactives\n\n')
            sleep(2)
            print('\n\n\nthe your results are here: (share with your friends!)\n\n')
            for c in responses:
                print(str(c).replace('[','').replace(']','').replace("'",'').replace(',',''))
            print(f'\nbut i lost at level {cont} and the account was: {num_big} / {num_small}, my answer was: {resp}')
            return False
    #//////////////////////////////#
    if operator == '-':
        res = [num_big-num_small,num_small-num_big+1-6*2,(num_big-8)+1-num_small+2+7]
        shuffle(res)
        print(f'\033[31;1m{num_big} - {num_small} = ?\n',str(res).replace(',',' ').replace("'",'').replace('[','').replace(']',''))
        resp = float(input('\033[31m: '))
        #/////////////////////////////#
        if resp == (num_big-num_small):
            print('\n\n\033[32myou WIN!\n\n')
            responses.append([f'the cont: {num_big} - {num_small} (= {num_big-num_small})       the options: {res[2]} {res[1]} {res[0]}     my response: {resp}'])
            return True
        #/////////////////////////////#
        else:
            print(f'\n\n\033[31myou lose! in \033[31;1m{cont}\033[31m tentactives\n\n')
            sleep(2)
            print('\n\n\nthe your results are here: (share with your friends!)\n\n')
            for c in responses:
                print(str(c).replace('[','').replace(']','').replace("'",'').replace(',',''))
            print(f'\nbut i lost at level {cont} and the account was: {num_big} + {num_small}, my answer was: {resp}')
            return False
    #//////////////////////////////#
    if operator == '+':
        res = [num_big+num_small,num_small+num_big+1+6*2,(num_big+8)+1+num_small+2+7]
        shuffle(res)
        print(f'\033[31;1m{num_big} + {num_small} = ?\n',str(res).replace(',',' ').replace("'",'').replace('[','').replace(']',''))
        resp = float(input('\033[31m: '))
        #/////////////////////////////#
        if resp == (num_big+num_small):
            print('\n\n\033[32myou WIN!\n\n')
            responses.append([f'the cont: {num_big} + {num_small} (= {num_big+num_small})       the options: {res[2]} {res[1]} {res[0]}     my response: {resp}'])
            return True
        #/////////////////////////////#
        else:
            print(f'\n\n\033[31myou lose! in \033[31;1m{cont}\033[31m tentactives\n\n')
            sleep(2)
            print('\n\n\nthe your results are here: (share with your friends!)\n\n')
            for c in responses:
                print(str(c).replace('[','').replace(']','').replace("'",'').replace(',',''))
            print(f'\nbut i lost at level {cont} and the account was: {num_big} + {num_small}, my answer was: {resp}')
            return False
    #////////////////////////////////#
    if operator == 'p':
        res = [num_big**num_small,num_small**num_big-100+6*2,(num_big+80)+10+num_small+2+7]
        shuffle(res)
        print(f'\033[31;1m{num_big} ** {num_small} = ?\n',str(res).replace(',',' ').replace("'",'').replace('[','').replace(']',''))
        resp = float(input('\033[31m: '))
        #/////////////////////////////#
        if resp == (num_big**num_small):
            print('\n\n\033[32myou WIN!\n\n')
            responses.append([f'the cont: {num_big} ** {num_small} (= {num_big**num_small})       the options: {res[2]} {res[1]} {res[0]}     my response: {resp}'])
            return True
        #/////////////////////////////#
        else:
            print(f'\n\n\033[31myou lose! in \033[31;1m{cont}\033[31m tentactives\n\n')
            sleep(2)
            print('\n\n\nthe your results are here: (share with your friends!)\n\n')
            for c in responses:
                print(str(c).replace('[','').replace(']','').replace("'",'').replace(',',''))
            print(f'\nbut i lost at level {cont} and the account was: {num_big} ** {num_small}, my answer was: {resp}')
    #///////////////////////////////#
    if operator == 'r':
        res = [ceil(sqrt(num_big)),ceil(sqrt(num_big))-1+10*2,(ceil(sqrt(num_big))+18)+10+num_small-5+7]
        shuffle(res)
        print(f'\033[31;1m sqrt {num_big} = ?\n',str(res).replace(',',' ').replace("'",'').replace('[','').replace(']',''))
        resp = float(input('\033[31m: '))
        #/////////////////////////////#
        if resp == (ceil(sqrt(num_big))):
            print('\n\n\033[32myou WIN!\n\n')
            responses.append([f'the cont: sqrt {num_big} (= {ceil(sqrt(num_big))})       the options: {res[2]} {res[1]} {res[0]}     my response: {resp}'])
            return True
        #/////////////////////////////#
        else:
            print(f'\n\n\033[31myou lose! in \033[31;1m{cont}\033[31m tentactives\n\n')
            sleep(2)
            print('\n\n\nthe your results are here: (share with your friends!)\n\n')
            for c in responses:
                print(str(c).replace('[','').replace(']','').replace("'",'').replace(',',''))
            print(f'\nbut i lost at level {cont} and the account was: sqrt {num_big}, my answer was: {resp}')
    if operator == 'bd':
        binary = bin(num_big)
        res = [int(binary,2),(int(binary,2)-110)*3,(int(binary,2)+16)-2+num_small]
        shuffle(res)
        print(f'\033[31;1m {binary} decimal = ?\n',str(res).replace(',',' ').replace("'",'').replace('[','').replace(']',''))
        resp = float(input('\033[31m: '))
        #/////////////////////////////#
        if resp == (int(binary,2)):
            print('\n\n\033[32myou WIN!\n\n')
            responses.append([f'the cont: {num_big} decimal (= {binary})       the options: {res[2]} {res[1]} {res[0]}     my response: {resp}'])
            return True
        #/////////////////////////////#
        else:
            print(f'\n\n\033[31myou lose! in \033[31;1m{cont}\033[31m tentactives\n\n')
            sleep(2)
            print('\n\n\nthe your results are here: (share with your friends!)\n\n')
            for c in responses:
                print(str(c).replace('[','').replace(']','').replace("'",'').replace(',',''))
            print(f'\nbut i lost at level {cont} and the account was: {binary} decimal, my answer was: {resp}')
    if operator == 'db':
        res = [int(bin(num_big)[2:]),(int(bin(num_big)[2:])-110)*3,(int(bin(num_big)[2:])+16)-2+num_small]
        shuffle(res)
        print(f'\033[31;1m {num_big} binary = ?\n',str(res).replace(',',' ').replace("'",'').replace('[','').replace(']',''))
        resp = float(input('\033[31m: '))
        #/////////////////////////////#
        if resp == (int(bin(num_big)[2:])):
            print('\n\n\033[32myou WIN!\n\n')
            responses.append([f'the cont: {num_big} binary (= {bin(num_big)})       the options: {res[2]} {res[1]} {res[0]}     my response: {resp}'])
            return True
        #/////////////////////////////#
        else:
            print(f'\n\n\033[31myou lose! in \033[31;1m{cont}\033[31m tentactives\n\n')
            sleep(2)
            print('\n\n\nthe your results are here: (share with your friends!)\n\n')
            for c in responses:
                print(str(c).replace('[','').replace(']','').replace("'",'').replace(',',''))
            print(f'\nbut i lost at level {cont} and the account was: {num_big} binary, my answer was: {resp}')

def impos():
    global cont 
    global rasponses
    # helf = 3
    control = 1800
    num_big = randint(1,51)
    num_small = randint(1,10)
    op = ['x','/','+','-','p','r','bd','db','a','p']
    operator = op[0] # 0,9
    #/////////////////////////////#
    if cont % 5 == 0:
        print(f'\033[33mcongratulations! you are in the level {cont}\nnow the numbers are little long\ngod luck ;)\n\n')
        sleep(1)
        num_big = randint(cont+11,60+cont)
    elif cont == 1:
        print('\n\n\033[32;1m3')
        sleep(1)
        print('\n\n\033[33;1m2')
        sleep(1)
        print('\n\n\033[31;1m1')
        sleep(1)
        print('\n\033[34m0 go!\n\n')
        sleep(0.5)
    #//////////////////////////////#
    if operator == 'x':
        res = [num_big*num_small,num_small*num_big*2+8-10,num_big-1*num_small+8]
        shuffle(res)
        print(f'\033[31;1m{num_big} x {num_small} = ?\n',str(res).replace(',',' ').replace("'",'').replace('[','').replace(']',''))
        print(f'temp ({control}) = ',end='')
        # contor = cont(1,control)
        # contor
        resp = int(input('\n\033[31m: '))
        #/////////////////////////////#
        while cont(1,60) < 60:
            if resp == (num_big*num_small):
                print('\n\n\033[32myou WIN!\n\n')
                responses.append([f' the cont: {num_big} x {num_small} (= {num_big*num_small})       the options: {res[2]} {res[1]} {res[0]}     my response: {resp}'])
                return True
            #/////////////////////////////#
            else:
                print(f'\n\n\033[31myou lose! in \033[31;1m{cont}\033[31m tentactives\n\n')
                sleep(2)
                print('\n\n\nthe your results are here: (share with your friends!)\n\n')
                for c in responses:
                    print(str(c).replace('[','').replace(']','').replace("'",'').replace(',',''))
                print(f'\nbut i lost at level {cont} and the account was: {num_big} x {num_small}, my answer was: {resp}')
                return False 
        if resp == 0:
            print('temp termined')
    #//////////////////////////////#
    if operator == '/':
        res = [ceil(num_big/num_small),ceil(num_small/num_big+1-2*2+5-10),ceil(num_big+3/num_small+1+10)]
        shuffle(res)
        print(f'\033[31;1m{num_big} / {num_small} = ?\n',str(res).replace(',',' ').replace("'",'').replace('[','').replace(']',''))
        resp = float(input('\033[31m: '))
        #/////////////////////////////#
        if resp == (ceil(num_big/num_small)):
            print('\n\n\033[32myou WIN!\n\n')
            responses.append([f'the cont: {num_big} / {num_small} (= {ceil(num_big/num_small)})     the options: {res[2]} {res[1]} {res[0]}     my response: {resp}'])
            return True
        #/////////////////////////////#
        else:
            print(f'\n\n\033[31myou lose! in \033[31;1m{cont}\033[31m tentactives\n\n')
            sleep(2)
            print('\n\n\nthe your results are here: (share with your friends!)\n\n')
            for c in responses:
                print(str(c).replace('[','').replace(']','').replace("'",'').replace(',',''))
            print(f'\nbut i lost at level {cont} and the account was: {num_big} / {num_small}, my answer was: {resp}')
            return False
    #//////////////////////////////#
    if operator == '-':
        res = [num_big-num_small,num_small-num_big+1-6*2,(num_big-8)+1-num_small+2+7]
        shuffle(res)
        print(f'\033[31;1m{num_big} - {num_small} = ?\n',str(res).replace(',',' ').replace("'",'').replace('[','').replace(']',''))
        resp = float(input('\033[31m: '))
        #/////////////////////////////#
        if resp == (num_big-num_small):
            print('\n\n\033[32myou WIN!\n\n')
            responses.append([f'the cont: {num_big} - {num_small} (= {num_big-num_small})       the options: {res[2]} {res[1]} {res[0]}     my response: {resp}'])
            return True
        #/////////////////////////////#
        else:
            print(f'\n\n\033[31myou lose! in \033[31;1m{cont}\033[31m tentactives\n\n')
            sleep(2)
            print('\n\n\nthe your results are here: (share with your friends!)\n\n')
            for c in responses:
                print(str(c).replace('[','').replace(']','').replace("'",'').replace(',',''))
            print(f'\nbut i lost at level {cont} and the account was: {num_big} + {num_small}, my answer was: {resp}')
            return False
    #//////////////////////////////#
    if operator == '+':
        res = [num_big+num_small,num_small+num_big+1+6*2,(num_big+8)+1+num_small+2+7]
        shuffle(res)
        print(f'\033[31;1m{num_big} + {num_small} = ?\n',str(res).replace(',',' ').replace("'",'').replace('[','').replace(']',''))
        resp = float(input('\033[31m: '))
        #/////////////////////////////#
        if resp == (num_big+num_small):
            print('\n\n\033[32myou WIN!\n\n')
            responses.append([f'the cont: {num_big} + {num_small} (= {num_big+num_small})       the options: {res[2]} {res[1]} {res[0]}     my response: {resp}'])
            return True
        #/////////////////////////////#
        else:
            print(f'\n\n\033[31myou lose! in \033[31;1m{cont}\033[31m tentactives\n\n')
            sleep(2)
            print('\n\n\nthe your results are here: (share with your friends!)\n\n')
            for c in responses:
                print(str(c).replace('[','').replace(']','').replace("'",'').replace(',',''))
            print(f'\nbut i lost at level {cont} and the account was: {num_big} + {num_small}, my answer was: {resp}')
            return False
    #////////////////////////////////#
    if operator == 'p':
        res = [num_big**num_small,num_small**num_big-100+6*2,(num_big+80)+10+num_small+2+7]
        shuffle(res)
        print(f'\033[31;1m{num_big} ** {num_small} = ?\n',str(res).replace(',',' ').replace("'",'').replace('[','').replace(']',''))
        resp = float(input('\033[31m: '))
        #/////////////////////////////#
        if resp == (num_big**num_small):
            print('\n\n\033[32myou WIN!\n\n')
            responses.append([f'the cont: {num_big} ** {num_small} (= {num_big**num_small})       the options: {res[2]} {res[1]} {res[0]}     my response: {resp}'])
            return True
        #/////////////////////////////#
        else:
            print(f'\n\n\033[31myou lose! in \033[31;1m{cont}\033[31m tentactives\n\n')
            sleep(2)
            print('\n\n\nthe your results are here: (share with your friends!)\n\n')
            for c in responses:
                print(str(c).replace('[','').replace(']','').replace("'",'').replace(',',''))
            print(f'\nbut i lost at level {cont} and the account was: {num_big} ** {num_small}, my answer was: {resp}')
    #///////////////////////////////#
    if operator == 'r':
        res = [ceil(sqrt(num_big)),ceil(sqrt(num_big))-1+10*2,(ceil(sqrt(num_big))+18)+10+num_small-5+7]
        shuffle(res)
        print(f'\033[31;1m sqrt {num_big} = ?\n',str(res).replace(',',' ').replace("'",'').replace('[','').replace(']',''))
        resp = float(input('\033[31m: '))
        #/////////////////////////////#
        if resp == (ceil(sqrt(num_big))):
            print('\n\n\033[32myou WIN!\n\n')
            responses.append([f'the cont: sqrt {num_big} (= {ceil(sqrt(num_big))})       the options: {res[2]} {res[1]} {res[0]}     my response: {resp}'])
            return True
        #/////////////////////////////#
        else:
            print(f'\n\n\033[31myou lose! in \033[31;1m{cont}\033[31m tentactives\n\n')
            sleep(2)
            print('\n\n\nthe your results are here: (share with your friends!)\n\n')
            for c in responses:
                print(str(c).replace('[','').replace(']','').replace("'",'').replace(',',''))
            print(f'\nbut i lost at level {cont} and the account was: sqrt {num_big}, my answer was: {resp}')
    if operator == 'bd':
        binary = bin(num_big)
        res = [int(binary,2),(int(binary,2)-110)*3,(int(binary,2)+16)-2+num_small]
        shuffle(res)
        print(f'\033[31;1m {binary} decimal = ?\n',str(res).replace(',',' ').replace("'",'').replace('[','').replace(']',''))
        resp = float(input('\033[31m: '))
        #/////////////////////////////#
        if resp == (int(binary,2)):
            print('\n\n\033[32myou WIN!\n\n')
            responses.append([f'the cont: {num_big} decimal (= {binary})       the options: {res[2]} {res[1]} {res[0]}     my response: {resp}'])
            return True
        #/////////////////////////////#
        else:
            print(f'\n\n\033[31myou lose! in \033[31;1m{cont}\033[31m tentactives\n\n')
            sleep(2)
            print('\n\n\nthe your results are here: (share with your friends!)\n\n')
            for c in responses:
                print(str(c).replace('[','').replace(']','').replace("'",'').replace(',',''))
            print(f'\nbut i lost at level {cont} and the account was: {binary} decimal, my answer was: {resp}')
    if operator == 'db':
        res = [int(bin(num_big)[2:]),(int(bin(num_big)[2:])-110)*3,(int(bin(num_big)[2:])+16)-2+num_small]
        shuffle(res)
        print(f'\033[31;1m {num_big} binary = ?\n',str(res).replace(',',' ').replace("'",'').replace('[','').replace(']',''))
        resp = float(input('\033[31m: '))
        #/////////////////////////////#
        if resp == (int(bin(num_big)[2:])):
            print('\n\n\033[32myou WIN!\n\n')
            responses.append([f'the cont: {num_big} binary (= {bin(num_big)})       the options: {res[2]} {res[1]} {res[0]}     my response: {resp}'])
            return True
        #/////////////////////////////#
        else:
            print(f'\n\n\033[31myou lose! in \033[31;1m{cont}\033[31m tentactives\n\n')
            sleep(2)
            print('\n\n\nthe your results are here: (share with your friends!)\n\n')
            for c in responses:
                print(str(c).replace('[','').replace(']','').replace("'",'').replace(',',''))
            print(f'\nbut i lost at level {cont} and the account was: {num_big} binary, my answer was: {resp}')


    

#^ MAIN PROGRAM ->
hed('MATH GAME')

dif_esc = str(input('enter the difficulty:\n\033[34me - easy \033[35mm - medium \033[33mh - hard: ')).strip().lower()[0]

if dif_esc == 'e':   
    cont = 1
    responses = []
    while game('e') == True:
        cont += 1
        sleep(1)

elif dif_esc == 'm':
    cont = 1
    responses = []
    while game('m') == True:
        cont += 1
        sleep(1)

elif dif_esc == 'h':
    cont = 1 
    responses = []
    while game('d') == True:
        cont += 1
        sleep(1)

elif dif_esc == 'i':
    cont = 1
    responses = []
    while impos() == True:
        cont += 1
        sleep(1)


