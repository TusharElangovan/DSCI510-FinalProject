import datetime
import requests
from bs4 import BeautifulSoup

def fetchyahooresults(ticker, date):

 
  try:
    # Parse the date string
    date_obj = datetime.datetime.strptime(date, "%B %d, %Y")
  except ValueError:
    print("Invalid date format. Please use 'Month Day, Year' format (e.g., July 26, 2023).")
    return None, None

  # Set the time to 5:00 PM for both timestamps
  date_obj = date_obj.replace(hour=17, minute=0, second=0, microsecond=0)
  previous_day_timestamp = (date_obj - datetime.timedelta(days=1)).timestamp()

  # Convert timestamps to integer for UNIX representation (optional)
  current_date_timestamp = int(date_obj.timestamp())
  previous_day_timestamp = int(previous_day_timestamp)


  # Print the timestamps
#   print(f"Current date UNIX timestamp: {current_date_timestamp}")
#   print(f"Previous day UNIX timestamp: {previous_day_timestamp}")


  url = f'https://finance.yahoo.com/quote/{ticker}/history?period1={int(previous_day_timestamp)}&period2={int(current_date_timestamp)}'

  headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
    }
  soup = BeautifulSoup(requests.get(url, headers=headers).content, "html.parser")


# Find the table under the heading "Fed Rate Hikes 2022-2023: Taming Inflation" 
  table = soup.find("tbody")


# Extract data from table cells (assuming there are 7 cells)
  date = table.find_all('td')[0].text.strip()
  open_price = float(table.find_all('td')[1].text.strip())
  high_price = float(table.find_all('td')[2].text.strip())
  low_price = float(table.find_all('td')[3].text.strip())
  close_price = float(table.find_all('td')[4].text.strip())
  volume = int(table.find_all('td')[6].text.strip().replace(',', ''))  # Remove commas and convert to integer

# Store values in separate lists
  date_list = [date]
  price_list = [open_price, high_price, low_price, close_price]
  volume_list = [volume]

  astockdata = [date, open_price, high_price, low_price, close_price, volume]
  stockdata = {'Date' : date, 'Opening Price' : open_price, 'High Price' : high_price, 'Low Price' : low_price, 'Closing Price' : close_price, 'Stock Volumes' : volume}

  return(stockdata)

# Example usage
# stock_price_date = "July 26, 2023"
# ticker = 'MSFT'
# fetchyahooresults(ticker, stock_price_date)
