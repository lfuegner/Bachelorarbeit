from sample import sampleInstallSeat,sampleExitSeat
from calculate import calculateLugaggeTime


def checkSeat(passenger: int, 
                     targeted_seat: int,
                     SeatsSequence: list,
                     Luggage: list,
                     DATA_SEATS:dict, 
                     DATA_ROWS: dict, 
                     DATA_PASSENGERS: dict) -> list:
  """
  Hello World
  """
  targeted_seat_occupied = DATA_SEATS[targeted_seat]["occupied"]

  targeted_row = DATA_SEATS[targeted_seat]["row"]

  if  targeted_seat_occupied == False:
    sitDown(passenger = passenger,
            targeted_seat = targeted_seat,
            Luggage=Luggage,
            DATA_SEATS=DATA_SEATS,
            DATA_ROWS=DATA_ROWS,
            DATA_PASSENGERS=DATA_PASSENGERS)
    
    return [None,None]

  elif targeted_seat_occupied == True:

    passengers_seat = SeatsSequence[passenger]

    if targeted_seat == passengers_seat: 
      [new_passenger,new_passengers_seat] = exchangeSeat(passenger = passenger,
                                                         targeted_seat = targeted_seat,
                                                         SeatsSequence = SeatsSequence,
                                                         Luggage = Luggage,
                                                         DATA_SEATS = DATA_SEATS,
                                                         DATA_ROWS = DATA_ROWS,
                                                         DATA_PASSENGERS = DATA_PASSENGERS)  

      return [new_passenger, new_passengers_seat]   
    
    elif not(targeted_seat == passengers_seat): 
      index = len(DATA_PASSENGERS[passenger]["arrival_row_timestamps"]) - 1
      arrival_row_timestamp = DATA_PASSENGERS[passenger]["arrival_row_timestamps"][index]

      new_passengers_seat = SeatsSequence[passenger]
      timestamp_till_row_is_blocked = arrival_row_timestamp

      if DATA_ROWS[targeted_row]["time_blocked"] < timestamp_till_row_is_blocked:
        DATA_ROWS[targeted_row]["time_blocked"] = timestamp_till_row_is_blocked

      return [passenger, new_passengers_seat]
    
def sitDown(passenger: int,
            targeted_seat: int,
            Luggage: list,
            DATA_SEATS: dict,
            DATA_ROWS: dict,
            DATA_PASSENGERS: dict) -> None:
  """
  Hello World
  """
  targeted_row = DATA_SEATS[targeted_seat]["row"]
  index = len(DATA_PASSENGERS[passenger]["arrival_row_timestamps"]) - 1
  arrival_row_timestamp = DATA_PASSENGERS[passenger]["arrival_row_timestamps"][index]
  
  install_seat_time = sampleInstallSeat()
  LuggageTimeList = calculateLugaggeTime(passenger,Luggage)
  luggage_time = sum(LuggageTimeList)
  extra_time_factor = checkSeatsClose(targeted_seat,DATA_SEATS)

  arrival_seat_timestamp = arrival_row_timestamp
  end_timestamp = arrival_row_timestamp + luggage_time + (install_seat_time * extra_time_factor)
  timestamp_till_row_is_blocked = arrival_row_timestamp + luggage_time + (install_seat_time * extra_time_factor)

  DATA_SEATS[targeted_seat]["occupied"] = True
  DATA_SEATS[targeted_seat]["occupied_by"] = passenger
  
  if DATA_ROWS[targeted_row]["time_blocked"] < timestamp_till_row_is_blocked:
    DATA_ROWS[targeted_row]["time_blocked"] = timestamp_till_row_is_blocked    

  DATA_PASSENGERS[passenger]["seated"] = True 
  DATA_PASSENGERS[passenger]["luggage_times"] = LuggageTimeList
  DATA_PASSENGERS[passenger]["install_seat_times"].append(install_seat_time)
  DATA_PASSENGERS[passenger]["arrival_seat_timestamps"].append(arrival_seat_timestamp)
  DATA_PASSENGERS[passenger]["end_timestamps"].append(end_timestamp)

