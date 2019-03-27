DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS secert;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL,
  email TEXT NOT NULL
);

CREATE TABLE secert (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  secert TEXT NOT NULL
);

INSERT INTO user VALUES (1,'Tony','12312asdasd3','Tony@gmail.com');
INSERT INTO secert VALUES (1,'test');
INSERT INTO user VALUES (2,'Tom','12312asdasd3','Tom@gmail.com');
INSERT INTO secert VALUES (2,'test');
INSERT INTO user VALUES (3,'Bob','12312asdasd3','Bob@gmail.com');
INSERT INTO secert VALUES (3,'test');
INSERT INTO user VALUES (4,'Mike','12312asdasd3','Tony@gmail.com');
INSERT INTO secert VALUES (4,'test');
INSERT INTO user VALUES (5,'admin','12312asddasd3','admin@admin.com');
INSERT INTO secert VALUES (5,'test');