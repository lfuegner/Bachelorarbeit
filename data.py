from main import main
import json
import statistics
import scipy.stats as st

### Inputparameter ###
total_seats: int = 132
wrong_seats_percentage: float = 0 # Options: [0,1] Intervall
load_: str ="normal" # Options: "normal" or "high"
wrong_seats_distance: int = total_seats # Options: [1,132], has to be an Integer, wrongs_seats_distance has to be greater or equal 1 and lower or equal to total_seats here 132, 

### Data Script ###
data_analysis = {}
f = open("sequence.txt").read()
lines = f.split("\n")
for line in lines:
  name, rest = line.split(":")
  type_, blocks, pattern = rest.split(",")
  print(name)
  #print(type_,blocks,pattern)
  
  total_boarding_times = []
  average_individual_boarding_times = []
  maximum_individual_boarding_times = []
  for i in range(20):
    end_timestamps = []
    individual_boarding_times = []
    
    data = main(total_seats = total_seats,
                wrong_seats_percentage = wrong_seats_percentage, 
                type_ = type_.strip(),
                blocks = blocks.strip(),
                pattern = pattern.strip(),
                load= load_,
                distance= wrong_seats_distance)
    for passenger in data:
        
      end_timestamps.append(data[passenger]["end_timestamps"][len(data[passenger]["end_timestamps"])-1])
      individual_boarding_times.append(data[passenger]["end_timestamps"][0] - data[passenger]["start_timestamp"]) #len(data[passenger]["end_timestamps"])-1

    total_boarding_times.append(max(end_timestamps))
    average_individual_boarding_times.append(statistics.mean(individual_boarding_times))
    maximum_individual_boarding_times.append(max(individual_boarding_times))

  total_boarding_time_mean = statistics.mean(total_boarding_times)
  total_boarding_time_sd = statistics.stdev(total_boarding_times)
  total_boarding_time_ci = st.t.interval(0.90, df=len(total_boarding_times)-1, loc=total_boarding_time_mean, scale=st.sem(total_boarding_times)) 

  average_individual_boarding_time_mean = statistics.mean(average_individual_boarding_times)
  average_individual_boarding_time_sd = statistics.stdev(average_individual_boarding_times)
  average_individual_boarding_time_ci = st.t.interval(0.90, df=len(average_individual_boarding_times)-1, loc=average_individual_boarding_time_mean, scale=st.sem(average_individual_boarding_times)) 

  maximum_individual_boarding_time_mean = statistics.mean(maximum_individual_boarding_times)
  maximum_individual_boarding_time_sd = statistics.stdev(maximum_individual_boarding_times)
  maximum_individual_boarding_time_ci = st.t.interval(0.90, df=len(maximum_individual_boarding_times)-1, loc=maximum_individual_boarding_time_mean, scale=st.sem(maximum_individual_boarding_times)) 

  data_analysis[name] = {"type": type_,
                        "blocks": blocks,
                        "pattern": pattern,
                        "total_boarding_time_mean":total_boarding_time_mean,
                        "total_boarding_time_sd": total_boarding_time_sd,
                        "total_boarding_time_ci": total_boarding_time_ci,

                        "average_individual_boarding_time_mean": average_individual_boarding_time_mean,
                        "average_individual_boarding_time_sd": average_individual_boarding_time_sd,
                        "average_individual_boarding_time_ci": average_individual_boarding_time_ci,

                        "maximum_individual_boarding_time_mean":maximum_individual_boarding_time_mean,
                        "maximum_individual_boarding_time_sd": maximum_individual_boarding_time_sd,
                        "maximum_individual_boarding_time_ci":maximum_individual_boarding_time_ci}

with open(f'data/data_analysis-{load_}.json', 'w', encoding='utf-8') as f:
        json.dump(data_analysis, f, ensure_ascii=False, indent=4)

print(f"Data saved")
