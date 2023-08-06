import pandas as pd
import numpy as np
import os
import logging
import pickle
import _pickle
import gc
import math

from nfl_insights import *
from contendo_utils import *

# noinspection PyUnresolvedReferences
class NFLAnalyticsGenerator:

    @contendo_classfunction_logger
    def __init__(self, seasons, build=False):
        assert type(seasons)==list, 'seasons parameter must be a list, "{}" is illegal'.format(seasons)
        self.generator = NFLStatsQueries('sportsight-tests')
        #
        # combining the regular and complex stats
        self.statsDict = self.generator.statsDict.copy()
        for key,value in self.generator.compStatsDict.items():
            self.statsDict[key] = value

        self.nfl_stats_pickle_filename = 'resource/nfl_all_stats.pkl'

        #build a table for each stats with all dimensions
        self.metrics = dict()
        if build:
            self._build_all_metrics(seasons=seasons)
        self._read_all_metrics(seasons)

    def _read_all_metrics(self, seasons):
        logger.info('Downloading pickle metrics files from GCP')
        self.generator.nfldata.bqu.download_from_gcp(NFL_GCP_BUCKET, self.nfl_stats_pickle_filename, self.nfl_stats_pickle_filename, checkTimestamp=True)
        logger.info('Loading pickle file to memory')
        gc.disable()
        with open(self.nfl_stats_pickle_filename, 'rb') as handle:
            self.allStatsDict = _pickle.load(handle)
        gc.enable()
        logger.info('Done loading')

    def _add_result_df_to_stats_dict(self, statName, df, isAscending):
        if df.shape[0] != 0:
            #
            # Enrich the df with aggregative stats.
            avg = df['statValue'].mean()
            std = df['statValue'].std()
            df['avg'] = avg
            df['stddev'] = std
            df['stddev/avg'] = std / avg if avg !=0 else 0.0
            df['stdFactor'] = (df['statValue'] - avg) / std if std != 0 else 0.0
            df['absStdFactor'] = abs((df['statValue'] - avg) / std) if std != 0 else 0.0
            df['avgDiff%'] = (df['statValue'] - avg) / avg * 100
            #df['nItems'] = df.shape[0]
            # calculate rank direction
            df['rank'] = df['statValue'].rank(method='min', ascending=isAscending)
            df.sort_values('statValue', ascending=isAscending, inplace=True)
            # Add the df to the dictionary
            row = dict(df.iloc[0])
            _mainkey = (row['season'], row['statName'], row['statObject'])
            _seckey = (row['dimensions'], row['calculation'])
            self.allStatsDict[_mainkey] = self.allStatsDict.get(_mainkey, dict())
            df.fillna(0, inplace=True)
            self.allStatsDict[_mainkey][_seckey] = df
            # add to the csv

    @contendo_classfunction_logger
    def _get_statobjects_from_statdef(self, statDef: dict) -> list:
        _teamObjects = [('team', team, '{}Team'.format(team)) for team in statDef['TeamObjects'].split(',')]
        _playerObjects = [('player', player, '{}Player'.format(player)) for player in
                          statDef['PlayerObjects'].split(',')]
        _statObjects = _teamObjects + _playerObjects
        return _statObjects

    @contendo_classfunction_logger
    def _build_all_metrics(self, seasons):

        _dimensionsMatrixDict = self.generator.dimentionsMatrixDict
        _dimensionsDF = self.generator.dimentionsDF
        _dimensionGroups = _dimensionsDF.groupby(['GroupCode'])
        _dimGroupList = list(_dimensionsMatrixDict.keys())
        _dimGroupList.sort()
        print(_dimGroupList)

        _dimensionGroupsDict = dict()
        for dimGroup in _dimGroupList:
            _dimDF = _dimensionGroups.get_group(dimGroup)
            _dimensionGroupsDict[dimGroup] = list(_dimDF['ConditionCode'])

        counter = 0
        lineCounter=0
        self.allStatsDict = dict()
        for _statName, _statDef in self.statsDict.items():
            if _statDef['Doit'] !='y':
                continue
            for season in seasons:
                _statObjects = self._get_statobjects_from_statdef(_statDef)
                for _statObject in _statObjects:
                    _objType, _obj, _statObject = _statObject
                    if _obj in ['none', 'all', '']:
                        continue

                    _objectDef = self.generator.ptmapDict[_statObject]
                    _teamObject = _objectDef['TeamType']
                    isAscending =  self.generator.is_ascending(obj=_statObject, statDef=_statDef)

                    _alldf = None
                    for dimGroup1 in _dimGroupList:
                        if _statDef[dimGroup1] != 1:  # dimension group not relevant for this stat
                            logger.debug('%4d. Discarding stat: %s, object: %s, dim-group1: %s, data: %s', counter,
                                        _statName, _statObject, dimGroup1, lineCounter)
                            continue
                        logger.info('%4d. calculating stat: %s, object: %s, dim-group1: %s, data: %s', counter, _statName, _statObject, dimGroup1, lineCounter)
                        for dimGroup2 in ['all']: # _dimGroupList:
                            if _dimensionsMatrixDict[dimGroup1][dimGroup2]!=1: # dimensions match not needed
                                continue
                            for dim1 in _dimensionGroupsDict[dimGroup1]:
                                for dim2 in _dimensionGroupsDict[dimGroup2]:
                                    # Ignore disabled dimensions

                                    counter+=1
                                    _dimComb2 = [dim1, dim2]

                                    # discarding team objects for relevant dimensions
                                    if _objType == 'team':
                                        _discard = False
                                        for _dim in _dimComb2:
                                            if self.generator.dimentionsDict[_dim]['Doit'] != 1:
                                                _discard=True
                                                break
                                            _teamObjects = self.generator.dimentionsDict[_dim]['TeamObjects']
                                            if _teamObjects!= 'all' and _teamObjects.find(_obj)==-1:
                                                _discard=True
                                                break
                                        if _discard:
                                            logger.debug('Discarding teamobjects by dim filtering %s, %s, %s', _statName, _statObject, _dimComb2)
                                            continue

                                    if 'StatRatio' in _statDef:
                                        _calculation = _statDef['Type'] #'ratio'
                                        _df = self.generator.pbp_get_composed_stat(
                                            compstat=_statName,
                                            object=_statObject,
                                            dimensions=_dimComb2,
                                            season=season,
                                        )
                                    else:
                                        _calculation = 'stat'
                                        _df = self.generator.pbp_get_stat(
                                            statName=_statName,
                                            object=_statObject,
                                            dimensions=_dimComb2,
                                            season=season,
                                        )

                                    if _dimComb2 == ['all', 'all']:
                                        _alldf = _df

                                    if _df.shape[0]>0:
                                        lineCounter+=_df.shape[0]
                                        if _objType=='player':
                                            _df = _df.query('playerName!=0')

                                        _calcDF = _df.copy()
                                        _calcDF['calculation'] = _calculation
                                        self._add_result_df_to_stats_dict(_statName, _calcDF, isAscending)

                                        if _statDef['Type']=='stat': # not ratio stat
                                            # Do pct (only if it's a counter).
                                            if _statDef['Function']=='count':
                                                _calcDF = _df.copy()
                                                _calcDF['calculation'] = 'pct'
                                                _calcDF['statValue'] = _df['statValue']/_alldf['statValue'] * 100
                                                if _calcDF['statValue'].max()<=100:
                                                    self._add_result_df_to_stats_dict(_statName, _calcDF, isAscending=False)
                                                else:
                                                    logger.error(
                                                        'Error using PCT for stat: %s, object: %s, dim: %s',
                                                        _statName, _statObject, dim1
                                                    )
                                            # Do per-game
                                            _calcDF = _df.copy()
                                            _calcDF['calculation'] = 'per_game'
                                            _calcDF['statValue'] = _df['statValue']/_df['nGames']
                                            self._add_result_df_to_stats_dict(_statName, _calcDF, isAscending)

                                            # Do per-drive/play only for teams.
                                            if _objType=='team':
                                                _calcDF = _df.copy()
                                                _calcDF['calculation'] = 'per_drive'
                                                _calcDF['statValue'] = _df['statValue']/_df['nDrives']
                                                self._add_result_df_to_stats_dict(_statName, _calcDF, isAscending)
                                                if _statDef['Function'] == 'sum':
                                                    # Do per-play (only to sum stats).
                                                    _calcDF = _df.copy()
                                                    _calcDF['calculation'] = 'per_play'
                                                    _calcDF['statValue'] = _df['statValue'] / _df['nPlays']
                                                    self._add_result_df_to_stats_dict(_statName, _calcDF, isAscending)
                    #break
                #break
            logger.info ('End stat: %s', _statName)
            #break
        logger.debug('Num queries: %d, Num results: %d', counter, lineCounter)
        logger.info('Saving pickle File %s', self.nfl_stats_pickle_filename)
        with open(self.nfl_stats_pickle_filename, 'wb') as handle:
            _pickle.dump(self.allStatsDict, handle, protocol=pickle.HIGHEST_PROTOCOL)
        logger.info('Uploading %s to GCP', self.nfl_stats_pickle_filename)
        self.generator.nfldata.bqu.upload_file_to_gcp(NFL_GCP_BUCKET, self.nfl_stats_pickle_filename, self.nfl_stats_pickle_filename, timestamp=True)
        logger.info('File %s uploaded to GCP', self.nfl_stats_pickle_filename)

        return lineCounter

    @contendo_classfunction_logger
    def get_dimentions(self) -> dict:
        _dimsDict = dict()
        for dim, dimdef in self.generator.dimentionsDict.items():
            grc = dimdef['GroupCode']
            if grc not in _dimsDict:
                _dimsDict[grc] = list()
            _dimsDict[grc].append(dim)
        return _dimsDict


    @contendo_classfunction_logger
    def get_stats(self, teamType: str) -> list:
        _retList = list()
        for statName, statDef in self.statsDict.items():
            if statDef['TeamObjects'].find(teamType) >= 0 and statDef['Doit']=='y':
                _retList.append(statName)
        return _retList

    @contendo_classfunction_logger
    def get_stats_table(self, statName:str, teamObject: str, dimension: str, calculation: str, season=NFL_DEFAULT_SEASON) -> pd.DataFrame:
        _mainkey = (season, statName, teamObject)
        _dims = ['all', dimension]
        _dims.sort()
        _seckey = (str(_dims), calculation)
        # return the dataset or an empty dataframe.
        return self.allStatsDict.get(_mainkey, dict()).get(_seckey, pd.DataFrame())

