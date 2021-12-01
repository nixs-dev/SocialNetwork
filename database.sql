create database socialNetwork;
use socialNetwork;

create table users (
	username varchar(30),
    displayName varchar(30),
    photo longblob,
    _password varchar(30)
);

create table posts (
	id int AUTO_INCREMENT primary key, 
	author varchar(30),
	title varchar(20),
    body varchar(200)
);

create table likes (
	postId int,
	liker varchar(30)
);

create table comments (
	postId int,
    author varchar(30),
    content varchar(500),
    
    constraint fk_comments_1 foreign key(author) references users(username) on delete cascade,
    constraint fk_comments_2 foreign key(postId) references posts(id) on delete cascade
);

ALTER TABLE users add constraint pk_users primary key(username);
ALTER TABLE posts add constraint fk_posts  foreign key(author) references users(username);
ALTER TABLE likes add constraint fk_likes foreign key(postId) references posts(id);
ALTER TABLE likes add constraint fk2_likes foreign key(liker) references users(username);
