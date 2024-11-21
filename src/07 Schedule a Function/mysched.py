import time

def schedule_function(when, func, *args):
  while time.time() <= when:
    pass
  
  func(*args)


if __name__ == '__main__':
  schedule_function(time.time() + 3 , print, "Howdy", "There", "!")