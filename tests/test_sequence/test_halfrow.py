from sequence_.halfrow import _generateHalfRowList,_generateHalfRowSequence
import numpy as np
"""
#############
Testing HalfRowList
#############
"""
def test_by_halfrow_des() -> None:
  HalfRowList = _generateHalfRowList(total_seats = 132, alt = 0)
  assert HalfRowList == [44,43,42,41,40,39,38,37,36,35,34,33,32,31,30,29,28,27,26,25,24,23,
                         22,21,20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1]

def test_by_halfrow_alt_1() -> None:
  HalfRowList = _generateHalfRowList(total_seats = 132, alt = 1)
  assert HalfRowList == [44,42,40,38,36,34,32,30,28,26,24,43,41,39,37,35,33,31,29,27,25,23,
                         22,20,18,16,14,12,10,8,6,4,2,21,19,17,15,13,11,9,7,5,3,1]

def test_by_halfrow_alt_2() -> None:
  HalfRowList = _generateHalfRowList(total_seats = 132, alt = 2)
  assert HalfRowList == [44,41,38,35,32,29,26,23,43,40,37,34,31,28,25,42,39,36,33,30,27,24,
                         22,19,16,13,10,7,4,1,21,18,15,12,9,6,3,20,17,14,11,8,5,2]

def test_by_halfrow_alt_4() -> None:
  HalfRowList = _generateHalfRowList(total_seats = 132, alt = 4)
  assert HalfRowList == [44,39,34,29,24,43,38,33,28,23,42,37,32,27,41,36,31,26,40,35,30,25,
                         22,17,12,7,2,21,16,11,6,1,20,15,10,5,19,14,9,4,18,13,8,3]

def test_by_halfrow_alt_5() -> None:
  HalfRowList = _generateHalfRowList(total_seats = 132, alt = 5)
  assert HalfRowList == [44,38,32,26,43,37,31,25,42,36,30,24,41,35,29,23,40,34,28,39,33,27,
                         22,16,10,4,21,15,9,3,20,14,8,2,19,13,7,1,18,12,6,17,11,5]

def test_by_halfrow_alt_8() -> None:
  HalfRowList = _generateHalfRowList(total_seats = 132, alt = 8)
  assert HalfRowList == [44,35,26,43,34,25,42,33,24,41,32,23,40,31,39,30,38,29,37,28,36,27,
                         22,13,4,21,12,3,20,11,2,19,10,1,18,9,17,8,16,7,15,6,14,5]
"""
#############
Testing HalfRowSequence
#############
"""
HalfRowList = [44,43,42,41,40,39,38,37,36,35,34,33,32,31,30,29,28,27,26,25,24,23,22,21,20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1]
def test_HalfRowSequence_44() -> None:
  HalfRowSequence: list = _generateHalfRowSequence(total_seats = 132, 
                                                  HalfRowList = HalfRowList,
                                                  halfrow_index=0) #HalfRowList[0] = 44
  bool_ = True
  for i in HalfRowSequence:
    if i not in [129,128,127]:
      bool_ = False

  assert bool_ == True
  assert len(np.unique(HalfRowSequence)) == 3

def test_HalfRowSequence_43() -> None:
  HalfRowSequence: list = _generateHalfRowSequence(total_seats = 132, 
                                                  HalfRowList = HalfRowList,
                                                  halfrow_index=1) #HalfRowList[1] = 43
  bool_ = True
  for i in HalfRowSequence:
    if i not in [123,122,121]:
      bool_ = False

  assert bool_ == True
  assert len(HalfRowSequence) == 3

def test_HalfRowSequence_42() -> None:
  HalfRowSequence: list = _generateHalfRowSequence(total_seats = 132, 
                                                  HalfRowList = HalfRowList,
                                                  halfrow_index=2) #HalfRowList[2] = 42
  bool_ = True
  for i in HalfRowSequence:
    if i not in [117,116,115]:
      bool_ = False

  assert bool_ == True
  assert len(HalfRowSequence) == 3

def test_HalfRowSequence_23() -> None:
  HalfRowSequence: list = _generateHalfRowSequence(total_seats = 132, 
                                                  HalfRowList = HalfRowList,
                                                  halfrow_index=21) #HalfRowList[21] = 23
  bool_ = True
  for i in HalfRowSequence:
    if i not in [1,2,3]:
      bool_ = False

  assert bool_ == True
  assert len(HalfRowSequence) == 3

def test_HalfRowSequence_22() -> None:
  HalfRowSequence: list = _generateHalfRowSequence(total_seats = 132, 
                                                  HalfRowList = HalfRowList,
                                                  halfrow_index=22) #HalfRowList[22] = 22
  bool_ = True
  for i in HalfRowSequence:
    if i not in [132,131,130]:
      bool_ = False

  assert bool_ == True
  assert len(HalfRowSequence) == 3

def test_HalfRowSequence_1() -> None:
  HalfRowSequence: list = _generateHalfRowSequence(total_seats = 132, 
                                                  HalfRowList = HalfRowList,
                                                  halfrow_index=43) #HalfRowList[43] = 1
  bool_ = True
  for i in HalfRowSequence:
    if i not in [4,5,6]:
      bool_ = False

  assert bool_ == True
  assert len(HalfRowSequence) == 3