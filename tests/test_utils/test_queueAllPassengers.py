from queueAllPassengers import queueAllPassengers
from data_structures import createDataSeats,createDataRows,createDataPassengers

def test_queueAllPassengers_no_problem(total_passengers = 12,
                            SeatSequence = [1,2,3,4,5,6,7,8,9,10,11,12],
                            FaultySeatsSequence = [1,2,3,4,5,6,7,8,9,10,11,12],
                            Luggage = [1,1,1,1,1,1,1,1,1,1,1,1]) -> None:
  
  DATA_SEATS: dict = createDataSeats(total_seats = total_passengers)
  DATA_ROWS: dict = createDataRows(total_rows = 3)
  DATA_PASSENGERS: dict = createDataPassengers(total_passengers = total_passengers,
                                               SeatsSequence = SeatSequence,
                                               FaultySeatsSequence = FaultySeatsSequence,
                                               Luggage = Luggage,
                                               DATA_SEATS = DATA_SEATS)
  

  queueAllPassengers(total_passengers = total_passengers,
                     SeatsSequence = SeatSequence,
                     FaultySeatsSequence = FaultySeatsSequence,
                     Luggage = Luggage,
                     DATA_SEATS = DATA_SEATS,
                     DATA_ROWS = DATA_ROWS,
                     DATA_PASSENGERS = DATA_PASSENGERS)
  
  assert DATA_ROWS[1]["time_blocked"] != 0
  assert DATA_ROWS[2]["time_blocked"] != 0
  assert DATA_ROWS[3]["time_blocked"] != 0

  assert DATA_ROWS[1]["time_blocked"] < DATA_ROWS[2]["time_blocked"] < DATA_ROWS[3]["time_blocked"]

  assert DATA_ROWS[1]["time_blocked"] == DATA_PASSENGERS[11]["arrival_row_timestamps"][1]
  assert DATA_ROWS[2]["time_blocked"] == DATA_PASSENGERS[11]["arrival_row_timestamps"][2]
  assert DATA_ROWS[3]["time_blocked"] == DATA_PASSENGERS[11]["end_timestamps"][0]

  assert len(DATA_PASSENGERS[0]["arrival_row_timestamps"]) == 1
  assert len(DATA_PASSENGERS[1]["arrival_row_timestamps"]) == 1
  assert len(DATA_PASSENGERS[2]["arrival_row_timestamps"]) == 1
  assert len(DATA_PASSENGERS[3]["arrival_row_timestamps"]) == 2
  assert len(DATA_PASSENGERS[4]["arrival_row_timestamps"]) == 2
  assert len(DATA_PASSENGERS[5]["arrival_row_timestamps"]) == 2
  assert len(DATA_PASSENGERS[6]["arrival_row_timestamps"]) == 2
  assert len(DATA_PASSENGERS[7]["arrival_row_timestamps"]) == 2
  assert len(DATA_PASSENGERS[8]["arrival_row_timestamps"]) == 2
  assert len(DATA_PASSENGERS[9]["arrival_row_timestamps"]) == 3
  assert len(DATA_PASSENGERS[10]["arrival_row_timestamps"]) == 3
  assert len(DATA_PASSENGERS[11]["arrival_row_timestamps"]) == 3
 

### neuer Sitzplatz für Passagier in der Reihe
def test_queueAllPassengers_old_passenger_new_seat_ascending(total_passengers = 12,
                            SeatSequence = [1,2,3,4,5,6,7,8,9,10,11,12],
                            FaultySeatsSequence = [1,2,3,4,5,6,7,8,9,10,11,1],
                            Luggage = [1,1,1,1,1,1,1,1,1,1,1,1]) -> None:
  
  DATA_SEATS: dict = createDataSeats(total_seats = total_passengers)
  DATA_ROWS: dict = createDataRows(total_rows = 3)
  DATA_PASSENGERS: dict = createDataPassengers(total_passengers= total_passengers,
                                               SeatsSequence=SeatSequence,
                                               FaultySeatsSequence=FaultySeatsSequence,
                                               Luggage = Luggage,
                                               DATA_SEATS=DATA_SEATS)
  

  queueAllPassengers(total_passengers = total_passengers,
                     SeatsSequence = SeatSequence,
                     FaultySeatsSequence = FaultySeatsSequence,
                     Luggage = Luggage,
                     DATA_SEATS = DATA_SEATS,
                     DATA_ROWS = DATA_ROWS,
                     DATA_PASSENGERS = DATA_PASSENGERS)

  assert len(DATA_PASSENGERS[11]["arrival_row_timestamps"]) == 3

