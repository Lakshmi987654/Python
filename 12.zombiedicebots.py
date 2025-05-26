import random

# Dice setup: colors with faces
dice_cup = {
    'green':  ['brain', 'brain', 'brain', 'footsteps', 'footsteps', 'shotgun'],
    'yellow': ['brain', 'brain', 'footsteps', 'footsteps', 'shotgun', 'shotgun'],
    'red':    ['brain', 'footsteps', 'footsteps', 'shotgun', 'shotgun', 'shotgun']
}

dice_distribution = ['green']*6 + ['yellow']*4 + ['red']*3

def draw_dice(cup, count=3):
    return random.sample(cup, count)

def roll_die(color):
    return random.choice(dice_cup[color])

def zombie_dice_turn(strategy_name):
    cup = dice_distribution.copy()
    brains_collected = 0
    shotgun_count = 0
    footprints = []

    print(f"\n{strategy_name} turn starts!")

    while True:
        # Draw dice to have 3 total dice to roll this round
        dice_to_roll = footprints
        footprints = []
        dice_needed = 3 - len(dice_to_roll)

        if dice_needed > 0:
            if len(cup) < dice_needed:
                # Refill cup from used dice except footprints
                cup += dice_distribution
            dice_to_roll += draw_dice(cup, dice_needed)
            for d in dice_to_roll[-dice_needed:]:
                cup.remove(d)

        print(f"Rolling dice: {dice_to_roll}")

        # Roll each die
        for die in dice_to_roll:
            result = roll_die(die)
            print(f"Rolled {die} die: {result}")
            if result == 'brain':
                brains_collected += 1
            elif result == 'shotgun':
                shotgun_count += 1
            else:  # footsteps
                footprints.append(die)

        print(f"Brains: {brains_collected}, Shotguns: {shotgun_count}, Footprints to reroll: {footprints}")

        if shotgun_count >= 3:
            print("Shotguned! Turn over, no brains collected this turn.")
            return 0

        # Strategy to decide whether to keep rolling
        if strategy_name == "CautiousBot":
            # Stop if 2 or more brains collected
            if brains_collected >= 2:
                print("CautiousBot stops.")
                return brains_collected
        elif strategy_name == "RiskyBot":
            # Always roll unless 2+ shotguns
            if shotgun_count >= 2:
                print("RiskyBot stops due to shotguns.")
                return brains_collected
        else:
            # Default: stop after first roll
            return brains_collected

def play_game():
    scores = {"CautiousBot": 0, "RiskyBot": 0}
    winning_score = 13
    turn_order = ["CautiousBot", "RiskyBot"]
    current = 0

    while max(scores.values()) < winning_score:
        player = turn_order[current]
        print(f"\n=== {player}'s turn ===")
        turn_score = zombie_dice_turn(player)
        scores[player] += turn_score
        print(f"{player} total brains: {scores[player]}")
        current = (current + 1) % len(turn_order)

    winner = max(scores, key=scores.get)
    print(f"\nGame over! Winner: {winner} with {scores[winner]} brains!")

if __name__ == "__main__":
    play_game()
