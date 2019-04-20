from players import Creatures, Wizard, Dragon, SmallMonster
import random

def main():
    print_header()
    game_loop()

def print_header():
    print('---------------------------')
    print('       WiZARD GAME')
    print('---------------------------')


def game_loop():

    creatures = [
        Creatures('Shrek', 30),
        SmallMonster('Spider', 10),
        Creatures('Loki', 19),
        SmallMonster('Mutant Turtle', 50),
        Dragon('Bowser', 1000, 75, True)
    ]

    #print(creatures)
    hero = Wizard('Gandolf', 75)

    while True:

        active_creature = random.choice(creatures)
        print('A {} of level {} has appear from the acid river'.format(active_creature.name, active_creature.level))
        print()

        cmd = input('Do you [a]ttack, [r]un, or [l]ook around?')
        if cmd == 'a':
            if hero.attack(active_creature):
                creatures.remove(active_creature)
            else:
                print("The wizard runs and hides taking time to recover...")
                print("The wizard returns revitalized")

            # print('attack')
        elif cmd == 'r':
            print('The wizard flees')
        elif cmd == 'l':
            print('The wizard {} takes in the surroundings and sees'.format(hero.name))
            for i in creatures:
                print('* {} of level {}'.format(i.name, i.level))

        else:
            print("exiting game...")
            break

        if not creatures:
            print("You've defeated all the creatures.")
            break


if __name__ == '__main__':
    main()
