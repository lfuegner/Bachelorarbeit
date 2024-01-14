from sequence_.row import _generateRowList, _generateRowSequence
import numpy as np

def test_RowList_des() -> None:
  RowList = _generateRowList(total_seats = 132, alt = 0)
  assert RowList == [23,22,21,20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1]

def test_RowList_alt_1() -> None:
  RowList = _generateRowList(total_seats = 132, alt = 1)
  assert RowList == [23,21,19,17,15,13,11,9,7,5,3,1,22,20,18,16,14,12,10,8,6,4,2]

def test_RowList_alt_2() -> None:
  RowList = _generateRowList(total_seats = 132, alt = 2)
  assert RowList == [23,20,17,14,11,8,5,2,22,19,16,13,10,7,4,1,21,18,15,12,9,6,3]

def test_RowList_alt_4() -> None:
  RowList = _generateRowList(total_seats = 132, alt = 4)
  assert RowList == [23,18,13,8,3,22,17,12,7,2,21,16,11,6,1,20,15,10,5,19,14,9,4]

def test_RowList_alt_5() -> None:
  RowList = _generateRowList(total_seats = 132, alt = 5)
  assert RowList == [23,17,11,5,22,16,10,4,21,15,9,3,20,14,8,2,19,13,7,1,18,12,6]

def test_RowList_alt_8() -> None:
  RowList = _generateRowList(total_seats = 132, alt = 8)
  assert RowList == [23,14,5,22,13,4,21,12,3,20,11,2,19,10,1,18,9,17,8,16,7,15,6]
"""
#############
Testing RowSequence
#############
"""
def test_RowSequence_23() -> None:
  RowSequence: list = _generateRowSequence(total_seats = 132,
                                          row_=23)
  bool_ = True
  for i in RowSequence:
    if i not in [132,131,130]:
      bool_ = False

  assert bool_ == True
  assert len(np.unique(RowSequence)) == 3
  
def test_RowSequence_22() -> None:
  RowSequence: list = _generateRowSequence(total_seats = 132,
                                          row_ = 22)
  bool_ = True
  for i in RowSequence:
    if i not in [129,128,127,126,125,124]:
      bool_ = False

  assert bool_ == True
  assert len(np.unique(RowSequence)) == 6

def test_RowSequence_21() -> None:
  RowSequence: list = _generateRowSequence(total_seats = 132,
                                          row_ = 21)
  bool_ = True
  for i in RowSequence:
    if i not in [123,122,121,120,119,118]:
      bool_ = False

  assert bool_ == True
  assert len(np.unique(RowSequence)) == 6

def test_RowSequence_1() -> None:
  RowSequence: list = _generateRowSequence(total_seats = 132,
                                          row_ = 1)
  bool_ = True
  for i in RowSequence:
    if i not in [3,2,1]:
      bool_ = False
      
  assert bool_ == True
  assert len(np.unique(RowSequence)) == 3