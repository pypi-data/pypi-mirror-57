from pprint import pprint
from sports_client_factory import SportsClientFactory
from datetime import datetime, timedelta, date
import json

factory = SportsClientFactory()
sr = factory.get_api_client('nba')
# print("\n Testing get_pre_game_odds_by_date \n")
# data = sr.get_pre_game_odds_by_date()
# pprint(data)

print("\n Testing Injuries \n")
start_date = date(2019, 12, 12)
end_date = date(2019, 12, 12)
#data = sr.get_teams()
#data = sr.get_pre_game_odds(start_date, end_date)
#data = sr.get_pre_game_odds('2019-10-30', '2019-10-31')
#print("\n Testing get_consolidated_games \n")
# data = sr.get_consolidated_games()
#data = sr.get_games('2019POST')
data = sr.get_injuries_report(start_date, end_date)
print("\n Llego \n")
i = 1
for a in data:
  pprint("LESION") 
  print (i)
  i = i + 1
  pprint(a)
