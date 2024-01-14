def getDirection(current_row: int, targeted_row: int) -> int:
  """
  This function return the direction for the passenger.
  1 is moving up the aishle
  -1 is moving down the aishle
  0 staying in the current_row
  """
  if current_row > targeted_row:
    direction = -1
  elif current_row < targeted_row:
    direction = 1
  else:
    direction = 0

  return direction