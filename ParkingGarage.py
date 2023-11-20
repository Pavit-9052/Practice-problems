'''
Parking garage problem
1.Write a program to calculate the revenue generated in a parking garage in a shopping mall

Parking fee is 
If you return within 15 mins, its free
Rs 100 for the first hr
Rs 150 for each hr after that. 
Fee is calculated in 30 min increments. (meaning, if you spent 25 mins, you will be charged for 30 mins
If you spend 35 mins, you will be charged for one hr)
Get entry time and exit time from customer as input and display the fee.'''

from datetime import datetime
def parking_fee(x,y):
    start=datetime.strptime(entry_time,"%H:%M")
    end=datetime.strptime(exit_time,"%H:%M")

    parking_duration = (end - start).total_seconds()/60

    if parking_duration<15:
        return 0
    elif parking_duration == 60:
        return 100
    else:
        remaining_duration = parking_duration - 60
        additional_hours = (remaining_duration // 30) + 1
        return 100 + (additional_hours * 150)

entry_time=input("Enter the entry time(H:M):")
exit_time=input("Enter the exit time(H:M):")
out=parking_fee(entry_time,exit_time)
print(f"The fee is:{out}")

OUTPUT:-
Enter the entry time(H:M):10:00
Enter the exit time(H:M):12:55
The fee is:700.0




2.same as above. End the program if 24hrs passes from when the first customer comes in. 
Print the total fees collected.

3. Same as above, adding more condition.
The parking garage has 10 spaces numbered from 1 to 10.
THere is a car entering or exiting every 10 mins.
When a car enters, you need to tell them which lot is allotted for them.
When the customer comes to pick up the car, get the lot number as input and calculate the fees.

Use arrays if needed.
'''
