#%%
import collections
import copy
from parse import parse

MOVE_FMT = "move {n:d} from {from_stack:d} to {to_stack:d}"

class ElfCrates:
    def __init__(self, input_path):
        with open(input_path) as f:
            raw_data = f.read()
        
        # construct crates
        crates_moves_split = raw_data.split('\n\n')
        rows = crates_moves_split[0].split('\n')

        stacks = collections.defaultdict(list)
        for row in rows[:-1]:
            stack = 1
            for index, c in enumerate(row):
                if (index - 1) % 4 == 0:
                    if c != " ":
                        stacks[stack].append(c)
                    stack += 1
        sorted_stacks = dict(sorted(stacks.items()))

        self.stacks = sorted_stacks
        move_list = crates_moves_split[1].split('\n')
        self.moves = [parse(MOVE_FMT, move) for move in move_list]

    def move_em(self, stacks, move):
    
        # crane moves one at a time
        for idx in range(move['n']):
            popped = stacks[move['from_stack']].pop(0)
            stacks[move['to_stack']].insert(0, popped)
        return stacks

    def move_crates(self):
        stacks_updated = copy.deepcopy(self.stacks)
        for move in self.moves:
            stacks_updated = self.move_em(stacks = stacks_updated, move = move)
        return stacks_updated

input_path = 'example_data/day_5_example.txt'

elf_crates = ElfCrates(input_path)

#%%
elf_crates.stacks

#%%
elf_crates.moves

#%%

tst = elf_crates.move_crates()

# %%
