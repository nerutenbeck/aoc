#%%

f = 'data/day_2.txt'

with open(f) as input:
    raw_data = input.read()

#%%
strategy_raw = raw_data.split('\n')

# %%

strategy_tuples = [tuple(s.split(" ")) for s in strategy_raw][:-1]

# %%
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

example_tuples = [('A', 'Y'), ('B', 'X'), ('C', 'Z')]

compute_total_score(example_tuples)

#%%
# total score

compute_total_score(strategy_tuples)

# %%
# part 2

