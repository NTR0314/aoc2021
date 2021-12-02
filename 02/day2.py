hoz = 0
depth = 0
hoz_gold = 0
depth_gold = 0
aim = 0

instr = [(x.split(" ")[0], int(x.split(" ")[1])) for x in open("input.txt").readlines()]
for inst, amount in instr:
    if inst == 'forward':
        hoz += amount
        hoz_gold += amount
        depth_gold += aim * amount
    elif inst == 'down':
        depth += amount
        aim += amount
    elif inst == 'up':
        depth -= amount
        aim -= amount

print(f"silver: {hoz * depth}")
print(f"gold: {hoz_gold * depth_gold}")