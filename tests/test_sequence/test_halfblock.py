from sequence_.halfblock import _generateHalfBlockList, _generateHalfBlockSequence
import numpy as np
"""
#############
Testing HalfBlockList
#############
"""
def test_by_halfblock_2_des() -> None:
  HalfBlockList = _generateHalfBlockList(total_blocks = 2, alt = 0, mix = False)
  assert HalfBlockList == [4,3,2,1]

def test_by_halfblock_2_des_mix() -> None:
  HalfBlockList = _generateHalfBlockList(total_blocks = 2, alt = 0, mix = True)
  assert HalfBlockList == [4,1,2,3]

def test_by_halfblock_3_des() -> None:
  HalfBlockList = _generateHalfBlockList(total_blocks = 3, alt = 0, mix = False)
  assert HalfBlockList == [6,5,4,3,2,1]

def test_by_halfblock_3_alt_1() -> None:
  HalfBlockList = _generateHalfBlockList(total_blocks = 3, alt = 1, mix = False)
  assert HalfBlockList == [6,4,5,3,1,2]

def test_by_halfblock_4_des() -> None:
  HalfBlockList = _generateHalfBlockList(total_blocks = 4, alt = 0, mix = False)
  assert HalfBlockList == [8,7,6,5,4,3,2,1]

def test_by_halfblock_4_alt_1() -> None:
  HalfBlockList = _generateHalfBlockList(total_blocks = 4, alt = 1, mix = False)
  assert HalfBlockList == [8,6,7,5,4,2,3,1]

def test_by_halfblock_4_des_mix() -> None:
  HalfBlockList = _generateHalfBlockList(total_blocks = 4, alt = 0, mix = True)
  assert HalfBlockList == [8,3,6,1,4,7,2,5]

def test_by_halfblock_6_des() -> None:
  HalfBlockList = _generateHalfBlockList(total_blocks = 6, alt = 0, mix = False)
  assert HalfBlockList == [12,11,10,9,8,7,6,5,4,3,2,1]

def test_by_halfblock_6_alt_1() -> None:
  HalfBlockList = _generateHalfBlockList(total_blocks = 6, alt = 1, mix = False)
  assert HalfBlockList == [12,10,8,11,9,7,6,4,2,5,3,1]

def test_by_halfblock_6_alt_2() -> None:
  HalfBlockList = _generateHalfBlockList(total_blocks = 6, alt = 2, mix = False)
  assert HalfBlockList == [12,9,11,8,10,7,6,3,5,2,4,1]

def test_by_halfblock_6_alt_1_mix() -> None:
  HalfBlockList = _generateHalfBlockList(total_blocks = 6, alt = 1, mix = True)
  assert HalfBlockList == [12,4,8,5,9,1,6,10,2,11,3,7] # [12,4,8,5,9,1,11,3,7,6,10,2]

def test_by_halfblock_10_des() -> None:
  HalfBlockList = _generateHalfBlockList(total_blocks = 10, alt = 0, mix = False)
  assert HalfBlockList == [20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1]

def test_by_halfblock_10_alt_1() -> None:
  HalfBlockList = _generateHalfBlockList(total_blocks = 10, alt = 1, mix = False)
  assert HalfBlockList == [20,18,16,14,12,19,17,15,13,11,10,8,6,4,2,9,7,5,3,1]

def test_by_halfblock_10_alt_4() -> None:
  HalfBlockList = _generateHalfBlockList(total_blocks = 10, alt = 4, mix = False)
  assert HalfBlockList == [20,15,19,14,18,13,17,12,16,11,10,5,9,4,8,3,7,2,6,1]

"""
#############
Testing BlockSequence 
############# 
"""
HalfBlockList = [8,7,6,5,4,3,2,1]
def test_HalfBlockSequence_4_8() -> None:
  HalfBlockSequence: list = _generateHalfBlockSequence(total_seats = 132, 
                                                      HalfBlockList = HalfBlockList,
                                                      halfblock_index = 0)
  bool_ = True
  for i in HalfBlockSequence:
    if i not in [
                 109,110,111,
                 115,116,117,
                 121,122,123,
                 127,128,129]:
      bool_ = False

  assert bool_ == True
  assert len(np.unique(HalfBlockSequence)) == 12

