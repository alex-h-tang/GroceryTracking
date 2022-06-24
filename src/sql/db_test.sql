select * from Categories;

select * from Products;

select p.product_id, c.category_name, p.name from Products p
join Categories c
on c.category_id = p.category_id;

select u.url_id, c.category_name, p.name, s.store, u.url
from ProductURLs u
left join Products p on u.product_id = p.product_id
left join Stores s on u.store_id = s.store_id
left join Categories c on c.category_id = p.category_id;

DELETE FROM ProductURLS WHERE url_id > 12;


select * from vUrlDetails where product_id=4001

select * from Prices

--drop table Prices