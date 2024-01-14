from sample import samplePassingOneRow
from calculate import calculateWaitingRowTime

def getToTargetedRow(passenger, 
                     targeted_row, 
                     current_row, 
                     direction: int,                     
                     DATA_ROWS: dict, 
                     DATA_PASSENGERS: dict):

  for row in range(current_row,targeted_row,direction):
    
    index = len(DATA_PASSENGERS[passenger]["arrival_row_timestamps"]) - 1
    arrival_row_timestamp = DATA_PASSENGERS[passenger]["arrival_row_timestamps"][index]

    passing_row_time = samplePassingOneRow()

    if direction == 1:
      waiting_row_time = calculateWaitingRowTime(row,
                                               arrival_row_timestamp,
                                               direction,
                                               DATA_ROWS)
      
      arrival_next_row_timestamp = arrival_row_timestamp + waiting_row_time + passing_row_time
      timestamp_till_row_is_blocked = arrival_row_timestamp + waiting_row_time + passing_row_time

      if DATA_ROWS[row]["time_blocked"] < timestamp_till_row_is_blocked:
        DATA_ROWS[row]["time_blocked"] = timestamp_till_row_is_blocked       
      
    elif direction == -1:
      waiting_row_time = 0

      arrival_next_row_timestamp = arrival_row_timestamp + passing_row_time
      timestamp_till_row_is_blocked = arrival_row_timestamp + passing_row_time

      if DATA_ROWS[row]["time_blocked"] < timestamp_till_row_is_blocked:
        DATA_ROWS[row]["time_blocked"] = timestamp_till_row_is_blocked
    
    DATA_PASSENGERS[passenger]["waiting_row_times"].append(waiting_row_time)
    DATA_PASSENGERS[passenger]["passing_row_times"].append(passing_row_time)
    DATA_PASSENGERS[passenger]["arrival_row_timestamps"].append(arrival_next_row_timestamp)