import time
import random as r
import util.pseudorand as p

NUM = 10000000

start_time = time.time()
for i in range(NUM):
    r.random()
end_time = time.time()
print(f'Native random: {start_time} - {end_time} : {start_time-end_time}')

start_time = time.time()
for i in range(NUM):
    p.random()
end_time = time.time()
print(f'New random: {start_time} - {end_time} : {start_time-end_time}')
