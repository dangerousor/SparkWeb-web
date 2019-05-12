create schema if not exists sparkwebproject collate utf8_general_ci;

use sparkwebproject;

create table if not exists data
(
	`index` int auto_increment
		primary key,
	task_id int null,
	step text null,
	data text null,
);


create table if not exists task
(
	id int auto_increment
		primary key,
	subtime datetime not null,
	endtime datetime null,
	status text not null,
	task text not null,
	user int not null,
	title text null,
	note text null,
	log text null,
	is_deleted tinyint(1) default 0 null,
);

create table if not exists user
(
	`index` int auto_increment
		primary key,
	user_id varchar(16) not null,
	password text not null,
	username text null,
	constraint user_user_id_uindex
		unique (user_id),
);
