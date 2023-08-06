import pandas as pd
import numpy as np
import random
import os
import json
from pathlib import Path
import logging
import math

from contendo_utils import *
from nfl_insights import *

eval(NFL_LANGUAGE_FILENAME_EVAL)


class NFLQuestions:
    @contendo_classfunction_logger
    def __init__(self, season=NFL_DEFAULT_SEASON, ostats=None):
        # load the definition file
        self.language = ProUtils.get_dict_from_jsonfile(eval(NFL_LANGUAGE_FILENAME_EVAL))

        # get ostats from external caller or initialize it.
        self._statsGen = ostats
        if ostats is None:
            self._statsGen = NFLAnalyticsGenerator([season])

        self._statementsGenerator = NFLStatements(ostats=self._statsGen)

        self.playerPosMap = self._statsGen.generator.ccm.get_configuration_dict(NFL_DOMAIN_NAME, 905419267, 'Group')
        self.statDimMapDF = self._statsGen.generator.ccm.get_configuration_df(NFL_DOMAIN_NAME, 2056229753)

        self.ordinal = lambda n: "%d%s" % (n, "tsnrhtdd"[(math.floor(n / 10) % 10 != 1) * (n % 10 < 4) * n % 10::4])
        self._columns = ['entityType', 'qScore', 'questionRank', 'QuestionText', 'Option1', 'Option2', 'Answer',
                         'dimensionText', 'dimprep', 'statnameText', 'ObjectDescription', 'dimensions', 'statObject',
                         'statName', 'calculation', 'actionText', 'teamId', 'teamName', 'statValue',
                         'count', 'rank', 'statRange', 'nRanks', 'teamId2', 'teamName2', 'statValue2', 'count2',
                         'rank2', 'rankDiff', 'Sentiment', 'Template', 'AnswerTemplate']
        self._qfieldsDict = {
            'team': ['teamId', 'teamName', 'statValue', 'count', 'rank', 'nGames'],
            'player': ['teamId', 'teamName', 'playerName', 'playerPosition', 'statValue', 'count', 'rank', 'nGames'],
        }


    @contendo_classfunction_logger
    def _generate_all_questions(self, calculationsFilter=None, statsFilter=None):
        if not calculationsFilter:
            calculationsFilter = self.language['entities']['calculations'].keys()
        logger.debug('Generating all stats for calculation: %s', calculationsFilter)
        if not statsFilter:
            statsFilter = self._statsGen.statsDict.keys()
        logger.debug('Generating all stats: %s', statsFilter)
        outfile = open(NFL_TEMP_QUESTIONS_FILE, 'w')
        _writeHeaders = True
        self.questionsDF = pd.DataFrame(columns=self._columns)
        for key1, _statDict in self._statsGen.allStatsDict.items():
            _season, _statname, _object = key1
            if not _statname in statsFilter:
                continue
            logger.debug('Covering main key: %s', key1)
            for key2, statsTable in _statDict.items():
                _dims, _calculation = key2
                # filter irrelevant calculations
                if not _calculation in calculationsFilter:
                    continue

                # Check if the dimension allows questions.
                _dimensions = eval(_dims)
                _discard = False
                for _dim in _dimensions:
                    if _dim == 'all':
                        continue
                    _dimdef = self._statsGen.generator.dimentionsDict[_dim]
                    if _dimdef['DoQuestion'] != 1:
                        _discard = True
                        break
                if _discard:
                    continue
                # get the questions DF
                logger.debug('Getting questions for %s, %s', key1, key2)
                _questionsDF = self._get_questions_df(statsTable, _statname, _object, _dimensions, _calculation)
                # write to file
                if _questionsDF.shape[0] > 0:
                    _questionsDF.to_csv(outfile, index=False, header=_writeHeaders)
                    # write header only in the first time
                    _writeHeaders = False
            # break
        outfile.close()
        # loading the file, sorting & saving
        self.questionsDF = pd.read_csv(NFL_TEMP_QUESTIONS_FILE)
        self.questionsDF.sort_values(by=['questionRank', 'qScore'], axis=0, inplace=True, ascending=True)
        self.questionsDF.to_csv(NFL_QUESTIONS_FILE, index=False)

    @contendo_classfunction_logger
    def _get_questions_df(
            self,
            statsTable: pd.DataFrame,
            statName: str,
            object: str,
            dimensions: list,
            calculation: str,
            filterQuery: str = '',
            playerPosition: str = 'all'
    ) -> pd.DataFrame:

        result = pd.DataFrame()

        _questionsTable = self._generate_questions_from_stats(statsTable, statName, object, filterQuery, playerPosition)
        if _questionsTable.shape[0] > 0:
            _enrichedQuestionsTable = self._get_questions(_questionsTable, dimensions, calculation)
            if _enrichedQuestionsTable.shape[0] > 0:
                # logger.info(_enrichedQuestionsTable.columns)
                result = _enrichedQuestionsTable[self._columns]

        return result

    @contendo_classfunction_logger
    def _generate_questions_from_stats(
            self,
            statDF: pd.DataFrame,
            statName: str,
            object: str,
            filterQuery: str = '',
            playerPosition: str = 'all'
    ) -> pd.DataFrame:

        if statDF.shape[0] == 0:
            return pd.DataFrame()


        _teamObject = self._statsGen.generator.ptmapDict[object]['TeamType']
        _entityType = self._statsGen.generator.ptmapDict[object]['EntityType']
        _statdef = self.language['entities']['statnames'][statName][_teamObject]

        _fields = self._qfieldsDict[_entityType]
        _df1 = statDF[_fields]
        # filtering the position if required.
        if _entityType == 'player':
            if playerPosition!='all':
                #print(_df1)
                _df1 = _df1.query('playerPosition in {}'.format(self.playerPosMap[playerPosition]['PositionCodes'].split(',')))
                if _df1.shape[0] == 0:
                    return pd.DataFrame()


        # filter according to query:
        if filterQuery:
            _df1 = _df1.query(filterQuery)

        #_df1 = _df1.head(50)
        _df1 = _df1.head(120)
        _df1['on'] = 1
        _df1.set_index('on', inplace=True)
        _df1['statRange'] = _df1['statValue'].max() - _df1['statValue'].min()
        _df1['nRanks'] = _df1['rank'].nunique()
        _df2 = _df1[_fields]
        _joinedDF = _df1.join(_df2, lsuffix='', rsuffix='2')
        _joinedDF = _joinedDF.query('rank<rank2').copy()
        if _joinedDF.shape[0] == 0:
            return pd.DataFrame()
        _joinedDF.reset_index(inplace=True)
        _joinedDF['rankDiff'] = _joinedDF['rank2'] - _joinedDF['rank']
        _joinedDF['qScore'] = _joinedDF.apply(
            lambda x: (1 - math.fabs(x['statValue'] - x['statValue2']) / x['statRange']) * 100 +
                      (x['rank'] / x['nRanks'] * 350 if x['rank'] < x['nRanks'] * 0.2 else 70 + x['rank'] / x[
                          'nRanks'] * 30),
            axis=1
        )
        _sdfRow = dict(statDF.iloc[0])
        for key in ['dimensions', 'statObject', 'statName', 'calculation', 'entityType']:
            _joinedDF[key] = _sdfRow[key]
        _joinedDF.sort_values('qScore', ascending=True, inplace=True)
        _joinedDF['questionRank'] = round(_joinedDF['qScore'].rank(method='min', pct=True, ascending=True) * 100)
        _joinedDF['playerPos'] = playerPosition
        logger.debug('Position: %s, nItems: %d, nQuestions %d', playerPosition, _df1.shape[0], _joinedDF.shape[0])
        return _joinedDF

    @contendo_classfunction_logger
    def _get_questions(self, questionsTable: pd.DataFrame, dimensions: dict, calculation: str) -> pd.DataFrame():
        # get interesting questions for a stat table - numst is number of top and bottom questions
        # result may be up to 2Xnumst questions
        # interest here is non contextual and based on standard deviation only
        _questions = list()

        for i, row in questionsTable.iterrows():
            questionRow = dict(row)
            self._update_question_fields(questionRow)
            _questions.append(questionRow)

        retDF = pd.DataFrame(_questions, columns=self._columns)
        return retDF

    @contendo_classfunction_logger
    def _get_random_text_from_textlist(self, textsList: list) -> str:
        return textsList[random.randint(0, len(textsList) - 1)]

    @contendo_classfunction_logger
    def _update_question_fields(self, questionRow: dict) -> None:
        # get stat text
        _statObject = questionRow['statObject']
        _objectDef = self._statsGen.generator.ptmapDict[_statObject]
        _teamObject = _objectDef['TeamType']
        _entityType = questionRow['entityType']
        _objectName = questionRow[_entityType + 'Name']
        _objectName2 = questionRow[_entityType + 'Name2']
        if _teamObject == 'allTeam':
            # logger.error('Illegal statement row: %s', questionRow)
            _teamObject = 'defenseTeam'
        _statdef = self.language['entities']['statnames'][questionRow['statName']][_teamObject]
        _statdef = self.language['entities']['statnames'][questionRow['statName']][_teamObject]
        _statText = self._get_random_text_from_textlist(_statdef['statDescriptions'])
        # get the dimensions
        _dimList = eval(questionRow['dimensions'])
        if all(x == 'all' for x in _dimList):
            _dimensionText = ""
            _dimpreposition = ""
            _dimDoPre = True
            _dimDoPost = True
        else:
            _dimIndex = int(not _dimList.index('all'))
            _dim = _dimList[_dimIndex]
            _dimensionText = self.language['entities']['dimensions'][_dim]['text']
            _dimpreposition = self.language['entities']['dimensions'][_dimList[_dimIndex]]['prep']
            _dimDoPre = self._statsGen.generator.dimentionsDict[_dim]['DoPre']
            _dimDoPost = self._statsGen.generator.dimentionsDict[_dim]['DoPost']
        # calculate rank text
        _rank = int(questionRow['rank'])
        if _entityType == 'team' or _rank <= 5:
            _rankText = self._get_random_text_from_textlist(self.language['entities']['ranks'][str(_rank)])
        else:  # player under rank 6
            _rankText = self.ordinal(_rank) + ' in the NFL'
        _rankText2 = self.ordinal(int(questionRow['rank2']))
        # get object description
        _objectDescription = self._get_random_text_from_textlist(
            self.language['entities']['objectDefinitions'][_teamObject]['descriptions'])
        # get calculation description
        _calculation = questionRow['calculation']
        # get the template
        _sentiment = 'positive' if _statdef['isPositive'] else 'negative'
        _calc = _calculation
        if _calc.find('per_') == 0:
            _calc = 'stat'

        # get the question & answer templates
        while True:
            _template = self._get_random_text_from_textlist(self.language['templates']['questions']['all'])
            assert _dimDoPre or _dimDoPost, 'At lease on must be true.'
            if _dimDoPre and _template.find('dimprep') == -1:
                break
            if _dimDoPost and _template.find('dimprep') > -1:
                break

        _optionTemplate = self.language['templates']['questions']['option']
        _answerTemplate = self._get_random_text_from_textlist(
            self.language['templates']['questions']['answer'][_entityType])
        # check if threshold requires to change calculation
        _valueThreshold = self.language['entities']['calculations'][_calculation].get('valueThreshold', 0)
        if _calculation == 'per_game':
            if abs(questionRow['statValue']) <= _valueThreshold or abs(questionRow['statValue2']) <= _valueThreshold:
                questionRow['statValue'] = round(questionRow['statValue'] * questionRow['nGames'], 0)
                questionRow['statValue2'] = round(questionRow['statValue2'] * questionRow['nGames'], 0)
                _calculation = 'stat'
                questionRow['calculation'] = _calculation
        # get calculations
        _calculationDef = self.language['entities']['calculations'][_calculation]
        _calculationText = self._get_random_text_from_textlist(_calculationDef['texts'])
        _valueFormat = _calculationDef.get('format', _statdef.get('format', '{:.f}'))
        # get the action text
        # decide if to get the past or present text based on calculation type - per-* gets present.
        if _calculation.find('per_') > -1:
            _actionText = self._get_random_text_from_textlist(
                self.language['entities']['statnames'][questionRow['statName']][_teamObject]['presActionSingle'])
        else:
            _actionText = self._get_random_text_from_textlist(
                self.language['entities']['statnames'][questionRow['statName']][_teamObject]['pastAction'])

        # calculating the object text
        if _entityType == 'team':
            _objectText = self.language['entities']['statnames'][questionRow['statName']][_teamObject]['ObjectText']
        else:  # player
            if questionRow['playerPos']=='all':
                _objectText = _objectDef['ObjectText']
            else:
                _objectText = self.playerPosMap[questionRow['playerPos']]['PositionName']

        _questionFormat = {
            'dimensionText': _dimensionText,
            'dimprep': _dimpreposition,
            'statnameText': _statText,
            'objectText': _objectText,
            'ObjectDescription': _objectDescription,
            'calculationText': _calculationText,
            'actionText': _actionText,
            'sentimentText': self.language['entities']['calculations'][_calculation]['sentimantTexts'][_sentiment]
        }
        # adding team/player instructions
        for key in self.language['entities']['entity']['team']:
            _questionFormat[key] = self.language['entities']['entity'][_entityType][key]

        _questionText = _template.format(**_questionFormat).replace(' ?', '?')
        # remove double blanks
        while _questionText.find('  ') > -1:
            _questionText = _questionText.replace('  ', ' ')
        _questionText = _questionText.replace(' ?', '?')

        self._statementsGenerator._update_statement_text(questionRow)

        _answerFormat = {
            'sentence1': questionRow['Text'],
            'subject2': _objectName2,
            'rankText2': _rankText2,
            'X2': _valueFormat.format(float(questionRow['statValue2'])),
            'ObjectDescription': _objectDescription,
        }
        for key, value in _questionFormat.items():
            _answerFormat[key] = value

        _answerText = _answerTemplate.format(**_answerFormat)
        # remove double blanks
        while _answerText.find('  ') > -1:
            _answerText = _answerText.replace('  ', ' ')

        # keep the text, template & sentiment
        questionRow['QuestionText'] = _questionText
        questionRow['Option1'] = _objectName
        questionRow['Option2'] = _objectName2
        questionRow['Answer'] = _answerText
        questionRow['Sentiment'] = _sentiment
        questionRow['Template'] = _template
        questionRow['AnswerTemplate'] = _answerTemplate
        for key, value in _questionFormat.items():
            questionRow[key] = value

        return

    @contendo_classfunction_logger
    def generate_questionnaire(self, questionnairesInst: list) -> pd.DataFrame:
        _dims = self._statsGen.generator.dimentionsDict.items()
        _questionnaire = list()
        _questionsCount = dict()
        for _statName, _statDef in self._statsGen.statsDict.items():
            if _statDef['Doit'] != 'y':
                continue

            _teamObjects = [('team', team, '{}Team'.format(team)) for team in _statDef['TeamObjects'].split(',')]
            _playerObjects = [('player', player, '{}Player'.format(player)) for player in
                              _statDef['PlayerObjects'].split(',')]
            _statObjects = _teamObjects + _playerObjects
            # _statObjects = _playerObjects

            for _entityType, _objectType, _object in _statObjects:
                if _objectType in ['none', 'all', '']:
                    continue

                for _dim, _dimDef in self._statsGen.generator.dimentionsDict.items():
                    if _dimDef['DoQuestion'] != 1:
                        continue
                    # check if to do the combination of stat/dimension/objectType
                    if _dim != 'all':
                        _statDimMap = self.statDimMapDF.query(
                            'StatName=="{stat}" and Dimension=="{dim}" and ObjectType=="{obj}" and EntityType=="{entity}"'.format(
                                stat=_statName,
                                dim=_dim,
                                obj=_objectType,
                                entity=_entityType,
                            )
                        )
                        if _statDimMap.shape[0] == 0:
                            continue
                        _statDimRow = dict(_statDimMap.iloc[0])
                        _playerPositions = _statDimRow['Positions'].split(',')
                    else:
                        _playerPositions = list(self.playerPosMap.keys())

                    _calc = 'per_game' if _statDef['Type'] == 'stat' else _statDef['Type']
                    params = {
                        'statName': _statName,
                        'object': _object,
                        'dimensions': [_dim, 'all'],
                        'calculation': _calc,
                    }
                    _statsTable = self._statsGen.get_stats_table(_statName, _object, _dim, _calc)
                    if _statsTable.shape[0] == 0:
                        logger.debug('Discarding with zero results: %s', params)
                        continue
                    # discarding small-numbers (if dim is all, otherwise present.
                    if _dim=='all' and self._statementsGenerator._smallnum(_statsTable):
                        logger.debug('Discarding due to small stat: %s', params)
                        if _calc == 'per_game':
                            params['calculation'] = 'stat'
                            _statsTable = self._statsGen.get_stats_table(_statName, _object, _dim, 'stat')
                            if self._statementsGenerator._smallnum(_statsTable):
                                logger.debug('Discarding due to small stat: %s', params)
                                continue
                    # diluting the table
                    # if player:
                    #       need to participate in at least 1/3 of the games.
                    #       need to have a count above count average.
                    if _entityType == 'player':
                        _countLimit = int(_statsTable['count'].mean() - _statsTable['count'].std())
                        _nGamesLimit = int(_statsTable['nGames'].max()/6)
                        _statsTable = _statsTable.query('count>{} and nGames>{}'.format(_countLimit, _nGamesLimit)).copy()
                        if _statsTable.shape[0] == 0:
                            continue

                    # organize the table before further filtering.
                    _statsTable = _statsTable.reset_index().query('statValue!=0')
                    _isAscending = self._statsGen.generator.is_ascending(obj=_object, statDef=_statDef)
                    _statsTable.sort_values(by=['statValue'], ascending=_isAscending, inplace=True)
                    _statsTable['rank'] = _statsTable['statValue'].rank(method='min', ascending=_isAscending)

                    logger.debug('Starting : %s', params)
                    # _questionsDF = self._get_questions_df(statsTable=_statsTable, **params)
                    # if _questionsDF.shape[0] == 0:
                    #     logger.debug('Discarding with zero questions: %s', params)
                    #     continue

                    _nItems=0
                    for _playerPosition in _playerPositions:
                        # teams only calculate for empty playe position
                        if _entityType=='team' and _playerPosition!='all' or _entityType=='player' and _playerPosition=='all':
                            continue
                        if not self.playerPosMap[_playerPosition]['Doit']:
                            continue
                        _questionsDF = self._get_questions_df(
                            statsTable=_statsTable,
                            playerPosition=_playerPosition,
                            **params
                        )
                        if _questionsDF.shape[0] == 0:
                            #logger.debug('Discarding with zero questions: %s', params)
                            continue

                        for _questInst in questionnairesInst:
                            if 'query' in _questInst:
                                _filteredQDF = _questionsDF.query(_questInst['query'])
                                if _filteredQDF.shape[0] == 0:
                                    #logger.debug('Discarding with zero questions: %s, %s', _playerPosition, _questInst)
                                    continue
                            else:
                                _filteredQDF = _questionsDF

                            _nItems = _filteredQDF.shape[0]
                            _questionsCount[_questInst['package']] = _questionsCount.get(_questInst['package'], 0) + _nItems

                            if _playerPosition!='all':
                                _nqPerQ = min(_nItems, 4)
                                logger.debug('Adding stat: %s, pos: %s, nItems: %d, %d', _statName, _playerPosition,_nItems, _nqPerQ)
                            else:
                                _nqPerQ = 1

                            # run over all questionnaires
                            for _qid in range(1, _questInst['nq'] + 1):
                                _selected = list()
                                _idx = 0
                                for _nq in range(0, _nqPerQ):
                                    while True:
                                        if _nItems > 1:
                                            _idx = random.randint(0, int(_nItems - 1))
                                        if _idx in _selected:
                                            continue
                                        _question = dict(_filteredQDF.iloc[_idx])
                                        _question['questionnaireId'] = _qid
                                        _question['package'] = _questInst['package']
                                        _questionnaire.append(_question)
                                        _selected.append(_idx)
                                        break

                    logger.debug('Added %s, nItems: %d', params, _nItems)

        #
        logger.debug('Total questions: %s', dict_to_string(_questionsCount))
        _retDF = pd.DataFrame(_questionnaire, columns=['package', 'questionnaireId', 'qindex'] + self._columns)
        # shuffle the questions
        _retDF['qindex'] = 1
        _retDF.sort_values(by=['package', 'questionnaireId', 'qScore'], inplace=True)
        _retDF.to_csv(NFL_QUESTIONNAIRE_FILE, index=False)

        _groupedQDF = _retDF.groupby('package')
        for _packageName, _packageDF in _groupedQDF:
            logger.info('Starting package: %s', _packageName)
            self._reshuffle_questionnaire(_packageDF, _retDF)

        _retDF.sort_values(by=['package', 'questionnaireId', 'qindex'], inplace=True)
        #
        # remove duplicate questions and
        return _retDF

    @contendo_classfunction_logger
    def generate_weekly_questionnaires(self, week: int, nQuestionnaires: int = 1,
                                       season: str = NFL_DEFAULT_SEASON) -> pd.DataFrame:
        _weeklyGamesDict = self._statsGen.generator.nfldata.get_week_games_info(week=week, season=season)
        _questionnairesInstList = list([
            {
                'nq': nQuestionnaires,
                'package': 'all',
            }
        ])
        # _questionnairesInstList=list()
        for _gameName, _gameInfo in _weeklyGamesDict.items():
            _inst = {
                'nq': 1,
                'package': _gameName,
                # only compare between the two teams or players from these teams.
                'query': 'teamId in [{ht}, {at}] and teamId2 in [{ht}, {at}] or teamId==teamId2 and teamId in [{ht}, {at}]'.format(
                # 'query': 'teamId in [{ht}, {at}]'.format(
                    ht=_gameInfo['homeTeamid'],
                    at=_gameInfo['awayTeamid'],
                )
            }
            # logger.debug(dict_to_string(_inst))
            _questionnairesInstList.append(_inst)

        return self.generate_questionnaire(questionnairesInst=_questionnairesInstList)

    @contendo_classfunction_logger
    def _generate_weekly_games_data(self, week):
        _gamesDict = self._statsGen.generator.ccm.get_configuration_dict(NFL_DOMAIN_NAME, 1794595946, 'gamename')

        _weekGames = self._statsGen.generator.nfldata.get_week_games_info(week=week)
        _teamScores = self._statsGen.generator.nfldata.get_team_scores()
        _teamsData = ProUtils.pandas_df_to_dict(
            self._statsGen.generator.nfldata.get_teams_df(season=NFL_DEFAULT_SEASON).reset_index(), 'teamFullname')
        _landingGames = list()
        for _gameName, _gameInfo in _weekGames.items():
            _homeTeam = _gameInfo['homeTeamName']
            _awayTeam = _gameInfo['awayTeamName']
            _matchDef = {
                'matchname': _gameInfo['matchname'],
                'venue': '{}, {}'.format(_gameInfo['venueName'], _gameInfo['city'].split(','[0])),
                'startTime': str(_gameInfo['startTime']),
                'description': _gamesDict[_gameInfo['matchname']]['description'],
                'hometeam': {
                    'name': _gameInfo['homeTeamName'],
                    'shortName': _teamsData[_homeTeam]['teamName'],
                    'city': _teamsData[_homeTeam]['city'],
                    'score': '{}, {} home'.format(_teamScores[_homeTeam]['Scores'],
                                                  _teamScores[_homeTeam]['homeScores']),
                    'logoURL': '/images/team-logos/{}.gif'.format(_teamsData[_homeTeam]['teamId']),
                },
                'awayteam': {
                    'name': _gameInfo['awayTeamName'],
                    'shortName': _teamsData[_awayTeam]['teamName'],
                    'city': _teamsData[_awayTeam]['city'],
                    'score': '{}, {} away'.format(_teamScores[_awayTeam]['Scores'],
                                                  _teamScores[_awayTeam]['awayScores']),
                    'logoURL': '/images/team-logos/{}.gif'.format(_teamsData[_awayTeam]['teamId']),
                },
            }
            _landingGames.append(_matchDef)

        ProUtils.save_dict_to_jsonfile(NFL_TRIVIA_CONFIG, _landingGames)
        self._statsGen.generator.nfldata.bqu.upload_file_to_gcp(NFL_GCP_BUCKET, NFL_TRIVIA_CONFIG, NFL_TRIVIA_CONFIG,
                                                                timestamp=True)

    @contendo_classfunction_logger
    def _reshuffle_questionnaire(self, qDF: pd.DataFrame, mainDF: pd.DataFrame) -> None:
        _stats =  list()
        _players =  list()
        _topics =  list()
        _postponed = list()
        _qIndex = 1
        _lookback=5
        _topicLookback=4

        def _check_row(i, _row:dict, _qIndex:int) -> int:
            _statname = _row['statName']
            _entityType = _row['entityType']
            _topic = self._statsGen.statsDict[_statname]['Topic']
            _option1 = _row['Option1']
            if _statname in _stats[-_lookback:]:
                _postponed.append((i, _row))
                return _qIndex

            if _topic in _topics[-_topicLookback:]:
                _postponed.append((i, _row))
                return _qIndex

            if _entityType=='player':
                if _option1 in _players[-_lookback:]:
                    _postponed.append((i, _row))
                    return _qIndex
                else:
                    _players.append(_option1)
            else:
                _players.append("team")

            _stats.append(_statname)
            _topics.append(_topic)

            mainDF.at[i, 'qindex'] = _qIndex
            _qIndex+=1
            return _qIndex

        for i,row in qDF.iterrows():
            _row=dict(row)
            _qIndex = _check_row(i, _row, _qIndex)

        count = len(_postponed)*20
        while len(_postponed)>0:
            count -= 1
            i,_row = _postponed.pop(0)
            if len(_postponed)<=_lookback or count<0:
                mainDF.at[i, 'qindex'] = _qIndex
                _qIndex += 1
            else:
                _qIndex = _check_row(i, _row, _qIndex)
            if count==0:
                print(len(_postponed))


