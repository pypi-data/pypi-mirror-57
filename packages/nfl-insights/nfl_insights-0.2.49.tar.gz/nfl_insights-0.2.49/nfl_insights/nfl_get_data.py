import os
import pandas as pd
from datetime import datetime as dt
from pathlib import Path
import logging

import gspread

from contendo_utils import *
from nfl_insights import *


# noinspection PyUnresolvedReferences
class NFLGetData():
    #
    # read in the configurations
    def __init__(self, project=None):
        #
        # get the initial configurations
        self.ccm = ContendoConfigurationManager()
        #
        # initialize BQ
        self.bqu = BigqueryUtils(project)
        #
        # data files definitions
        self.dataObjects = ['games', 'teams', 'players']
        self.resourceDir = 'resource'
        self.pbpDataFileName = '{}/nfl_pbp_data.csv'.format(self.resourceDir)
        self._statspbpDataFileName = '{}/nfl_stats_pbp_data.csv'.format(self.resourceDir)
        #
        # data variables
        self.pbpDF = None
        self.playerspbpDF = None
        self.gamesDF = None
        self.dataDFs = dict()

    @contendo_classfunction_logger
    def _update_nfl_data(self, source, outfile):
        assert source in self.dataObjects, 'Illegal source: {}, must be one of {}'.format(source, self.dataObjects)
        _query = ProUtils.get_string_from_file('{}/queries/nfl_{}_info.sql'.format(Path(__file__).parent, source))
        _df = self.bqu.execute_query_to_df(_query)
        logger.debug('Read %s query data, shape=%s, columns=%s', source, _df.shape, _df.columns)
        ProUtils.create_path_directories(outfile)
        _df.to_csv(outfile, index=False)
        url = self.bqu.upload_file_to_gcp(NFL_GCP_BUCKET, outfile, outfile, timestamp=True)
        logger.debug('Updated %s file %s', source, outfile)
        self.dataDFs[source] = _df

    @contendo_classfunction_logger
    def _read_nfl_data(self, source, update=False):
        #
        # Read the pbp data from file.
        _datafile = '{resourceDir}/{source}_data.csv'.format(resourceDir=self.resourceDir, source=source)
        if update:
            logger.debug('Updating %s data', source)
            self._update_nfl_data(source, _datafile)

        # getting the source DF is required (first time)
        if not source in self.dataDFs:
            self.bqu.download_from_gcp(NFL_GCP_BUCKET, _datafile, _datafile, checkTimestamp=True)
            self.dataDFs[source] = pd.read_csv(_datafile)

    @contendo_classfunction_logger
    def get_player_by_id(self, playerId, season=NFL_DEFAULT_SEASON):
        self._read_nfl_data('players')
        query = '(playerId=={}) & (season=="{}")'.format(playerId, season)
        logger.debug('Players query= %s', query)
        _playerDF = self.dataDFs['players'].query(query)
        if _playerDF.shape[0] == 0:
            # Error
            logger.error('Player id %s not found', playerId)
            return {}

        return dict(_playerDF.iloc[0])

    @contendo_classfunction_logger
    def get_players_df(self, season, update=False):
        key = ('players', season)
        if not key in self.dataDFs:
            self._read_nfl_data('players', update)
            _playersDF = self.dataDFs['players'].query('season=="{}"'.format(season)).copy()
            # _playersDF['pid1'] = _playersDF['playerId']
            # _playersDF['tid1'] = _playersDF['teamId']
            _playersDF.set_index(['playerId', 'teamId'], inplace=True)
            self.dataDFs[key] = _playersDF
        return self.dataDFs[key]

    @contendo_classfunction_logger
    def get_teams_df(self, season, update=False):
        key = ('teams', season)
        if not key in self.dataDFs:
            self._read_nfl_data('teams', update)
            _teamsDF = self.dataDFs['teams'].query('season=="{}"'.format(season))
            _teamsDF.set_index(['teamId'], inplace=True)
            self.dataDFs[key] = _teamsDF
        return self.dataDFs[key]

    @contendo_classfunction_logger
    def get_games_df(self, season: str, update: bool = False) -> pd.DataFrame:
        key = ('games', season)
        if not key in self.dataDFs:
            self._read_nfl_data('games', update)
            _gamesDF = self.dataDFs['games'].query('season=="{}"'.format(season))
            self.dataDFs[key] = _gamesDF
        return self.dataDFs[key]

    @contendo_classfunction_logger
    def _generate_pbp_query(self):
        exceptionList = [
            'interceptedAtPosition',
            'recoveringTeam',  # abbreviation
            'fumblingTeam',
            'scrambles',
            'kneels',
        ]
        pbp_schema = self.bqu.get_table_schema(NFL_DATA_DATASET, NFL_PBP_TABLEID)
        fieldsList = []

        def aggregate_fieldslist(schema, parent=None):
            def calc_fieldname(name, parent):
                if parent:
                    return '{parent}.{name}'.format(parent=parent, **field)
                else:
                    return name

            for field in schema:
                name = field['name']
                if name in exceptionList or name[0] == '_':
                    continue

                fieldname = calc_fieldname(name, parent)
                if field['type'] == 'RECORD':
                    if field['mode'] == 'REPEATED':
                        logger.debug(name)
                        continue
                    else:
                        aggregate_fieldslist(field['fields'], fieldname)
                else:
                    fieldsList.append('{} as {}'.format(fieldname, fieldname.replace('.', '_'), field['type']))

        aggregate_fieldslist(pbp_schema)
        fieldsStr = str(fieldsList).replace('[', '').replace(']', '').replace(',', ',\n').replace("'", '')
        query = 'SELECT {fields} FROM `sportsight-tests.NFL_Data.{tableId}`'.format(fields=fieldsStr,
                                                                                    tableId=NFL_PBP_TABLEID)
        if 'CONTENDO_DEV' in os.environ:
            ProUtils.write_string_to_file('{}/queries/pbp_flat_query.sql'.format(str(Path(__file__).parent)), query)
        return query

    @contendo_classfunction_logger
    def write_pbp_data(self, pbpdataDF: pd.DataFrame):
        pbpdataDF.to_csv(self.pbpDataFileName + 'new')
        url = self.bqu.upload_file_to_gcp(NFL_GCP_BUCKET, self.pbpDataFileName + 'new',
                                          self.pbpDataFileName, timestamp=True)
        return url

    @contendo_classfunction_logger
    def get_pbp_data(self):
        #
        # Read the pbp data from file.
        if self.pbpDF is None:
            self.bqu.download_from_gcp(NFL_GCP_BUCKET, self.pbpDataFileName, self.pbpDataFileName, checkTimestamp=True)
            self.pbpDF = pd.read_csv(self.pbpDataFileName).fillna(0)

        return self.pbpDF

    @contendo_classfunction_logger
    def write_pbp_stats(self, pbpstatsDF: pd.DataFrame):
        pbpstatsDF.to_csv(self._statspbpDataFileName + 'new')
        url = self.bqu.upload_file_to_gcp(NFL_GCP_BUCKET, self._statspbpDataFileName + 'new',
                                          self._statspbpDataFileName, timestamp=True)
        return url

    @contendo_classfunction_logger
    def get_pbp_stats(self):
        #
        # Read the pbp data from file.
        if self.playerspbpDF is None:
            self.bqu.download_from_gcp(NFL_GCP_BUCKET, self._statspbpDataFileName, self._statspbpDataFileName,
                                       checkTimestamp=True)
            _dtype = {}
            self.playerspbpDF = pd.read_csv(self._statspbpDataFileName, dtype=_dtype, low_memory=False).fillna(0)
            _dtype = {
                'blockingPlayer_position': str,
                'defenseTouchdown': bool,
                'isSafety1': bool,
                'spiked': bool,
                'returnTouchdown': bool,
            }
            self.playerspbpDF.astype(_dtype)

        return self.playerspbpDF

    @contendo_classfunction_logger
    def get_team_scores(self, season=NFL_DEFAULT_SEASON) -> dict:
        _playedGamesDF = self.get_games_df(season=NFL_DEFAULT_SEASON).query('playedStatus == "COMPLETED"')
        _teamsDict = dict()
        _teamDict = {
            'wins': 0,
            'loses': 0,
            'draws': 0,
            'homewins': 0,
            'homeloses': 0,
            'homedraws': 0,
            'awaywins': 0,
            'awayloses': 0,
            'awaydraws': 0,
        }
        for i, gameRow in _playedGamesDF.iterrows():
            _gameRow = dict(gameRow)
            _homeTeamDict = _teamsDict.get(_gameRow['homeTeamName'], _teamDict.copy())
            _awayTeamDict = _teamsDict.get(_gameRow['awayTeamName'], _teamDict.copy())
            _scoreDiff = _gameRow['homeScoreTotal'] - _gameRow['awayScoreTotal']
            if _scoreDiff > 0:  # home team wins
                _homeTeamDict['wins'] += 1
                _homeTeamDict['homewins'] += 1
                _awayTeamDict['loses'] += 1
                _awayTeamDict['awayloses'] += 1
            elif _scoreDiff < 0:  # away wins
                _homeTeamDict['loses'] += 1
                _homeTeamDict['homeloses'] += 1
                _awayTeamDict['wins'] += 1
                _awayTeamDict['awaywins'] += 1
            else:  # draw
                _homeTeamDict['draws'] += 1
                _homeTeamDict['homedraws'] += 1
                _awayTeamDict['draws'] += 1
                _awayTeamDict['awaydraws'] += 1

            if not _gameRow['homeTeamName'] in _teamsDict:
                _teamsDict[_gameRow['homeTeamName']] = _homeTeamDict
                _homeTeamDict['teamName'] = _gameRow['homeTeamName']
            if not _gameRow['awayTeamName'] in _teamsDict:
                _teamsDict[_gameRow['awayTeamName']] = _awayTeamDict
                _awayTeamDict['teamName'] = _gameRow['awayTeamName']

        def format_score(wins, loses, draws):
            if draws>0:
                return '{}-{}-{}'.format(wins, loses, draws)
            else:
                return '{}-{}'.format(wins, loses)

        _scoresDF = pd.DataFrame(list(_teamsDict.values()))
        _scoresDF.sort_values(['wins', 'loses'], ascending=False, inplace=True)
        _scoresDF['Scores'] = _scoresDF.apply(
            lambda x: format_score(x['wins'], x['loses'], x['draws']), axis=1)
        _scoresDF['homeScores'] = _scoresDF.apply(
            lambda x: format_score(x['homewins'], x['homeloses'], x['homedraws']), axis=1)
        _scoresDF['awayScores'] = _scoresDF.apply(
            lambda x: format_score(x['awaywins'], x['awayloses'], x['awaydraws']), axis=1)
        # print(_scoresDF[['teamName', 'Scores', 'homeScores', 'awayScores']])
        return ProUtils.pandas_df_to_dict(_scoresDF[['teamName', 'Scores', 'homeScores', 'awayScores']], 'teamName')

    @contendo_classfunction_logger
    def get_week_games_info(self, week: int, season=NFL_DEFAULT_SEASON) -> dict:
        _gamesDF = self.get_games_df(season=season)
        _weeksGamesDF = _gamesDF.query('week=={week}'.format(week=week))
        # make sure we have results
        if _weeksGamesDF.shape[0] == 0:
            return dict()
        #logger.debug('Games DF:\n%s',_weeksGamesDF)
        _columns = ['matchname', 'homeTeamid', 'awayTeamid', 'homeTeamAbv', 'awayTeamAbv', 'startTime',
                    'homeScoreTotal', 'awayScoreTotal', 'playedStatus', 'week', 'venueName', 'city', 'homeTeamName',
                    'awayTeamName']

        return ProUtils.pandas_df_to_dict(_weeksGamesDF[_columns], 'matchname')


