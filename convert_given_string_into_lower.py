usr_str=input('Enter you string: ')
usr_cnf=input('Do you want to convert you string into lower case? (Yes or No): ')

if usr_cnf.lower()=="yes":
    print(usr_str.lower())
else:
    print('you chose not to convert your text into lowercase')