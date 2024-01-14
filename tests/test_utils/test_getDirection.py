from getDirection import getDirection

def test_getDirection_ascending() -> None:

  direction = getDirection(current_row = 1, targeted_row = 2)
  assert direction == 1

def test_getDirection_descending() -> None:

  direction = getDirection(current_row = 3, targeted_row = 1)
  assert direction == -1 

def test_getDirection_equal() -> None:
  
  direction = getDirection(current_row = 1,targeted_row = 1)
  assert direction == 0