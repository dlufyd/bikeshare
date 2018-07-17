import time
import pandas as pd
import numpy as np
import json


CITY_DATA = { 'chicago': 'chicago.csv',
              'newyork': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    print('Name of the city to analyze? chicago/newyork/washington')
    city = input()
    while True:
        if city in ('chicago','newyork','washington'):
            break
        else:
            print('Name of the city to analyze? chicago/newyork/washington')
            city = input()
            
    # TO DO: get user input for month (all, january, february, ... , june)
    print('Name of the month to filter by, or "all" to apply no month filter? 1..6/all')
    month = input()
    while True:
        if month in ('1','01','2','02','3','03','4','04','5','05','6','06','all'):
            break
        else:
            print('Name of the month must be one of 1..6/all')
            month = input()
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    print('Name of the day of week to filter by, or "all" to apply no day filter? monday/tuesday/wednesday/thursday/friday/saturday/sunday/all')
    day = input()
    while True:
        if day in ('monday','tuesday','wednesday','thursday','friday','saturday','sunday','all'):
            break
        else:
            print('Name of the day must be one of monday/tuesday/wednesday/thursday/friday/saturday/sunday/all')
            day = input()

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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':
        df = df[df['month'] == int(month)]
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('Most common Month : {}'.format(df['month'].mode()[0]))

    # TO DO: display the most common day of week
    print('Most common day of week : {}'.format(df['day_of_week'].mode()[0]))

    # TO DO: display the most common start hour
    print('Most common start hour : {}'.format(df['hour'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))

    print('-'*40)
    input()

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    
    # TO DO: display most commonly used start station
    most_used_start_station = df['Start Station'].mode()[0]
    print('Most commonly used start station : {} -- count : {}'.format(most_used_start_station, len(df[df['Start Station']==most_used_start_station])))
 
    # TO DO: display most commonly used end station
    most_used_end_station = df['End Station'].mode()[0]
    print('Most commonly used end station : {} -- count : {}'.format(most_used_end_station, len(df[df['End Station']==most_used_end_station])))

    # TO DO: display most frequent combination of start station and end station trip
    df['Start End Station'] = df['Start Station'] + "---" + df['End Station']
    most_used_start_end_station =  df['Start End Station'].mode()[0]
    print('Most frequent combination of start station and end station : {} -- count : {}'.format(most_used_start_end_station, len(df[df['Start End Station']==most_used_start_end_station])))
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    input()


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("Total travel time : {}".format(df['Trip Duration'].sum()))

    # TO DO: display mean travel time
    print("Mean travel time : {}".format(df['Trip Duration'].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    input()

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('\n\nDisplaying counts of user types')
    print(df['User Type'].value_counts())

    # TO DO: Display counts of gender
    # Checking for Gender Column for Washington
    if 'Gender' in df.columns: 
        print('\n\nDisplaying counts of gender')
        print(df['Gender'].value_counts())
    if 'Birth Year' in df.columns: 
        # TO DO: Display earliest, most recent, and most common year of birth
        print("The most common birth year:", df['Birth Year'].mode()[0])
        print("The most recent birth year:", df['Birth Year'].max())
        print("The most earliest birth year:", df['Birth Year'].min())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    input()

def display_data(df):    
    row_count = df.shape[0]

    for i in range(0, row_count, 5):
        print('Would you like to see the particular user trip data? yes/no')
        detail_data = input()
        if detail_data.lower() != 'yes':
            break
        rows = df.iloc[i: i + 5].to_json(orient="records").split('\n')
        for row in rows:
            print(json.dumps(json.loads(row), indent=5))
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
