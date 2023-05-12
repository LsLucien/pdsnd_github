import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': '../data/chicago.csv',
              'new york city': '../data/new_york_city.csv',
              'washington': '../data/washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('Enter the city you want see data for Chicago , New York City or Washington : ')
    city = city.casefold()
    while city not in CITY_DATA:
        city = input('Invalid city name， please input again:')
        city = city.casefold()

    # get user input for month (all, january, february, ... , june)
    months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    month = input('Enter the month from January to June OR Enter "all" for no month filter : ')
    month = month.casefold()
    while month not in months:
        month = input('Invalid month name, please input again:')
        month = month.casefold()

    # get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    day = input('Enter the day from Monday to Sunday OR Enter "all" for no day filter : ')
    day = day.casefold()
    while day not in days:
        day = input('Invalid day name, please input again:')
        day = day.casefold()

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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    months = ['January', 'February', 'March', 'April', 'May', 'June']
    print('Most common day of month is: {}'.format(months[df['month'].mode()[0]-1]))

    # display the most common day of week
    print('Most common day of week is: {}'.format(df['day_of_week'].mode()[0]))
    
    # display the most common start hour
    print('Most common day of start hour is: {}\n'.format(df['hour'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('Most commonly used start station is: {}'.format(df['Start Station'].mode()[0]))

    # display most commonly used end station
    print('Most commonly used end station is: {}'.format(df['End Station'].mode()[0]))

    # display most frequent combination of start station and end station trip
    print('Most frequent combination of trip is: \n{}\n'.format(df.groupby(['Start Station', 'End Station']).size().nlargest(1)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print('Total trip time is: {}'.format(df['Trip Duration'].sum()))

    # display mean travel time
    print('Mean trip time is: {}\n'.format(df['Trip Duration'].mean()))  

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    if 'User Type' in df.columns:
        print('Counts of user types is: \n{}\n'.format(df['User Type'].value_counts()))

    # Display counts of gender
    if 'Gender' in df.columns:
        print('Counts of user types is: \n{}\n'.format(df['Gender'].value_counts()))

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print('Earliest year of Birth: {}'.format(df['Birth Year'].min()))
        print('Most Recent year of Birth: {}'.format(df['Birth Year'].max()))
        print('Most Common year of Birth: {}\n'.format(df['Birth Year'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    """Display raw data by request from user"""
    
    answers = ['yes', 'no']
    user_answer = input('Do you want to see the first 5 rows of data? (Yes/No)\n')
    
    while user_answer.casefold() not in answers:
        user_answer = input('Please input Yes or No:\n')
        user_answer = user_answer.casefold()
        
    row_number = 0
    df_size = df.shape[0]
    
    while user_answer == 'yes':
        if df_size < row_number+5:
            print(df.iloc[row_number : df_size])
            print('\n That is all of the data.\n')
            break
        else:
            print(df.iloc[row_number : row_number+5])
            row_number += 5
            user_answer = input('\nDo you want to see the next 5 rows of raw data? (Yes/No)\n')
            while user_answer.casefold() not in answers:
                user_answer = input('Please input Yes or No:\n')
                user_answer = user_input.casefold()            

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