@contendo_function_logger
def test():
    logger.info('Starting...')
    os.chdir('{}/tmp/'.format(os.environ['HOME']))
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '{}/sportsight-tests.json'.format(os.environ['HOME'])
    _questionnairesInstList = list([
        {
            'nq': 10,
            'package': 'all',
        }
    ])
    week=16
    nflq = NFLQuestions(season=NFL_DEFAULT_SEASON, ostats=None)
    # nflq._generate_weekly_games_data(week)
    # _questionnaireDF = nflq.generate_weekly_questionnaires(week=week, nQuestionnaires=1)
    # _questionnaireDF.to_csv(NFL_QUESTIONNAIRE_FILE, index=False)
    # nflq._statsGen.generator.nfldata.bqu.upload_file_to_gcp(NFL_GCP_BUCKET, NFL_QUESTIONNAIRE_FILE, NFL_QUESTIONNAIRE_FILE, timestamp=True)
    _questionnaireDF = pd.read_csv(NFL_QUESTIONNAIRE_FILE).query('package!="all"')
    _groupedQDF = _questionnaireDF.groupby('package')
    for _packageName, _packageDF in _groupedQDF:
        logger.info('Starting package: %s', _packageName)
        nflq._reshuffle_questionnaire(_packageDF, _questionnaireDF)

    _questionnaireDF.sort_values(by=['package', 'questionnaireId', 'qindex'], inplace=True)
    _questionnaireDF.to_csv(NFL_QUESTIONNAIRE_FILE, index=False)
    # return
    _questionnaireDF['teams'] = _questionnaireDF.apply(lambda x: x['teamName'] + '-' + x['teamName2'], axis=1)
    _qdfAnalyzed = _questionnaireDF.groupby('teamName', as_index=True).agg({'teamName2': 'count'}).sort_values(by='teamName2', ascending=False).reset_index()
    _qdfAnalyzed.columns = ['teamName', 'winCount']
    std = _qdfAnalyzed['winCount'].std()
    avg = _qdfAnalyzed['winCount'].mean()
    _qdfAnalyzed['stdDiff'] = (_qdfAnalyzed['winCount']-avg)/std
    print(avg, std)
    print(_qdfAnalyzed)
    return
    # nflq._generate_all_questions(calculationsFilter=['stat', 'ratio', 'pct', 'per_game', 'per_drive'], statsFilter=[])
    # nflq._generate_all_questions(calculationsFilter=['stat', 'ratio', 'per_game'], statsFilter=[])
    nflq._generate_all_questions(calculationsFilter=['stat', 'ratio', 'per_game'],
                                 statsFilter=['offensePoints', 'fumbles', 'yardsRushed', 'completionRate'])
    # nflq._generate_all_questions(calculationsFilter=['ratio'], statsFilter=[])
    # Sort the sentences
    # uploading the sentences - uncomment only when you want to upload them to the cloud and the demo.
    # nflq._ostats.generator.nfldata.bqu.upload_file_to_gcp(bucketName=NFL_GCP_BUCKET, inFileName=NFL_SENTENCES_FILE, targerFileName=NFL_SENTENCES_FILE, timestamp=True)
    logger.info('Done')


if __name__ == '__main__':
    contendo_logging_setup(default_level=logging.DEBUG)
    pd.set_option('display.max_rows', 1500)
    pd.set_option('display.max_columns', 1500)
    pd.set_option('display.width', 20000)
    test()
