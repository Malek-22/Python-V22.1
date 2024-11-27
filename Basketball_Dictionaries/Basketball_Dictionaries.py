# Define the Player class
class Player:
    # Constructor updated to accept a dictionary with player information
    def __init__(self, player_info):
        self.name = player_info['name']
        self.age = player_info['age']
        self.position = player_info['position']
        self.team = player_info['team']

    # Class method to populate a list of Player instances from a list of dictionaries
    @classmethod
    def get_team(cls, team_list):
        return [cls(player) for player in team_list]

# Challenge 2: Create individual player dictionaries
kevin = {
    "name": "Kevin Durant", 
    "age": 34, 
    "position": "small forward", 
    "team": "Brooklyn Nets"
}

jason = {
    "name": "Jason Tatum", 
    "age": 24, 
    "position": "small forward", 
    "team": "Boston Celtics"
}

kyrie = {
    "name": "Kyrie Irving", 
    "age": 32, 
    "position": "Point Guard", 
    "team": "Brooklyn Nets"
}

# Create Player instances using the player dictionaries
player_kevin = Player(kevin)
player_jason = Player(jason)
player_kyrie = Player(kyrie)

# Challenge 3: Create a list of players from a list of dictionaries
players = [
    {"name": "Kevin Durant", "age": 34, "position": "small forward", "team": "Brooklyn Nets"},
    {"name": "Jason Tatum", "age": 24, "position": "small forward", "team": "Boston Celtics"},
    {"name": "Kyrie Irving", "age": 32, "position": "Point Guard", "team": "Brooklyn Nets"},
    {"name": "Damian Lillard", "age": 33, "position": "Point Guard", "team": "Portland Trailblazers"},
    {"name": "Joel Embiid", "age": 32, "position": "Power Forward", "team": "Philadelphia 76ers"},
]

# Populate a new list with Player instances
new_team = []

for player_info in players:
    new_team.append(Player(player_info))

# Ninja Bonus: Using the get_team class method to create a team of Player instances
brooklyn_team = Player.get_team([
    {"name": "Kevin Durant", "age": 34, "position": "small forward", "team": "Brooklyn Nets"},
    {"name": "Jason Tatum", "age": 24, "position": "small forward", "team": "Boston Celtics"},
    {"name": "Kyrie Irving", "age": 32, "position": "Point Guard", "team": "Brooklyn Nets"},
])

# Print the results to verify the Player instances
print(f"Player 1: {player_kevin.name}, Age: {player_kevin.age}, Position: {player_kevin.position}, Team: {player_kevin.team}")
print(f"Player 2: {player_jason.name}, Age: {player_jason.age}, Position: {player_jason.position}, Team: {player_jason.team}")
print(f"Player 3: {player_kyrie.name}, Age: {player_kyrie.age}, Position: {player_kyrie.position}, Team: {player_kyrie.team}")

print("\nNew Team Players:")
for player in new_team:
    print(f"{player.name} - {player.position} - {player.team}")

print("\nBrooklyn Team:")
for player in brooklyn_team:
    print(f"{player.name} - {player.position} - {player.team}")
