DROP TABLE petowners;
CREATE TABLE petowners(
    username VARCHAR PRIMARY KEY NOT NULL,
    contact VARCHAR NOT NULL,
    preferred_name VARCHAR,
    card VARCHAR NOT NULL,
    password VARCHAR NOT NULL
);

DROP TABLE admins;
CREATE TABLE admins(
    username VARCHAR PRIMARY KEY NOT NULL,
    contact VARCHAR NOT NULL,
    preferred_name VARCHAR,
    Card VARCHAR NOT NULL,
    password VARCHAR NOT NULL
);

CREATE TABLE categories (
    category VARCHAR PRIMARY KEY NOT NULL
);

DROP TABLE caretakers;
CREATE TABLE caretakers(
    username VARCHAR PRIMARY KEY NOT NULL,
    contact VARCHAR NOT NULL,
    preferred_name VARCHAR,
    isFullTime BOOLEAN,
    password VARCHAR NOT NULL
);

DROP TABLE pets;
CREATE TABLE pets(
    petName VARCHAR NOT NULL,
    owner VARCHAR NOT NULL REFERENCES public.petowners(username),
    category VARCHAR NOT NULL REFERENCES public.categories(category),
    PRIMARY KEY (petName, owner)
);

