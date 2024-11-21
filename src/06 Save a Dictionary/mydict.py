import json

def save_dict(data, file_name): 
  with open(file_name, 'w') as out:
    json.dump(data, out, ensure_ascii=True, indent=4)

def load_dict(file_name):
  with open(file_name, 'r') as src:
    return json.load(src)

if __name__ == '__main__':
  dict_file = './test.json'
  save_dict({1: 'a', 2: 'b', 3: 'c'}, dict_file)
  d = load_dict(dict_file)
  print(d['1'])
  print(d['2'])
  print(d['3'])