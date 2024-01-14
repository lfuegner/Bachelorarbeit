from sequence_.letter import _generateLetterSequence, _generateLetterList
import numpy as np
"""
#############
Testing LetterList
#############
"""
def test_LetterList_wintocorr() -> None:
  LetterList = _generateLetterList(pattern = "wintocorr")
  assert LetterList == [1,2,3,0,5,4]

def test_LetterList_alt() -> None:
  LetterList = _generateLetterList(pattern = "alt")
  assert LetterList == [1,0,2,5,3,4]
"""
#############
Testing LetterSequence
#############
"""
LetterList = [1,2,3,4,5,0] # wintocorr
def test_LetterSequence_A() -> None:
  LetterSequence = _generateLetterSequence(total_seats=132,
                                           LetterList=LetterList,
                                           letter_index=0)
  bool_ = True
  for i in LetterSequence:
    if i not in [4,10,16,22,28,34,40,46,52,58,64,70,76,82,88,94,100,106,112,118,124,130]:
      bool_ = False

  assert bool_ == True
  assert len(np.unique(LetterSequence)) == 22

def test_LetterSequence_B() -> None:
  LetterSequence = _generateLetterSequence(total_seats=132,
                                           LetterList=LetterList,
                                           letter_index=1)
  bool_ = True
  for i in LetterSequence:
    if i not in [5,11,17,23,29,35,41,47,53,59,65,71,77,83,89,95,101,107,113,119,125,131]:
      bool_ = False

  assert bool_ == True
  assert len(np.unique(LetterSequence)) == 22

def test_LetterSequence_C() -> None:
  LetterSequence = _generateLetterSequence(total_seats=132,
                                           LetterList=LetterList,
                                           letter_index=2)
  bool_ = True
  for i in LetterSequence:
    if i not in [6,12,18,24,30,36,42,48,54,60,66,72,78,84,90,96,102,108,114,120,126,132]:
      bool_ = False

  assert bool_ == True
  assert len(np.unique(LetterSequence)) == 22

def test_LetterSequence_D() -> None:
  LetterSequence = _generateLetterSequence(total_seats=132,
                                           LetterList=LetterList,
                                           letter_index=3)
  bool_ = True
  for i in LetterSequence:
    if i not in [1,7,13,19,25,31,37,43,49,55,61,67,73,79,85,91,97,103,109,115,121,127]:
      bool_ = False

  assert bool_ == True
  assert len(np.unique(LetterSequence)) == 22

def test_LetterSequence_E() -> None:
  LetterSequence = _generateLetterSequence(total_seats=132,
                                           LetterList=LetterList,
                                           letter_index=4)
  bool_ = True
  for i in LetterSequence:
    if i not in [2,8,14,20,26,32,38,44,50,56,62,68,74,80,86,92,98,104,110,116,122,128]:
      bool_ = False

  assert bool_ == True
  assert len(np.unique(LetterSequence)) == 22

def test_LetterSequence_F() -> None:
  LetterSequence = _generateLetterSequence(total_seats=132,
                                           LetterList=LetterList,
                                           letter_index=5)
  bool_ = True
  for i in LetterSequence:
    if i not in [3,9,15,21,27,33,39,45,51,57,63,69,75,81,87,93,99,105,111,117,123,129]:
      bool_ = False

  assert bool_ == True
  assert len(np.unique(LetterSequence)) == 22