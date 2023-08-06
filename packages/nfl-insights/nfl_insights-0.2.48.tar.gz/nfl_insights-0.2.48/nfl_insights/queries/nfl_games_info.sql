WITH
  venues AS (
  SELECT
    id AS venueId,
    city
  FROM
    `sportsight-tests.NFL_Data.seasonal_games`
  LEFT JOIN
    UNNEST (Seasondata.references.venueReferences) ),
  teams AS (
  SELECT
    id AS teamId,
    season,
    FORMAT('%s %s',city, name) AS teamFullname
  FROM
    `sportsight-tests.NFL_Data.game_boxscore_*`
  LEFT JOIN
    UNNEST ( references.teamReferences )
  GROUP BY
    teamId,
    season,
    city,
    name ),
  games AS (
  SELECT
    schedule.id AS gameid,
    FORMAT('%s-%s-%s', FORMAT_TIMESTAMP('%Y%d%m', schedule.startTime), schedule.homeTeam.abbreviation, schedule.awayTeam.abbreviation) AS matchname,
    schedule.homeTeam.id AS homeTeamid,
    schedule.awayTeam.id AS awayTeamid,
    schedule.homeTeam.abbreviation AS homeTeamAbv,
    schedule.awayTeam.abbreviation AS awayTeamAbv,
    schedule.startTime,
    score.homeScoreTotal,
    score.awayScoreTotal,
    schedule.playedStatus,
    schedule.week,
    schedule.venue.name AS venueName,
    venues.city,
    season
  FROM
    `sportsight-tests.NFL_Data.seasonal_games`
  LEFT JOIN
    UNNEST (Seasondata.games)
  left join venues on schedule.venue.id=venueId
  WHERE
    TRUE
    # and schedule.playedStatus = 'COMPLETED'
    # AND schedule.week = 15
    )
SELECT
  games.*,
  teams1.teamFullname AS homeTeamName,
  teams2.teamFullname AS awayTeamName
FROM
  games
LEFT JOIN
  teams teams1
ON
  teams1.teamId=games.homeTeamid
  AND teams1.season=games.season
LEFT JOIN
  teams teams2
ON
  teams2.teamId=games.awayTeamid
  AND teams2.season=games.season
ORDER BY
  startTime DESC