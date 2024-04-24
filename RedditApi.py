import requests
from datetime import datetime
from ForbesFedRatesHike import RatesDates
import pandas as pd

def redditapicall(date_str):
    
    # Parse the date string into a datetime object
    date_obj = datetime.strptime(date_str, "%B %d, %Y")

    # Format the date string with desired separator
    formatted_date = date_obj.strftime("%Y-%m-%d")  
    # print(formatted_date)

    url = f'https://tradestie.com/api/v1/apps/reddit?date={formatted_date}'
    # url = f'https://tradestie.com/api/v1/apps/reddit?date=April 13, 2024'

    response = requests.get(url)

    return response.json()

# print(RatesDates)


firsthike =  redditapicall(RatesDates[0])
df1 = pd.DataFrame(firsthike)
df1.insert(0, 'Date', RatesDates[0])
# print(df1.to_string)

secondhike =  redditapicall(RatesDates[1])
df2 = pd.DataFrame(secondhike)
df2.insert(0, 'Date', RatesDates[1])

thirdhike =  redditapicall(RatesDates[2])
df3 = pd.DataFrame(thirdhike)
df3.insert(0, 'Date', RatesDates[2])

fourthhike =  redditapicall(RatesDates[3])
df4 = pd.DataFrame(fourthhike)
df4.insert(0, 'Date', RatesDates[3])

fifthhike =  redditapicall(RatesDates[4])
df5 = pd.DataFrame(fifthhike)
df5.insert(0, 'Date', RatesDates[4])

sixthhike =  redditapicall(RatesDates[5])
df6 = pd.DataFrame(sixthhike)
df6.insert(0, 'Date', RatesDates[5])

seventhhike =  redditapicall(RatesDates[6])
df7 = pd.DataFrame(seventhhike)
df7.insert(0, 'Date', RatesDates[6])

eigthhike =  redditapicall(RatesDates[7])
df8 = pd.DataFrame(eigthhike)
df8.insert(0, 'Date', RatesDates[7])

ninthhike =  redditapicall(RatesDates[8])
df9 = pd.DataFrame(ninthhike)
df9.insert(0, 'Date', RatesDates[8])

tenthhike =  redditapicall(RatesDates[9])
df10 = pd.DataFrame(tenthhike)
df10.insert(0, 'Date', RatesDates[9])

eleventhhike =  redditapicall(RatesDates[10])
df11 = pd.DataFrame(eleventhhike)
df11.insert(0, 'Date', RatesDates[10])
# print(df11)


df1 = df1.reset_index(drop=True)  # Removes the default integer index
df2 = df2.reset_index(drop=True)  
df3 = df3.reset_index(drop=True)
df4 = df4.reset_index(drop=True)
df5 = df5.reset_index(drop=True)
df6 = df6.reset_index(drop=True)
df7 = df7.reset_index(drop=True)
df8 = df8.reset_index(drop=True)
df9 = df9.reset_index(drop=True)
df10 = df10.reset_index(drop=True)
df11 = df11.reset_index(drop=True)


# Concatenate DataFrames, ignoring indexes and column names of the second
df_concat = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11], ignore_index=True)

# Print the concatenated DataFrame
# print(df_concat)


row = df_concat[df_concat['no_of_comments'] == 308.0]
print(row)