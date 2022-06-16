import time


time_to_wait = time.strftime('%S-%M-%H').split('-')
current_time = time.strftime('%S-%M-%H').split('-')

for i in range(len(time_to_wait)):
    time_to_wait[i] = int(time_to_wait[i])

for i in range(len(current_time)):
    current_time[i] = int(current_time[i])

last = time_to_wait[0]
time_to_wait[0] = time_to_wait[0] + 40
if time_to_wait[0] > 59:
    time_to_wait[0] = last + 40 - 60
    time_to_wait[1] += 1

while True:
    current_time = time.strftime('%S-%M-%H').split('-')
    for i in range(len(current_time)):
        current_time[i] = int(current_time[i])
    print(current_time)
    print(time_to_wait)
    print('\n')
    if current_time == time_to_wait:
        print('fuck it')
        break