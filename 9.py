# !/usr/bin/env python3

fname = "weer.txt"

f = open(fname, "rt")
# Parse into dict
lookup = {
    line.split()[0]: int(line.split()[1]) 
    for line in f 
    if not line.startswith('#')
}
f.close()

# Calc average
avg = sum(lookup.values()) / len(lookup)

# Split dict by temp
lower_than_avg = {k:v for k,v in lookup.items() if v < avg}
higher_than_avg= {k:v for k,v in lookup.items() if v >= avg}

# Print report
print("File: {:}".format(fname))
print("Average: {:}".format(avg))
print("Lower than average ({:.2f}):".format(avg))
for item in lower_than_avg.items():
    print("  {}: {}".format(item[0], item[1]))
print("Higher than average ({:.2f}):".format(avg))
for item in higher_than_avg.items():
    print("  {}: {}".format(item[0], item[1]))