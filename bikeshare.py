import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters(city, month, day):
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while 1:
        city = input("Enter a city(Chicago, New York, Washington): ").lower()
        if city not in CITY_DATA:
            print("\nInvalid City! Please enter a valid city.\n")
            continue
        else:
            break

    while 1:
        time = input("Please choose a filtering method as month, day, both or none: ").lower()
        if time == 'month':
            month = input("Please enter a month(January, Feburary, March, April, May or June): ").lower()
            day = 'all'
            break

        elif time == 'day':
            month = 'all'
            day = input("Please enter a day(Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or Sunday): ").lower()
            break

        elif time == 'both':
            month = input("Please enter a month(January, Feburary, March, April, May or June): ").lower()
            day = input("Please enter a day(Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or Sunday): ").lower()
            break
        elif time == 'none':
            month = 'all'
            day = 'all'
            break
        else:
            input("Invalid Entry! Please choose a filtering method as month, day, both or none: ")
            break

    print(city)
    print(month)
    print(day)
    # print('-'*40)
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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) +1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df['month'].mode()[0]
    print(common_month)

    # display the most common day of week
    common_day_of_week = df['day_of_week'].mode()[0]
    print(common_day_of_week)

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print(common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print(common_start_station)

    # display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print(common_end_station)

    # display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station'] + ' to ' + df['End Station']
    common_combination = df['combination'].mode()[0]
    print(common_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print(total_travel_time)

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print(mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    # Display counts of gender
    if 'Gender' in df:
        gender = df['Gender'].value_counts()
        print(gender)
    else:
        print("There is no gender information in this city.")

    # Display earliest, most recent, and most common year of birth
    if 'Birth_Year' in df:
        earliest = df['Birth_Year'].min()
        print(earliest)
        recent = df['Birth_Year'].max()
        print(recent)
        common_birth = df['Birth_Year'].mode()[0]
        print(common_birth)
    else:
        print("There is no year of birth data for this city.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

'''Five lines of the raw data and more if it is required'''

def data(df):
    raw_data = 0
    while 1:
        answer = input("Would like to see raw data?(Y/N): ").lower()
        if answer not in ['y', 'n']:
            answer = input("Invalid Entry! Please try again(Y/N): ").lower()
        elif answer == 'y':
            raw_data += 5
            print(df.iloc[raw_data : raw_data + 5])
            repeat = input("Would you like to see more data?(Y/N): ").lower()
            if repeat == 'n':
                break
        elif answer == 'n':
            return

def main():
    city = ""
    month = ""
    day = ""
    while 1:
        city, month, day = get_filters(city, month, day)
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        data(df)

        restart = input("Would you like to restart?(Y/N): ")
        if restart.lower() != 'y':
            break

if __name__ == "__main__":
	main()
