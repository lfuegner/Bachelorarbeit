import math
import numpy as np

def generateSequenceHalfRow(total_seats: int, alt: int) -> list:
  Sequence: list = []
  HalfRowList: list = _generateHalfRowList(total_seats=total_seats,
                                          alt=alt)
  total_halfrows = len(HalfRowList)

  for halfrow_index in range(total_halfrows):
    HalfRowSequence: list = _generateHalfRowSequence(total_seats=total_seats,
                                                    HalfRowList=HalfRowList,
                                                    halfrow_index=halfrow_index)
    Sequence += HalfRowSequence 

  return Sequence

def _generateHalfRowList(total_seats: int, alt: int) -> list:
  HalfRowList: list = []
  alternate = alt + 1

  start_halfrows = math.ceil(total_seats / 3)
  end_halfrows = int(start_halfrows / 2)
  for j in range(2):
    for i in range(alternate):

      for halfrow in range(start_halfrows,end_halfrows,-alternate):
        HalfRowList.append(halfrow)
      start_halfrows -= 1
    start_halfrows = end_halfrows
    end_halfrows = 0
    

  return HalfRowList

def _generateHalfRowSequence(total_seats: int, HalfRowList: list, halfrow_index: int)-> list:
  HalfRowSequence: list = []
  first_row_seats:int  = 3
  seats_per_row: int = 6
  total_halfrows = len(HalfRowList)

  for seat in range(total_seats,0,-1):
    letter = (seat + first_row_seats) % seats_per_row

    if HalfRowList[halfrow_index] > total_halfrows / 2:

      if letter == 0 or letter == 5 or letter == 4:
        halfrow = math.ceil((seat + first_row_seats) / seats_per_row) + (total_halfrows/2)

        if  HalfRowList[halfrow_index] == halfrow:
          HalfRowSequence.append(seat)

    elif HalfRowList[halfrow_index] <= total_halfrows/2:

      if letter == 1 or letter == 2 or letter == 3:
        halfrow = math.ceil((seat + first_row_seats) / seats_per_row) - 1

        if  HalfRowList[halfrow_index] == halfrow:
          HalfRowSequence.append(seat)
    
  np.random.shuffle(HalfRowSequence)
  return HalfRowSequence