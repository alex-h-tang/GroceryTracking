INSERT INTO Categories (category_id, category_name) VALUES (1, 'Milk');
INSERT INTO Categories (category_id, category_name) VALUES (2, 'Egg');
INSERT INTO Categories (category_id, category_name) VALUES (3, 'Fruit');
INSERT INTO Categories (category_id, category_name) VALUES (4, 'Vegetable');

INSERT INTO Products (category_id, product_id, name) VALUES (1, 1001, 'Fat-free Milk Normal 1 Gal');
INSERT INTO Products (category_id, product_id, name) VALUES (1, 1002, '2% Milk Normal 1 Gal');
INSERT INTO Products (category_id, product_id, name) VALUES (1, 1003, 'Whole Milk Normal 1 Gal');
INSERT INTO Products (category_id, product_id, name) VALUES (1, 1004, 'Fat-free Milk Organic 1 Gal');
INSERT INTO Products (category_id, product_id, name) VALUES (1, 1005, '2% Milk Organic 1 Gal');
INSERT INTO Products (category_id, product_id, name) VALUES (1, 1006, 'Whole Milk Organic 1 Gal');

INSERT INTO Products (category_id, product_id, name) VALUES (2, 2001, 'Eggs Normal');
INSERT INTO Products (category_id, product_id, name) VALUES (2, 2002, 'Eggs Organic');

INSERT INTO Products (category_id, product_id, name) VALUES (3, 3001, 'Banana Normal');
INSERT INTO Products (category_id, product_id, name) VALUES (3, 3002, 'Banana Organic');

INSERT INTO Products (category_id, product_id, name) VALUES (4, 4001, 'Long English Cucumber Each');
INSERT INTO Products (category_id, product_id, name) VALUES (4, 4002, 'Mini Cucumber 1 lb');

INSERT INTO Stores (store_id, store) VALUES (1, 'Lidl');
INSERT INTO Stores (store_id, store) VALUES (2, 'Harris Teeter');
INSERT INTO Stores (store_id, store) VALUES (3, 'Walmart');
--INSERT INTO Stores (store_id, store) VALUES (, 'Publix');
--INSERT INTO Stores (store_id, store) VALUES (, 'Aldi');

-- (1001) Milk/Fat-free Normal 1 Gal
INSERT INTO ProductURLs (product_id, url, store_id, descr)
VALUES (1001, 'https://www.lidl.com/products/1068506', 1, 'vitamin A/D');
INSERT INTO ProductURLs (product_id, url, store_id, descr)
VALUES (1001, 'https://www.harristeeter.com/p/harris-teeter-fat-free-skim-milk/0007203663128', 2, 'vitamin A/D');
INSERT INTO ProductURLs (product_id, url, store_id, descr)
VALUES (1001, 'https://www.walmart.com/ip/Great-Value-Fat-Free-Milk-Gallon-128-fl-oz/10450117', 3, 'Greate Value, vitamin A/D');

-- (2001) Vegetable/Eggs Normal
-- (2002) Vegetable/Eggs Organic

-- (3001) Fruit/Banana Normal
-- (3002) Fruit/Banana Organic

-- (4001) Vegetable/Long English Cucumber Each
INSERT INTO ProductURLs (product_id, url, store_id, descr)
VALUES (4001, 'https://www.lidl.com/products/985605001', 1, '');
INSERT INTO ProductURLs (product_id, url, store_id, descr)
VALUES (4001, 'https://www.harristeeter.com/p/english-cucumber/0000000004593', 2, '');
INSERT INTO ProductURLs (product_id, url, store_id, descr)
VALUES (4001, 'https://www.walmart.com/ip/Fresh-Long-English-Cucumber-Each/44390996', 3, '');

-- (4002) Vegetable/Mini Cucumber 1 lb
INSERT INTO ProductURLs (product_id, url, store_id, descr)
VALUES (4002, 'https://www.lidl.com/products/985612001', 1, '');
INSERT INTO ProductURLs (product_id, url, store_id, descr)
VALUES (4002, 'https://www.harristeeter.com/p/mini-cucumbers/0073447533423', 2, '');
INSERT INTO ProductURLs (product_id, url, store_id, descr)
VALUES (4002, 'https://www.walmart.com/ip/Fresh-Mini-Cucumber-1lb-bag/44419690', 3, '');
