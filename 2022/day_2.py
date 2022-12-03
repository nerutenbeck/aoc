#%%

f = 'data/day_2.txt'

with open(f) as input:
    raw_data = input.read()

#%%
strategy_raw = raw_data.split('\n')

# %%

strategy_tuples = [tuple(s.split(" ")) for s in strategy_raw][:-1]
example_tuples = [('A', 'Y'), ('B', 'X'), ('C', 'Z')]


# %%
# Part 1
# Play scores

def compute_play_score(tup):
    score_dict = {"X" : 1, "Y" : 2, "Z" : 3}
    return score_dict[tup[1]]

# %%
# Compute wins

def compute_win_score(tup):
    win_tuples = [
        ('A', 'Y'), # rock, paper
        ('B', 'Z'), # paper, scissors
        ('C', 'X') # scissors, rock
    ]
    draw_tuples = [
        ('A', 'X'), # rock, rock
        ('B', 'Y'), # paper, paper
        ('C', 'Z') # scissors, scissors
    ]
    score = 6 if tup in win_tuples else 3 if tup in draw_tuples else 0
    return score

def compute_total_score(tup_list):
    round_scores = [
        compute_win_score(t) + compute_play_score(t) for t in tup_list
    ]
    return sum(round_scores)

#%%
# example score

compute_total_score(example_tuples)

#%%
# total score

compute_total_score(strategy_tuples)

# %%
# part 2

def decode_strategy(strategy_tuple):
    play_dict = {'A' : 'rock', 'B' : 'paper', 'C' : 'scissors'}
    outcome_dict = {'X' : 'lose', 'Y' : 'draw', 'Z' : 'win'}
    decoded = (play_dict[strategy_tuple[0]], outcome_dict[strategy_tuple[1]])
    return decoded

decoded_example_strategies = [decode_strategy(t) for t in example_tuples]
decoded_real_strategies = [decode_strategy(t) for t in strategy_tuples]

# %%
def make_play(decoded_strategy):
    
    # play keys for outcomes
    win_dict = {'rock' : 'paper', 'paper' : 'scissors', 'scissors' : 'rock'}
    lose_dict = {'rock' : 'scissors', 'paper' : 'rock', 'scissors' : 'paper'}    
    
    outcome = decoded_strategy[1]
    opponent_play = decoded_strategy[0]
    
    if outcome == 'win':
        return win_dict[opponent_play]
    elif outcome == 'lose':
        return lose_dict[opponent_play]
    else:
        return opponent_play

example_plays = [make_play(d) for d in decoded_example_strategies]
real_plays = [make_play(d) for d in decoded_real_strategies]

# %%
def score_round(strategy_tuple):    
    # Decode and make play
    decoded = decode_strategy(strategy_tuple)
    outcome = decoded[1]
    play = make_play(decoded)

    # Count score
    outcome_score_dict = {'win' : 6, 'draw' : 3, 'lose' : 0}
    play_score_dict = {'rock' : 1, 'paper' : 2, 'scissors' : 3}

    outcome_score = outcome_score_dict[outcome]
    play_score = play_score_dict[play]
    total_score = outcome_score + play_score
    return total_score

# %%

example_scores = [score_round(t) for t in example_tuples]
print(example_scores)

example_total = sum(example_scores)
print(example_total)

# %%

real_scores = [score_round(t) for t in strategy_tuples]
real_total = sum(real_scores)
print(real_total)
# %%
