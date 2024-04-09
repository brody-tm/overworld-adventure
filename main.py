import os

locations = {
    'Dark Forest': {'North': 'Giant Cliffs', 'South': 'The Caverns', 'East': 'The Ocean', 'West': 'Green Plains'},
    'Green Plains': {'East': 'Dark Forest'},
    'Giant Cliffs': {'North': 'Heaven', 'South': 'Dark Forest', 'Enemy': 'Giant'},
    'Heaven': {'South': 'Giant Cliffs', 'Item': 'Heavenly Sword'},
    'The Ocean': {'West': 'Dark Forest', 'Item': 'Shark Tooth Necklace'},
    'The Caverns': {'North': 'Dark Forest', 'South': 'Hell'},
    'Hell': {'North': 'The Caverns', 'Enemy': 'Satan'}
}

enemies = {
    'Giant': {'HP': 80},
    'Satan': {'HP': 120}
}

current_location = 'Dark Forest'
msg = 'Welcome to Dark Forest!'
game_items = 2

inventory = []
enemies_killed = []
player_health = 100

# Clear screen
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    
# Check if there is an item in the current location and handle appropriately
def handleItem():
    if 'Item' in locations[current_location]:
        item = locations[current_location]['Item']
        # If player does not have the item
        if item not in inventory:
            print(f'You found {item}!')
            inventory.append(item)
        # Player already has the item (pretty sure not needed)
        # else:
        #     print(f'You already found {locations[current_location]['Item']}!')

# Check if there is an enemy in the current location and handle appropriately
def handleEnemy():
    if 'Enemy' in locations[current_location]:
        # If player has not killed the enemy:
            # Would player like to battle?
        # If they have, skip this
        enemy_name = locations[current_location]['Enemy']
        enemy_health = enemies[enemy_name]['HP']
        print(f'{enemy_name} lurks... HP: {enemy_health}')
        print(f'Would you like to fight {enemy_name}?')
        choice = input('> ')

# Start Game
while True:
    clear()
    print(msg)
    print('Inventory:', ', '.join(inventory), 'HP:', player_health)

    handleItem()

    handleEnemy()

    # Check if all items have been found
    if len(inventory) == game_items:
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
    
    # not used anymore
    # next_location = locations.get(current_location, {}).get(choice)
    # if next_location is not None:
    #     current_location = next_location
    #     msg = f'You are in {current_location}.'
    # else:
    #     msg = 'Not a valid direction.'
    
print('Thanks for playing!')