def test_HalfBlockSequence_4_7() -> None:
  HalfBlockSequence: list = _generateHalfBlockSequence(total_seats = 132, 
                                                      HalfBlockList = HalfBlockList,
                                                      halfblock_index = 1)
  bool_ = True
  for i in HalfBlockSequence:
    if i not in [73,74,75,
                 79,80,81,
                 85,86,87,
                 91,92,93,
                 97,98,99,
                 103,104,105]:
      bool_ = False

  assert bool_ == True
  assert len(np.unique(HalfBlockSequence)) == 18

def test_HalfBlockSequence_4_6() -> None:
  HalfBlockSequence: list = _generateHalfBlockSequence(total_seats = 132, 
                                                      HalfBlockList = HalfBlockList,
                                                      halfblock_index = 2)
  bool_ = True
  for i in HalfBlockSequence:
    if i not in [37,38,39,
                 43,44,45,
                 49,50,51,
                 55,56,57,
                 61,62,63,
                 67,68,69]:
      bool_ = False

  assert bool_ == True
  assert len(np.unique(HalfBlockSequence)) == 18

def test_HalfBlockSequence_4_5() -> None:
  HalfBlockSequence: list = _generateHalfBlockSequence(total_seats = 132, 
                                                      HalfBlockList = HalfBlockList,
                                                      halfblock_index = 3)
  bool_ = True
  for i in HalfBlockSequence:
    if i not in [1,2,3,
                 7,8,9,
                 13,14,15,
                 19,20,21,
                 25,26,27,
                 31,32,33]:
      bool_ = False

  assert bool_ == True
  assert len(np.unique(HalfBlockSequence)) == 18

def test_HalfBlockSequence_4_4() -> None:
  HalfBlockSequence: list = _generateHalfBlockSequence(total_seats = 132, 
                                                      HalfBlockList = HalfBlockList,
                                                      halfblock_index = 4)
  bool_ = True
  for i in HalfBlockSequence:
    if i not in [106,107,108,
                 112,113,114,
                 118,119,120,
                 124,125,126,
                 130,131,132]:
      bool_ = False

  assert bool_ == True
  assert len(np.unique(HalfBlockSequence)) == 15

def test_HalfBlockSequence_4_3() -> None:
  HalfBlockSequence: list = _generateHalfBlockSequence(total_seats = 132, 
                                                      HalfBlockList = HalfBlockList,
                                                      halfblock_index = 5)
  bool_ = True
  for i in HalfBlockSequence:
    if i not in [70,71,72,
                 76,77,78,
                 82,83,84,
                 88,89,90,
                 94,95,96,
                 100,101,102]:
      bool_ = False

  assert bool_ == True
  assert len(np.unique(HalfBlockSequence)) == 18

def test_HalfBlockSequence_4_2() -> None:
  HalfBlockSequence: list = _generateHalfBlockSequence(total_seats = 132, 
                                                      HalfBlockList = HalfBlockList,
                                                      halfblock_index = 6)
  bool_ = True
  for i in HalfBlockSequence:
    if i not in [34,35,36,
                 40,41,42,
                 46,47,48,
                 52,53,54,
                 58,59,60,
                 64,65,66]:
      bool_ = False

  assert bool_ == True
  assert len(np.unique(HalfBlockSequence)) == 18

def test_HalfBlockSequence_4_1() -> None:
  HalfBlockSequence: list = _generateHalfBlockSequence(total_seats = 132, 
                                                      HalfBlockList = HalfBlockList,
                                                      halfblock_index = 7)
  bool_ = True
  for i in HalfBlockSequence:
    if i not in [4,5,6,
                 10,11,12,
                 16,17,18,
                 22,23,24,
                 28,29,30]:
      bool_ = False

  assert bool_ == True
  assert len(np.unique(HalfBlockSequence)) == 15

