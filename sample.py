import numpy as np
import math

def sampleArrivalTime(lam:float) -> float:
  # alle 6 Sekunden Arrival Time im Durchschnitt
  u = np.random.rand()
  sample = -(math.log(u)) / (lam) 
  return sample

def samplePassingOneRow() -> float:

  sample = np.random.triangular(1.8,2.4,3)
  return sample

def sampleInstallSeat() -> float:
  sample = np.random.triangular(6,9,30)
  return sample

def sampleExitSeat() -> float:
  sample = np.random.triangular(3,3.6,4.2)
  return sample

def sampleLuggageAmount(condition: str) -> int:
  u = np.random.uniform()
  if condition == "normal": # normal luggage distribution
    if u < 0.6: # 60% - 1
      amount = 1
    elif u > 0.9: # 10% - 3
      amount = 3
    else: # 30% - 2
      amount  =2

  elif condition == "high": # high luggagge distribution
    if u < 0.2: # 20% - 1
      amount = 1
    elif u > 0.8: # 20% - 3
      amount = 3
    else: # 60% - 2
      amount  =2

  return amount