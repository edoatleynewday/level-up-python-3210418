import sys
from math import sqrt

def isqrt(num):
  return int(sqrt(num)) + 1

# Simple function to check if a number is prime
def is_prime(n):
  # rule out even or less than 2
  if n < 2 or n%2 == 0:
    return False
  elif n == 2:
    return True
  
  # look for a prime divisor
  sq_rt_n = isqrt(n)
  for d in range(3, sq_rt_n, 2):
    if n % d == 0:
      return False

  return True

# # generate all primes up to the limit (inclusive)
def primes(limit):
  # print('yield', 2)
  yield 2
  num = 3
  while num <= limit:
    if is_prime(num):
      # print('yield', num)
      yield num
    num += 2

def next_factor(num):
  if is_prime(num):
    raise RuntimeError('Already Prime')
  for p in primes(isqrt(num)):
    if num % p == 0:
      return p, int(num/p)
  
  raise RuntimeError(f'No Prime Factor Found For {num}')
  
def get_prime_factors(num):
  prime_factors = []
  remainder = num
  while not is_prime(remainder):
    factor, rem = next_factor(remainder)
    prime_factors.append(factor)
    remainder = rem
  
  prime_factors.append(remainder)
  
  return prime_factors


if __name__ == '__main__':
  num = int(sys.argv[1])
  print('Factors for', num)
  factors = get_prime_factors(num)
  print(factors)