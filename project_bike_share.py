#change in the file to the third project of udacity (git)
import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
city = ''
while True:
 city = input('Hello, Dear! Let\'s explore some US bikeshare data! \n Would you like to see data for Chicago, New York City, or Washington?\n').lower()
 if city not in ('chicago', 'new york city', 'washington'):
  print('Incorrect city. Please try again!\n')
elif city.lower() == 'chicago':
    return 'chicago.csv'
elif city.lower() == 'new york':
    return 'new_york_city.csv'
elif city.lower() == 'washington':
    return 'washington.csv'


    # TO DO: get user input for month (all, january, february, ... , june)

    def get_time_period():
        '''Asks the user for a time period and returns the specified filter.
        Args:
            none.
        Returns:
            (str) Time filter for the bikeshare data.
        '''
        time_period = ''
        while time_period.lower() not in ['month', 'day', 'all']:
            time_period = input('\nWould you like to filter the data by month, day,'
                                ' or all? Type "all" for no time filter.\n')
            if time_period.lower() not in ['month', 'day', 'all']:
                print('Sorry, I do not understand your input.')
        return time_period

    def get_month():
        '''Asks the user for a month and returns the specified month.
            Returns:
            (tuple) Lower limit, upper limit of month for the bikeshare data.
        '''
        month_input = ''
        months_tuple = ('january', 'february', 'march', 'april', 'may', 'june')
        while month_input.lower() not in months_tuple.keys():
            month_input = input('\nWhich month do you like to filter? January, February, March, April,'
                                ' May, or June?\n')
            if month_input.lower() not in months_tuple.keys():
                print('Sorry, I do not understand your input. Try again - choose between January and June')
        month = months_tuple[month_input.lower()]
        return ('2017-()'.format(month), '2017-()'.format(month + 1))



#return ('Which month would you like to filter? january, february, march, april, may, june or all?')
#if month != 'all':
#        months = ['january', 'february', 'march', 'april', 'may', 'june']
#        month = months.index(month) + 1
#        df = df[df['month'] == month]
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    def get_day():
        '''Asks the user for a day and returns the specified day.
        Args:
            none.
        Returns:
            (tuple) Lower limit, upper limit of date for the bikeshare data.
        '''
        this_month = get_month()[0]
        month = int(this_month[5:])
        valid_date = False
        while valid_date == False:
            is_int = False
            day = input('\nWhich day? Please type your response as an integer.\n')
            while is_int == False:
                try:
                    day = int(day)
                    is_int = True
                except ValueError:
                    print('Sorry, I do not understand your input. Please type your'
                          ' response as an integer.')
                    day = input('\nWhich day? Please type your response as an integer.\n')
            try:
                start_date = datetime(2017, month, day)
                valid_date = True
            except ValueError as e:
                print(str(e).capitalize())
        end_date = start_date + timedelta(days=1)
        return (str(start_date), str(end_date))




print('Which day of week? Su, M, Tu, W, Th, F or Sa?')
if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month

def popular_month(df):
    '''Finds and prints the most popular month for start time. '''
    months = ['January', 'February', 'March', 'April', 'May', 'June']
    index = int(df['start_time'].dt.month.mode())
    most_pop_month = months[index - 1]
    print('The most popular month is {}.'.format(most_pop_month))

    # TO DO: display the most common day of week
def popular_day(df):
    '''Finds and prints the most popular day of week (Monday, Tuesday, etc.) for start time.'''
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
                    'Saturday', 'Sunday']
    index = int(df['start_time'].dt.dayofweek.mode())
    most_pop_day = days_of_week[index]
    print('The most popular day of week for start time is {}.'.format(most_pop_day))

    # TO DO: display the most common start hour

def popular_hour(df):
    '''Finds and prints the most popular hour of day for start time. '''
    most_pop_hour = int(df['start_time'].dt.hour.mode())
    if most_pop_hour == 0:
        am_pm = 'am'
        pop_hour_readable = 12
    elif 1 <= most_pop_hour < 13:
        am_pm = 'am'
        pop_hour_readable = most_pop_hour
    elif 13 <= most_pop_hour < 24:
        am_pm = 'pm'
        pop_hour_readable = most_pop_hour - 12
    print('The most popular start hour is {}{}.'.format(pop_hour_readable, am_pm))



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
def popular_stations(df):
    '''Finds and prints the most popular start station and most popular end station.'''
    pop_start = df['start_station'].mode().to_string(index = False)
    pop_end = df['end_station'].mode().to_string(index = False)
    print('The most popular start station is {}.'.format(pop_start))
    # TO DO: display most commonly used end station
    print('The most popular end station is {}.'.format(pop_end))

    # TO DO: display most frequent combination of start station and end station trip

def popular_trip(df):
    '''Finds and prints the most popular trip. '''
    most_pop_trip = df['journey'].mode().to_string(index = False)
    print('The most popular trip is {}.'.format(most_pop_trip))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    #start_time = time.time()

total_duration = df['trip_duration'].sum()
minute, second = divmod(total_duration, 60)
hour, minute = divmod(minute, 60)
print('The total trip duration is {} hours, {} minutes and {}'
      ' seconds.'.format(hour, minute, second))
average_duration = round(df['trip_duration'].mean())
m, s = divmod(average_duration, 60)
if m > 60:
    h, m = divmod(m, 60)
    # TO DO: display total travel time
    print('The average trip duration is {} hours, {} minutes and {}'
          ' seconds.'.format(h, m, s))
else:
    # TO DO: display mean travel time
    print('The average trip duration is {} minutes and {} seconds.'.format(m, s))







    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
#    start_time = time.time()

    # TO DO: Display counts of user types
    subs = df.query('user_type == "Subscriber"').user_type.count()
    cust = df.query('user_type == "Customer"').user_type.count()
    print('There are {} Subscribers and {} Customers.'.format(subs, cust))


    # TO DO: Display counts of gender
    male_count = df.query('gender == "Male"').gender.count()
    female_count = df.query('gender == "Male"').gender.count()
    print('There are {} male users and {} female users.'.format(male_count, female_count))


    # TO DO: Display earliest, most recent, and most common year of birth
    earliest = int(df['birth_year'].min())
    latest = int(df['birth_year'].max())
    mode = int(df['birth_year'].mode())
    print('The oldest users are born in {}.\nThe youngest users are born in {}.'
          '\nThe most popular birth year is {}.'.format(earliest, latest, mode))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
