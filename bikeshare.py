#!python3.10

import pandas as pd
import numpy as np
<<<<<<< HEAD
=======
from tabulate import tabulate
>>>>>>> refactoring
import time

import re

CITY_DATA = {'chicago': 'chicago.csv',
             'newyorkcity': 'new_york_city.csv',
             'washington': 'washington.csv'}
MONTHS = ['january', 'february', 'march', 'april', 'may', 'june']
WEEK_DAYS = ['monday', 'tuesday', 'wednesday',
             'thursday', 'friday', 'saturday', 'sunday']


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!\n')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city_input = input('Please enter the name of the city: ')
    # Removing all spaces the input and converting to lower case.
    test_city = city_input.replace(" ", "").lower()
    while test_city not in CITY_DATA.keys():
        print('The city you have selected does not match any of Washington, New York City or Chicago.\n')
        print('Please make sure your choice does not contain spelling errors or any other characters\n')
        new_city_input = input('Please enter the name of the city: ')
        test_city = new_city_input.replace(" ", "").lower()

    city = test_city

    print('Do you wish to filter the data by month, day of the week or not at all?\n')
    print('Type in the word \'month\' to fiter the data by month.\nType in the word \'day\' to fiter the data by day.\nType in the word \'all\' for unfiltered data.\n(All without quotation marks.)')
    # Receive input from user.
    user_choice = input('Enter your option: ')
    # Removing all spaces in user's choice and converting the result to lower case.
    testing_choices = user_choice.replace(" ", "").lower()
    # Testing if the user choice is one of the three valid choices.
    while testing_choices not in ('month', 'day', 'all'):
        print('You have entered an invalid option.')
        print('Please type in the word \'month\' to fiter the data by month,\'day\' \
            to fiter the data by day or \'all\' for unfiltered data.\n(All without quotation marks.)')
        user_choice_again = input('Please enter a valid option: ')
        testing_choices = user_choice_again.replace(" ", "").lower()

    if testing_choices == 'all':
        month, day = 'all', 'all'

    elif testing_choices == 'month':
        # Receive month of choice from user.
        month_choice = input(
            'Enter a month between January and June for which you wish to view that data.\n')
        # Remove spaces and convert month to lower case
        month_name = month_choice.replace(" ", "").lower()
        # Testing if the month chosen is valid.
        while month_name not in MONTHS:
            print('You have entered an invalid month.')
            month_choice_again = input('Please enter a valid month: ')
            month_name = month_choice_again.replace(" ", "").lower()
        month = month_name
        month, day = month, 'all'

    elif testing_choices == 'day':
        day_choice = input(
            'Enter the day of the week for which you wish to view that data: ')
        # Remove spaces and convert month to lower case
        day_name = day_choice.replace(" ", "").lower()
        while day_name not in WEEK_DAYS:
            print('You have entered an invalid day.')
            day_choice_again = input('Please enter a valid day: ')
            day_name = day_choice_again.replace(" ", "").lower()
        day = day_name
        month, day = 'all', day

    print('-'*80)
    return city, month, day


