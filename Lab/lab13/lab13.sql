.read data.sql


CREATE TABLE average_prices AS
  SELECT category, avg(MSRP) as average_price from products 
  GROUP by category;


CREATE TABLE lowest_prices AS
  SELECT store, item, min(price) from inventory
  group by item;


create table best_value_for_money_products as
  select name as name, min(MSRP/rating) from products
  group by category;

CREATE TABLE shopping_list AS
  SELECT a.name, b.store as store from best_value_for_money_products as a, lowest_prices as b
  where a.name = b.item GROUP by item;


CREATE TABLE total_bandwidth AS
  SELECT sum(b.Mbs) from shopping_list as a, stores as b
  where a.store = b.store;