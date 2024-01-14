from sequence_.block import _generateBlockList,_generateBlockSequence
import numpy as np
"""
#############
Testing BlockList
#############
"""
def test_BlockList_2_des() -> None:
  BlockList = _generateBlockList(total_blocks = 2, alt = 0)
  assert BlockList == [2,1]

def test_BlockList_3_des() -> None:
  BlockList = _generateBlockList(total_blocks = 3, alt = 0)
  assert BlockList == [3,2,1]

def test_BlockList_3_alt_1() -> None:
  BlockList = _generateBlockList(total_blocks = 3, alt = 1)
  assert BlockList == [3,1,2]

def test_BlockList_4_des() -> None:
  BlockList = _generateBlockList(total_blocks = 4, alt = 0)
  assert BlockList == [4,3,2,1]

def test_BlockList_4_alt_1() -> None:
  BlockList = _generateBlockList(total_blocks = 4, alt = 1)
  assert BlockList == [4,2,3,1]

def test_BlockList_4_alt_2() -> None:
  BlockList = _generateBlockList(total_blocks = 4, alt = 2)
  assert BlockList == [4,1,3,2]

def test_BlockList_6_des() -> None:
  BlockList = _generateBlockList(total_blocks = 6, alt = 0)
  assert BlockList == [6,5,4,3,2,1]

def test_BlockList_6_alt_1() -> None:
  BlockList = _generateBlockList(total_blocks = 6, alt = 1)
  assert BlockList == [6,4,2,5,3,1]

def test_BlockList_6_alt_2() -> None:
  BlockList = _generateBlockList(total_blocks = 6, alt = 2)
  assert BlockList == [6,3,5,2,4,1]

def test_BlockList_6_alt_3() -> None:
  BlockList = _generateBlockList(total_blocks = 6, alt = 3)
  assert BlockList == [6,2,5,1,4,3]

def test_BlockList_10_des() -> None:
  BlockList = _generateBlockList(total_blocks = 10, alt = 0)
  assert BlockList == [10,9,8,7,6,5,4,3,2,1]

def test_BlockList_10_alt_1() -> None:
  BlockList = _generateBlockList(total_blocks = 10, alt = 1)
  assert BlockList == [10,8,6,4,2,9,7,5,3,1]

def test_BlockList_10_alt_4() -> None:
  BlockList = _generateBlockList(total_blocks = 10, alt = 4)
  assert BlockList == [10,5,9,4,8,3,7,2,6,1]
"""
#############
Testing BlockSequence 
############# 
"""
BlockList3 = [3,2,1]
def test_BlockSequence_3_3() -> None:
  BlockSequence: list = _generateBlockSequence(total_seats = 132, 
                                               BlockList = BlockList3,
                                               block_index = 0)
  bool_ = True
  for i in BlockSequence:
    if i not in [132,131,130,
                129,128,127,126,125,124,
                123,122,121,120,119,118,
                117,116,115,114,113,112,
                111,110,109,108,107,106,
                105,104,103,102,101,100,
                99,98,97,96,95,94]:
      bool_ = False

  assert bool_ == True
  assert len(np.unique(BlockSequence)) == 39

def test_BlockSequence_3_2() -> None:
  BlockSequence: list = _generateBlockSequence(total_seats = 132, 
                                               BlockList = BlockList3,
                                               block_index = 1)
  bool_ = True
  for i in BlockSequence:
    if i not in [46,47,48,49,50,51,
                52,53,54,55,56,57,
                58,59,60,61,62,63,
                64,65,66,67,68,69,
                70,71,72,73,74,75,
                76,77,78,79,80,81,
                82,83,84,85,86,87,
                88,89,90,91,92,93]:
      bool_ = False

  assert bool_ == True
  assert len(np.unique(BlockSequence)) == 48

def test_BlockSequence_3_1() -> None:
  BlockSequence: list = _generateBlockSequence(total_seats = 132, 
                                               BlockList = BlockList3,
                                               block_index = 2)
  bool_ = True
  for i in BlockSequence:
    if i not in [1,2,3,
                  4,5,6,7,8,9,
                  10,11,12,13,14,15,
                  16,17,18,19,20,21,
                  22,23,24,25,26,27,
                  28,29,30,31,32,33,
                  34,35,36,37,38,39,
                  40,41,42,43,44,45,]:
      bool_ = False

  assert bool_ == True
  assert len(np.unique(BlockSequence)) == 45

BlockList4 = [4,3,2,1] #by_block_4
def test_BlockSequence_4_4() -> None:
  BlockSequence: list = _generateBlockSequence(total_seats = 132, 
                                               BlockList = BlockList4,
                                               block_index = 0)
  bool_ = True
  for i in BlockSequence:
    if i not in [132,131,130,
                  129,128,127,126,125,124,
                  123,122,121,120,119,118,
                  117,116,115,114,113,112,
                  111,110,109,108,107,106]:
      bool_ = False

  assert bool_ == True
  assert len(np.unique(BlockSequence)) == 27


def test_BlockSequence_4_3() -> None:
  BlockSequence: list = _generateBlockSequence(total_seats = 132, 
                                               BlockList = BlockList4,
                                               block_index = 1)
  bool_ = True
  for i in BlockSequence:
    if i not in [70,71,72,73,74,75,
                76,77,78,79,80,81,
                82,83,84,85,86,87,
                88,89,90,91,92,93,
                94,95,96,97,98,99,
                100,101,102,103,104,105]:
      bool_ = False

  assert bool_ == True
  assert len(np.unique(BlockSequence)) == 36

def test_BlockSequence_4_2() -> None:
  BlockSequence: list = _generateBlockSequence(total_seats = 132, 
                                               BlockList = BlockList4,
                                               block_index = 2)
  bool_ = True
  for i in BlockSequence:
    if i not in [34,35,36,37,38,39,
                  40,41,42,43,44,45,
                  46,47,48,49,50,51,
                  52,53,54,55,56,57,
                  58,59,60,61,62,63,
                  64,65,66,67,68,69]:
      bool_ = False

  assert bool_ == True
  assert len(np.unique(BlockSequence)) == 36

def test_BlockSequence_4_1() -> None:
  BlockSequence: list = _generateBlockSequence(total_seats = 132, 
                                               BlockList = BlockList4,
                                               block_index = 3)
  bool_ = True
  for i in BlockSequence:
    if i not in [1,2,3,
                 4,5,6,7,8,9,
                 10,11,12,13,14,15,
                 16,17,18,19,20,21,
                 22,23,24,25,26,27,
                 28,29,30,31,32,33]:
      bool_ = False
      
  assert bool_ == True
  assert len(np.unique(BlockSequence)) == 33

BlockList6 = [6,5,4,3,2,1] #by_block_6
def test_BlockSequence_6_1() -> None:
  BlockSequence: list = _generateBlockSequence(total_seats = 132, 
                                               BlockList = BlockList6,
                                               block_index = 5)
  print(BlockSequence)
  bool_ = True
  for i in BlockSequence:
    if i not in [1,2,3,
                 4,5,6,7,8,9,
                 10,11,12,13,14,15,
                 16,17,18,19,20,21]:
      bool_ = False
      
  assert bool_ == True
  assert len(np.unique(BlockSequence)) == 21