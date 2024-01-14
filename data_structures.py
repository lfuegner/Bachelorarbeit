import math

def createDataSeats(total_seats: int) -> dict:
  """
  Creates a Dictionary, which maps the seat number to a dictionary with the three values row, letter, occupied.

  ### Parameter
  total_seats : integer
    How many Seats are in the airplane.
  first_row_seats  : integer
    How many seats are in the first row, if it is not the normal amount for one full row.
  seats_per_row : integer
    How many seats are installed per row.
  """
  DATA_SEATS: dict = {}
  first_row_seats: int = 3
  seats_per_row: int = 6

  for seat_number in range(1,total_seats + 1):
    DATA_SEATS[seat_number] = {
      'row' : math.ceil((seat_number - first_row_seats) / seats_per_row) + 1,
      'letter' : (seat_number - first_row_seats) % seats_per_row,
      'occupied': False,
      'occupied_by': None
    }
  return DATA_SEATS

def createDataRows(total_rows: int) -> dict:
  """
  Creates a Dictionary, which maps the row number to a dictionary with the three values time, time_blocked, blocked.

  ### Parameter:
  total_rows : integer
    How many rows are in the airplane
  """
  DATA_ROWS:dict = {}
  for row_number in range(1,total_rows + 1):
    DATA_ROWS[row_number] = {'time_blocked': 0}
  return DATA_ROWS


def createDataPassengers(total_passengers: int,
                         SeatsSequence: list,
                         FaultySeatsSequence: list,
                         Luggage: list,
                         DATA_SEATS:dict) -> dict:
  """
  Creates a dictionary, which maps the passengers to a dictionary with data storage place to model the process.
  All the random variable will be stored in this dictionray.
  
  ### Parameter: 
  Sequence : list
    List in which order the passengers enter the plane with their seat number, the seat number is not always correct.
    Sequence[0] = 5 | the first passenger hast the seat number 5, which is not correct, but he will go to seat 5 and will later find his right seat
  CorrectSequence : list
    List in which order the passengers enter the plan with their correct seat number
    CorrectSequence[0] = 23 | the first passenger has the seat number 23, which is correct
  Luggage : list
    List which passenger has how many luggage items
    Luggage[0] = 1 | the first passenger has 1 Luggage item
  total_passengers : int 
    Total number of passengers who can enter the plane. Total number of passengers = total number of seats.
  """
  DATA_PASSENGERS: dict = {}
  for passenger in range(0 ,total_passengers):
    passengers_luggage_amount: int = Luggage[passenger]
    passengers_seat: int = SeatsSequence[passenger]
    passengers_faulty_seat: int = FaultySeatsSequence[passenger]    

    faulty_row_number = DATA_SEATS[passengers_faulty_seat]["row"]
    row_number = DATA_SEATS[passengers_seat]["row"]

    DATA_PASSENGERS[passenger] = {
      # Input seats & Luggage
      'seat' : passengers_seat,
      'faulty_seat': passengers_faulty_seat,
      'correct_seat':passengers_seat == passengers_faulty_seat,
      'luggage_amount': passengers_luggage_amount,
      'row': [row_number,faulty_row_number],

      # Variables needed later
      'seated': False,
      
      # Random Variables    
      'arrival_time': 0, 
      'start_timestamp': 0,
      'waiting_start_time': 0,

      'passing_row_times': [],
      'luggage_times': [],
      'install_seat_times': [], 
      'exit_seat_times': [],         

      'arrival_row_timestamps': [],
      'waiting_row_times': [],
      'arrival_seat_timestamps': [],
      'exit_seat_timestamps': [],
      'end_timestamps': [], 
    }

  return DATA_PASSENGERS