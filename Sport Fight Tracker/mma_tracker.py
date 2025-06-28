# Use nested loops to simulate rounds and fighters
# Use lists to store figher NAMES
# Use sets to track unique moves used
# USe tuples to track fighter states
import random
import time

fighters = ["Khabib Nurmagomedov", "Conor McGregor"] # List of fighter names

fighter_stats = { # Tuple of fighter stats (Weight in pounds, Height in inches)
    "Khabib Nurmagomedov": (155, 78),
    "Conor McGregor": (155, 76),
}

move_log = { # DIctionary to track moves used per fighter
    fighter: set() for fighter in fighters
}

all_moves = ["Jab", "Cross", "Leg Kick", "Body Kick", "Left Hook", "Body Punch", "Left Body Hook", "Head Kick", "Front Kick", "Elbow", "Knee", "Double-Leg Takedown", "Judo Hip Toss", "Hammer Fist", "Right Hook", "Body Cross", "Body Jab", "Spinning Back Fist", "Spinning Back Kick", "Crane Kick", "Switch Kick", "Double Jab"] # Pre-defined moves fighters will use

health = {fighter: 100 for fighter in fighters} # Initialize health with 100 points

scores = {fighter: 0 for fighter in fighters} # Initialize total scores with 0

# List of MMA Commenary lines
commentary = [
    "What a phenomenal display of skill!",
    "Both fighters are showing great heart tonight.",
    "This is a technical masterpiece in the making.",
    "You can feel the tension in the arena.",
    "Those strikes are landing with precision!",
    "An incredible pace from both warriors.",
    "This fight could go either way, folks.",
    "The crowd is on their feet as the action heats up!",
    "Neither fighter is giving an inch.",
    "Expect fireworks in the next round!"
]
# Health bar function
def print_health_bar(current_health, max_health = 100, bar_length=20):
    health_ratio = current_health / max_health
    filled_length = int(bar_length * health_ratio)
    bar = '🟩' * filled_length + '-' * (bar_length - filled_length)
    return f"[{bar}] {current_health}/{max_health} HP"

# Bruce buffer intro for fighters
def intro(fighters):
    print("\n*** Now, ladies and gentlemen... ***")
    time.sleep(0.3)
    print("Introducing first, fighting out of the blue corner...")
    time.sleep(0.3)
    print(f"Weight: {fighter_stats[fighters[0]][0]} lbs, Health: {fighter_stats[fighters[0]][1]} inches") 
    time.sleep(0.3)
    print(f"Please welcome... {fighters[0]}!")
    time.sleep(0.3)
    print("\nAnd now, fighting out of the red corner...")
    time.sleep(0.3)
    print(f"Weight: {fighter_stats[fighters[1]][0]} lbs, Height: {fighter_stats[fighters[1]][1]} inches")
    time.sleep(0.3)
    print(f"Please welcome... {fighters[1]}!")
    time.sleep(0.3)
    print("\nLet's get ready to rumble!\n")
    time.sleep(0.3)

intro(fighters) # Call intro before fight begins

round_move_count = {fighter: {} for fighter in fighters}
round_damage = {fighter: 0 for fighter in fighters}
winner_by_ko = None

for round in range(1, 4): # Simulate 3 rounds
    print(f"\nROUND {round}")
    time.sleep(0.5)

    for fighter in fighters:
        print(f"\n{fighter} enters the octagon!")
        time.sleep(0.5)

        for i in range(5): # Each fighter uses 5 moves per round
            move = random.choice(all_moves)
            move_log[fighter].add(move)
            print(f"{fighter} uses {move}.")
            time.sleep(0.5)

            round_move_count[fighter][move] = round_move_count[fighter].get(move, 0) + 1 # Counts moves in each round
        
        damage = random.randint(5, 20) # Simulates damage for each round
        round_damage[fighter] = damage
        health[fighter] = max(0, health[fighter] - damage)

        if random.randint(1, 10) ==1:
            winner_by_ko = fighter
            print(f"\n💥{fighter} lands a DEVASTATING SHOT! {fighter} knocks them out cold!")
            break
    if winner_by_ko:
        break # Stop entire match on KO

# Decides round winnter: Fighter will less damage loses, 10 point must system
    if round_damage[fighters[0]] < round_damage[fighters[1]]:
        scores[fighters[0]] += 10
        scores[fighters[1]] += 9
    elif round_damage[fighters[1]] < round_damage[fighters[0]]:
        scores[fighters[1]] += 10
        scores[fighters[0]] += 9
    else:
        scores[fighters[0]] += 10
        scores[fighters[1]] += 10

    if round < 3: # Commentary after each round
        comment = random.choice(commentary)
        print(f"{comment}")
        time.sleep(1)

# If there was a knocked, skip scoring and name winnrer
if winner_by_ko:
    print((f"\nWinner by knockout, {winner_by_ko}! 🏆"))

else:
    print("\nHealth after fight: ")

    for fighter in fighters:
        print(f"{fighter}: {print_health_bar(health[fighter])}")
        time.sleep(0.5)

    print("\nStrikes Thrown: ")
    for fighter in fighters:
        print(f"{fighter}:")
        time.sleep(0.5)
    for move, count in round_move_count[fighter].items():
        print(f" {move}:{count}")
        time.sleep(0.3)

    
    print("\n---Fighter Summary---")

    for fighter in fighters:
        weight_lbs, height_inches = fighter_stats[fighter] # Retrieves tuple of weight & height inside of dictionary & assigns them

        moves = move_log[fighter] # Retrieves set of moves used by a fighter in move_log by a fighter inside, then stores it in moves

        sampled_moves = random.sample(list(moves), min(5, len(moves))) # ensures if fighter uses less than 5 moves, wont be an error, then picks 5 moves from set

        print(f"\n{fighter} (Height: {height_inches} in, Weight: {weight_lbs} lbs.)")

        print(f"Unique moves used {', '.join(sampled_moves)}!") # prints a message showing all unique moves used by fighter by joining the items in the moves set into a single comma-separated string.

        print(f"Final Health: {print_health_bar(health[fighter])}")
        time.sleep(0.5)

    # Decides overall winner
    if health[fighters[0]] > health[fighters[1]]:
        overall_winner = fighters[0]
    elif health[fighters[1]] > health[fighters[0]]:
        overall_winner = fighters[1]
    else:
        overall_winner = None # Draw

    if overall_winner:
        print(f"\nWinner is {overall_winner}!")
    else:
        print(("\nFight is a draw!"))

# Add commnets for all functions and complex blocks, wrapping the main fight simulation into a function/ class, add user input options to pick fighters, numbers of rounds, time limit, expand fighter stats (stamina, speed ) that influence damage or move choice, add more detailed scoring based on move types/ damage dealt, add unit tests for functions like print_health_bar, use logging instead of print for better debugging control