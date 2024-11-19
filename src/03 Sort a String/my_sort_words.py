def sort_words(text):
  return ' '.join(sorted(text.split(), key=lambda x: x.lower()))
  # return ' '.join([s for s in sorted(text.split(), key=lambda x: x.lower())])

# commands used in solution video for reference
if __name__ == '__main__':
    print(sort_words('banana ORANGE apple'))  # apple banana ORANGE