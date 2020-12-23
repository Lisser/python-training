#!/usr/bin/env python3

UUR_WAARDEN = "673,1499,82,119341,13,-100000,1,53,7"

def map_width (uur): 
    return len(str(uur))

string_parts = UUR_WAARDEN.split(",")
int_parts = list(map(int, string_parts))
width_parts = list(map(map_width, string_parts))

total = sum(int_parts)
width_parts.append(len(str(total)))
padding = max(width_parts)

for i, uur in enumerate(string_parts):
    print("Uur {:>2}: {:>2}".format(i, uur.rjust(padding)))

print("Totaal: " + str(total).rjust(padding))