#%%
import collections
import copy
from parse import parse

MOVE_FMT = "move {n:d} from {from_stack:d} to {to_stack:d}"
class ElfCrates:
    def __init__(self, input_path,  mover_model):
        with open(input_path) as f:
            raw_data = f.read()
        
        self.mover_model = mover_model

        crates_moves_split = raw_data.split('\n\n')

        self.start_stacks = self.stack_crates(
            raw_crates = crates_moves_split[0]
        )
        self.moves = self.parse_moves(raw_moves = crates_moves_split[1])
        
        self.end_stacks = self.move_crates()

        self.start_top_crates = self.inspect_stacks(self.start_stacks)
        self.end_top_crates = self.inspect_stacks(self.end_stacks)

    def stack_crates(self, raw_crates):
        rows = raw_crates.split('\n')

        stacks = collections.defaultdict(list)
        for row in rows[:-1]:
            stack = 1
            for index, c in enumerate(row):
                if (index - 1) % 4 == 0:
                    if c != " ":
                        stacks[stack].append(c)
                    stack += 1
        sorted_stacks = dict(sorted(stacks.items()))
        return sorted_stacks
    
    def inspect_stacks(self, stacks):
        top_list = [stacks[key][0] for key in stacks]
        top_string = ''.join(top_list)
        return top_string

    def parse_moves(self, raw_moves):
        move_list = raw_moves.split('\n')
        moves = [parse(MOVE_FMT, move) for move in move_list if move != '']
        return moves

    # CrateMover 9000
    def move_em_9000(self, stacks, move):
    
        # crane moves one at a time
        for idx in range(move['n']):
            popped = stacks[move['from_stack']].pop(0)
            stacks[move['to_stack']].insert(0, popped)
        return stacks

    # CrateMover 9001
    def move_em_9001(self, stacks, move):

        # crane moves n crates at a time
        move_crates = stacks[move['from_stack']][:move['n']] 
        del stacks[move['from_stack']][:move['n']]
        stacks[move['to_stack']] = move_crates + stacks[move['to_stack']]
        return stacks

    def move_crates(self):
        stacks_updated = copy.deepcopy(self.start_stacks)

        if self.mover_model == 9000:
            mover = self.move_em_9000
        elif self.mover_model == 9001:
            mover = self.move_em_9001
        else:
            raise Exception("The only models the elves have are 9000 and 9001!")

        for move in self.moves:
            stacks_updated = mover(stacks = stacks_updated, move = move)
        
        return stacks_updated


#%% Part One example

example_input_path = 'example_data/day_5_example.txt'

example_elf_crates_9000 = ElfCrates(example_input_path, mover_model = 9000)

assert example_elf_crates_9000.start_top_crates == 'NDP'
assert example_elf_crates_9000.end_top_crates == 'CMZ'

# %% Part One

input_path = 'data/day_5.txt'
elf_crates_9000 = ElfCrates('data/day_5.txt', mover_model = 9000)

assert elf_crates_9000.end_top_crates == 'RFFFWBPNS'

# %% Part Two Example

example_elf_crates_9001 = ElfCrates(example_input_path, mover_model = 9001)

assert example_elf_crates_9001.start_top_crates == 'NDP'
assert example_elf_crates_9001.end_top_crates == 'MCD'

# %% Part Two

elf_crates_9001 = ElfCrates('data/day_5.txt', mover_model = 9001)
elf_crates_9001.end_top_crates

# %%
