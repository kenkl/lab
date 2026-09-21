#!/usr/bin/env python3
"""This week's (2026-09-21) question: Given a year and month, return an array containing every date in that month that falls on a Sunday. Return each date in YYYY-MM-DD format."""

import datetime
import calendar

def getSundays(year, month):
    """
    Returns a list of all Sundays in a given year and month 
    in YYYY-MM-DD format.
    """
    sundays = []
    
    # calendar.monthrange returns a tuple: (day of the week of first day, number of days in month)
    # We only need the second value (the total number of days).
    _, num_days = calendar.monthrange(year, month)
    
    for day in range(1, num_days + 1):
        # Create a date object for the current day being checked
        current_date = datetime.date(year, month, day)
        
        # In Python's datetime module, weekday() returns:
        # Monday = 0, Tuesday = 1, ..., Saturday = 5, Sunday = 6
        if current_date.weekday() == 6:
            sundays.append(current_date.strftime('%Y-%m-%d'))
            
    return sundays

# --- Example Usage ---
year_input = 2023
month_input = 10  # October

result = getSundays(year_input, month_input)
print(f"Sundays in {year_input}-{month_input:02d}: {result}")

# Test with a leap year (February 2024)
print(f"Sundays in 2024-02: {getSundays(2024, 2)}")

# Run the examples/tests from Cassido's prompt:
print(f"September 2026 Sundays: {getSundays(2026, 9)}")
print(f"February 2024 Sundays: {getSundays(2024, 2)}")

