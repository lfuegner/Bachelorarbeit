import numpy as np
def generateLuggageSequence(total_seats:int, LuggageList: list, Luggage: list) -> list:
  Sequence: list = []

  for luggage_amount in LuggageList:
    LuggageSequence: list = []

    for seat_index in range(0,total_seats):
      if luggage_amount == Luggage[seat_index]:
        seat = seat_index + 1 
        LuggageSequence.append(seat)

    np.random.shuffle(LuggageSequence)
    Sequence += LuggageSequence

  return Sequence
