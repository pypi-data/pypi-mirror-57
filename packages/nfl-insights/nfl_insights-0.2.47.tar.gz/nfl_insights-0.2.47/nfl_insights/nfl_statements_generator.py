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


class NFLStatements:
    @contendo_classfunction_logger
    def __init__(self, season=NFL_DEFAULT_SEASON, ostats=None):
        # load the definition file
        self.language = ProUtils.get_dict_from_jsonfile(eval(NFL_LANGUAGE_FILENAME_EVAL))
        # get ostats from external caller or initialize it.
        self._statsGen = ostats
        if ostats is None:
            self._statsGen = NFLAnalyticsGenerator([season])

        self.ordinal = lambda n: "%d%s" % (n, "tsnrhtdd"[(math.floor(n / 10) % 10 != 1) * (n % 10 < 4) * n % 10::4])

        self._columns = ['entityType', 'Interest', 'TextOK', 'CompOK', 'Text', 'subject', 'rankText', 'dimensionText', 'dimprep',
                         'statnameText', 'ObjectDescription', 'calculationText', 'actionText', 'X', 'teamName',
                         'playerName', 'dimensions', 'statObject', 'statName', 'statValue', 'absFactor', 'rank',
                         'nItems', 'calculation', 'Sentiment', 'Template', 'CompTemplate']

    @contendo_classfunction_logger
    def _generate_all_statements(self, calculationsFilter=None, statsFilter=None):
        if not calculationsFilter:
            calculationsFilter = self.language['entities']['calculations'].keys()
        logger.debug('Generating all stats for calculation: %s', calculationsFilter)
        if not statsFilter:
            statsFilter = self._statsGen.statsDict.keys()
        logger.debug('Generating all stats: %s', statsFilter)
        _writeHeaders = True
        _statementsList = list()
        self.statementsDF = pd.DataFrame(columns=self._columns)
        for key1, _statDict in self._statsGen.allStatsDict.items():
            _season, _statname, _object = key1
            if not _statname in statsFilter:
                continue
            logger.debug('Covering main key: %s', key1)
            for key2, statTable in _statDict.items():
                _dims, _calculation = key2
                if not _calculation in calculationsFilter:
                    continue
                if self._smallnum(statTable):
                    continue
                _dimensions = eval(_dims)
                _statements = self._get_statements_list(statTable, _statname, _object, _dimensions, _calculation)
                _statementsList += _statements

        # loading the file, sorting & saving
        self.statementsDF = pd.DataFrame(_statementsList, columns=self._columns)
        self.statementsDF.sort_values(by=['Interest', 'nItems', 'absFactor'], axis=0, inplace=True, ascending=False)
        self.statementsDF.to_csv(NFL_SENTENCES_FILE, index=False)

    @contendo_classfunction_logger
    def _refactor_definition_json(self):
        _statDefs = self._statsGen.statsDict
        # updating the stats statements per team.
        _statements = self.language['entities']['statnames']
        for _statname, _statDef in _statDefs.items():
            if _statDef['Doit'] != 'y':
                continue
            _statStatements = _statements.get(_statname, dict())

            _teamObjects = [('team', team, '{}Team'.format(team)) for team in _statDef['TeamObjects'].split(',')]
            _playerObjects = [] #[('player', player, '{}Player'.format(player)) for player in _statDef['PlayerObjects'].split(',')]
            _statObjects = _teamObjects + _playerObjects
            _newStatDef = dict()

            for _statObject in _statObjects:
                _entityType, _obj, _objectType = _statObject
                if _obj in ['none', 'all', '']:
                    continue

                _objectSentences = _statStatements.get(_objectType, dict())
                _objectDef = self._statsGen.generator.ptmapDict[_objectType]
                _newObjectDef = dict()
                _newObjectDef['isRelevant'] = True
                if _obj in _statDef['Direction'].split(',') and _obj not in _statDef['Sentiment'].split(','):
                    _newObjectDef['isPositive'] = True
                else:
                    _newObjectDef['isPositive'] = False
                _newObjectDef['statDescriptions'] = _objectSentences.get('statDescriptions', [_statname + '-xxxx'])
                _newObjectDef['format'] = _statDef['Format']
                # which text to show for ObjectText
                if _statDef['ShowObjText']:
                    _newObjectDef['ObjectText'] = _objectDef['ObjectText']
                else:
                    _newObjectDef['ObjectText'] = _objectDef['EntityType']

                # copy the isAllowed if exists
                if 'isAllowed' in _objectSentences:
                    _newObjectDef['isAllowed'] = True

                if 'isPositive' in _newObjectDef:
                    if _newObjectDef['isPositive']:
                        _newObjectDef['presActionSingle'] = _statDef['PresPosSingle'].split(',')
                        _newObjectDef['presActionPlural'] = _statDef['PresPosPlural'].split(',')
                        _newObjectDef['pastAction'] = _statDef['PastPos'].split(',')
                        _newObjectDef['adverbText'] = [""]
                    else:
                        _newObjectDef['presActionSingle'] = _statDef['PresNegSingle'].split(',')
                        _newObjectDef['presActionPlural'] = _statDef['PresNegPlural'].split(',')
                        _newObjectDef['pastAction'] = _statDef['PastNeg'].split(',')
                        _newObjectDef['adverbText'] = _statDef['NegAdverb'].split(',')
                _newStatDef[_objectType] = _newObjectDef
            _statements[_statname] = _newStatDef

        _templateDefFilenameNew = eval(NFL_LANGUAGE_FILENAME_EVAL) + '_new'
        ProUtils.save_dict_to_jsonfile(_templateDefFilenameNew, self.language)
        return

    @contendo_classfunction_logger
    def _get_statements_list(self, statTable: pd.DataFrame, statName:str, object:str, dimensions:str, calculation:str) -> list:
        result = pd.DataFrame(columns=self._columns)
        if 'all' not in dimensions:
            return result

        #_statsTable = statTable.head(80)
        distMeasure = self.get_dispersion(statTable, 10)
        if distMeasure < 0.15:
            numst = 1
        elif distMeasure < 0.3:
            numst = 3
        else:
            numst = 5

        rawStatements = self._get_statements(statTable, statName, object, dimensions, calculation, numst)
        return rawStatements

    @contendo_classfunction_logger
    def get_dispersion(self, statTable, factor):
        # find l2norm bsed measure of diversity
        statTable['statValue'] = statTable['statValue'].fillna(0)
        _arr = np.array(statTable['statValue'])
        a = _arr / sum(_arr)
        a = a ** factor
        zoDistribution = a / sum(a)
        l2Norm = np.linalg.norm(zoDistribution, ord=2)
        minUniformity = 1 / np.sqrt(len(zoDistribution))
        distMeasure = (l2Norm - minUniformity) / (1 - minUniformity)
        return distMeasure

    @contendo_classfunction_logger
    def _get_statements(self, statTable: pd.DataFrame, statName:str, object:str, dimensions:str, calculation:str, numst:int) -> list:
        # get interesting statements for a stat table - numst is number of top and bottom statements
        # result may be up to 2Xnumst statements
        # interest here is non contextual and based on standard deviation only
        _statements = list()
        # get entity-type (team/player)
        _entityType = self._statsGen.generator.ptmapDict[object]['EntityType']
        # team takes list top and bottom, player takes only top
        _indices = list(statTable.index[0:numst])
        if _entityType=='team':
            _indices += list(statTable.index[len(statTable) - numst:len(statTable)])

        _interestThreshold = self.language['config']['interestThreshold']
        _valueThreshold = self.language['entities']['calculations'][calculation].get('valueThreshold', 0)
        for _ind in (_indices):
            _statementRow = dict(statTable.loc[_ind])
            # skip if stat value is smallet than value-threshold (defined per-calculation).
            if abs(_statementRow['statValue']) < _valueThreshold:
                continue

            _absFactor = abs(_statementRow['stdFactor']) - _interestThreshold
            if _absFactor > 0:
                _statementRow['Interest'] = min(1, _absFactor)
                _statementRow['absFactor'] = _absFactor
                self._update_statement_text(_statementRow)
                # add comparison only to teams.
                if _entityType == 'team':
                    _statementRow["Text"] += '. ' + self._get_comparison_text(statTable, _statementRow)
                    _statementRow["Text"] = _statementRow["Text"].replace(' .', '.')

                # appens statements to list
                _statements.append(_statementRow)

        return _statements  # pd.DataFrame(_statements)

    @contendo_classfunction_logger
    def _get_random_text_from_textlist(self, textsList: list) -> str:
        return textsList[random.randint(0, len(textsList) - 1)]

    @contendo_classfunction_logger
    def _update_statement_text(self, statementRow: dict) -> None:
        # get stat text
        _teamObject = self._statsGen.generator.ptmapDict[statementRow['statObject']]['TeamType']
        _entityType = statementRow['entityType']
        if _teamObject=='allTeam':
            #logger.error('Illegal statement row: %s', statementRow)
            _teamObject='defenseTeam'
        _statdef = self.language['entities']['statnames'][statementRow['statName']][_teamObject]
        _statsentences = _statdef['statDescriptions']
        _statText = _statsentences[random.randint(0, len(_statsentences) - 1)]
        # get the dimensions
        _dimList = eval(statementRow['dimensions'])
        if all(x == 'all' for x in _dimList):
            _dimensionText = ""
            _dimpreposition = ""
            _dimDoPre = True
        else:
            _dimIndex = int(not _dimList.index('all'))
            _dim = _dimList[_dimIndex]
            _dimensionText = self.language['entities']['dimensions'][_dim]['text']
            _dimpreposition = self.language['entities']['dimensions'][_dimList[_dimIndex]]['prep']
            _dimDoPre = self._statsGen.generator.dimentionsDict[_dim]['DoPre']

        # calculate rank text
        _rank = int(statementRow['rank'])
        if _entityType=='team' or _rank<=5:
            _rankText = self._get_random_text_from_textlist(self.language['entities']['ranks'][str(_rank)])
        else: # player under rank 6
            _rankText = self.ordinal(_rank) + ' in the NFL'

        # get object description
        _objectDescription = "" #self._get_random_text_from_textlist(self.language['entities']['objectDefinitions'][_teamObject]['descriptions'])
        # get calculation description
        _calculation = statementRow['calculation']
        _calculationDef = self.language['entities']['calculations'][_calculation]
        _calculationText = self._get_random_text_from_textlist(_calculationDef['texts'])
        # get the text template
        _sentiment = 'positive' if _statdef['isPositive'] else 'negative'
        _calc = _calculation
        if _calc.find('per_') == 0:
            _calc = 'stat'

        # get the action text
        # decide if to get the past or present text based on calculation type - per-* gets present.
        if _calculation.find('per_') > -1:
            _presAction = 'presActionPlural' if _entityType=='team' else 'presActionSingle'
            _actionText = self._get_random_text_from_textlist(
                self.language['entities']['statnames'][statementRow['statName']][_teamObject][_presAction]
            )
        else:
            _actionText = self._get_random_text_from_textlist(
                self.language['entities']['statnames'][statementRow['statName']][_teamObject]['pastAction']
            )
        _adverbText = self._get_random_text_from_textlist(self.language['entities']['statnames'][statementRow['statName']][_teamObject]['adverbText'])

        while True:
            _template = self._get_random_text_from_textlist(self.language['templates']['statements'][_calc][_sentiment])
            if _dimDoPre or _template.find('dimprep')>-1:
                break
            #logger.debug('Illegal template for dimension %s', _dim)

        # format the value
        _valueFormat = _calculationDef.get('format', _statdef.get('format', '{:.f}'))
        _statFormatedValue = _valueFormat.format(float(statementRow['statValue']))

        _statementFormat = {
            'subject': statementRow['{entityType}Name'.format(**statementRow)], #team/player name accordingly
            'rankText': _rankText,
            'dimensionText': _dimensionText,
            'dimprep': _dimpreposition,
            'statnameText': _statText,
            'ObjectDescription': _objectDescription,
            'calculationText': _calculationText,
            'actionText': _actionText,
            'adverbText': _adverbText,
            'X': _statFormatedValue,
        }
        # adding team/player instructions
        for key in self.language['entities']['entity']['team']:
            _statementFormat[key] = self.language['entities']['entity'][_entityType][key]

        _statementText = _template.format(**_statementFormat)
        # remove double blanks
        while _statementText.find('  ') > -1:
            _statementText = _statementText.replace('  ', ' ')

        # keep the text, template & sentiment
        statementRow['Text'] = _statementText
        statementRow['Sentiment'] = _sentiment
        statementRow['Template'] = _template
        for key, value in _statementFormat.items():
            statementRow[key] = value

        return

    def _smallnum(self, statTable: pd.DataFrame) -> bool:
        result = False
        if statTable.shape[0] == 0:
            return result
        if statTable['rank'].nunique() <= 6:
            result = True
        if statTable['calculation'].iloc[0] == "per_game" and statTable["statValue"].max() < 5 and "TD" not in \
                statTable["statName"].iloc[0]:
            result = True
        if statTable['calculation'].iloc[0] == "per_drive" and statTable["statValue"].max() < 2:
            result = True
        return result

    @contendo_classfunction_logger
    def _get_comparison_text(self, statTable, statementRow):
        candidate = ""
        # default is compare to average
        avgdif = statementRow["avgDiff%"]
        thresh = 1 + abs(statementRow["avgDiff%"])
        if avgdif > 0:
            position = "higher"
            if avgdif > 100:
                diff = str(round((avgdif + 100) / 100, 1)) + " times"
            else:
                diff = str(int(round(avgdif, 0))) + "%"
        else:
            position = "lower"
            diff = str(int(round(abs(avgdif), 0))) + "%"
        candidateTemplate = self._get_random_text_from_textlist(self.language["entities"]['comparisons']["average"])
        candidate = candidateTemplate.format(diff=diff, position=position)
        # process the difference from the next team

        if avgdif < 0:
            position = "less than"
            comprank = statementRow["rank"] - 1
        else:
            position = "more than"
            comprank = statementRow["rank"] + 1
        if any(statTable["rank"] == comprank):
            comprow = dict(statTable.loc[statTable["rank"] == comprank].iloc[0])
            facdif = abs(statementRow["stdFactor"]) - comprow["absStdFactor"]
            if facdif / abs(statementRow["stdFactor"]) > 0.3 and comprow["statValue"] != 0:
                diff = str(int(round(
                    abs(statementRow["statValue"] - comprow["statValue"]) * 100 / comprow["statValue"],
                    0))) + "%"
                compentity = comprow["teamName"]
                comprank = str(int(comprow["rank"]))
                candidateTemplate = self._get_random_text_from_textlist(
                    self.language["entities"]['comparisons']["next"])
                candidate = candidateTemplate.format(diff=diff, position=position, compentity=compentity,
                                                     comprank=self.ordinal(int(comprank)))

        statementRow['CompTemplate'] = candidateTemplate
        statementRow['TextOK'] = True
        statementRow['CompOK'] = True

        return candidate


