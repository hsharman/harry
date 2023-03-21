from datetime import datetime

# Create time string 
date_str = "2022-03-17 10:45:30"

# Create time object using string
date_obj = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')

# Get formatted data from the date object
formatted_date = date_obj.strftime('%m/%d/%Y %H:%M:%S')

# Print the formatted date 
print(formatted_date)
