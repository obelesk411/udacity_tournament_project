# Swiss Tournament

## Introduction

This is a class for running a swiss style tournament

## Requirement

Requires Python 2.5+
Postgresql
pgcopy module

## Installation

Clone the master branch.

	$ git clone https://github.com/obelesk411/udacity_movie_project.git

Navigate to the main folder

    $ cd udacity_movie_project

Connect to Postgresql and import tournament.sql file

	$ psql 
	$ database=> \i tournament.sql
	DROP DATABASE
	CREATE DATABASE
	You are now connected to database "tournament" as user "vagrant".
	psql:tournament.sql:9: NOTICE:  table "tournaments" does not exist, skipping
	DROP TABLE
	CREATE TABLE
	psql:tournament.sql:16: NOTICE:  table "players" does not exist, skipping
	DROP TABLE
	CREATE TABLE
	psql:tournament.sql:23: NOTICE:  table "matches" does not exist, skipping
	DROP TABLE
	CREATE TABLE
	psql:tournament.sql:32: NOTICE:  view "player_standings" does not exist, skipping
	DROP VIEW
	CREATE VIEW
	psql:tournament.sql:49: NOTICE:  view "swiss_pairings" does not exist, skipping
	DROP VIEW
	CREATE VIEW
	tournament=> 

Press CNTL+D to quit

Run unit tests

	$ python tournament_test.py 
	1. After registering a tournament, count_tournaments() returns 1.
	2. Tournaments can be deleted.
	3. Old matches can be deleted.
	4. Player records can be deleted.
	5. After deleting, count_players() returns zero.
	6. After registering a player, count_players() returns 1.
	7. Players can be registered and deleted.
	8. Newly registered players appear in the standings with no matches.
	9. After a match, players have updated standings.
	10. After one match, players with one win are paired.
	Success!  All tests pass!