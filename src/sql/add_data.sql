INSERT INTO Categories (category_id, category_name) VALUES (1, 'Milk');
INSERT INTO Categories (category_id, category_name) VALUES (2, 'Egg');
INSERT INTO Categories (category_id, category_name) VALUES (3, 'Fruit');
INSERT INTO Categories (category_id, category_name) VALUES (4, 'Vegetable');

INSERT INTO Products (category_id, product_id, name) VALUES (1, 1, 'Fat-free Milk Non-Organic 1 Gal');
INSERT INTO Products (category_id, product_id, name) VALUES (1, 2, '2% Milk Non-Organic 1 Gal');
INSERT INTO Products (category_id, product_id, name) VALUES (1, 3, 'Whole Milk Non-Organic 1 Gal');

INSERT INTO ProductURLs (category_id, product_id, url, store, descr) 
VALUES (1, 1, 'https://www.lidl.com/products/1068506', 'Lidl', 'vitamin A & D');
INSERT INTO ProductURLs (category_id, product_id, url, store, descr) 
VALUES (1, 1, 'https://www.harristeeter.com/p/harris-teeter-fat-free-skim-milk/0007203663128', 'Harris Teeter', 'vitamin A & D');

