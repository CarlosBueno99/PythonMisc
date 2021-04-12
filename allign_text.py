import os
t_w=os.get_terminal_size().columns

given_str = input("Enter your string: ")

usr_confirmation = input('Do you want to write down your text? (Yes or No): ')

if usr_confirmation.lower()=="yes":
    print(given_str.title().center(t_w))
    print(given_str.title().ljust(t_w))
    print(given_str.title().rjust(t_w))

elif usr_confirmation.lower()=="no":
    print('you chose not to write you text')
    
else:
    print('you didn´t answer the question with a valid answer, so we assumed the answer was "no"')