"""
The reviewer has suggested that this get_filters() definition can be written
in fewer lines to avoid repetition. Hence at some point in future I will do
some refactoring to improve this definition.
"""


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - pandas DataFrame containing city data filtered by month and day
    """
    filename = CITY_DATA[city]
    # load data file into a dataframe

    df = pd.read_csv(filename)
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    if month == 'all' and day == 'all':
        df

    if month != 'all' and day == 'all':
        df['month'] = df['Start Time'].dt.month
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if month == 'all' and day != 'all':
        df['day_of_week'] = df['Start Time'].dt.dayofweek
        days = ['monday', 'tuesday', 'wednesday',
                'thursday', 'friday', 'saturday', 'sunday']
        day = days.index(day)
        df = df[df['day_of_week'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    months = ['January', 'February', 'March', 'April', 'May', 'June']
    df['month'] = df['Start Time'].dt.month
    month = df['month'].mode()[0]
    popular_month = months[month-1]
    print(f'The most popular month is {popular_month}.')
    # display the most common day of week
    days = ['Monday', 'Tuesday', 'Wednesday',
            'Thursday', 'Friday', 'Saturday', 'Sunday']
    df['day'] = df['Start Time'].dt.dayofweek
    day = df['day'].mode()[0]
    popular_day = days[day]
    print(f'The most popular day of the week is {popular_day}.')

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print(f'The most popular start hour is {popular_hour}00hrs.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*80)


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    months = ['January', 'February', 'March', 'April', 'May', 'June']
    df['month'] = df['Start Time'].dt.month
    month = df['month'].mode()[0]
    popular_month = months[month-1]
    print(f'The most popular month is {popular_month}.')
    # display the most common day of week
    days = ['Monday', 'Tuesday', 'Wednesday',
            'Thursday', 'Friday', 'Saturday', 'Sunday']
    df['day'] = df['Start Time'].dt.dayofweek
    day = df['day'].mode()[0]
    popular_day = days[day]
    print(f'The most popular day of the week is {popular_day}.')

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    if popular_hour <= 9:
        print(f'The most popular starting hour is 0{popular_hour}00hrs.')
    else:
        print(f'The most popular starting hour is {popular_hour}00hrs.')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*80)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    start_station = df['Start Station'].mode()[0]
    print(f'Most trips start at the station on {start_station}.')
    # display most commonly used end station
    end_station = df['End Station'].mode()[0]
    print(f'Most trips end at the station on {end_station}.')

    # display most frequent combination of start station and end station trip
    start_and_end_combination = df.groupby(
        ['Start Station', 'End Station']).size().idxmax()
    print(
        f'The most frequently travelled route starts at the station on {start_and_end_combination[0]}\nand end at the station on {start_and_end_combination[1]}.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*80)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_time = df['Trip Duration'].sum()
    print(f'The total travel time is {total_time} seconds.')

    # display mean travel time
    mean_time = df['Trip Duration'].mean()
    print(f'The mean travel time is {mean_time} seconds.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*80)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    # Remove name, dtype from the user_types pandas series
    user_types = user_types.to_string(index=True)
    print(
        f'The breakdown of bike users by user type is as follows:\n{user_types}\n')

    try:
        # Display counts of gender
        user_gender = df['Gender'].value_counts()
        # Remove name, dtype from the user_types pandas series
        user_gender = user_gender.to_string(index=True)
        print(
            f'The breakdown of bike users by gender is as follows:\n{user_gender}\n')
        earliest_birth_year = df['Birth Year'].min()
        latest_birth_year = df['Birth Year'].max()
        most_common_birth_year = df['Birth Year'].mode()[0]
        print(f'The earliest birth year is {int(earliest_birth_year)}.')
        print(f'The latest birth year is {int(latest_birth_year)}.')
        print(f'The most common birth year is {int(most_common_birth_year)}.')
    except KeyError:
        print('There is no gender or birth year data for Washington DC.')
    finally:
        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*80)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        # Capitalizing the name of city and inserting spaces in case of New York City
        city1 = re.sub("newyorkcity", "new york city", city).title()
        """
        The reviewer suggested that I should add the following line of code to avoid 
        column getting collapsed when displayed in terminal.
        """
        pd.set_option('display.max_columns', 200)

        print(
            f'\nDo you wish to view the first 5 rows of the unfiltered {city1} dataframe?.\n')
        request_for_raw_data = input('Enter yes or no: ')
        request_for_raw_data = request_for_raw_data.replace(" ", "").lower()
        i = 0
        Dataframe_of_five_rows = load_data(city, 'all', 'all')
        """ 
        The following lines of code will have also been suggested by the reviewer.
        This introduces pretty printing and makes the displayed results easier to read.
        """
        while True:
            display_data = input(
                '\nWould you like to see 5 lines of raw data? Enter yes or no.\n')
            if display_data.lower() != 'yes':
                break
            print(
                tabulate(Dataframe_of_five_rows.iloc[np.arange(0+i, 5+i)], headers="keys"))
            i += 5
        print('-'*160)
        print(f'\nHere are some statistics for {city1}.')
        print('-'*80)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        print('-'*160)
        print(f'\nHere are some statistics for {city1}.')
        print('-'*80)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
