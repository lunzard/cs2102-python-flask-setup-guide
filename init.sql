DROP SCHEMA public CASCADE;
CREATE SCHEMA public;

-- CREATE TABLE petowners(
--     username VARCHAR NOT NULL,
--     contact VARCHAR PRIMARY KEY NOT NULL,
--     card VARCHAR,
--     password VARCHAR NOT NULL,
--     usertype VARCHAR NOT NULL,
--     postalcode INTEGER
-- );

-- CREATE TABLE admins(
    -- username VARCHAR NOT NULL,
    -- contact VARCHAR PRIMARY KEY NOT NULL,
    -- Card VARCHAR NOT NULL,
    -- password VARCHAR NOT NULL,
    -- usertype VARCHAR NOT NULL
-- );

CREATE TABLE categories (
    category VARCHAR PRIMARY KEY NOT NULL
);

-- CREATE TABLE caretakers(
--     username VARCHAR NOT NULL,
--     contact VARCHAR PRIMARY KEY NOT NULL,
--     isPartTime BOOLEAN,
--     password VARCHAR NOT NULL,
--     usertype VARCHAR NOT NULL,
--     postalcode INTEGER
-- );

CREATE TABLE users (
    username VARCHAR NOT NULL,
    contact VARCHAR PRIMARY KEY NOT NULL,
    card VARCHAR NOT NULL,
    password VARCHAR NOT NULL,
    usertype VARCHAR NOT NULL,
    isPartTime BOOLEAN,
    postalcode INTEGER
)

CREATE TABLE pets(
    petname VARCHAR NOT NULL,
    pcontact VARCHAR NOT NULL REFERENCES public.users(contact),
    category VARCHAR NOT NULL REFERENCES public.categories(category),
    age INTEGER,
    PRIMARY KEY (petName, pcontact)
);

CREATE TABLE available (
    startday DATE NOT NULL,
    endday DATE NOT NULL CHECK(endday - startday >= 0),
    ccontact VARCHAR NOT NULL REFERENCES public.users(contact),
    PRIMARY KEY (ccontact, startday, endday)
);

CREATE TABLE cantakecare (
    ccontact VARCHAR NOT NULL REFERENCES public.careuserstakers(contact),
    category VARCHAR REFERENCES public.categories(category),
    dailyprice INT NOT NULL,
    PRIMARY KEY (ccontact, category)
);

CREATE TABLE biddings(
  pcontact VARCHAR NOT NULL,
  ccontact VARCHAR NOT NULL REFERENCES public.users(contact),
  petname VARCHAR NOT NULL,

  startday DATE NOT NULL,
  endday DATE NOT NULL CHECK(endday - startday >= 0),

  /* paymentmode is either 'creditcard' or 'cash' */
  paymentmode VARCHAR NOT NULL,
  /* delivermode is either 'pet owner deliver' or 'pick up' or 'transfer through PCS' */
  deliverymode VARCHAR NOT NULL,

  /* status can be pending, success, fail or end */
  status VARCHAR NOT NULL,

  PRIMARY KEY (pcontact, ccontact, petname, startday, endday),
  FOREIGN KEY (pcontact, petname) REFERENCES public.pets(pcontact, petname)
);

CREATE TABLE reviews(
    pcontact VARCHAR NOT NULL,
    ccontact VARCHAR NOT NULL,
    petname VARCHAR NOT NULL,
    startday DATE NOT NULL,
    endday DATE NOT NULL CHECK(endday - startday >= 0),
    rating INTEGER NOT NULL CHECK(rating <= 5 AND rating >= 0),
    review VARCHAR NOT NULL,
    PRIMARY KEY (pcontact, ccontact, petname, rating, review),
    FOREIGN KEY (pcontact, ccontact, petname, startday, endday) REFERENCES public.biddings(pcontact, ccontact, petname, startday, endday)
);
 