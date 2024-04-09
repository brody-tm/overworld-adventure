import os

locations = {
    'Dark Forest': {'North': 'Giant Cliffs', 'South': 'The Caverns', 'East': 'The Ocean', 'West': 'Green Plains'},
    'Green Plains': {'East': 'Dark Forest'},
    'Giant Cliffs': {'North': 'Heaven', 'South': 'Dark Forest', 'Enemy': 'Giant'},
    'Heaven': {'South': 'Giant Cliffs', 'Item': 'Heavenly Sword'},
    'The Ocean': {'West': 'Dark Forest', 'Item': 'Shark Tooth Hatchet'},
    'The Caverns': {'North': 'Dark Forest', 'South': 'Hell', 'Item': 'Wooden Slingshot'},
    'Hell': {'North': 'The Caverns', 'Enemy': 'Satan'}
}

enemies = {
    'Giant': {'HP': 80},
    'Satan': {'HP': 120}
}

game_items = {
    'Heavenly Sword': {'DMG': 40},
    'Shark Tooth Hatchet': {'DMG': 25},
    'Wooden Slingshot': {'DMG': 15}
}

current_location = 'Dark Forest'
msg = 'Welcome to Dark Forest!'

inventory = []
enemies_killed = []
player_HP = 100

# Clear screen
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Check if there is an item in the current location and handle appropriately
def handleItem(location):
    if 'Item' in location:
        item_name = location['Item']
        item_DMG = game_items[item_name]['DMG']
        if item_name not in inventory:
            print(f'You found {item_name}! It does {item_DMG} DMG!')
            inventory.append(item_name)

# Check if there is an enemy in the current location and handle appropriately
def handleEnemy(location):
    if 'Enemy' in location:
        enemy_name = location['Enemy']
        enemy_HP = enemies[enemy_name]['HP']
        if enemy_name not in enemies_killed:
            print(f'{enemy_name} lurks... HP: {enemy_HP}')
            while True:
                print(f'Would you like to fight {enemy_name}? (Y/N)')
                choice = input('> ').upper()
                if choice == 'Y':
                    print(f'You choose to fight {enemy_name}.')
                    # Add logic for fighting the enemy here
                    break
                elif choice == 'N':
                    print('You choose to flee.')
                    break
                else:
                    print('Invalid choice. Please enter Y or N.')

# Start Game
while True:
    clear()
    print(msg)
    print('Inventory:')
    for item in inventory:
        item_DMG = game_items[item]['DMG']
        print(f'  {item} (DMG: {item_DMG})')
    print('HP:', player_HP)

    handleItem(locations[current_location])

    handleEnemy(locations[current_location])

    # Check if all items have been found
    if len(inventory) == len(game_items):
        print('You have found all the items!')
        print('Your items:', ', '.join(inventory))
        break

    # Player move
    print('Which way would you like to go?')
    choice = input('> ').title()
    try:
        current_location = locations[current_location][choice]
        msg = f'You are in {current_location}.'
    except:
        msg = f'Not a valid direction.\nYou are in {current_location}.'
    
print('Thanks for playing!')