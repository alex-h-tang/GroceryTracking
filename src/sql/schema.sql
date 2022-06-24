DROP VIEW IF EXISTS vUrlDetails;
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
    created datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
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
    price_dt datetime DEFAULT CURRENT_TIMESTAMP,
    price REAL NOT NULL,
    FOREIGN KEY (url_id) 
      REFERENCES ProductURLs (url_id) 
         ON DELETE CASCADE 
         ON UPDATE NO ACTION,
    PRIMARY KEY (url_id, price_dt)
);

CREATE VIEW vUrlDetails AS
    select u.url_id, c.category_name, c.category_id, p.name, p.product_id, s.store, s.store_id, u.url, u.descr
    from ProductURLs u
    left join Products p on u.product_id = p.product_id
    left join Stores s on u.store_id = s.store_id
    left join Categories c on c.category_id = p.category_id;
