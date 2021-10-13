
import generate
from random import randint
l =[]
for x in range(0,50000):
    int =randint(0,2147483648)
    l.append(int)

generate.generate_images(".Z/network-snapshot-000240.pkl", l, 0.5,"./static/gan", None, None)
