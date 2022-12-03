#%%
import string

example = [
    'vJrwpWtwJgWrhcsFMMfFFhFp',
    'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL',
    'PmmdzqPrVvPwwTWBwg',
    'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn',
    'ttgJtRGJQctTZtZT',
    'CrZsJsPPZsGzwwsLwLmpwMDw'
]

#%% find shared item

def prioritize_shared_item(rucksack):

    priorities = dict(
        zip(string.ascii_lowercase + string.ascii_uppercase, range(1, 53))
    )

    i = int(len(rucksack) / 2)
    c1 = set(rucksack[:i])
    c2 = set(rucksack[i:])
    shared_item = c1.intersection(c2)
    priority = priorities[list(shared_item)[0]]
    return(priority)

assert prioritize_shared_item(example[0]) == 16

example_priorities = [prioritize_shared_item(e) for e in example]
assert example_priorities == [16, 38, 42, 22, 20, 19]
assert sum(example_priorities) == 157

print(example_priorities)
print(sum(example_priorities))

# %%

def get_priority_sum(path):

    total_priority = 0
    with open(path, 'r') as rdr:
        for rucksack in rdr.readlines():
            priority = prioritize_shared_item(rucksack)
            total_priority += priority
    return total_priority

priorities_total = get_priority_sum('data/day_3.txt')
print(priorities_total) # 8349

# %%
