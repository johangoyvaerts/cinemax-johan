-- SQLite

DROP TABLE IF EXISTS vertoningen;

CREATE TABLE IF NOT EXISTS vertoningen(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    zaal INTEGER NOT NULL,
    uur INTEGER NOT NULL,
    drie_d TEXT NOT NULL,
    vertoning_actief TEXT NOT NULL,
    films_id INTEGER,
    FOREIGN KEY (films_id) REFERENCES films (id) ON DELETE SET NULL
    );