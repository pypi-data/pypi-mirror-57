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
        self._teamStats = ostats
        if ostats is None:
            self._teamStats = NFLTeamAnalytics([season])

        self._statementsGenerator = NFLStatements(ostats=self._teamStats)

        self.ordinal = lambda n: "%d%s" % (n, "tsnrhtdd"[(math.floor(n / 10) % 10 != 1) * (n % 10 < 4) * n % 10::4])
        self._columns = ['qScore', 'questionRank', 'QuestionText', 'Option1', 'Option2', 'Answer', 'dimensionText', 'dimprep', 'statnameText',
                         'ObjectDescription', 'dimensions', 'statObject', 'statName', 'calculation', 'teamId',
                         'teamName', 'statValue', 'count', 'rank', 'statRange', 'nRanks', 'teamId2', 'teamName2',
                         'statValue2', 'count2', 'rank2', 'rankDiff', 'Sentiment', 'Template', 'AnswerTemplate']

    @contendo_classfunction_logger
    def _generate_all_questions(self, calculationsFilter=None, statsFilter=None):
        if not calculationsFilter:
            calculationsFilter = self.language['entities']['calculations'].keys()
        logger.debug('Generating all stats for calculation: %s', calculationsFilter)
        if not statsFilter:
            statsFilter = self._teamStats.statsDict.keys()
        logger.debug('Generating all stats: %s', statsFilter)
        outfile = open(NFL_TEMP_QUESTIONS_FILE, 'w')
        _writeHeaders = True
        self.questionsDF = pd.DataFrame(columns=self._columns)
        for key1, _statDict in self._teamStats.allStatsDict.items():
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
                    _dimdef = self._teamStats.generator.dimentionsDict[_dim]
                    if _dimdef['DoQuestion']!=1:
                        _discard=True
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
    def _get_questions_df(self, statsTable:pd.DataFrame, statName: str, object: str, dimensions: list, calculation: str) -> pd.DataFrame:
        result=pd.DataFrame()

        _questionsTable = self._generate_questions_from_stats(statsTable, statName, object)
        if _questionsTable.shape[0] > 0:
            _enrichedQuestionsTable = self._get_questions(_questionsTable, dimensions, calculation)
            if _enrichedQuestionsTable.shape[0] > 0:
                # logger.info(_enrichedQuestionsTable.columns)
                result = _enrichedQuestionsTable[self._columns]

        return result

    @contendo_classfunction_logger
    def _generate_questions_from_stats(self, statDF: pd.DataFrame, statName:str, object:str) -> pd.DataFrame:

        if statDF.shape[0]==0:
            return pd.DataFrame()

        _statdef = self.language['entities']['statnames'][statName][object]
        #_isAscending  = not _statdef['isPositive']

        _fields = ['teamId', 'teamName', 'statValue', 'count', 'rank', 'nGames']
        _df1 = statDF.reset_index().query('statValue!=0')[_fields]
        #_df1['rank'] = _df1['statValue'].rank(method='dense', ascending=_isAscending)
        _df1['on'] = 1
        _df1.set_index('on', inplace=True)
        _df1['statRange'] = _df1['statValue'].max() - _df1['statValue'].min()
        _df1['nRanks'] = _df1['rank'].nunique()
        #if _df1['nRanks']<=3:
        #    return pd.DataFrame()

        #_df2 = _df1[['teamId', 'teamName', 'statValue', 'count', 'rank', 'nGames', 'nDrives', 'nPlays']]
        _df2 = _df1[_fields]
        _joinedDF = _df1.join(_df2, lsuffix='', rsuffix='2')
        _joinedDF = _joinedDF.query('rank<rank2').copy()
        if _joinedDF.shape[0]==0:
            return pd.DataFrame()
        _joinedDF.reset_index(inplace=True)
        _joinedDF['rankDiff'] = _joinedDF['rank2'] - _joinedDF['rank']
        _joinedDF['qScore'] =  _joinedDF.apply(
            lambda x: (1-math.fabs(x['statValue']-x['statValue2'])/x['statRange'])*100 +
                       (x['rank']/x['nRanks']*350 if x['rank']<x['nRanks']*0.2 else 70+x['rank']/x['nRanks']*30),
            axis=1
        )
        _sdfRow = dict(statDF.iloc[0])
        for key in ['dimensions', 'statObject', 'statName', 'calculation']:
            _joinedDF[key] = _sdfRow[key]
        _joinedDF.sort_values('qScore', ascending=True, inplace=True)
        _joinedDF['questionRank'] = round(_joinedDF['qScore'].rank(method='min', pct=True, ascending=True)*100)
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
        _statdef = self.language['entities']['statnames'][questionRow['statName']][questionRow['statObject']]
        _statText = self._get_random_text_from_textlist(_statdef['statDescriptions'])
        # get the dimensions
        _dimList = eval(questionRow['dimensions'])
        if all(x == 'all' for x in _dimList):
            _dimensionText = ""
            _dimpreposition = ""
        else:
            _dimIndex = int(not _dimList.index('all'))
            _dimensionText = self.language['entities']['dimensions'][_dimList[_dimIndex]]['text']
            _dimpreposition = self.language['entities']['dimensions'][_dimList[_dimIndex]]['prep']
        # calculate rank text
        _rankText1 = self._get_random_text_from_textlist(self.language['entities']['ranks'][str(int(questionRow['rank']))])
        _rankText2 = self.ordinal(int(questionRow['rank2']))
        # get object description
        _objectDescription = self._get_random_text_from_textlist(self.language['entities']['objectDefinitions'][questionRow['statObject']]['descriptions'])
        # get calculation description
        _calculation = questionRow['calculation']
        # get the template
        _sentiment = 'positive' if _statdef['isPositive'] else 'negative'
        _calc = _calculation
        if _calc.find('per_') == 0:
            _calc = 'stat'
        _template = self._get_random_text_from_textlist(self.language['templates']['questions'][_calc][_sentiment])
        _optionTemplate = self.language['templates']['questions']['option']
        _answerTemplate = self._get_random_text_from_textlist(self.language['templates']['questions']['answer'])
        # format the value
        _pastAction=self._get_random_text_from_textlist(self.language['entities']['statnames'][questionRow['statName']][questionRow['statObject']]['pastAction'])
        _presAction=self._get_random_text_from_textlist(self.language['entities']['statnames'][questionRow['statName']][questionRow['statObject']]['presActionSingle'])
        # check if threshold requires to change calculation
        _valueThreshold = self.language['entities']['calculations'][_calculation].get('valueThreshold', 0)
        if _calculation=='per_game':
            if abs(questionRow['statValue']) <= _valueThreshold or abs(questionRow['statValue2']) <= _valueThreshold:
                questionRow['statValue'] = round(questionRow['statValue']*questionRow['nGames'],0)
                questionRow['statValue2'] = round(questionRow['statValue2']*questionRow['nGames'],0)
                _calculation = 'stat'
                questionRow['calculation'] = _calculation
        # get calculations
        _calculationDef = self.language['entities']['calculations'][_calculation]
        _calculationText = self._get_random_text_from_textlist(_calculationDef['texts'])
        _valueFormat = _calculationDef.get('format', _statdef.get('format', '{:.f}'))

        _questionFormat = {
            'dimensionText': _dimensionText,
            'dimprep': _dimpreposition,
            'statnameText': _statText,
            'ObjectDescription': _objectDescription,
            'calculationText': _calculationText,
            'presAction': _presAction,
            'pastAction': _pastAction,
        }
        _questionText = _template.format(**_questionFormat).replace(' ?', '?')
        # remove double blanks
        while _questionText.find('  ') > -1:
            _questionText = _questionText.replace('  ', ' ')
        _questionText = _questionText.replace(' ?', '?')

        self._statementsGenerator._update_statement_text(questionRow)

        _answerFormat = {
            'sentence1': questionRow['Text'],
            'subject2': questionRow['teamName2'],
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
        questionRow['Option1'] = _optionTemplate.format(subject=questionRow['teamName'], **_questionFormat)
        questionRow['Option2'] = _optionTemplate.format(subject=questionRow['teamName2'], **_questionFormat)
        questionRow['Answer'] = _answerText
        questionRow['Sentiment'] = _sentiment
        questionRow['Template'] = _template
        questionRow['AnswerTemplate'] = _answerTemplate
        for key, value in _questionFormat.items():
            questionRow[key] = value

        return

    @contendo_classfunction_logger
    def generate_questionnaire(self, nQuestionnaires=1) -> pd.DataFrame:
        _dims = self._teamStats.generator.dimentionsDict.items()
        _questionnaire = list()
        for _statName, _statDef in self._teamStats.statsDict.items():
            if _statDef['Doit'] !='y':
                continue

            _teamObjects = _statDef['TeamObjects'].split(',')
            for _obj in _teamObjects:
                _dim='all'
                _object = _obj+'Team' #_teamObjects[random.randint(0, len(_teamObjects) - 1)]+'Team'
                _calc = 'per_game' if _statDef['Type'] == 'stat' else _statDef['Type']
                params = {
                    'statsTable': self._teamStats.get_stats_table(_statName, _object, _dim, _calc),
                    'statName': _statName,
                    'object': _object,
                    'dimensions': [_dim, 'all'],
                    'calculation': _calc,
                }
                if params['statsTable'].shape[0]==0:
                    params.pop('statsTable')
                    logger.debug('Discarding with zero results: %s', params)
                    continue
                _questionsDF = self._get_questions_df(**params)
                params.pop('statsTable')
                if _questionsDF.shape[0]==0:
                    logger.debug('Discarding with zero questions: %s', params)
                    continue
                params['nItems'] = _questionsDF.shape[0]
                logger.debug('Adding %s', params)
                for _qid in range(1,nQuestionnaires):
                    if params['nItems']<=90:
                        params['item'] = random.randint(0, _questionsDF.shape[0] - 1)
                    else:
                        params['item'] = random.randint(0, int(_questionsDF.shape[0]/2))
                    _question = dict(_questionsDF.iloc[params['item']])
                    _question['questionnaireId'] = _qid
                    _questionnaire.append(_question)
        #
        retDF = pd.DataFrame(_questionnaire, columns=['questionnaireId']+self._columns)
        retDF.sort_values(by=['questionnaireId', 'qScore'], inplace=True)
        return retDF


@contendo_function_logger
def test():
    logger.info('Starting...')
    os.chdir('{}/tmp/'.format(os.environ['HOME']))
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '{}/sportsight-tests.json'.format(os.environ['HOME'])
    nflq = NFLQuestions(season=NFL_DEFAULT_SEASON, ostats=None)
    _questionnareDF = nflq.generate_questionnaire(nQuestionnaires=1000)
    _questionnareDF.to_csv(NFL_QUESTIONNAIRE_FILE, index=False)
    nflq._teamStats.generator.nfldata.bqu.upload_file_to_gcp(NFL_GCP_BUCKET, NFL_QUESTIONNAIRE_FILE,
                                      NFL_QUESTIONNAIRE_FILE, timestamp=True)
    return
    # nflq._refactor_definition_json()
    # return
    #nflq._generate_all_questions(calculationsFilter=['stat', 'ratio', 'pct', 'per_game', 'per_drive'], statsFilter=[])
    #nflq._generate_all_questions(calculationsFilter=['stat', 'ratio', 'per_game'], statsFilter=[])
    nflq._generate_all_questions(calculationsFilter=['stat', 'ratio', 'per_game'], statsFilter=['offensePoints', 'fumbles', 'yardsRushed', 'completionRate'])
    #nflq._generate_all_questions(calculationsFilter=['ratio'], statsFilter=[])
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