@contendo_function_logger
def test():
    logger.info('Starting...')
    os.chdir('{}/tmp/'.format(os.environ['HOME']))
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '{}/sportsight-tests.json'.format(os.environ['HOME'])
    nfls = NFLStatements(season=NFL_DEFAULT_SEASON, ostats=None)
    # nfls._refactor_definition_json()
    # return
    nfls._generate_all_statements(calculationsFilter=['stat', 'ratio', 'pct', 'per_game', 'per_drive'], statsFilter=[])
    # nfls._generate_all_statements(calculationsFilter=['pct'], statsFilter=['offensePoints', 'fumbles', 'yardsRushed'])
    # nfls._generate_all_statements(calculationsFilter=['per_game', 'ratio', 'pct'], statsFilter=['defensePoints', 'fumbles', 'interceptionReturnYds', 'rushTD', 'kickingPoints', 'yardsPerCatch', 'completionRate'])
    # Sort the sentences
    # uploading the sentences - uncomment only when you want to upload them to the cloud and the demo.
    # nfls._ostats.generator.nfldata.bqu.upload_file_to_gcp(bucketName=NFL_GCP_BUCKET, inFileName=NFL_SENTENCES_FILE, targerFileName=NFL_SENTENCES_FILE, timestamp=True)
    logger.info('Done')


if __name__ == '__main__':
    contendo_logging_setup(default_level=logging.DEBUG)
    pd.set_option('display.max_columns', 1500)
    pd.set_option('display.width', 20000)
    test()
