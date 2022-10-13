from datetime import datetime,date

# Get the current day, month, year, hour, minute and timestamp from datetime module

hoy = datetime.now()
print(f'dia: {hoy.day}\nmes: {hoy.month}\naño: {hoy.year}\nhora: {hoy.hour}\nminuto: {hoy.minute}\nsegundo: {hoy.second}\ntimestamp: {hoy.timestamp()}\n')

# Format the current date using this format: "%m/%d/%Y, %H:%M:%S")

print(f'{hoy.strftime("%m/%d/%Y, %H:%M:%S")}')

# Today is 5 December, 2019. Change this time string to time.

a = "5 December 2019"
print(f'{datetime.strptime(a,"%d %B %Y")}')

# Calculate the time difference between now and new year.

print(f'la diferencia entre hoy y año nuevo es: {(datetime(year = 2023,month = 1,day = 1)-hoy)}')

# Calculate the time difference between 1 January 1970 and now.

print(hoy.timestamp())

# Think, what can you use the datetime module for? Examples:

'''pues para saber el tiempo entre acciones de los usuarios'''

    # Time series analysis



    # To get a timestamp of any activities in an application



    # Adding posts on a blog


