import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    
    print('Hello! Let\'s explore some US bikeshare data!')
    
    city = input('\nWould you like to see data for chicago, new york city, or washington?\n').lower()
    while city != 'chicago' and city != 'new york city' and city != 'washington':
        print('Oops! looks like we don\'t have data for the city you\'re interested in! please try again!')
        city = input('\nWould you like to see data for chicago, new york city, or washington?\n').lower()
        
    
   
    month = input('\nPlease select a month between january and june, or type "all" to see data for the six months\n').lower()
    while month != 'all' and month != 'january' and month != 'february' and month != 'march' and month != 'april' and month != 'may' and month != 'june':
        print('Oops! choice not available, please try again!')
        month = input('\nPlease select a month between january and june, or type "all" to see data for the six months\n').lower()
            
   
    day = input('\nPlease select a day, or type "all"\n').lower()
    while day != 'all' and day != 'monday' and day != 'tuesday' and day != 'wednesday' and day != 'thursday' and day != 'friday' and day != 'saturday' and day != 'sunday':
        print('Oops! choice not available, please try again!')
        day = input('\nPlease select a day, or type "all"\n').lower()
        
    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    
    
    df = pd.read_csv(CITY_DATA[city])

    
    df['Start Time'] = pd.to_datetime(df['Start Time'])

   
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

   
    if month != 'all':
       
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        
        df = df[df['month'] == month]

   
    if day != 'all':
        
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
   

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

   
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]
    print('Most common month:', popular_month)
                       

   
    df['Start Time'] = pd.to_datetime(df['Start Time'], format ='%d-%m-%y')
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    popular_day = df['day_of_week'].mode()[0]
    print('Most common day of the week:', str(popular_day))

   
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most common start hour:', popular_hour)



    print("\nThis took %s seconds." % round((time.time() - start_time)))
    print('-'*40)


def station_stats(df):
   
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

   
    popular_start = df['Start Station'].mode()[0]
    print('Most commonly used start station:', popular_start)

    
    popular_end = df['End Station'].mode()[0]
    print('Most commonly used end station:', popular_end)

    
    popular_trip = df.groupby(['Start Station', 'End Station']).size().idxmax()
    print('Most common trip:', popular_trip)


    print("\nThis took %s seconds." % round((time.time() - start_time)))
    print('-'*40)
        
def trip_duration_stats(df):
   
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

   
    total_time = df['Trip Duration'].sum()
    print('Total travel time:', total_time, 'seconds')


   
    mean_time = df['Trip Duration'].mean()
    print('Mean travel time:', mean_time, 'seconds')


    print("\nThis took %s seconds." % round((time.time() - start_time)))
    print('-'*40)

def user_stats(df):
   

    print('\nCalculating User Stats...\n')
    start_time = time.time()

   
    user_types = df['User Type'].value_counts()
    print(user_types)

   
    if 'Gender' not in df:
        pass
    else:
        gender_count = df['Gender'].value_counts()
        print(gender_count)

   
    if 'Birth Year' not in df:
        pass
    else:
        earliest_year = int(df['Birth Year'].min())
        latest_year = int(df['Birth Year'].max())
        common_year = int(df['Birth Year'].mode()[0])
        print('\nEarliest birth year:', earliest_year)
        print('\nMost recent birth year:', latest_year)
        print('Most common year of birth:', common_year)

    print("\nThis took %s seconds." % round((time.time() - start_time)))
    print('-'*40)

def display_raw_data(df):
   
    
    i = 0
    raw = input('\nWould you like to see any raw data? Please enter yes or no.\n').lower()
    pd.set_option('display.max_columns', 15)
    
    while True:
        if raw == 'no':
            break
        elif raw == 'yes':
            if i > df.shape[0]:
                print('No more data to display.')
                break
            else:           
                print(df.iloc[i:i+5, :])
                
            
            raw = input('\nWould you like to see 5 more rows of data? Please enter yes or no.\n').lower()
            i += 5
        else:
            raw = input('\nYour input is invalid. Please enter only yes or no.\n').lower()

    print('-'*40)
    
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
       


if __name__ == "__main__":
	main()
    