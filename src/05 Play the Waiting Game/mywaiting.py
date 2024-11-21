import time
import random

def user_input(target_time):
  print(f'Your target time is {target_time} seconds')
  input('---Press Enter to Begin---\n')
  start_time = time.time()
  input(f'...Press Enter again after {target_time} seconds...')
  end_time = time.time()
  return (end_time - start_time)

def print_result(actual_time, delta):
  print(f'Elapsed time: {actual_time:.3f} seconds')
  speed = 'fast' if delta > 0 else 'slow'
  print(f'{delta:.3f} seconds too {speed}')

def waiting_game():
  target_time = random.randint(2, 4)
  actual_time = user_input(target_time)
  delta = (target_time - actual_time)
  print_result(actual_time, delta)

if __name__ == '__main__':
    waiting_game()