def exchangeSeat(passenger:int,
                 targeted_seat:int,
                 SeatsSequence: list,
                 Luggage: list,
                 DATA_SEATS: dict, 
                 DATA_ROWS: dict, 
                 DATA_PASSENGERS: dict) -> None:
  """
  Hello World
  """
  targeted_row = DATA_SEATS[targeted_seat]["row"]

  index = len(DATA_PASSENGERS[passenger]["arrival_row_timestamps"]) - 1
  arrival_row_timestamp = DATA_PASSENGERS[passenger]["arrival_row_timestamps"][index]
  passenger_who_exits_seat = DATA_SEATS[targeted_seat]["occupied_by"]

  install_seat_time = sampleInstallSeat()
  exit_seat_time = sampleExitSeat()
  LuggageTimeList = calculateLugaggeTime(passenger,Luggage)
  luggage_time = sum(LuggageTimeList)
  extra_time_factor = checkSeatsClose(targeted_seat,DATA_SEATS)

  exit_seat_timestamp = arrival_row_timestamp
  end_timestamp = arrival_row_timestamp + luggage_time + exit_seat_time + (install_seat_time * extra_time_factor)
  timestamp_till_row_is_blocked = arrival_row_timestamp + luggage_time + exit_seat_time + (install_seat_time * extra_time_factor)  

  DATA_SEATS[targeted_seat]["occupied_by"] = passenger

  DATA_ROWS[targeted_row]["time_blocked"] = timestamp_till_row_is_blocked

  DATA_PASSENGERS[passenger]["seated"] = True
  DATA_PASSENGERS[passenger]["luggage_times"] = LuggageTimeList
  DATA_PASSENGERS[passenger]["install_seat_times"].append(install_seat_time)
  DATA_PASSENGERS[passenger]["end_timestamps"].append(end_timestamp)
  
  DATA_PASSENGERS[passenger_who_exits_seat]["seated"] = False
  DATA_PASSENGERS[passenger_who_exits_seat]["exit_seat_times"].append(exit_seat_time)
  DATA_PASSENGERS[passenger_who_exits_seat]["exit_seat_timestamps"].append(exit_seat_timestamp)
  DATA_PASSENGERS[passenger_who_exits_seat]["arrival_row_timestamps"].append(exit_seat_timestamp + exit_seat_time)

  new_passengers_seat = SeatsSequence[passenger_who_exits_seat]
  new_passenger = passenger_who_exits_seat 

  return [new_passenger,new_passengers_seat]

def checkSeatsClose(seat:int ,DATA_SEATS:dict) -> float:
  """
  This function determines if a aishle or mid seat is already occupied and returns a multiplier for the install seat time of our passenger.
  """
  first_row_seats = 3
  seats_per_row = 6
  extra_time_factor = 1
  letter = (seat + first_row_seats) % seats_per_row

  if letter == 1: # Window A
    if DATA_SEATS[seat+1]["occupied"] == True and DATA_SEATS[seat+2]["occupied"] == True: # B and C have to be occupied
      extra_time_factor = 1.5

    elif (DATA_SEATS[seat+1]["occupied"] == False and DATA_SEATS[seat+2]["occupied"] == True) or (DATA_SEATS[seat+1]["occupied"] == True and DATA_SEATS[seat+2]["occupied"] == False):
      extra_time_factor = 1.25

  elif letter == 0: # Window F
    if DATA_SEATS[seat+1]["occupied"] == True and DATA_SEATS[seat+1]["occupied"] == True:
      extra_time_factor = 1.5

    elif (DATA_SEATS[seat-1]["occupied"] == False and DATA_SEATS[seat-2]["occupied"] == True) or (DATA_SEATS[seat-1]["occupied"] == True and DATA_SEATS[seat-2]["occupied"] == False):
      extra_time_factor = 1.25

  elif letter == 2: # Mid B
    if DATA_SEATS[seat+1]["occupied"] == True:
      extra_time_factor = 1.25

  elif letter == 5: # Mid E
    if DATA_SEATS[seat-1]["occupied"] == True: 
      extra_time_factor = 1.25

  return extra_time_factor