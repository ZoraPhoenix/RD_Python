# SSH Authentication Successful!!!

class Games():
    def __init__(self, name, genre, platform):
        self.name = name
        self.genre = genre
        self.platform = platform

    def print_game(self):
        print(f"Game: {self.name}, Genre: {self.genre}, Platform: {self.platform}")

HollowKnight = Games("Hollow Knight", "Metroidvania", "PC")
Undertale = Games("Undertale", "RPG", "PC")

HollowKnight.print_game()
Undertale.print_game()