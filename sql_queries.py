# DROP TABLES

songplay_table_drop = "drop table if exists songplays"
user_table_drop = "drop table if exists users"
song_table_drop = "drop table if exists songs"
artist_table_drop = "drop table if exists artists"
time_table_drop = "drop table if exists time"

# CREATE TABLES

songplay_table_create = ("""create table songplays 
(songplay_id serial NOT NULL PRIMARY KEY,
start_time bigint NOT NULL,
user_id int NOT NULL,
level varchar,
song_id varchar NOT NULL,
artist_id varchar NOT NULL,
session_id int,
location varchar,
user_agent varchar)
""")

user_table_create = ("""create table users 
(user_id int NOT NULL PRIMARY KEY,
first_name varchar NOT NULL,
last_name varchar NOT NULL,
gender varchar,
level varchar)
""")

song_table_create = ("""create table songs 
(song_id varchar NOT NULL PRIMARY KEY,
title varchar,
artist_id varchar NOT NULL,
year int,
duration float)
""")

artist_table_create = ("""create table artists 
(artist_id varchar NOT NULL PRIMARY KEY,
name varchar,
location varchar,
lattitude numeric,
longitude numeric)
""")

time_table_create = ("""create table time 
(start_time bigint PRIMARY KEY,
hour int, day int,
week int, month int,
year int,
weekday int)
""")

# INSERT RECORDS

songplay_table_insert = ("""insert into songplays 
(songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent) 
values(%s, %s, %s, %s, %s, %s, %s, %s, %s)
ON CONFLICT(songplay_id)
DO UPDATE
SET level= excluded.level
""")

user_table_insert = ("""insert into users 
(user_id, first_name, last_name, gender, level) 
values(%s, %s, %s, %s, %s) 
ON CONFLICT(user_id)
DO UPDATE
SET level= excluded.level
""")

song_table_insert = ("""insert into songs 
(song_id, title, artist_id, year, duration) 
values(%s, %s, %s, %s, %s)
ON CONFLICT(song_id)
DO NOTHING
""")

artist_table_insert = ("""insert into artists 
(artist_id, name, location, lattitude, longitude) 
values(%s, %s, %s, %s, %s)
ON CONFLICT(artist_id)
DO NOTHING
""")

time_table_insert = ("""insert into time 
(start_time, hour, day, week, month, year, weekday) 
values(%s, %s, %s, %s, %s, %s, %s)
ON CONFLICT(start_time)
DO NOTHING
""")

# FIND SONGS

#song_select = ("""select songs.song_id, artists.artist_id from songs join artists on songs.artist_id=artists.artist_id where songs.title=%s and artists.name=%s and songs.duration=%s""")

song_select = ("""select song_id, artist_id from songs""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]