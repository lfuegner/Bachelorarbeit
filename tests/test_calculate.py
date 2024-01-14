from calculate import calculateStartTime,calculateWaitingRowTime,calculateLugaggeTime

def test_startTime() -> None:
  DATA_PASSENGERS: dict = {
    0: {"arrival_time": 0,
        "start_timestamp": 0,
        "waiting_start_time": 0,
    },
    1: {"arrival_time": 0,
        "start_timestamp": 0,
        "waiting_start_time": 0,
    },
    2: {"arrival_time": 0,
        "start_timestamp": 0,
        "waiting_start_time": 0,
    }
  }
  
  DATA_PASSENGERS = calculateStartTime(total_passengers=3, 
                                       lam=1/6,
                                       DATA_PASSENGERS=DATA_PASSENGERS)
  
  passenger_0 = 0
  passenger_1 = 1
  passenger_2 = 2

  assert DATA_PASSENGERS[passenger_0]["start_timestamp"] < DATA_PASSENGERS[passenger_1]["start_timestamp"]
  assert DATA_PASSENGERS[passenger_1]["start_timestamp"] < DATA_PASSENGERS[passenger_2]["start_timestamp"]

  arrival_time_1 = DATA_PASSENGERS[passenger_1]["arrival_time"]
  last_start_timestamp = DATA_PASSENGERS[passenger_1]["start_timestamp"]
  arrival_time_2 = DATA_PASSENGERS[passenger_2]["arrival_time"]

  assert  DATA_PASSENGERS[passenger_0]["start_timestamp"] == 0
  assert DATA_PASSENGERS[passenger_1]["start_timestamp"]  == arrival_time_1
  assert DATA_PASSENGERS[passenger_2]["start_timestamp"] == last_start_timestamp + arrival_time_2

def test_waitingRowTime() -> None:
  """
  Tests if the the correct waiting time is calculated.
  Output of waiting_time should be 0, because the arrival time is bigger than the time which blocks the row.
  6 > 5 -> waiting_time == 0
  """
  DATA_ROWS: dict = {1: {"time_blocked": 3},
                     2: {"time_blocked": 5}
                     }
  
  waiting_time = calculateWaitingRowTime(row = 1,arrival_time = 6,direction = 1,
                                              DATA_ROWS=DATA_ROWS)
  assert waiting_time == 0

def test_waitingRowTime_direction_plus1() -> None:
  """
  Tests if the the correct waiting time is calculated.
  Output of waiting_time should be 4, because the arrival time is smaller than the time which blocks the row.
  1 < 5 -> waiting_time == 5 - 1 == 4
  """
  DATA_ROWS: dict = {1: {"time_blocked": 3},
                     2: {"time_blocked": 5}
                     }

  waiting_time = calculateWaitingRowTime(row = 1, arrival_time = 1,direction = 1, 
                                          DATA_ROWS=DATA_ROWS)
  assert waiting_time == 4

def test_waitingRowTime_direction_minus1() -> None:
  """
  Tests if the the correct waiting time is calculated.
  Output of waiting_time should be 0, because we move against the aishle. That means we have been to the row before
  and don't have to wait, because we queue every passenger one at a time.
  direction == -1 -> waiting_time == 0
  """
  DATA_ROWS: dict = {1: {"time_blocked": 3},
                     2: {"time_blocked": 5}
                     }
  row = 2
  waiting_time = calculateWaitingRowTime(row = row, arrival_time = 1, direction = -1,
                                              DATA_ROWS=DATA_ROWS)
  assert row > 1
  assert waiting_time == 0

def test_calculateLugaggeTime(passenger = 7, LuggageList = [1,1,3,2,3,3,3]) -> None:
  List = calculateLugaggeTime(passenger=passenger,
                                      LuggageList=LuggageList)
  assert len(List) == 3