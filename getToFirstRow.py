def getToFirstRow(passenger: int,
                  DATA_ROWS: dict, 
                  DATA_PASSENGERS:dict) -> dict:

  start_timestamp = DATA_PASSENGERS[passenger]["start_timestamp"]

  time_till_row_1_is_blocked = DATA_ROWS[1]["time_blocked"]
  
  if time_till_row_1_is_blocked > start_timestamp:
    waiting_time = time_till_row_1_is_blocked - start_timestamp

  else:
    waiting_time = 0 

  arrival_row_timestamp = start_timestamp + waiting_time
  
  DATA_PASSENGERS[passenger]["waiting_start_time"] = waiting_time
  DATA_PASSENGERS[passenger]["arrival_row_timestamps"].append(arrival_row_timestamp)

  return DATA_PASSENGERS