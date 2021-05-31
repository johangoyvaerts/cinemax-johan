-- SQLite

INSERT INTO films (titel, duur, knt, MDB_id)
VALUES ("Emma Stone and Emma Thompson answer fan questions", 205, "F","vi80592921"),
    ("The Unholy", 99, "F", "tt9419056"),
    ("Seven", 127, "T", "tt0114369"),
    ("Cruella", 134, "F", "tt3228774"),
    ("100% Wolf", 96, "F", "tt8774798"),
    ("The Conjuring: The Devil Made Me Do It",112,"T","tt7069210"),
    ("Army of the Dead", 148, "F","tt0993840")
;  

INSERT INTO vertoningen (zaal, uur, drie_d, vertoning_actief, films_id)
VALUES (2,"1300", "F", "F", 3),
    (1, "1500", "F", "T", 1),
    (2, "2200", "F", "T", 2),
    (6, "1500", "T", "T", 5),
    (3, "2000", "F", "T", 3),
    (1, "1900", "F", "T", 7),
    (4,"1300", "F", "T", 4)
;


INSERT INTO tickets ( datum, prijs, aant_volw, aant_kind, vertoningen_id)
VALUES ("2021-04-20", 27.5, 1, 2,  4),
    ("2021-04-20", 17.0, 2, 0,  4),
    ("2021-04-20", 34.0, 1, 3,  6),
    ("2021-04-20", 50.0, 0, 5,  5),
    ("2021-04-21", 40.0, 5, 0,  1),
    ("2021-04-20", 16.0, 1, 1,  6),
    ("2021-03-20", 19.0, 1, 1,  4),
    ("2021-05-21", 30.0, 0, 3,  5),
    ("2021-04-20", 10.0, 1, 1,  2),
    ("2021-04-20", 20.0, 0, 2,  3)

;