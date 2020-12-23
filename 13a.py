#!/usr/bin/env python3

def dubbelen(lijst):
  """
  Maakt een lijst aan met indexnummers van de
  dubbelen in lijst. De lijst moet gesorteerd zijn.
  Parameter:
  lijst - de te onderzoeken lijst
  """
  unieken_name = list(set(lijst))
  return [lijst.index(naam) for naam in unieken_name]

namen = [ 'jan', 'piet', 'henk', 'els', 'piet',
    'els', 'john', 'els', 'jan', 'els', 'henk']

namen.sort()

print("De lijst was:", namen)

dub= dubbelen(namen)

dub

print("De indexen van de dubbelen zijn:", dub)