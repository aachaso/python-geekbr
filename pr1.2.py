time_user = int(input('Enter time in seconds - '))

h = int(time_user / 3600)
m = int(time_user / 60 - (h * 60))
s = int(time_user - (h * 3600) - (m * 60))
print(f'Time {h}:{m}:{s}')
