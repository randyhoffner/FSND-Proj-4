-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

-- Start clean by dropping the tournament database if it already exists.  If it does
-- not already exist, this will throw an error when this file is run.  The error
-- is inconsequential and may be ignored.
DROP DATABASE tournament;


-- Tournament database is created, along with two tables:  players and matches,
-- and one view:  standings.
CREATE DATABASE tournament;
\c tournament;

CREATE TABLE players (id SERIAL primary key, name TEXT);

CREATE TABLE matches (id SERIAL primary key, winner INTEGER REFERENCES players (id), loser INTEGER REFERENCES players (id));

CREATE VIEW standings AS
SELECT players.id, players.name,
(SELECT count(matches.winner)
    FROM matches
    WHERE players.id = matches.winner)
    AS total_wins,
(SELECT count(matches.id)
    FROM matches
    WHERE players.id = matches.winner
    OR players.id = matches.loser)
    AS total_matches
FROM players
ORDER BY total_wins DESC, total_matches DESC;
