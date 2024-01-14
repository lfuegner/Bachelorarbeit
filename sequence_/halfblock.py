import math
import numpy as np

def generateSequenceHalfBlock(total_seats: int, total_blocks:int, alt: int, mix: bool) -> list:
  Sequence: list = []
  HalfBlockList: list = _generateHalfBlockList(total_blocks = total_blocks,
                                              alt = alt,
                                              mix = mix)

  for halfblock_index in range(total_blocks*2):
    HalfBlockSequence: list = _generateHalfBlockSequence(total_seats = total_seats, 
                                                        HalfBlockList = HalfBlockList, 
                                                        halfblock_index = halfblock_index)
    Sequence += HalfBlockSequence
  return Sequence

def _generateHalfBlockList(total_blocks: int, 
                          alt: int, 
                          mix: bool) -> list:
  HalfBlockList: list = []
  alternate = alt + 1
  total_halfblocks = total_blocks * 2
  blocks = total_blocks

  for i in range(2):
    for i in range(alternate):
      HelperList: list = []
      for halfblock_number in range(total_halfblocks, blocks, -alternate):
        HelperList.append(halfblock_number)
      total_halfblocks -= 1
      HalfBlockList += HelperList

    total_halfblocks = blocks
    blocks = 0

  if mix is True:
    index = 1
    for i in range(int(total_blocks/2)):

      x = HalfBlockList[index]
      HalfBlockList[index] = HalfBlockList[index + total_blocks]
      HalfBlockList[index + total_blocks] = x
      index += 2
    
  return HalfBlockList

def _generateHalfBlockSequence(total_seats: int, 
                              HalfBlockList: list, 
                              halfblock_index: int) -> list:
  HalfBlockSequence: list = []
  first_row_seats: int = 3
  seats_per_row: int = 6

  total_halfblocks = len(HalfBlockList)
  total_row = math.ceil((total_seats + first_row_seats) / seats_per_row)
  weight = math.ceil(total_row / (total_halfblocks*0.5))

  halfblock = HalfBlockList[halfblock_index]
 
  for seat in range(total_seats,0,-1):
    letter = (seat + first_row_seats) % seats_per_row
    row = math.ceil((seat + first_row_seats) / seats_per_row)

    if halfblock <= total_halfblocks/2:
      if letter in [1,2,3]:
        
        if  HalfBlockList[halfblock_index] == math.ceil(row / weight):
          HalfBlockSequence.append(seat)

    elif halfblock > total_halfblocks/2:
      if letter in [4,5,0]:

        if  HalfBlockList[halfblock_index] == math.ceil(row / weight) + total_halfblocks*0.5:
          HalfBlockSequence.append(seat)
      
  np.random.shuffle(HalfBlockSequence)

  return HalfBlockSequence