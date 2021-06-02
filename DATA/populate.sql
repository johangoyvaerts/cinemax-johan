-- SQLite

INSERT INTO films (titel, duur, knt, MDB_id)
VALUES ("Emma Stone and Emma Thompson answer fan questions", 205, "KT","vi80592921"),
    ("The Unholy", 99, "KT", "tt9419056"),
    ("Seven", 127, "KNT", "tt0114369"),
    ("Cruella", 134, "KT", "tt3228774"),
    ("100% Wolf", 96, "KT", "tt8774798"),
    ("The Conjuring: The Devil Made Me Do It",112,"KT","tt7069210"),
    ("Army of the Dead", 148, "KT","tt0993840")
;  

INSERT INTO vertoningen (zaal, uur, drie_d, vertoning_actief, films_id)
VALUES (2,"1300", "2D", "AC", 3),
    (1, "1500", "2D", "NA", 1),
    (2, "2200", "2D", "AC", 2),
    (6, "1500", "3D", "NA", 5),
    (3, "2000", "2D", "AC", 3),
    (1, "1900", "2D", "AC", 7),
    (4,"1300", "2D", "AC", 4)
;


INSERT INTO tickets ( datum, prijs_volw, prijs_kind, aant_volw, aant_kind, vertoningen_id)
VALUES ("2021-04-20", 9.5, 8.5, 1, 2,  4),
    ("2021-04-20", 10.5, 8.5, 2, 0,  4),
    ("2021-04-20", 9.0, 7.0, 1, 3,  6),
    ("2021-04-20", 10.0, 0.0, 4, 0,  5),
    ("2021-04-21", 10, 8.0, 0, 5,  1),
    ("2021-04-20", 10.0, 8.0, 1, 1,  6),
    ("2021-03-20", 10.5, 8.5, 1, 1, 4),
    ("2021-05-21", 10.0, 8.0, 3, 0,  5),
    ("2021-04-20", 10.0, 8.0, 1, 1,  2),
    ("2021-04-20", 9.0, 7.0, 2, 2,  3)

;