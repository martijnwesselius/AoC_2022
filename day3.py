part = 2
total_priority = 0

def intersect(string1, string2): 
    return ''.join(set(string1).intersection(string2))

def intersect3(string1, string2, string3):
    intersection = set(string1).intersection(string2)
    intersection = intersection.intersection(string3)
    return ''.join(intersection)

def char_to_priority(character):
    if character.islower():
        prio = ord(character)-96
    else:
        prio = ord(character)-38
    return prio

with open('day3_input.txt') as f:
    lines = f.read().splitlines()

if part == 1:
    for l in lines:
        split_idx = round(len(l)/2)
        comp_one = l[:split_idx]
        comp_two = l[split_idx:]    
        intersection = intersect(comp_one, comp_two)
        priority = char_to_priority(intersection)
        total_priority += priority

if part == 2:
    num_3lines = round(len(lines)/3)
    for n in range(num_3lines):
        line1 = lines[n*3]
        line2 = lines[n*3+1]
        line3 = lines[n*3+2]
        intersection = intersect3(line1, line2, line3)
        priority = char_to_priority(intersection)
        total_priority += priority

print(total_priority)
