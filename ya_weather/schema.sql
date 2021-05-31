DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS weather;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);

CREATE TABLE weather (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  author_id INTEGER NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  city TEXT NOT NULL,
  temperature INTEGER NOT NULL,
  condition TEXT NOT NULL,
  FOREIGN KEY (author_id) REFERENCES user (id)
);
