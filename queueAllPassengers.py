from getToFirstRow import getToFirstRow
from getToTargetedRow import getToTargetedRow
from getDirection import getDirection
from checkSeat import checkSeat
from calculate import calculateStartTime

def queueAllPassengers(total_passengers: int,
                       SeatsSequence: list,
                       FaultySeatsSequence: list,
                       Luggage: list,
                       DATA_SEATS: dict, 
                       DATA_ROWS: dict,
                       DATA_PASSENGERS:dict):
  
  DATA_PASSENGERS = calculateStartTime(total_passengers = total_passengers,
                                       lam = 1/6,
                                       DATA_PASSENGERS= DATA_PASSENGERS)
 
  for passenger in range(total_passengers):
    getToFirstRow(passenger, 
                  DATA_ROWS, 
                  DATA_PASSENGERS)
    
    current_row = 1
    direction = 1
    targeted_seat = FaultySeatsSequence[passenger]
    targeted_row = DATA_SEATS[targeted_seat]["row"]

    while DATA_PASSENGERS[passenger]["seated"] == False:
      
      if not(current_row == targeted_row):
        getToTargetedRow(passenger, 
                         targeted_row,
                         current_row,
                         direction,
                         DATA_ROWS,
                         DATA_PASSENGERS)
              
        current_row = targeted_row
      
      elif current_row == targeted_row:
          
        [new_passenger, new_targeted_seat] = checkSeat(passenger = passenger,
                                                      targeted_seat = targeted_seat,
                                                      SeatsSequence = SeatsSequence,
                                                      Luggage=Luggage,
                                                      DATA_SEATS = DATA_SEATS,
                                                      DATA_ROWS = DATA_ROWS,
                                                      DATA_PASSENGERS = DATA_PASSENGERS)
        if not(new_passenger == None):
          current_row = targeted_row
          targeted_seat = new_targeted_seat
          targeted_row = DATA_SEATS[targeted_seat]["row"]
          
          passenger = new_passenger

          direction = getDirection(current_row, targeted_row)