# import module random
import random

# initialize random seed generator
random.seed()

# random numbers
champ = random.randint(1,8)

# declaration of champions
draven = 1
jinx = 2
twitch = 3
ashe = 4
vayne = 5
caitlyn = 6
kalista = 7
xayah = 8

# output
print("Welcome to ADC-Selector!")

if champ == draven:
    print("You should pick Draven!")

if champ == jinx:
    print("You should pick Jinx!")

if champ == twitch:
    print("You should pick Twitch!")

if champ == ashe:
    print("You should pick Ashe!")

if champ == vayne:
    print("You should pick Vayne!")

if champ == caitlyn:
    print("You should pick Caitlyn!")

if champ == kalista:
    print("You should pick Kalista!")

if champ == xayah:
    print("You should pick Xayah!")
