import math
import numpy as np

def generateBlock(total_seats: int, total_blocks:int, alt: int) -> list:
  Sequence: list = []
  BlockList: list = _generateBlockList(total_blocks = total_blocks, 
                                      alt = alt)

  for block_index in range(total_blocks):
    BlockSequence: list = _generateBlockSequence(total_seats = total_seats, 
                                                BlockList = BlockList, 
                                                block_index = block_index)
    Sequence += BlockSequence
  return Sequence

def _generateBlockList(total_blocks: int, alt:int) -> list:
  BlockList: list = []
  alternate = alt + 1
  for i in range(alternate):
    for block in range(total_blocks, 0, -alternate):
      BlockList.append(block)
    total_blocks -= 1

  return BlockList

def _generateBlockSequence(total_seats: int, BlockList: list, block_index: int) -> list:
  BlockSequence: list = []
  first_row_seats: int = 3
  seats_per_row: int = 6

  total_blocks = len(BlockList)
  total_row = math.ceil((total_seats + first_row_seats) / seats_per_row)
  weight = math.ceil(total_row / total_blocks)
  upper_row_bound = weight * (BlockList[block_index])
  lower_row_bound = weight * (BlockList[block_index]-1)
 
  for seat in range(total_seats,0,-1):

    row = math.ceil((seat + first_row_seats) / seats_per_row)

    if row > lower_row_bound and row <= upper_row_bound:
      BlockSequence.append(seat)
  np.random.shuffle(BlockSequence)

  return BlockSequence