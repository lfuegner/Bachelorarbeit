from data_structures import createDataSeats,createDataRows,createDataPassengers
from getToFirstRow import getToFirstRow

def test_getToFirstRow(passenger = 0) -> None:

  DATA_ROWS: dict = {1: {"time_blocked": 0}}
  DATA_PASSENGERS: dict = {0: {"arrival_time": 1,
                               "start_timestamp": 1,
                               "waiting_start_time" : 0,
                               "arrival_row_timestamps": [],
    }
  }
  
  assert len(DATA_PASSENGERS[passenger]["arrival_row_timestamps"]) == 0


  DATA_PASSENGERS = getToFirstRow(passenger = passenger,
                                  DATA_ROWS = DATA_ROWS,
                                  DATA_PASSENGERS = DATA_PASSENGERS)

  assert len(DATA_PASSENGERS[passenger]["arrival_row_timestamps"]) == 1

  start_timestamp = DATA_PASSENGERS[passenger]["start_timestamp"]
  waiting_time = DATA_PASSENGERS[passenger]["waiting_start_time"]

  assert DATA_PASSENGERS[passenger]["waiting_start_time"] == 0
  assert DATA_PASSENGERS[passenger]["arrival_row_timestamps"][0] == 1

def test_getToFirstRow_(passenger = 1) -> None:

  DATA_ROWS: dict = {1: {"time_blocked": 5}}
  DATA_PASSENGERS: dict = {1: {"arrival_time": 1,
                               "start_timestamp": 1,
                               "waiting_start_time" : 0,
                               "arrival_row_timestamps": [],

    }
  }
  
  assert len(DATA_PASSENGERS[passenger]["arrival_row_timestamps"]) == 0

  DATA_PASSENGERS = getToFirstRow(passenger = passenger,
                                  DATA_ROWS = DATA_ROWS,
                                  DATA_PASSENGERS = DATA_PASSENGERS)

  assert len(DATA_PASSENGERS[passenger]["arrival_row_timestamps"]) == 1

  assert DATA_PASSENGERS[passenger]["waiting_start_time"] == 4 # 5 - 1
  assert DATA_PASSENGERS[passenger]["arrival_row_timestamps"][0] == 5 # 4 + 1