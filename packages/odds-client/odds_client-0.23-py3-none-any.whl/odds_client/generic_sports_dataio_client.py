from datetime import datetime, timedelta
from os import environ
from default_http_client import DefaultHttpClient
from abc import abstractmethod
import sys
import json
import threading


def get_env(var_name, default_value=None):
    return environ.get(var_name) if environ.get(var_name) else default_value


class GenericSportsDataIOClient:
    def __init__(self, custom_http_client=None):
        self.base_url = get_env('SPORT_RADAR_BASE_URL',
                                'https://api.sportsdata.io/v3')
        self.secret_key = None
        self.auth_header = 'Ocp-Apim-Subscription-Key'
        self.http_client = custom_http_client or DefaultHttpClient()
        self.max_threads = 15
        self.thread_args = {}
        self.threads = []

    @abstractmethod
    def get_league(self):
        return None

    # == Instance Methods
    def get_teams(self):
        league_name = self.get_league()
        current_secret_key = self.secret_key
        self.secret_key = get_env('SD_FREE_SUBS_KEY')
        full_url = self.__build_func_url(
            '/%(league)s/scores/json/'
            'teams',
            league=league_name
        )
        response = self.__do_api_call(full_url)
        self.secret_key = current_secret_key

        return response

    def get_stadiums(self):
        league_name = self.get_league()
        current_secret_key = self.secret_key
        self.secret_key = get_env('SD_FREE_SUBS_KEY')
        full_url = self.__build_func_url(
            '/%(league)s/scores/json/'
            'Stadiums',
            league=league_name
        )
        response = self.__do_api_call(full_url)
        self.secret_key = current_secret_key

        return response

    def get_active_players(self):
        league_name = self.get_league()
        current_secret_key = self.secret_key
        self.secret_key = get_env('SD_FREE_SUBS_KEY')
        full_url = self.__build_func_url(
            '/%(league)s/scores/json/'
            'Players',
            league=league_name
        )
        response = self.__do_api_call(full_url)
        self.secret_key = current_secret_key

        return response

    def get_player_detail(self, playerId=None):
        league_name = self.get_league()
        current_secret_key = self.secret_key
        self.secret_key = get_env('SD_SCORE_REAL_TIME_SUBS_KEY')
        full_url = self.__build_func_url(
            '/%(league)s/scores/json/'
            'Player/%(playerId)d',
            league=league_name, playerId=playerId
        )
        print(full_url)
        response = self.__do_api_call(full_url)
        self.secret_key = current_secret_key

        return response

    def get_season(self, season=None):
        calculated_season = season or str(datetime.now().year)

        return calculated_season

    def get_games(self, customSeason=None):
        league_name = self.get_league()
        current_secret_key = self.secret_key
        self.secret_key = get_env('SD_FREE_SUBS_KEY')
        season = self.get_season(customSeason)
        full_url = self.__build_func_url(
            '/%(league)s/scores/json/'
            'Games/%(season)s',
            league=league_name, season=season
        )
        response = self.__do_api_call(full_url)
        self.secret_key = current_secret_key

        return response

    def get_pre_game_odds_by_date(self, date=None):
        now = date if date else datetime.now().date()
        now_iso = now.isoformat()
        league_name = self.get_league()
        full_url = self.__build_func_url(
            '/%(league)s/odds/json/'
            'GameOddsByDate/%(date)s',
            date=now_iso, league=league_name
        )
        response = self.__do_api_call(full_url)

        return response

    # start_date and end_date are strings %Y-%m-%d (isodate)
    def get_pre_game_odds(self, start_date=None, end_date=None):
        pre_games = []
        threads_data = {}

        sdate = datetime.strptime(start_date, '%Y-%m-%d') if start_date else \
            datetime.now()
        edate = datetime.strptime(end_date, '%Y-%m-%d') if end_date else \
            sdate + timedelta(days=15)

        self.__spread_dates(sdate, edate)
        self.__create_threads(threads_data)

        for th in self.threads:
            th.start()

        for th in self.threads:
            th.join()

        for (i, thread_odds) in threads_data.items():
            for th_jdds in thread_odds:
                if th_jdds:
                    for odds in th_jdds:
                        pre_games.append(odds)

        return pre_games

    def get_injuries_news_by_date(self, date=None):
        now = date or datetime.now().date()
        league_name = self.get_league()
        current_secret_key = self.secret_key
        self.secret_key = get_env('SD_NBA_ROTOBALLER_NEWS_SUBS_KEY')
        full_url = self.__build_func_url(
            '/%(league)s/news-rotoballer/json/'
            'RotoBallerPremiumNewsByDate/%(date)s',
            date=now.isoformat(), league=league_name
        )
        response = self.__do_api_call(full_url)
        output = [x for x in response if ('Sit-Start' in x['Categories']) or
                                         ('Injuries' in x['Categories']) or
                                         ('Lineups' in x['Categories'])]
        self.secret_key = current_secret_key

        return output

    def get_injuries_report(self, start_date=None, end_date=None):
        output = []
        injuries_news = []
        sdate = start_date or datetime.now().date()
        edate = end_date or datetime.now().date()
        for d in self.__date_range(sdate, edate):
            injuries_news += self.get_injuries_news_by_date(d)

        for i in injuries_news:
            player_i = self.get_player_detail(i['PlayerID'])
            output.append({'injury_new': i, 'player_detail': player_i})

        return output

    def get_player_game_stats_by_player(self, date=None, playerId=None):
        now = date or datetime.now().date()
        league_name = self.get_league()
        current_secret_key = self.secret_key
        self.secret_key = get_env('SD_NBA_FREE_TRIAL_SUBS_KEY')
        full_url = self.__build_func_url(
            '/%(league)s/stats/json/'
            'PlayerGameStatsByPlayer/%(date)s/%(playerId)d',
            league=league_name, date=now.isoformat(), playerId=playerId
        )
        response = self.__do_api_call(full_url)
        self.secret_key = current_secret_key

        return response

    # == Private Methods
    def __get_auth_headers(self, headers={}):
        altered_headers = headers.copy()
        altered_headers[self.auth_header] = self.secret_key

        return altered_headers

    def __build_func_url(self, func_url, **place_holders):
        try:
            return self.base_url + func_url % place_holders
        except Exception as e:
            sys.stderr.write(repr(e) + "\n")
            return self.base_url

    def __do_api_call(self, full_url, headers={}):
        auth_headers = self.__get_auth_headers(headers)
        response = self.http_client.get(full_url, auth_headers)

        return json.loads(response) if response else None

    def __date_range(self, start_date, end_date):
        for n in range(int((end_date - start_date).days)+1):
            yield start_date + timedelta(n)

    def __get_pre_game_odds_by_dates(self, dates, response_hash, th_id):
        odds_for_dates = []
        for now in dates:
            odds = self.get_pre_game_odds_by_date(now)
            odds_for_dates.append(odds)
        response_hash[th_id] = odds_for_dates

    def __spread_dates(self, start_date, end_date):
        self.thread_args = {}
        index = 0
        for d in self.__date_range(start_date, end_date):
            try:
                self.thread_args[index].append(d.date())
            except Exception:
                self.thread_args[index] = []
                self.thread_args[index].append(d.date())
                index = (index + 1) % self.max_threads

    def __create_threads(self, response_hash):
        self.threads = []
        index = 0
        for (k, dates) in self.thread_args.items():
            self.threads.append(
                threading.Thread(
                    target=self.__get_pre_game_odds_by_dates,
                    args=(dates, response_hash, index)))
            index = index + 1
