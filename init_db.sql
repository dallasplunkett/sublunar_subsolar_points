create database ground_tracks;

use ground_tracks;

create table tracks (
	id int primary key auto_increment,
	date date not null,
	time time(0) not null,
	body varchar(16) not null,
	latitude float not null,
	longitude float not null
);

-- insert into tracks
-- values (
-- 	'2023-01-09',
-- 	'20:50:00',
-- 	'sun',
-- 	22.05,
-- 	130.7167
-- );

-- insert into tracks
-- values (
-- 	'2023-01-09',
-- 	'20:50:00',
-- 	'moon',
-- 	19.2167,
-- 	83.2833
-- );
