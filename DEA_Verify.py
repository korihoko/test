# Program to verify if DEA numbers add up correctly
deaInsert = input("Hello! This is the DEA Verification Program.\n\
Please enter in the seven digit number you are trying to verify: ")

while True:
    deaInsert_fixed = input('Please recheck your number and try again: ')
    if len(deaInsert_fixed) == 7 and deaInsert_fixed.isdecimal():
# Need to check for 6 #'s and int
        deaInsert = str(deaInsert_fixed)
        position = 0
        deaList = ''
            #Trying to find a way for a for-loop to cycle through str[0:1], [1:2]
        for digit in deaInsert:
            deaList = str(deaList) + str(deaInsert[position : position + 1])
            position += 1
        #deaList is now DEA in 'str' form    check: print(type(deaList))

        first_digit = int(deaList[0:1]) + int(deaList[2:3]) + int(deaList[4:5])
        second_digit = int(deaList[1:2]) + int(deaList[3:4]) + int(deaList[5:6])
        second_digit *= 2
        total_sum = first_digit + second_digit

        if str(total_sum)[-1] == str(deaList[-1]):
            print('\nThe digit values you have entered are valid!')
            break
        else:
            print('\nThe DEA number you have entered is INVALID.')
            break
else:
    print('hi')
