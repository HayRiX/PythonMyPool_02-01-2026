data = {
    'players': {
        'alice': {
            'items': {
                'sword': 1,
                'potion': 5,
                'shield': 1,
            },
            'total_value': 950,
            'item_count': 7
        },
        'bob': {
            'items': {
                'shield': 1,
                'sword': 1
            },
            'total_value': 700,
            'item_count': 2
        },
        'charlie': {
            'items': {
                'sword': 1,
                'potion': 9,
                'magic_ring': 1
            },
            'total_value': 1350,
            'item_count': 11
        },
        'diana': {
            'items': {
                'shield': 1,
                'sword': 1,
                'potion': 3,
                'data_crystal': 4
            },
            'total_value': 4850,
            'item_count': 9
        }
    },
    'catalog': {
        'sword': {
            'type': 'weapon',
            'value': 500,
            'rarity': 'rare'
        },
        'potion': {
            'type': 'consumable',
            'value': 50,
            'rarity': 'common'
        },
        'data_crystal': {
            'type': 'material',
            'value': 1000,
            'rarity': 'legendary'
        },
        'shield': {
            'type': 'armor',
            'value': 200,
            'rarity': 'uncommon'
        },
        'magic_ring': {
            'type': 'material',
            'value': 400,
            'rarity': 'rare'
        }
    }
}


def calculate_inventory_stats(items):
    total_value = 0
    item_count = 0
    for item_name, qty in items.items():
        item_value = data['catalog'][item_name]['value']
        total_value += item_value * qty
        item_count += qty
    return total_value, item_count


def player_inventory(player):
    player_a = data['players'][player]
    player_a_items = player_a['items']

    catalog = data['catalog']
    print(f"\n=== {player.capitalize()}'s Inventory ===")

    for item_name, qty in player_a_items.items():
        item_details = catalog.get(item_name)
        if item_details is not None:
            item_type = item_details.get('type')
            item_value = item_details.get('value')
            item_rarity = item_details.get('rarity')
            total_val = qty * item_value
            print(f"{item_name} ({item_type}, {item_rarity}): {qty}x @ "
                  f"{item_value} gold each = {total_val} gold")

    total_value, item_count = calculate_inventory_stats(player_a_items)

    print(f"\nInventory value: {total_value} gold")
    print(f"Item count: {item_count} items")

    categories = {}

    for item_name, qty in player_a_items.items():
        item_type = catalog[item_name]['type']
        categories[item_type] = categories.get(item_type, 0) + qty

    cat_strings = []
    for cat, total_qty in categories.items():
        cat_strings.append(f"{cat}({total_qty})")

    print("Categories: " + ", ".join(cat_strings))


def analytics_transaction(player1, player2, item, quantity):
    print(f"\n=== Transaction: {player1.capitalize()} gives "
          f"{player2.capitalize()} {quantity} {item} ===")

    player_a_items = data['players'][player1]['items']
    player_b_items = data['players'][player2]['items']

    if player_a_items.get(item, 0) < quantity:
        print("Transaction failed: insufficient items")
        return

    player_a_items[item] -= quantity
    if player_a_items[item] == 0:
        del player_a_items[item]

    player_b_items[item] = player_b_items.get(item, 0) + quantity

    total_value_a, item_count_a = calculate_inventory_stats(player_a_items)
    data['players'][player1]['total_value'] = total_value_a
    data['players'][player1]['item_count'] = item_count_a

    total_value_b, item_count_b = calculate_inventory_stats(player_b_items)
    data['players'][player2]['total_value'] = total_value_b
    data['players'][player2]['item_count'] = item_count_b

    print("Transaction successful!\n")
    print("=== Updated Inventories ===")
    print(f"{player1.capitalize()} {item}: {player_a_items.get(item, 0)}")
    print(f"{player2.capitalize()} {item}: {player_b_items.get(item, 0)}")


def inventory_analytics():
    catalog = data['catalog']
    players = data['players']

    max_value = -1
    most_valuable_player = ""
    for player, pdata in players.items():
        if pdata['total_value'] > max_value:
            max_value = pdata['total_value']
            most_valuable_player = player

    max_items = -1
    most_items_player = ""
    for player, pdata in players.items():
        if pdata['item_count'] > max_items:
            max_items = pdata['item_count']
            most_items_player = player

    rarity_order = {'common': 1, 'uncommon': 2, 'rare': 3, 'legendary': 4}
    max_rarity = -1
    rarest_items = []
    for item_name, details in catalog.items():
        r = rarity_order[details['rarity']]
        if r > max_rarity:
            max_rarity = r
            rarest_items = [item_name]
        elif r == max_rarity:
            rarest_items.append(item_name)

    print("\n=== Inventory Analytics ===")
    print(f"Most valuable player: {most_valuable_player.capitalize()} "
          f"({max_value} gold)")
    print(f"Most items: {most_items_player.capitalize()} ({max_items} items)")
    print(f"Rarest items: {', '.join(rarest_items)}")


def main():
    print("=== Player Inventory System ===")
    player_inventory('alice')
    analytics_transaction('diana', 'bob', 'potion', 2)
    inventory_analytics()


if __name__ == "__main__":
    main()
