import numpy as np

def generateLetter(total_seats: int, pattern: str) -> list:
  Sequence: list = [] 
  LetterList: list = _generateLetterList(pattern)

  total_letter = len(LetterList)
  for letter_index in range(total_letter):
    LetterSequence = _generateLetterSequence(total_seats=total_seats,
                                             letter_index=letter_index,
                                             LetterList=LetterList)
    Sequence += LetterSequence
  return Sequence

def _generateLetterList(pattern) -> list:
  LetterList: list = []
  seats_per_row = 6

  if pattern == "wintocorr":
    for letter in range(1, int(seats_per_row / 2) + 1):
      LetterList.append(letter % seats_per_row)
    for letter in range(seats_per_row, int(seats_per_row / 2), -1):
      LetterList.append(letter % seats_per_row)

  elif pattern == "alt":
    helper = seats_per_row - 1
    for letter in range(1,int(seats_per_row / 2 ) + 1):
      LetterList.append(letter)
      LetterList.append((letter + helper) % seats_per_row)
      helper -= 2

  return LetterList

def _generateLetterSequence(total_seats: int, letter_index :int, LetterList :list) -> list:
  LetterSequence: list = []
  first_row_seats = 3
  seats_per_row = 6
 
  for seat in range(1,total_seats+1):
    if  LetterList[letter_index] == (seat + first_row_seats) % seats_per_row:
      LetterSequence.append(seat)
  np.random.shuffle(LetterSequence)
   
  return LetterSequence