@contendo_function_logger
def test():
    logger.info('Starting...')
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "{}/sportsight-tests.json".format(os.environ["HOME"])
    os.chdir('{}/tmp/'.format(os.environ["HOME"]))
    pd.set_option('display.max_columns', 1500)
    pd.set_option('display.max_rows', 1500)
    pd.set_option('display.width', 20000)
    ostats = NFLAnalyticsGenerator(seasons=[NFL_DEFAULT_SEASON], build=True)
    # ostats = NFLAnalyticsGenerator(seasons=[NFL_DEFAULT_SEASON], build=False)
    # print (ostats.get_stats_table(statName='tackles', teamObject='soloTacklingPlayer', dimension='all', calculation='stat'))
    # return

    #logger.info ('offense stats: %s', ostats.get_stats(teamType='offense'))
    #logger.info ('Dimensions: %s', ostats.get_dimentions())
    #groups = ostats.allStatsDF.groupby(['statName',  'statObject', 'seasons', 'dimensions', 'calculation'])
    #logger.info(len(groups.groups.keys()))
    stats = ostats.get_stats(teamType='offense')
    logger.info('starting dict, len=%d', len(ostats.allStatsDict))
    count=0
    distList = list()
    for key1 in ostats.allStatsDict:
        for key2 in ostats.allStatsDict[key1]:
            count+=1
            df = ostats.allStatsDict[key1][key2]
            continue
            if df.shape[0] not in [32]:
                logger.error('Error with metric %s, %s #teams=%d', stat, key, df.shape[0])
            if df.query('statValue!=0.0').shape[0] == 0:
                logger.error('All values are 0.0 with metric %s, %s #teams=%d', stat, key, df.shape[0])
            _arr = np.array(df["statValue"])
            a = _arr/sum(_arr)
            a = a ** 10
            zoDistribution = a/sum(a)
            l2Norm = np.linalg.norm(zoDistribution, ord=2)
            minUniformity = 1 / np.sqrt(len(zoDistribution))
            distMeasure = (l2Norm - minUniformity) / (1 - minUniformity)
            distVal = int(math.floor(distMeasure * 10))
            #_qdf = ostats.generator.get_stat_questions(df)
            #print(_qdf.sort_values('qScore', ascending=True))
            #return
            _distObj = {
                'statName': key1[1],
                'statObject': key1[2],
                'calculation': key2[1],
                'dimensions': key2[0],
                'distValue': distVal,
                'nGT0': df.query('statValue!=0.0').shape[0],
                'nItems': df.iloc[0]['nItems'],
                'nCount': df.query('count>0').shape[0],
                'nMeasures': sum(df['count']),
                #'nQuestions': _qdf.shape[0],
            }
            distList.append(_distObj)
            #logger.info('%d. %s', len(distList), _distObj)
    df = pd.DataFrame(distList)
    print(df.shape)
    df.to_csv('resource/teams-distlist.csv')
    logger.info('dict done, #DFs: %d', count)
    logger.info('Done.')


if __name__ == '__main__':
    contendo_logging_setup(default_level=logging.INFO)
    test()
