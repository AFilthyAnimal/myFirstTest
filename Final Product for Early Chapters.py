print('Welcome to Remind-a-pet! Please follow the Instructions!')
print('First, Please input the Amount of animals you Have')
animalNumber = int(input())

def animalAmount(animalNumber):
        if animalNumber < 1:
            return 'Please input Amount!'
        if animalNumber > 1:
            return 'Thank you!'


aniAm = animalAmount(animalNumber)
print(aniAm)


print ('Now, please Display their Names')
Animalnames = str(input())

def namesAnimals(Animalnames):
        if len(Animalnames) > 2:
            return 'thank you, I dont have to break kneecaps!'
        if len(Animalnames) < 1:
            return 'Do I have to Break your kneecaps?'

aniNa = namesAnimals(Animalnames)
print(aniNa)


animalBreeds =[]
print('Now, Last but Not least, Insert their Breed.(Note this is just a test, It wont contain all 100+ house hold animals and all subbreeds.)')
while True:
        breed = input()
        if breed == '':
            break
        animalBreeds = animalBreeds + [breed]
        print('why Thank you for their Breeds!')




print ('Now, Lets Review. You have ' + str(animalNumber) + ' Animals in Your Household.')
print('')
print('Their Names are ' + str(Animalnames) + ' Why, How pretty!')
print('')
print('With their Breeds being' + str(animalBreeds) + ' Now Thats an Army of them!')
