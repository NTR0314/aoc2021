import functools

# coding: utf-8

a = open('input.txt').readlines()
a = [x.strip() for x in a]

bit_count = [0] * 12
for x in a:
    for y in range(len(x)):
        if x[y] == '1':
            bit_count[y] += 1

red = [str(x) for x in list(map(lambda x: 1 if x > (len(a) // 2) else 0, bit_count))]
gamma = int(functools.reduce(lambda a, b: a + b, red), 2)
red = [str(x) for x in list(map(lambda x: 1 if x < (len(a) // 2) else 0, bit_count))]
epsilon = int(functools.reduce(lambda a, b: a + b, red), 2)

print(f"Silver result: {gamma * epsilon}")


def most_common_bit(list, index=0, invert=False):
    one_count = 0
    for el in list:
        if int(el[index]) == 1:
            one_count += 1

    if invert:
        return 0 if one_count >= len(list) / 2 else 1
    else:
        return 1 if one_count >= len(list) / 2 else 0


oxygen = a.copy()
rubber = a.copy()

for i in range(len(a[0])):
    msb_o = most_common_bit(oxygen, index=i, invert=False)
    msb_r = most_common_bit(rubber, index=i, invert=True)
    if len(oxygen) > 1:
        oxygen = [x for x in oxygen if int(x[i]) == msb_o]
    if len(rubber) > 1:
        rubber = [x for x in rubber if int(x[i]) == msb_r]

rubber = int(rubber[0], 2)
oxygen = int(oxygen[0], 2)

print(f"Gold result: {rubber=}, {oxygen=} {rubber * oxygen}")
