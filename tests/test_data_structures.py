from data_structures import createDataSeats,createDataRows,createDataPassengers

def test_createDataSeats() -> None:
  DATA_SEATS:dict = createDataSeats(total_seats=12)

  assert 1 == DATA_SEATS[1]["row"]
  assert 1 == DATA_SEATS[2]["row"]
  assert 1 == DATA_SEATS[3]["row"]

  assert 2 == DATA_SEATS[4]["row"]
  assert 2 == DATA_SEATS[5]["row"]
  assert 2 == DATA_SEATS[6]["row"]
  assert 2 == DATA_SEATS[7]["row"]
  assert 2 == DATA_SEATS[8]["row"]
  assert 2 == DATA_SEATS[9]["row"]

  assert 3 == DATA_SEATS[10]["row"]
  assert 3 == DATA_SEATS[11]["row"]
  assert 3 == DATA_SEATS[12]["row"]

  assert 4 == DATA_SEATS[1]["letter"]
  assert 5 == DATA_SEATS[2]["letter"]
  assert 0 == DATA_SEATS[3]["letter"]

  assert 1 == DATA_SEATS[4]["letter"]
  assert 2 == DATA_SEATS[5]["letter"]
  assert 3 == DATA_SEATS[6]["letter"]
  assert 4 == DATA_SEATS[7]["letter"]
  assert 5 == DATA_SEATS[8]["letter"]
  assert 0 == DATA_SEATS[9]["letter"]

  assert 1 == DATA_SEATS[10]["letter"]
  assert 2 == DATA_SEATS[11]["letter"]
  assert 3 == DATA_SEATS[12]["letter"]