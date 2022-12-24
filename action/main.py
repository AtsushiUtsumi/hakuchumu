import codecs
import json

file = codecs.open('Actions.txt', 'w', encoding='utf-8')
file.write('Input SerialNo 000000\n')
file.write('Input SerialNo 123456\n')
file.write('Input SerialNo 999999\n')
file.close()

file = codecs.open('Actions.txt', 'r', encoding='utf-8')
lines = [i.strip() for i in file.readlines()]
print(lines)
file.close()

from itertools import permutations
depth = len(lines)
for i in permutations(lines, depth):
    print(i)

for i in permutations(range(depth), depth):
    print(i)
print('DONE')
exit(0)
