'''
num=eval(input('enter any number between 1 to 10:'))

if num==1:
    print("one")
elif num==2:
    print("two")
elif num==3:
    print("three")
elif num==4:
    print("four")
elif num==5:
    print("five")
elif num==6:
    print("six")
elif num==7:
    print("seven")
elif num==8:
    print("eight")
elif num==9:
    print("nine")
elif num==10:
    print("ten")
else:
    print('you number is not between 1 and 10')
'''
'''
num=eval(input('enter any number between 1 to 10:'))

if num not in [1,2,3,4,5,6,7,8,9,10]:
    print('you number is not between 1 and 10')
elif num==1:
    print('one')
elif num==2:
    print("two")
elif num==3:
    print("three")
elif num==4:
    print("four")
elif num==5:
    print("five")
elif num==6:
    print("six")
elif num==7:
    print("seven")
elif num==8:
    print("eight")
elif num==9:
    print("nine")
elif num==10:
    print("ten")
'''

num=eval(input('enter any number between 1 to 10:'))

conversion_dict={1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",10:"ten"}

if num in [1,2,3,4,5,6,7,8,9,10]:
    print(f'your number is: {conversion_dict[num].title()}')
else:
    print('your number is out or range, please select a number from 1 to 10')