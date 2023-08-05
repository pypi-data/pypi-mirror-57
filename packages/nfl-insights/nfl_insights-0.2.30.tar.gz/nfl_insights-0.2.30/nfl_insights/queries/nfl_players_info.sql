WITH
  teams AS (
  SELECT
    id AS teamId,
    season,
    abbreviation AS teamAbv,
    FORMAT('%s %s',city, name) AS teamFullname
  FROM
    `sportsight-tests.NFL_Data.game_boxscore_*`
  LEFT JOIN
    UNNEST ( references.teamReferences )
  GROUP BY
    teamId,
    season,
    abbreviation,
    city,
    name ),
  players AS (
  SELECT
    season,
    id AS playerId,
    currentTeam.id AS teamId,
    MAX(firstName) AS firstName,
    MAX(lastName) AS lastName,
    MAX(age) AS age,
    MAX(primaryPosition) AS primaryPosition,
    MAX(height) AS height,
    MAX(weight) AS weight,
    MAX(handedness.throws) AS handedness,
    MAX(birthCountry) AS birthCountry,
    MAX(birthCity) AS birthCity,
    MAX(birthDate) AS birthDate
  FROM
    `NFL_Data.game_boxscore_*`
  LEFT JOIN
    UNNEST (references.playerReferences)
  GROUP BY
    season,
    teamId,
    PlayerId)
SELECT
  players.playerId,
  players.firstName,
  players.lastName,
  players.teamId,
  players.season,
  FORMAT('%s %s (%s)', players.firstName, players.lastName, teams.teamAbv) AS playerFullname,
  teams.teamFullname
FROM
  players
LEFT JOIN
  teams
ON
  players.teamId = teams.teamId
  AND players.season=teams.season
GROUP BY
  players.playerId,
  players.firstName,
  players.lastName,
  players.teamId,
  players.season,
  teamAbv,
  teamFullname
HAVING
  teamid IS NOT NULL
  AND playerId IS NOT NULL
ORDER BY
  playerid,
  season DESC,
  teamid