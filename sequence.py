import numpy as np
import math
from sample import sampleLuggageAmount
from sequence_.block import generateBlock
from sequence_.halfblock import generateSequenceHalfBlock
from sequence_.row import generateSequenceRow
from sequence_.halfrow import generateSequenceHalfRow
from sequence_.letter import generateLetter
from sequence_.seat import generateSeat
from sequence_.luggage import generateLuggageSequence

def generateLuggage(total_seats: int, condition: str) -> list:
  Luggage: list = [sampleLuggageAmount(condition) for i in range(0,total_seats)]

  return Luggage

def generateSequence(total_seats: int, type_: str, blocks: str, pattern: str, Luggage: list) -> list:
  Sequence:list = []
  ### Random ###
  if type_ == "random":
    Sequence: list = [seat_number for seat_number in range (1,total_seats+1)]
    np.random.shuffle(Sequence)

  ### Block ###
  elif type_ == "block":
    blocks = int(blocks)
    if blocks == 2:
      if pattern == "B-E": alt = 0
      elif pattern == "des": alt = 0

    elif blocks == 3:
      if pattern == "des": alt = 0 
      elif pattern == "alt_1": alt = 1

    elif blocks == 4:
      if pattern == "des": alt = 0
      elif pattern == "alt_1": alt = 1
      elif pattern == "alt_2": alt = 2      

    elif blocks == 6:
      if pattern == "des": alt = 0
      elif pattern == "alt_1": alt = 1
      elif pattern == "alt_2": alt = 2
      elif pattern == "alt_3": alt = 3

    elif blocks == 10:
      if pattern == "des": alt = 0
      elif pattern == "alt_1": alt = 1
      elif pattern == "alt_4": alt = 4

    else: print(f"This block amount: {blocks} does not exist with type: {type_}!")
  
    Sequence = generateBlock(total_seats,blocks,alt)
    if pattern == "B-E": 
      Sequence = list(reversed(Sequence))

  ### Halfblock ###
  elif type_ == "halfblock":
    blocks = int(blocks)
    if blocks == 2:
      if pattern == "des": alt = 0; mix = False
      elif pattern == "des_mix": alt = 0; mix = True

    elif blocks == 3:
      if pattern == "des": alt = 0; mix = False
      elif pattern == "alt_1": alt = 1; mix = False
    
    elif blocks == 4:
      if pattern == "des": alt = 0; mix = False
      elif pattern == "alt_1": alt = 1; mix = False
      elif pattern == "des_mix": alt = 0; mix = True

    elif blocks == 6:
      if pattern == "des": alt = 0; mix = False
      elif pattern == "alt_1": alt = 1; mix = False
      elif pattern == "alt_2": alt = 2; mix = False
      elif pattern == "alt_1_mix": alt = 1; mix = True

    elif blocks == 10:
      if pattern == "des": alt = 0; mix = False
      elif pattern == "alt_1": alt = 1; mix = False
      elif pattern == "alt_4": alt = 4; mix = False

    else: print(f"This block amount: {blocks} does not exist with type: {type_}!")

    Sequence = generateSequenceHalfBlock(total_seats, blocks, alt, mix)

  ### Row ###
  elif type_ == "row":
    if pattern == "des": alt = 0
    elif pattern == "alt_1": alt = 1
    elif pattern == "alt_2": alt = 2
    elif pattern == "alt_4": alt = 4
    elif pattern == "alt_5": alt = 5
    elif pattern == "alt_8": alt = 8
    else: print(f"This pattern: {pattern} does not exist with type: {type_}!")

    Sequence = generateSequenceRow(total_seats,alt)  

  ### Halrow ###
  elif type_ == "halfrow":
    if pattern == "des": alt = 0
    elif pattern == "alt_1": alt = 1
    elif pattern == "alt_2": alt = 2
    elif pattern == "alt_5": alt = 5
    elif pattern == "alt_8": alt = 8
    else: print(f"This pattern: {pattern} does not exist with type: {type_}!")

    Sequence = generateSequenceHalfRow(total_seats,alt)

  ### Letter ###
  elif type_ == "letter":
    Sequence = generateLetter(total_seats, pattern)

  ### Seat ###
  elif type_ == "seat":
    if pattern == "des_row_by_letter": alt = 0; alt_letter = False
    elif pattern == "des_row_alt_letter": alt = 0; alt_letter = True
    elif pattern == "alt_1_row_alt_letter": alt = 1; alt_letter = True
    elif pattern == "alt_5_row_alt_letter": alt = 5; alt_letter = True
    elif pattern == "alt_8_row_alt_letter": alt = 8; alt_letter = True
    
    Sequence = generateSeat(total_seats, alt, alt_letter)

  elif type_ == "luggage":
    if pattern == "3_2_1": LuggageList = [3,2,1]
    elif pattern == "1_2_3": LuggageList = [1,2,3]
    
    Sequence = generateLuggageSequence(total_seats,LuggageList,Luggage)
  else: print(f"This type: {type_} does not exist!")

  return Sequence

def generateFaultySequence(total_seats: int, Sequence: list, wrong_seats_percentage: float, distance: int) -> list:
  FaultySequence: list = []
  for passenger in range(0,total_seats):
    u = np.random.rand()
    if u < wrong_seats_percentage:
      if distance >= 1 and distance <= total_seats:
        WrongSeatsPossibilities = []
        u = np.random.rand()

        seat = Sequence[passenger]
        
        lower_bound = seat - distance
        if lower_bound < 1:
          lower_bound = 1

        upper_bound = seat + distance
        if upper_bound > total_seats:
          upper_bound = total_seats

        for wrong_seat in range(lower_bound,upper_bound + 1):
          if wrong_seat != seat:
            WrongSeatsPossibilities.append(wrong_seat)

        faulty_seat_index = math.ceil(u * len(WrongSeatsPossibilities)) - 1
        faulty_seat = WrongSeatsPossibilities[faulty_seat_index]
        FaultySequence.append(faulty_seat)

      else:
        print(f"False distance: {distance}! Distance: {distance} > total_seats: {total_seats} or distance: {distance} < 1")
    else:
      FaultySequence.append(Sequence[passenger])
    
  return FaultySequence
