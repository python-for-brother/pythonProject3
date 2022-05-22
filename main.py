print("Enter time in seconds")
duration = int(input())
print('You set ' + str(duration) + ' seconds')
time_ = [' sec ', ' min ', ' hours ', ' days ']
time = [duration, 0, 0, 0]
if time[0] >= 60:
    time[1] = int(time[0] / 60)
    time[0] = time[0] % 60
if time[1] >= 60:
    time[2] = int(time[1] / 60)
    time[1] = time[1] % 60
if time[2] >= 24:
    time[3] = int(time[2] / 24)
    time[2] = time[2] % 24
for i in reversed(range(0, 4)):
    print(str(time[i]) + time_[i], end='')
