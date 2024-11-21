def add_die(die, scores):
  # print(f'add_die({die}, {scores})')
  updated_scores = []
  
  for d in range(1, die+1):
    new_scores = [s+[d] for s in scores]
    updated_scores.extend(new_scores)
  
  # print(f'{updated_scores=}')
  return updated_scores

def calculate_combos(dice):
  working_dice = dice.copy()
  this_d = working_dice.pop()
  # print(f'{this_d=}')
  scores = [[d] for d in range(1, this_d + 1)]
  while len(working_dice) > 0:
    this_d = working_dice.pop()
    print(f'{this_d=}')
    scores = add_die(this_d, scores)

  print(f'{len(scores)}')  
  return scores

def print_scores(scores):
  print('OUTCOME PROBABILITY')
  for k, v in scores.items():
    print(f'{k:<3}     {v:.2f}%')

def calculate_proba(scores):
  score_occurrence = {}
  for score_list in scores:
    total = sum(score_list)
    if score_occurrence.get(total):
      score_occurrence[total] += 1
    else:
      score_occurrence[total] = 1
  return {s: (c * 100 / len(scores)) for s, c in score_occurrence.items()}

def roll_dice(*args):
  dice = [int(x) for x in args]
  combos = calculate_combos(dice)
  proba = calculate_proba(combos)
  print_scores(proba)

if __name__ == '__main__':
  roll_dice(4, 6, 6)