select * 
from packers_plays;

select Distinct play_type_nfl from packers_plays;

select start_time, yards_gained, passer_player_name, passer_player_id
from packers_plays
Where play_type_nfl = 'PASS';
;

select *
from packers_roster
where jersey_number = 10;

player_id


SELECT name FROM sqlite_master WHERE type='table';

SELECT game_seconds_remaining, (60-(CAST(game_seconds_remaining AS FLOAT)/60)) AS game_time, p.week, p.play_type_nfl, p.yards_gained, p.receiver_player_name AS P_Name, p.receiver_player_id AS P_ID, r.player_name, r.headshot_url
FROM packers_plays p
JOIN packers_roster r
  ON p.receiver_player_id = r.player_id and p.week = r.week
WHERE p.play_type_nfl = 'PASS' and p.posteam = 'GB';

SELECT game_seconds_remaining, (60-(CAST(game_seconds_remaining AS FLOAT)/60)) AS game_time, p.week, p.play_type_nfl, p.yards_gained, p.rusher_player_name AS P_Name, p.rusher_player_id AS P_ID, r.player_name, r.headshot_url
FROM packers_plays p
JOIN packers_roster r
  ON p.rusher_player_id = r.player_id and p.week = r.week
WHERE p.play_type_nfl = 'RUSH' and p.posteam = 'GB';