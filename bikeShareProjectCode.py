import time
import pandas as pd
import numpy as np

#Dictionary for city data.
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

    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = ""
    cities = ("chicago","new york city","washington")
    while city not in cities:
        city = input('Which city information would you like to view? - chicago, new york city or washington:\n').lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    month = ""
    months =    ("all","january","february","march","april","may","june")
    while month not in months:
        month = input('Please include a month for this data - january to june or all to include every month:\n').lower()

    day=""
    days =("all","sunday","monday","tuesday","wednesday","thursday","friday","saturday")
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while day not in days:
        day = input('Any specific day - monday to sunday or all to include everyday:\n').lower()

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

    # TO DO: display the most common month

   # return popular_month
    popular_month= df['month'].mode()[0]
    print("popular_month:",popular_month)

    # TO DO: display the most common day of week
    popular_day= df['day_of_week'].mode()[0]

    # TO DO: display the most common start hour
    df['hour']=df['Start Time'].dt.hour
    popular_hour= df['hour'].mode()[0]
    print("popular_hour:",popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station= df['Start Station'].mode()[0]

    print("popular_start_station",popular_start_station)

    # TO DO: display most commonly used end station
    popular_end_station= df['End Station'].mode()[0]

    print("popular_end_station",popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['combination'] =df['Start Station'] + " TO " + df['End Station']
    popularCombination = df['combination'].mode()[0]
    print("combined destination",popularCombination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    trip_duration = df['Trip Duration'].sum()
    #trip_duration_hr = str(int(trip_duration/3600)) + "hr"+
    print ("trip_duration",trip_duration)
    # TO DO: display mean travel time
    mean_duration = df['Trip Duration'].mean()
    print ("mean_duration",mean_duration)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()

    print(user_types)

    # TO DO: Display counts of gender
    try:
        user_gender = df['Gender'].value_counts()
        print(user_gender)
    except:
        print("Gender info not available for Washington")

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_birth = df['Birth Year'].min()
        print ('earliest_birth:',earliest_birth)

        most_recent_birth =df['Birth Year'].max()
        print ('most_recent_birth:',most_recent_birth)

        most_common_birth =df['Birth Year'].mode()[0]
        print ('most_common_birth:',most_common_birth)

    except:
        print('Age data not present for Washington')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    rawData = input("Would you like to see raw data? Enter yes or no:\n").lower()
    if rawData == "yes":
        print(df.iloc[:5])
        rawLocation = 5
        while input("Would you like to see more raw data? Enter yes Or no:\n").lower() != "no":
            print(df.iloc[rawLocation:rawLocation+5])
            rawLocation+=5

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        cont = input('press enter to continue')
        station_stats(df)
        cont = input('press enter to continue')
        trip_duration_stats(df)
        cont = input('press enter to continue')
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
