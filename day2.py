total_score = 0
letter_to_move = {'A': 'rock', 'B': 'paper', 'C': 'scissors', 
                  'X': 'rock', 'Y': 'paper', 'Z': 'scissors'}
score_of_move = {'rock': 1, 'paper': 2, 'scissors': 3}
loses_from = {'rock': 'scissors', 'paper': 'rock', 'scissors': 'paper'}
wins_from = {'rock': 'paper', 'paper': 'scissors', 'scissors': 'rock'}

part = 2

with open('day2_input.txt') as f:
    lines = f.read().splitlines()
    for l in lines:
        # translate letters
        opp_choice = letter_to_move[l[0]]
        # your choice depends on part
        if part == 1:
            your_choice  = letter_to_move[l[2]]
        if part == 2:
            your_choice  = l[2]
            if your_choice == 'X':
                your_choice = loses_from[opp_choice]
            elif your_choice == 'Z':
                your_choice = wins_from[opp_choice]
            else:
                your_choice = opp_choice
        # add score for move
        total_score += score_of_move[your_choice]
        # add score for outcome
        if opp_choice == your_choice:
            total_score += 3
        elif (opp_choice == 'rock' and your_choice == 'paper'):
            total_score += 6
        elif (opp_choice == 'paper' and your_choice == 'scissors'):
            total_score += 6
        elif (opp_choice == 'scissors' and your_choice == 'rock'):
            total_score += 6

print(total_score)

