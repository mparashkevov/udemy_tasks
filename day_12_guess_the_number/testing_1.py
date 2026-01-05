enemies = 6

def incese_enemies(enemy):
    print(f"Enemies inside function before increase: {enemies}")
    return enemy + 2

enemies = incese_enemies(enemies)
print(f"Enemies outside function after increase: {enemies}")