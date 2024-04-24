from bs4 import BeautifulSoup
import requests
import pprint
from datetime import datetime
import pandas as pd


# Forbes Fed Rates and Dates
# Define the URL of the webpage
url = "https://www.forbes.com/advisor/investing/fed-funds-rate-history/"

# Make a GET request to the webpage
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Find the table under the heading "Fed Rate Hikes 2022-2023: Taming Inflation"
table = soup.find("tbody")

# Extract the table data
data = []
for row in table.find_all("tr")[0:]:  
    cells = row.find_all("td")
    data.append([cell.text.strip() for cell in cells])

# Print the extracted data
#pprint.pp(data)

fedRatesHeader = ['Date', 'Change Points', "Fed Rates"]
fedRatesdf = pd.DataFrame(data, columns=fedRatesHeader)  # Use the first row as column names

# Print the table
#print(fedRatesdf)

RatesDates = fedRatesdf.iloc[:,0].tolist()
#Correcting the month's names 
RatesDates[3] = 'February 1, 2023'
RatesDates[4] = 'December 14, 2022'
RatesDates[5] = 'November 2, 2022'
RatesDates[6] = 'September 21, 2022'
# print(RatesDates)



ratesfromntoDates = ['July 25, 2023', RatesDates[0], 'May 2, 2023', RatesDates[1], 'March 21, 2023', RatesDates[2], 'January 31, 2023', 'February 1, 2022', 'December 13, 2023', 'December 14, 2023', 'November 1, 2022', 'November 2, 2022', 'September 20, 2022', 'September 21, 2022', 'July 26, 2022', RatesDates[7], 'June 15, 2022', RatesDates[8], 'May 4, 2022', RatesDates[9], 'March 16, 2022', RatesDates[10]]
# print(ratesfromntoDates)


def convert_to_unix(date_str):
  """
  This function takes a date string in format 'Month Day, Year' and returns the corresponding Unix timestamp (seconds since epoch).
  """
  try:
    # Parse the date string and create a datetime object
    date_obj = datetime.strptime(date_str, "%B %d, %Y")
  except ValueError:
    # Handle invalid date format (optional)
    print(f"Invalid date format: {date_str}. Skipping...")
    return None

  # Get the Unix timestamp (seconds since epoch)
  unix_timestamp = date_obj.timestamp()
  return unix_timestamp

unix_timestamps = []
for date_str in ratesfromntoDates:
  timestamp = convert_to_unix(date_str)
  if timestamp:  # Only append if conversion was successful
    unix_timestamps.append(timestamp)

formattedFedDatesUnixCodes = []
for values in unix_timestamps:
    formattedFedDatesUnixCodes.append(int(values))

# print(formattedFedDatesUnixCodes)
