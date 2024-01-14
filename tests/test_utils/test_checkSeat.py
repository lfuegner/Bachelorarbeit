from checkSeat import checkSeat

def test_checkSeat_sitDown(passenger = 0,
                           targeted_seat = 1,
                           SeatsSequence = [],
                           Luggage = [1]) -> None:
  """
  Tests the function checkSeat(), when the targeted seat is not occupied by another passenger.

  Passenger 0 enters the plane and is searching for the seat number 1.
  """
  DATA_SEATS: dict = {1: {"row": 1,"letter": 4,"occupied": False,"occupied_by": None}}
  DATA_ROWS: dict = {1: {"time_blocked": 0}}
  DATA_PASSENGERS: dict = {0: {"seated": False,
        "install_seat_times": [],
        "arrival_row_timestamps": [26.46],
        "arrival_seat_timestamps": [],
        "exit_seat_timestamps": [],
        "end_timestamps": [],
        "luggage_times":[]
    }
  }

  [new_passenger, new_passenger_seat] = checkSeat(passenger,
                                                  targeted_seat,
                                                  SeatsSequence,
                                                  Luggage,
                                                  DATA_SEATS, 
                                                  DATA_ROWS, 
                                                  DATA_PASSENGERS

                                                               )
  
  targeted_row = DATA_SEATS[targeted_seat]["row"]
  index = len(DATA_PASSENGERS[passenger]["arrival_row_timestamps"]) - 1
  arrival_row_timestamp = DATA_PASSENGERS[passenger]["arrival_row_timestamps"][index]

  install_seat_time = DATA_PASSENGERS[passenger]["install_seat_times"][0]

  assert new_passenger == None
  assert new_passenger_seat == None
  assert DATA_SEATS[targeted_seat]["occupied"] == True
  assert DATA_SEATS[targeted_seat]["occupied_by"] == passenger

  assert DATA_ROWS[targeted_row]["time_blocked"] == arrival_row_timestamp + install_seat_time

  assert len(DATA_PASSENGERS[passenger]["install_seat_times"]) == 1
  assert len(DATA_PASSENGERS[passenger]["luggage_times"]) == 1
  assert len(DATA_PASSENGERS[passenger]["arrival_seat_timestamps"]) == 1
  assert len(DATA_PASSENGERS[passenger]["end_timestamps"]) == 1  

  assert DATA_PASSENGERS[passenger]["install_seat_times"][0] == install_seat_time
  assert DATA_PASSENGERS[passenger]["arrival_seat_timestamps"][0] == arrival_row_timestamp
  assert DATA_PASSENGERS[passenger]["end_timestamps"][0] == arrival_row_timestamp + install_seat_time

  assert DATA_PASSENGERS[passenger]["seated"] == True 

