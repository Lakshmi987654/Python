import random

def invent_character():
    races = ['Elf', 'Dwarf', 'Human', 'Orc', 'Goblin', 'Dragonborn', 'Tiefling']
    classes = ['Warrior', 'Mage', 'Rogue', 'Cleric', 'Ranger', 'Paladin', 'Bard']
    weapons = ['Sword', 'Bow', 'Staff', 'Dagger', 'Axe', 'Mace', 'Spear']
    abilities = ['Fireball', 'Invisibility', 'Healing', 'Lightning Strike', 'Shadowstep', 'Earthquake', 'Charm']

    character = {
        'Race': random.choice(races),
        'Class': random.choice(classes),
        'Weapon': random.choice(weapons),
        'Special Ability': random.choice(abilities)
    }

    return character

def main():
    print("Welcome to Fantasy Game Inventor!")
    while True:
        char = invent_character()
        print("\nYour new fantasy character:")
        for key, value in char.items():
            print(f"  {key}: {value}")

        again = input("\nCreate another character? (y/n): ").lower()
        if again != 'y':
            print("Good luck on your ad
