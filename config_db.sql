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