def test_queueAllPassengers_old_passenger_new_seat_descending(total_passengers = 12,
                            SeatSequence = [1,2,4,5,6,7,8,9,10,11,12,3],
                            FaultySeatsSequence = [1,2,4,5,6,7,8,9,10,11,12,12],
                            Luggage = [1,1,1,1,1,1,1,1,1,1,1,1]) -> None:
  
  DATA_SEATS: dict = createDataSeats(total_seats = total_passengers)
  DATA_ROWS: dict = createDataRows(total_rows = 3)
  DATA_PASSENGERS: dict = createDataPassengers(total_passengers= total_passengers,
                                               SeatsSequence=SeatSequence,
                                               FaultySeatsSequence=FaultySeatsSequence,
                                               Luggage = Luggage,
                                               DATA_SEATS=DATA_SEATS)
  
  
  queueAllPassengers(total_passengers = total_passengers,
                     SeatsSequence = SeatSequence,
                     FaultySeatsSequence = FaultySeatsSequence,
                     Luggage = Luggage,
                     DATA_SEATS = DATA_SEATS,
                     DATA_ROWS = DATA_ROWS,
                     DATA_PASSENGERS = DATA_PASSENGERS)
  

  assert DATA_ROWS[1]["time_blocked"] > DATA_ROWS[2]["time_blocked"] > DATA_ROWS[3]["time_blocked"]

  assert DATA_ROWS[1]["time_blocked"] == DATA_PASSENGERS[11]["end_timestamps"][0]
  assert DATA_ROWS[2]["time_blocked"] == DATA_PASSENGERS[11]["arrival_row_timestamps"][4]
  assert DATA_ROWS[3]["time_blocked"] == DATA_PASSENGERS[11]["arrival_row_timestamps"][3]
  
  assert len(DATA_PASSENGERS[11]["arrival_row_timestamps"]) == 5

def test_queueAllPassengers_old_passenger_new_seat_equal(total_passengers = 12,
                            SeatSequence = [1,2,3,4,5,6,7,8,9,10,11,12],
                            FaultySeatsSequence = [1,2,3,4,4,6,7,8,9,10,11,12],
                            Luggage = [1,1,1,1,1,1,1,1,1,1,1,1]) -> None:
  
  DATA_SEATS: dict = createDataSeats(total_seats = total_passengers)
  DATA_ROWS: dict = createDataRows(total_rows = 3)
  DATA_PASSENGERS: dict = createDataPassengers(total_passengers= total_passengers,
                                               SeatsSequence=SeatSequence,
                                               FaultySeatsSequence=FaultySeatsSequence,
                                               Luggage = Luggage,
                                               DATA_SEATS=DATA_SEATS)
  
  
  queueAllPassengers(total_passengers = total_passengers,
                     SeatsSequence = SeatSequence,
                     FaultySeatsSequence = FaultySeatsSequence,
                     Luggage = Luggage,
                     DATA_SEATS = DATA_SEATS,
                     DATA_ROWS = DATA_ROWS,
                     DATA_PASSENGERS = DATA_PASSENGERS)
  
  assert len(DATA_PASSENGERS[4]["arrival_row_timestamps"]) == 2

  assert DATA_SEATS[5]["occupied_by"] == 4 # Passenger 5 ,da 0,1,2,3,4