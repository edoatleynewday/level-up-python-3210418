def is_palindrome(text):
  cleaned = ''.join([c.lower() for c in text if c.isalpha()])
  return cleaned == cleaned[::-1]

if __name__ == '__main__':
  text='hello world'
  print(text)
  print(is_palindrome(text))
  text='Go hang a salami, I’m a lasagna hog.'
  print(text)
  print(is_palindrome(text))