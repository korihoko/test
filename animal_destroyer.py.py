
# animalList = input('Hello, and welcome to the animal destroyer.\nPlease type in ALL animals to be destroyed.\n')
# animalList = animalList.split(" ")
# animalList = list[animalList]
# print(animalList)

animals = ['cat', 'bat', 'rat', 'cat', 'hat', 'cat']
print('Hello, this is the animal destroyer.\nToday we have the following list of animals.\n' + str(animals))

chosenOne = input('Which animal would you like to destroy?\n')

if chosenOne in animals:
    animals.remove(chosenOne)
    print('One ' + chosenOne + ' has been removed.')
else:
    print('All ' + chosenOne + ' has been removed.')


while chosenOne in animals:
    animals.remove(chosenOne)
    print('One ' + chosenOne + ' has been removed.')
else:
    print('All ' + chosenOne + ' has been removed.')


for chosenOne in animals:
    animals.remove(chosenOne)
    print('One ' + chosenOne + ' has been removed.')
else:
    print('All ' + chosenOne + ' has been removed.')




print('All chosen animals have been destroyed.\nThe remaining animals are: ' + str(animals))


