create schema if not exists sparkwebproject collate utf8_general_ci;

use sparkwebproject;

create table if not exists data
(
	`index` int auto_increment
		primary key,
	task_id int null,
	step text null,
	data text null
);


create table if not exists task
(
	id int auto_increment
		primary key,
	subtime datetime not null,
	endtime datetime null,
	status text not null,
	task text not null,
	user varchar(16) not null,
	title text null,
	note text null
);
