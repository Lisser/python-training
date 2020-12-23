# !/usr/bin/env python3

INPUT_FILE = "verhaal.txt"

def read_words_in_file (fname):
    f = open(fname, "rt")
    lines = f.readlines()
    f.close()
    for (line_index, line) in enumerate(lines):
        words = line.split()
        for word in words:
            yield (word.strip('()?!.:,;\''), line_index + 1)

occurrences = {}
frequencies = {}
for (word, line_index) in read_words_in_file(INPUT_FILE):
    frequencies[word] = frequencies.get(word, 0) + 1
    occurrences[word] = occurrences.get(word, [])
    occurrences[word].append(line_index)
    
sorted_frequencies = sorted(frequencies.items(), key=lambda p: p[1], reverse=True)
for (word, freq) in sorted_frequencies:
    print("{}: {}".format(word, freq))

sorted_occurrences = sorted(occurrences.items())
for (word, occ) in sorted_occurrences:
    print("{}: {}".format(word, occ))