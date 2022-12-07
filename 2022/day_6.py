#%% example signal

def find_marker(signal_string, marker_length):
    for s in range(marker_length, len(signal_string) + 1):
        start = s - marker_length
        stop = s
        target = signal_string[start : stop]
        target_set = set(target)
        is_marker = len(target_set) == len(target)
        if is_marker:
            return s

# %%
example_signals = [
    'mjqjpqmgbljsphdztnvjfqwrcgsmlb',
    'bvwbjplbgvbhsrlpgdmjqwftvncz',
    'nppdvjthqldpwncqszvftbrmjlhg',
    'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg',
    'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'
]

example_packet_markers = [find_marker(s, 4) for s in example_signals]

assert example_packet_markers == [7, 5, 6, 10, 11]
        
# %%

example_message_markers = [find_marker(s, 14) for s in example_signals]

assert example_message_markers == [19, 23, 23, 29, 26]

#%% 

class ElfSignal:
    
    def __init__(self, input_path):
        with open(input_path) as input:
            signal_string = input.read()

        self.signal_string = signal_string

    def find_marker(self, marker_length):
        for s in range(marker_length, len(self.signal_string) + 1):
            start = s - marker_length
            stop = s
            target = self.signal_string[start : stop]
            target_set = set(target)
            is_marker = len(target_set) == len(target)
            if is_marker:
                return s

#%%

signal = ElfSignal(input_path = 'data/day_6.txt')
# %%
packet_marker = signal.find_marker(marker_length = 4)
packet_marker

#%% 

message_marker = signal.find_marker(marker_length = 14)
message_marker

# %%
