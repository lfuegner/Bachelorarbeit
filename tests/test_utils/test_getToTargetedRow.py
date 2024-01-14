from getToTargetedRow import getToTargetedRow

def test_getToTargetedRow_ascending(passenger = 0,
                                    current_row = 1,
                                    targeted_row = 3,
                                    direction = 1,) -> None:
  """
  Tests the funciton getToTargetedRow.
  Here our current row is smaller than our targeted row. 1 < 3
  That means we have to go forth in the aishle.
  """
  DATA_ROWS: dict = {1: {"time_blocked": 0},
                     2: {"time_blocked": 0},
                     3: {"time_blocked": 0},
                     }
  DATA_PASSENGERS: dict = {0: {"arrival_time": 0,
                               "start_timestamp": 0,
                               "waiting_start_time": 0,
                               "arrival_row_timestamps": [0],
                               "waiting_row_times": [],
                               "passing_row_times": [], 
    }
  }

  assert len(DATA_PASSENGERS[passenger]["arrival_row_timestamps"]) == 1
  assert len(DATA_PASSENGERS[passenger]["waiting_row_times"]) == 0
  assert len(DATA_PASSENGERS[passenger]["passing_row_times"]) == 0
  
  getToTargetedRow(passenger = passenger,
                  current_row=current_row,
                  targeted_row = targeted_row,
                  direction = direction,
                  DATA_ROWS = DATA_ROWS,
                  DATA_PASSENGERS = DATA_PASSENGERS)

  row_1 = 1
  row_2 = 2

  assert DATA_ROWS[row_1]["time_blocked"] < DATA_ROWS[row_2]["time_blocked"]

  # ROW 1 -> ROw 2
  arrival_row_1_timestamp = DATA_PASSENGERS[passenger]["arrival_row_timestamps"][0]
  waiting_row_2_time = DATA_PASSENGERS[passenger]["waiting_row_times"][0]
  passing_row_1_time = DATA_PASSENGERS[passenger]["passing_row_times"][0]

  time_blocked_row_1 = arrival_row_1_timestamp + waiting_row_2_time  + passing_row_1_time

  assert DATA_ROWS[row_1]["time_blocked"] == time_blocked_row_1
  assert DATA_ROWS[row_1]["time_blocked"] == DATA_PASSENGERS[passenger]["arrival_row_timestamps"][1]

  # ROW 2 -> ROW 3
  arrival_row_2_timestamp = DATA_PASSENGERS[passenger]["arrival_row_timestamps"][1]
  waiting_row_3_time = DATA_PASSENGERS[passenger]["waiting_row_times"][1]
  passing_row_2_time = DATA_PASSENGERS[passenger]["passing_row_times"][1]

  time_blocked_row_2 = arrival_row_2_timestamp  + waiting_row_3_time + passing_row_2_time

  assert DATA_ROWS[row_2]["time_blocked"] == time_blocked_row_2
  assert DATA_ROWS[row_2]["time_blocked"] == DATA_PASSENGERS[passenger]["arrival_row_timestamps"][2]  
  
  assert len(DATA_PASSENGERS[passenger]["arrival_row_timestamps"]) == 3
  assert len(DATA_PASSENGERS[passenger]["waiting_row_times"]) == 2
  assert len(DATA_PASSENGERS[passenger]["passing_row_times"]) == 2

def test_getToTargetedRow_descending(passenger = 1,
                                     current_row = 3,
                                     targeted_row = 1,
                                     direction = -1) -> None:
  """
  Tests the funciton getToTargetedRow.
  Here our current row is bigger than our targeted row. 2 > 1
  That means we have to go back in the aishle.
  """
  DATA_ROWS: dict = {1: {"time_blocked": 2},
                     2: {"time_blocked": 4.5},
                     3: {"time_blocked": 6.5}
  }
  DATA_PASSENGERS: dict = {1: {"arrival_time": 1,
                               "start_timestamp": 1,
                               "waiting_start_time" : 0,
                               "arrival_row_timestamps": [1,4,6.5],
                               "waiting_row_times": [1,0.5],
                               "passing_row_times": [2,2],
    }
  }
  
  assert len(DATA_PASSENGERS[passenger]["arrival_row_timestamps"]) == 3
  assert len(DATA_PASSENGERS[passenger]["waiting_row_times"]) == 2
  assert len(DATA_PASSENGERS[passenger]["passing_row_times"]) == 2
  
  getToTargetedRow(passenger = passenger,
                  targeted_row = targeted_row,
                  current_row = current_row,
                  direction = direction,
                  DATA_ROWS = DATA_ROWS, 
                  DATA_PASSENGERS = DATA_PASSENGERS)

  row_2 = 2
  row_3 = 3

  assert DATA_ROWS[row_2]["time_blocked"] > DATA_ROWS[row_3]["time_blocked"]
  
  # Row 3 -> Row 2
  arrival_row_timestamp = DATA_PASSENGERS[passenger]["arrival_row_timestamps"][2]
  waiting_row_time = DATA_PASSENGERS[passenger]["waiting_row_times"][2]
  passing_row_time = DATA_PASSENGERS[passenger]["passing_row_times"][2]

  time_blocked = arrival_row_timestamp + passing_row_time + waiting_row_time

  assert DATA_ROWS[row_3]["time_blocked"] == time_blocked
  assert DATA_ROWS[row_3]["time_blocked"] == DATA_PASSENGERS[passenger]["arrival_row_timestamps"][3]

  # Row 2 -> Row 1
  arrival_row_timestamp = DATA_PASSENGERS[passenger]["arrival_row_timestamps"][3]
  waiting_row_time = DATA_PASSENGERS[passenger]["waiting_row_times"][3]
  passing_row_time = DATA_PASSENGERS[passenger]["passing_row_times"][3]

  time_blocked = arrival_row_timestamp + passing_row_time + waiting_row_time

  assert DATA_ROWS[row_2]["time_blocked"] == time_blocked
  assert DATA_ROWS[row_2]["time_blocked"] == DATA_PASSENGERS[passenger]["arrival_row_timestamps"][4]

  assert DATA_PASSENGERS[passenger]["waiting_row_times"][2] == 0
  assert DATA_PASSENGERS[passenger]["waiting_row_times"][3] == 0

  assert len(DATA_PASSENGERS[passenger]["arrival_row_timestamps"]) == 5
  assert len(DATA_PASSENGERS[passenger]["waiting_row_times"]) == 4
  assert len(DATA_PASSENGERS[passenger]["passing_row_times"]) == 4