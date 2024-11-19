def index_all(src, tgt):
  matches = []
  for i, x in enumerate(src):
    if x == tgt:
       matches.append([i])
    elif isinstance(x, list):
       for j in index_all(x, tgt):
          matches.append([i] + j)
  return matches

# commands used in solution video for reference
if __name__ == '__main__':
    example = [[[1, 2, 3], 2, [1, 3]], [1, 2, 3]]
    print(index_all(example, 2))  # [[0, 0, 1], [0, 1], [1, 1]]
    print(index_all(example, [1, 2, 3]))  # [[0, 0], [1]]