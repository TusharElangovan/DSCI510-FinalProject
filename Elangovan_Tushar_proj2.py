from ForbesFedRatesHike import RatesDates
from RedditApi import df_concat
from YahooApi import fetchbyahooapi
import pprint

print('---------------------------------x------------------------------------')
print('Scraping through the Forbes Website for the Fed Rate hikes dates')
#print(RatesDates)
print('---------------------------------x------------------------------------')

print('Fetching the response from the Reddit Api for all the fed rate hikes')
print('Consolidating into a single dataframe')
#print(df_concat)
print('---------------------------------x------------------------------------')

stock = 'MSFT'
print(f'Yahoo Api Response for {stock}')
#fetchbyahooapi(stock)
print('---------------------------------x------------------------------------')

#print(df_concat.dtypes)