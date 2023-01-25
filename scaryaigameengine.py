class Game:
    def __init__(self):
        self.player = Player()
        self.enemies = [Enemy(), Enemy()]
        self.items = [Item(), Item()]

    def play(self):
        while True:
            self.display_status()
            self.get_input()
            self.update_game_state()

    def display_status(self):
        print("Player health: ", self.player.health)
        print("Player inventory: ", self.player.inventory)
        print("Enemy health: ", [enemy.health for enemy in self.enemies])

    def get_input(self):
        command = input("What would you like to do? ")
        if command == "attack":
            self.player.attack(self.enemies[0])
        elif command == "pickup":
            self.player.pickup(self.items[0])
        elif command == "run":
            self.player.run()
        else:
            print("Invalid command.")

    def update_game_state(self):
        for enemy in self.enemies:
            enemy.attack(self.player)

class Player:
    def __init__(self):
        self.health = 100
        self.inventory = []

    def attack(self, enemy):
        enemy.health -= 10

    def pickup(self, item):
        self.inventory.append(item)

    def run(self):
        print("You run away.")

class Enemy:
    def __init__(self):
        self.health = 50

    def attack(self, player):
        player.health -= 5

class Item:
    def __init__(self):
        self.name = "item"

if __name__ == "__main__":
    game = Game()
    game.play()
