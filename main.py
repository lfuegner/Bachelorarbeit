import math, json
from sequence import generateSequence,generateFaultySequence,generateLuggage
from data_structures import createDataPassengers,createDataRows,createDataSeats
from queueAllPassengers import queueAllPassengers

def main(total_seats,wrong_seats_percentage,type_: str, blocks: str, pattern :str, load: str, distance: int) -> dict:
    total_passengers: int = total_seats
    total_rows: int = math.ceil((total_seats + 3) / 6)

    Luggage: list = generateLuggage(total_seats, load)
    SeatsSequence :list = generateSequence(total_seats = total_seats, type_ = type_, blocks = blocks, pattern = pattern, Luggage=Luggage)
    FaultySeatsSequence: list = generateFaultySequence(total_seats, SeatsSequence, wrong_seats_percentage, distance)

    DATA_SEATS: dict = createDataSeats(total_seats)
    DATA_ROWS: dict = createDataRows(total_rows)
    DATA_PASSENGERS: dict = createDataPassengers(total_passengers,
                                                 SeatsSequence,
                                                 FaultySeatsSequence,
                                                 Luggage, 
                                                 DATA_SEATS
                                                 )

    queueAllPassengers(total_passengers,
                       SeatsSequence,
                       FaultySeatsSequence,
                       Luggage,
                       DATA_SEATS,
                       DATA_ROWS,
                       DATA_PASSENGERS
    )    

    with open('data/DATA_SEATS.json', 'w', encoding='utf-8') as f:
        json.dump(DATA_SEATS, f, ensure_ascii=False, indent=4)
    with open('data/DATA_ROWS.json', 'w', encoding='utf-8') as f:
        json.dump(DATA_ROWS, f, ensure_ascii=False, indent=4)
    with open('data/DATA_PASSENGERS.json', 'w', encoding='utf-8') as f:
        json.dump(DATA_PASSENGERS, f, ensure_ascii=False, indent=4)
        
    return DATA_PASSENGERS

if __name__ == '__main__':
    total_seats: int = 132
    wrong_seats_percentage: float = 0.05
    type_: str = "random"
    blocks: str = ""
    pattern: str = ""
    load = "normal" # "normal" or "high"
    wrong_seats_distance: int = 132

    DATA_PASSENGERS = main(total_seats,wrong_seats_percentage,type_,blocks,pattern,load,wrong_seats_distance)

    with open('data/DATA_PASSENGERS.json', 'w', encoding='utf-8') as f:
        json.dump(DATA_PASSENGERS, f, ensure_ascii=False, indent=4)

    print("Data saved")