
#%%

example = [
    '2-4,6-8',
    '2-3,4-5',
    '5-7,7-9',
    '2-8,3-7',
    '6-6,4-6',
    '2-6,4-8'
]

#%%

def get_rangelists(pair):
    split_pair = pair.split(',')
    ranges = [rangestring.split('-') for rangestring in split_pair]
    return ranges

example_rangelists = [get_rangelists(r) for r in example]

# %%
def build_range_dict(rangelist):
    lower = int(rangelist[0])
    upper = int(rangelist[1])
    range_dict = {'lower' : lower, 'upper' : upper}
    return range_dict

def within(r, comp):
    within = (r['lower'] >= comp['lower']) & (r['upper'] <= comp['upper'])
    return within

def detect_total_overlap(r):
    r0 = build_range_dict(r[0])
    r1 = build_range_dict(r[1])
    total_overlap = within(r0, r1) | within(r1, r0)
    return total_overlap

example_overlaps = [detect_total_overlap(r) for r in example_rangelists]
sum(example_overlaps)

#%%

def detect_total_overlaps(f):
    with open(f) as input:
        data = input.read().split('\n')[:-1]
    
    rangelists = [get_rangelists(line) for line in data]
    total_overlaps = [detect_total_overlap(r) for r in rangelists]
    return sum(total_overlaps)

print(detect_total_overlaps('data/day_4.txt'))

# %%

def any_overlap(target, compare):
    target_set = set(range(target['lower'], target['upper'] + 1))
    compare_set = set(range(compare['lower'], compare['upper'] + 1))
    intersection = target_set.intersection(compare_set)
    return len(intersection) > 0

def detect_any_overlap(r):
    r0 = build_range_dict(r[0])
    r1 = build_range_dict(r[1])
    overlap = any_overlap(r0, r1)    
    return overlap

example_any_overlap = [detect_any_overlap(r) for r in example_rangelists]

#%%

def count_all_overlaps(f):
    with open(f) as input:
        data = input.read().split('\n')[:-1]
    
    rangelists = [get_rangelists(line) for line in data]
    overlaps = [detect_any_overlap(r) for r in rangelists]
    return sum(overlaps)

print(count_all_overlaps('data/day_4.txt'))
# %%