def test_checkSeat_exchangeSeat(passenger = 1,
                                targeted_seat = 1,
                                SeatsSequence = [2,1],
                                Luggage = [1,2]) -> None:
  """
  Tests the function checkSeat(), when the targeted seat is occupied by a passenger. 
  And that passenger is sitting on the wrong seat number.

  Passenger 1 arrives at his targeted seat and sees that the seat is already occupied by Passenger 0.
  But Passenger 0 has to leave, because he doesn't sit on his correct seat.
  ### Output:
    new passenger
    new seat
  """
  
  DATA_SEATS: dict = {1: {"row": 1,"letter": 4,"occupied": True,"occupied_by": 0},
                      2: {"row": 1,"letter": 5,"occupied": False,"occupied_by": None}
  }
  DATA_ROWS: dict = {1: {"time_blocked": 0}}
  DATA_PASSENGERS: dict = {0: {"seated": True,
        "install_seat_times": [11],
        "exit_seat_times": [],
        "arrival_row_timestamps": [0],
        "arrival_seat_timestamps": [0],
        "exit_seat_timestamps": [],
        "end_timestamps": [11]
    },
    1: {"seated": False,
        "install_seat_times": [],
        "exit_seat_times": [],
        "arrival_row_timestamps": [2],
        "arrival_seat_timestamps": [],
        "exit_seat_timestamps": [],
        "end_timestamps": []
    }
  }

  [new_passenger, new_passenger_seat] = checkSeat(passenger,
                                                  targeted_seat,
                                                  SeatsSequence,
                                                  Luggage,
                                                  DATA_SEATS, 
                                                  DATA_ROWS, 
                                                  DATA_PASSENGERS)
  
  targeted_row = DATA_SEATS[targeted_seat]["row"]
  index = len(DATA_PASSENGERS[passenger]["arrival_row_timestamps"]) - 1
  arrival_row_timestamp = DATA_PASSENGERS[passenger]["arrival_row_timestamps"][index]
  
  passenger_who_exits_seat = 0 # DATA_SEATS[targeted_seat]["occupied_by"]
  install_seat_time = DATA_PASSENGERS[passenger]["install_seat_times"][0]
  exit_seat_time = DATA_PASSENGERS[passenger_who_exits_seat]["exit_seat_times"][0]

  assert new_passenger == 0
  assert new_passenger_seat == 2

  assert DATA_SEATS[targeted_seat]["occupied_by"] == passenger

  assert DATA_ROWS[targeted_row]["time_blocked"] == arrival_row_timestamp + exit_seat_time + install_seat_time

  assert DATA_PASSENGERS[passenger]["seated"] == True
  assert len(DATA_PASSENGERS[passenger]["arrival_row_timestamps"]) == 1
  assert len(DATA_PASSENGERS[passenger]["install_seat_times"]) == 1
  assert len(DATA_PASSENGERS[passenger]["end_timestamps"]) == 1
  
  
  assert DATA_PASSENGERS[passenger_who_exits_seat]["seated"] == False
  assert len(DATA_PASSENGERS[passenger_who_exits_seat]["exit_seat_times"]) == 1
  assert len(DATA_PASSENGERS[passenger_who_exits_seat]["exit_seat_timestamps"]) == 1
  assert len(DATA_PASSENGERS[passenger_who_exits_seat]["arrival_row_timestamps"]) == 2

  assert DATA_PASSENGERS[passenger_who_exits_seat]["exit_seat_timestamps"][0] < DATA_PASSENGERS[passenger_who_exits_seat]["arrival_row_timestamps"][1]
  
def test_checkSeat_targeted_seat_changes(passenger = 1,
                                         targeted_seat = 4,
                                         SeatsSequence = [4,18],
                                         Luggage = []) -> None:
  """
  Test the function checkSeat(), when the next passenger arrives at his seat, but one passenger already sits there.
  In this case the arriving passenger searched for the wrong seat 
  ### Output:
    old passenger
    new seat
  """
  DATA_SEATS: dict = {4: {"row": 2,"letter": 1,"occupied": True,"occupied_by": 0},
                      18: {"row": 4,"letter": 3,"occupied": False,"occupied_by": None},
  }
  DATA_ROWS: dict = {2: {"time_blocked": 0}
  }
  DATA_PASSENGERS: dict = {0: {"seated": True,
        "install_seat_times": [14],
        "exit_seat_times": [],
        "arrival_row_timestamps": [0,2.5],
        "arrival_seat_timestamps": [2.5],
        "exit_seat_timestamps": [],
        "end_timestamps": [14]
    },
    1: {"seated": False,
        "install_seat_times": [],
        "exit_seat_times": [],
        "arrival_row_timestamps": [15.15,17],
        "arrival_seat_timestamps": [],
        "exit_seat_timestamps": [],
        "end_timestamps": []
    }
  }
  
  [passenger, new_passenger_seat] = checkSeat(passenger,
                                              targeted_seat,
                                              SeatsSequence,
                                              Luggage,
                                              DATA_SEATS,
                                              DATA_ROWS, 
                                              DATA_PASSENGERS)
  
  targeted_row = DATA_SEATS[targeted_seat]["row"]

  index = len(DATA_PASSENGERS[passenger]["arrival_row_timestamps"]) - 1
  arrival_row_timestamp = DATA_PASSENGERS[passenger]["arrival_row_timestamps"][index]

  assert passenger == 1
  assert new_passenger_seat == 18

  assert len(DATA_PASSENGERS[passenger]["arrival_row_timestamps"]) == 2
  assert len(DATA_PASSENGERS[passenger]["exit_seat_timestamps"]) == 0
  assert len(DATA_PASSENGERS[passenger]["end_timestamps"]) == 0
  assert len(DATA_PASSENGERS[passenger]["install_seat_times"]) == 0
  assert len(DATA_PASSENGERS[passenger]["arrival_seat_timestamps"]) == 0

  assert DATA_ROWS[targeted_row]["time_blocked"] == arrival_row_timestamp

  assert DATA_PASSENGERS[passenger]["seated"] == False