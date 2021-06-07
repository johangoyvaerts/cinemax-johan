-- SQLite

DROP TABLE IF EXISTS tickets;

CREATE TABLE IF NOT EXISTS tickets(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    datum TEXT NOT NULL,
    prijs_volw TEXT NOT NULL,
    prijs_kind TEXT NOT NULL,
    aant_volw TEXT NOT NULL,  
    aant_kind TEXT NOT NULL,
    vertoningen_id INTEGER,
    FOREIGN KEY (vertoningen_id) REFERENCES vertoningen (id) ON DELETE SET NULL
    );