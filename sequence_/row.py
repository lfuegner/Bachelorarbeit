import math
import numpy as np

def generateSequenceRow(total_seats: int, alt: int) -> list:
  Sequence: list = []
  RowList: list = _generateRowList(total_seats=total_seats,
                                  alt=alt)

  for row_ in RowList:
    RowSequence: list = _generateRowSequence(total_seats=total_seats,
                                            row_=row_)
    Sequence += RowSequence

  return Sequence

def _generateRowList(total_seats: int, alt: int) -> list:
  RowList: list = []
  alternate = alt + 1
  total_rows = math.ceil((total_seats + 3) / 6)

  for i in range(alternate):
    for row in range(total_rows,0,-alternate):
      RowList.append(row)
    total_rows -= 1

  return RowList

def _generateRowSequence(total_seats: int, row_: int) -> list:
  RowSequence: list = []

  for seat in range(total_seats,0,-1):
    row = math.ceil((seat + 3) / 6)
    if  row_ == row:
      RowSequence.append(seat)
  np.random.shuffle(RowSequence)
  return RowSequence