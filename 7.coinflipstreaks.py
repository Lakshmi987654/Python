import random

def flip_coin():
    return random.choice(['H', 'T'])

def longest_streak(flips):
    max_streak = 1
    current_streak = 1
    
    for i in range(1, len(flips)):
        if flips[i] == flips[i-1]:
            current_streak += 1
        else:
            if current_streak > max_streak:
                max_streak = current_streak
            current_streak = 1
    # Check at the end
    if current_streak > max_streak:
        max_streak = current_streak
    return max_streak

def simulate_coin_flips(num_flips=100):
    flips = [flip_coin() for _ in range(num_flips)]
    print("Flips:", ''.join(flips))
    streak = longest_streak(flips)
    print(f"Longest streak in {num_flips} flips: {streak}")

# Run the simulation
simulate_coin_flips(100)
