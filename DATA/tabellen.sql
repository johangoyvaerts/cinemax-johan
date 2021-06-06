-- SQLite

DROP TABLE IF EXISTS films;
DROP TABLE IF EXISTS vertoningen;
DROP TABLE IF EXISTS tickets;

CREATE TABLE IF NOT EXISTS films(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titel TEXT NOT NULL,
    duur INTEGER NOT NULL,
    knt TEXT NOT NULL,
    MDB_id TEXT NOT NULL
    );


CREATE TABLE IF NOT EXISTS vertoningen(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    zaal INTEGER NOT NULL,
    uur INTEGER NOT NULL,
    drie_d TEXT NOT NULL,
    vertoning_actief TEXT NOT NULL,
    films_id INTEGER,
    FOREIGN KEY (films_id) REFERENCES films (id) ON DELETE SET NULL
    );

CREATE TABLE IF NOT EXISTS tickets(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    datum TEXT NOT NULL,
    prijs_volw REAL NOT NULL,
    prijs_kind REAL NOT NULL,
    aant_volw INTEGER NOT NULL,  
    aant_kind INTEGER NOT NULL,
    vertoningen_id INTEGER,
    FOREIGN KEY (vertoningen_id) REFERENCES vertoningen (id) ON DELETE SET NULL
    );