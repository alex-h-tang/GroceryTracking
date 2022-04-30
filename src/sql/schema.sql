DROP TABLE IF EXISTS Prices;
DROP TABLE IF EXISTS ProductURLs;
DROP TABLE IF EXISTS Stores;
DROP TABLE IF EXISTS Products;
DROP TABLE IF EXISTS Categories;

CREATE TABLE Categories (
    category_id INTEGER PRIMARY KEY,
    category_name TEXT NOT NULL
);

CREATE TABLE Products (
    product_id INTEGER PRIMARY KEY,
    category_id INTEGER,
    name TEXT NOT NULL,
    FOREIGN KEY (category_id) 
      REFERENCES Categories (category_id) 
         ON DELETE CASCADE 
         ON UPDATE NO ACTION
);

CREATE TABLE Stores (
    store_id INTEGER PRIMARY KEY,
    store TEXT NOT NULL
);

CREATE TABLE ProductURLs (
    url_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER,
    url TEXT NOT NULL,
    store_id INTEGER NOT NULL,
    descr TEXT NOT NULL,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (store_id)
      REFERENCES Stores (store_id)
         ON DELETE CASCADE
         ON UPDATE NO ACTION,
    FOREIGN KEY (product_id)
      REFERENCES Products (product_id) 
         ON DELETE CASCADE 
         ON UPDATE NO ACTION
);

CREATE TABLE Prices (
    url_id INTEGER,
    price_date Date DEFAULT CURRENT_DATE,
    price REAL NOT NULL,
    FOREIGN KEY (url_id) 
      REFERENCES ProductURLs (url_id) 
         ON DELETE CASCADE 
         ON UPDATE NO ACTION,
    PRIMARY KEY (url_id, price_date)
);