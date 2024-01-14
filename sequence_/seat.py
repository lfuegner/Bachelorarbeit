import math
def generateSeat(total_seats: int, alt ,alt_letter) -> list:
  seats_per_row = 6
  first_row_seats = 3
  Sequence: list = []
  alternate = alt + 1
  
  SeatList = [1,2,3,4,5,0]
  
  if alt_letter == False:
    for letter_index in range(seats_per_row):
      for seat in range(total_seats,0,-1):
        if SeatList[letter_index] == (seat + first_row_seats )% seats_per_row :
          Sequence.append(seat)

  elif alt_letter == True:
    total_rows = math.ceil((total_seats + 3) / 6)

    for k in range(alternate):
      direction = 1
      start_row = 1
      end_row = 4

      for j in range(2):
        for letter in range(start_row,end_row,direction):
          for row in range(total_rows,0,-alternate):
            if j == 0:
              seat = (row*seats_per_row) - first_row_seats + letter - seats_per_row

              if seat > 0 and seat <= total_seats:
                Sequence.append(seat)

              letter = 7 - letter # alternate beteen letters
              
            elif j == 1:
              seat = (row*seats_per_row) - first_row_seats + letter - seats_per_row

              if  seat > 0 and seat <= total_seats:
                Sequence.append(seat)

              letter = 7 - letter # alternate beteen letters
               
        direction = -1
        start_row = 6
        end_row = 3
      total_rows -= 1

  return Sequence
