from sample import sampleArrivalTime
def calculateStartTime(total_passengers: int, 
                       lam: float,
                       DATA_PASSENGERS: dict) -> dict:
  """
  Generates the Arrival Times for every Passenger
  """
  for passenger in range(1,total_passengers):
    passenger_before = passenger - 1

    arrival_time = sampleArrivalTime(lam)
    last_start_timestamp = DATA_PASSENGERS[passenger_before]["start_timestamp"]

    start_timestamp = last_start_timestamp + arrival_time

    DATA_PASSENGERS[passenger]["arrival_time"] = arrival_time
    DATA_PASSENGERS[passenger]["start_timestamp"] = start_timestamp

  return DATA_PASSENGERS  

def calculateWaitingRowTime(row: int, 
                            arrival_time: float, 
                            direction: int,
                            DATA_ROWS: dict) -> float:
  """
  Calculates the waiting time for a passenger, until the next row is free.
  """
  next_row = row + direction
  time_till_row_is_blocked = DATA_ROWS[next_row]["time_blocked"]
  
  if time_till_row_is_blocked > arrival_time and direction == 1:
    waiting_row_time = time_till_row_is_blocked - arrival_time

  else:
    waiting_row_time = 0 

  return waiting_row_time

def calculateLugaggeTime(passenger: int,LuggageList: list) -> float:
  """
  Calculates the time a passenger needs to storage his luggage.
  """
  lam = 1/6
  UsedLuggageList = LuggageList[:passenger-1]
  used_luggage_amount = sum(UsedLuggageList)
  total_luggage_amount: int = sum(LuggageList)
  luggage_amount = LuggageList[passenger-1]
  LuggageTimeList: list = []

  for i in range(luggage_amount):
    luggage_time = (used_luggage_amount / total_luggage_amount) * sampleArrivalTime(lam)
    LuggageTimeList.append(luggage_time)
    used_luggage_amount += 1

  return LuggageTimeList