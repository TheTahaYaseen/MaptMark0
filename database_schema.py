"""

Users >
    Id (Auto-Increment)
    Username
    Email
    Password

Tasks >
    Id (Auto-Increment)
    Task
    Details
    Deadline
    Created By 

Medias >
    Id (Auto-Increment)
    Task Id (Foreign Key)
    Media Source 
    
"""

import sqlite3

database_connection = sqlite3.connect("mapt_database.db")
database_cursor = database_connection.cursor()

database_connection.execute("PRAGMA foreign_keys = ON")

create_users_table_query = f"CREATE TABLE users(id integer primary key autoincrement, username varchar(255) not null, email varchar(255) not null, password varchar(255) not null)"
create_tasks_table_query = f"CREATE TABLE tasks(id integer primary key autoincrement, task varchar(255) not null, details varchar(2550) not null, deadline datetime not null, state varchar(255) not null, created_by integer, foreign key (created_by) references users(id))"
create_medias_table_query = f"CREATE TABLE medias(id integer primary key autoincrement, media_of integer, media_source varchar(2550) not null, foreign key (media_of) references tasks(id))"

database_cursor.execute(create_users_table_query)
database_cursor.execute(create_tasks_table_query)
database_cursor.execute(create_medias_table_query)

database_connection.commit()
database_connection.close()