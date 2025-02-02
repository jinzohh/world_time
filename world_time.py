#!/usr/bin/env python
# coding: utf-8

# In[56]:


# A simple program that will output the time of the country based on user input.

def world_time(t, tz_fr, tz_to):
    # This function caculates the destination time from user input.
    # Initializing list of timezones and time differences as compared to UTC.
    timezone_diff = [
        ('hawaii', 10),
        ('alaska', 9),
        ('pst', 8),
        ('mst', 7),
        ('cst', 6),
        ('est', 5),
        ('brazil', 3),
        ('gmt', 0),
        ('cet', -1),
        ('eet', -2),
        ('israel', -2),
        ('trt', -3),
        ('msk', -3),
        ('gst', -4),
        ('india', -5),
        ('ict', -7),
        ('singapore', -8),
        ('china', -8),
        ('taiwan', -8),
        ('korea', -9),
        ('japan', -9),
        ('aest', -10),
        ('nzst', -12)
    ]

    # Getting the time difference value of tz_fr.
    time_diff = [i[1] for i in timezone_diff if i[0] == tz_fr][0]

    # Splitting t into a list. Separating hour, minute, and am/pm value as separate indices.
    t_list = []
    t_list.append(int(t[:t.index(':')]))
    t_list.append(int(t[t.index(':')+1:t.index(':')+3]))
    t_list.append(t[t.index(':')+3:])

    # Converting the hour value into 24-hr format.
    if t_list[2] == 'am':
        t_list[0] = t_list[0] % 12
    else:
        t_list[0] = 12 + (t_list[0] % 12)

    # Subtracting the time difference value of tz_to to calculate the total time difference from tz_fr to tz_to.
    for i in timezone_diff:
        if tz_to == i[0]:
            time_diff -= i[1]
        else:
            continue

    # Adding the total time difference value to the user input hour value.
    hour = t_list[0] + time_diff

    # Special case for India due to having an extra 30min difference.
    if tz_to == 'india':
        min = (t_list[1] + 30)
        if min >= 60:
            hour += 1
            min = min % 60
            t_list[1] = min
        else:
            t_list[1] = min
    else:
        pass

    # Taking hour mod 24 to put the total calculated hour value into 24-hr format.
    hour = hour % 24

    # Setting am/pm.
    if hour >= 12:
        ampm = 'pm'
    else:
        ampm = 'am'

    # Finally taking hour mod 12 to put the hour value into 12-hr format.
    hour = hour % 12

    # Making sure to show correct time for the case where hour == 0 because of mod 12 above.
    if hour == 0:
        hour = 12
    else:
        pass

    # Organizing and putting it all back together into a string value.
    t_list[0] = hour
    t_list[2] = ampm
    t_list = [str(i) for i in t_list]

    if len(t_list[1]) < 2:
        t_list[1] = '0' + t_list[1]
    else:
        pass
    
    final_time = str(':'.join(t_list[0:2])) + t_list[2] + ' ' + tz_to.upper()
    
    return final_time

def input_check(t, tz_fr, tz_to):
    # This function checks whether user input is in correct format.
    # Initializing timezone values for validation use.
    timezones = [
        'pst',
        'hawaii',
        'alaska',
        'mst',
        'cst',
        'est',
        'korea',
        'gmt',
        'cet',
        'msk',
        'gst',
        'singapore',
        'india',
        'china',
        'japan',
        'aest',
        'nzst',
        'brazil',
        'israel',
        'taiwan',
        'ict',
        'trt',
        'eet'
    ]

    # Making sure user input was in a valid format.
    try:
        # Checking validity of am or pm input.
        day_or_night = 'pm' in t or 'am' in t

        if day_or_night == False:
            raise Exception
        else:
            pass

        # Checking whether time was input in the format of 00:00
        colon_check = t[:t.index(':')]
        
        # Checking that hours and minutes are within the correct range.
        hours = int(t[:t.index(':')])
        minutes = int(t[t.index(':')+1:t.index(':')+3])
        if hours <= 0 or hours > 12:
            raise Exception
        elif minutes >= 60 or minutes < 0:
            raise Exception
        else:
            pass
            
        # Checking validity of timezone inputs.
        tz_check = tz_fr in timezones and tz_to in timezones

        if tz_check == False:
            raise Exception
        else:
            pass

        return True
    
    except Exception:
        return False

def main():
    # This is the main function.
    # Printing all available timezones to choose from.
    print('''
Available Timezones are:

1. Hawaii     (Hawaii Standard Time)
2. Alaska     (Alaska Standard Time)
3. PST        (Pacific Standard Time)
4. MST        (Mountain Standard Time)
5. CST        (Central Standard Time)
6. EST        (Eastern Standard Time)
7. Brazil     (Brazil Standard Time)
8. GMT        (Greenwich Mean Time [UTC, UK])
9. CET        (Central European Time)
10. EET       (Eastern European Time)
11. Israel    (Israel Standard Time)
12. TRT       (Turkey Time)
13. MSK       (Moscow Time)
14. GST       (Gulf Standard Time [UAE, Dubai])
15. India     (India Standard Time)
16. ICT       (Indochina Time [Vietnam, Thailand, Cambodia, Myanmar, Laos])
17. Singapore (Singapore Standard Time)
18. China     (China Standard Time)
19. Taiwan    (Taiwan Standard Time)
20. Korea     (Korea Standard Time)
21. Japan     (Japan Standard Time)
22. AEST      (Australian Eastern Standard Time)
23. NZST      (New Zealand Standard Time)

*NOTE: If Daylight time, mentally add +1 hour to the result.
''')

    time = input("Enter current time (e.g. 4:32pm): ")
    time = time.lower()
    timezone_from = input("Enter current timezone: ")
    timezone_from = timezone_from.lower()
    timezone_to = input("Enter destination timezone: ")
    timezone_to = timezone_to.lower()

    check = input_check(time, timezone_from, timezone_to)

    # If user input is validated, perform time conversion calculation. If not, raise error message.
    if check:
        to_time = world_time(time, timezone_from, timezone_to)
        print("\nDestination time:", to_time)
    else:
        print("\nInvalid input. Please try again.\n")

if __name__ == "__main__":
    main()


# In[ ]:




