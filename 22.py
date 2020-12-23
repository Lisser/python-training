import os
import sys
from os.path import join, getsize

if len(sys.argv) != 2:
    print('Ik heb 1 argument nodig!')
    sys.exit(10)

root = sys.argv[1]

som = 0
for dezedir, subdirs, nondirs in os.walk(root):
    for naam in nondirs:
        padnaam = join(dezedir, naam)
        try:
            size = getsize(padnaam)
            # print("{} {}".format(size, naam))
            som += size
        except OSError as e:
            print('Can bestand {} niet verwerken: {}'.format(padnaam, e.args),
                   file=sys.stderr)

print("Totaal in {}: {}".format(root, som))