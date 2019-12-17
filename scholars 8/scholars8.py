scholars = {}

def register(num, name, fname, age, score):
    scholars[num] = [name, fname, age, score]
    print (scholars)

def remove(num):
    scholars.pop(num)
    print (scholars)

def show_by_code(num):
    print (scholars[num])

def show_by_name(dictOfElements, valueToFind):
    listOfKeys = list()
    listOfItems = dictOfElements.items()
    for item  in listOfItems:
        if item[1][0] == valueToFind:
            listOfKeys.append(item[0])
    print  (listOfKeys)

def show_by_fname(dictOfElements, valueToFind):
    listOfKeys = list()
    listOfItems = dictOfElements.items()
    for item  in listOfItems:
        if item[1][1] == valueToFind:
            listOfKeys.append(item[0])
    print  (listOfKeys)

def show_by_age(dictOfElements, valueToFind):
    listOfKeys = list()
    listOfItems = dictOfElements.items()
    for item  in listOfItems:
        if item[1][2] == valueToFind:
            listOfKeys.append(item[0])
    print  (listOfKeys)

def show_by_score(dictOfElements, valueToFind):
    listOfKeys = list()
    listOfItems = dictOfElements.items()
    for item  in listOfItems:
        if item[1][3] == valueToFind:
            listOfKeys.append(item[0])
    print  (listOfKeys)

def look_for(dictOfElements, valueToFind):
    listOfKeys = list()
    listOfItems = dictOfElements.items()
    for item  in listOfItems:
        print(item[1])
        if valueToFind in item[1]:
            listOfKeys.append(item[0])
    print(listOfKeys)

def change(num, name, fname, age, score):
    scholars[num] = [name, fname, age, score]
    print (scholars[num])

def save():
    x = str(scholars)
    f = open("scholars_data.py","w")
    f.write(x)
    f.close()
    

loop = 1
print ('Welcome to scholars \n you can see the help section by writing //help\n thanks ;)\n')
print ('-- menu : --------------------\n 1 register\n 2 remove\n 3 show\n 4 change\n 5 //help or help\n 6 save\n 7 about\n 8 open\n 9 exit\n'+"-"*30)
while loop == 1:
    action = input('\n# ')
    if action == 'register' or action == '1':
        register(input('scholar code: '), input('name: '), input('fname: '), input('age: '), input('score: '))
    elif action == 'remove' or action == '2':
        remove(input('scholar code: '))
    elif action == "show" or action == '3':
        print ('-- show : --------------------\n 3-1 show-by-code\n 3-2 show-by-name\n 3-3 show-by-fname\n 3-4 show-by-age\n 3-5 show-by-score\n 3-6 look-for\n'+"-"*30)
        pass
    elif action == 'show-by-code' or action == '3-1':
        show_by_code(input('scholar code: '))
    elif action == 'show-by-name' or action == '3-2':
        show_by_name(scholars,input('scholar name: '))
    elif action == 'show-by-fname' or action == '3-3':
        show_by_fname(scholars,input('scholar fname: '))
    elif action == 'show-by-age' or action == '3-4':
        show_by_age(scholars,input('scholar age: '))
    elif action == 'show-by-score' or action == '3-5':
        show_by_score(scholars,input('scholar score: '))
    elif action == 'look-for' or action == '3-6':
        look_for(scholars,input('look for: '))
    elif action == 'change' or action == '4':
        change(input('scholar code: '), input('name: '), input('fname: '), input('age: '), input('score: '))
    elif action == '//help' or action == '5' or action == 'help':
        print ('-- List of commands : --------\n 1 register\n 2 remove\n 3 show\n 4 change\n 5 //help or help\n 6 save\n 7 about\n 8 open\n 9 exit\n'+"-"*30)
    elif action == 'save' or action == '6':
    	save()
    	print('-- save : --------------------\nfile saved as scholars_data.py\n'+'-'*30)
    elif action == 'about' or action == '7':
    	print("-- about : -------------------\nScholars is an open-source app made in python by ali mokhtari (ali82496) \nlicensed under gpl-v3\n"+'-'*30)
    elif action == 'open' or action == '8':
        f = open(r"scholars_data.py","r")
        x = f.read()
        scholars = eval(x)
        f.close()
        print('-- open : --------------------\nfile opened\n'+'-'*30)
        print(scholars)
    elif action == 'exit' or action == '9':
    	print('-- exit : --------------------\nprogram finished\n'+'-'*30)
    	break
    else :
        print("command not found \n type //help for list of commands\n")
        pass