# Main Test function
@contendo_function_logger
def test():
    logger.info('Start...')
    startTime = dt.now()
    pd.set_option('display.max_columns', 20)
    pd.set_option('display.width', 200)
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "{}/sportsight-tests.json".format(os.environ["HOME"])
    os.environ['CONTENDO_DEV'] = 'y'
    os.chdir('{}/tmp/'.format(os.environ["HOME"]))
    nfldata = NFLGetData()
    _teamScoresDict = nfldata.get_team_scores()
    print(dict_to_string(_teamScoresDict))
    print(nfldata.get_teams_df(season=NFL_DEFAULT_SEASON, update=False))
    # print(nfldata.get_games_df(season=NFL_DEFAULT_SEASON, update=True))
    print(dict_to_string(nfldata.get_week_games_info(week=15)))
    return
    nfldata.get_pbp_stats()
    _playersDF = nfldata.get_players_df(season=NFL_DEFAULT_SEASON, update=False)
    _poslist = list(_playersDF['primaryPosition'])
    _poslist.sort()
    print(set(_poslist), len(set(_poslist)))
    return
    print(nfldata.get_player_by_id(playerId=12606))
    print(nfldata.get_teams_df(season=NFL_DEFAULT_SEASON, update=False))
    print(nfldata.get_games_df(season=NFL_DEFAULT_SEASON, update=True))
    logger.info('Done.')


if __name__ == '__main__':
    pd.set_option('display.max_rows', 1500)
    pd.set_option('display.max_columns', 150)
    pd.set_option('display.width', 20000)
    contendo_logging_setup(default_level=logging.DEBUG)
    test()
