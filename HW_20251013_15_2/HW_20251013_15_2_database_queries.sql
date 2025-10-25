-- ---------------------------------------------------------------------
-- Завдання 1.
-- Створити наступні запити для бази даних з інформацією
-- про овочі та фрукти:
-- ---------------------------------------------------------------------

-- 1. Відображення усіх овочів з калорійністю, меншою за вказану.
--    Приклад: менше 50 ккал.
SELECT *
FROM products
WHERE kind = 'Vegetable'
  AND calories < 50;


-- 2. Відображення усіх фруктів з калорійністю у вказаному діапазоні.
--    Наприклад: від 30 до 60 включно.
SELECT *
FROM products
WHERE kind = 'Fruit'
  AND calories BETWEEN 30 AND 60;


-- 3. Відображення усіх овочів, у назві яких є вказане слово.
--    Наприклад: "капуста".
--    У нашій таблиці це "Cabbage".
SELECT *
FROM products
WHERE kind = 'Vegetable'
  AND name ILIKE '%cabbage%';


-- 4. Відображення усіх овочів та фруктів, у короткому описі яких є вказане слово.
--    Наприклад: "гемоглобін", "залізо", "вітамін".
SELECT *
FROM products
WHERE description ILIKE '%гемоглобін%'
   OR description ILIKE '%залізо%'
   OR description ILIKE '%вітамін%'
   OR description ILIKE '%iron%'
   OR description ILIKE '%vitamin%';


-- 5. Показати усі овочі та фрукти жовтого або червоного кольору.
--    Враховуємо і випадки на кшталт 'Green/Red'.
SELECT *
FROM products
WHERE color ILIKE '%yellow%'
   OR color ILIKE '%red%';



-- ---------------------------------------------------------------------
-- Завдання 2.
-- Створити наступні запити:
-- ---------------------------------------------------------------------

-- 1. Показати кількість овочів.
SELECT COUNT(*) AS vegetable_count
FROM products
WHERE kind = 'Vegetable';


-- 2. Показати кількість фруктів.
SELECT COUNT(*) AS fruit_count
FROM products
WHERE kind = 'Fruit';


-- 3. Показати кількість овочів та фруктів заданого кольору.
--    Наприклад, рахуємо всі елементи, які мають "Green" у полі color.
SELECT COUNT(*) AS green_items_count
FROM products
WHERE color ILIKE '%green%';


-- 4. Показати кількість овочів та фруктів кожного кольору.
--    Тобто групування за color.
SELECT color,
       COUNT(*) AS items_per_color
FROM products
GROUP BY color
ORDER BY items_per_color DESC;


-- 5. Показати колір мінімальної кількості овочів та фруктів.
SELECT color,
       COUNT(*) AS items_per_color
FROM products
GROUP BY color
ORDER BY items_per_color ASC
LIMIT 1;


-- 6. Показати колір максимальної кількості овочів та фруктів.
SELECT color,
       COUNT(*) AS items_per_color
FROM products
GROUP BY color
ORDER BY items_per_color DESC
LIMIT 1;


-- 7. Показати мінімальну калорійність овочів та фруктів.
SELECT MIN(calories) AS min_calories_all
FROM products;


-- 8. Показати максимальну калорійність овочів та фруктів.
SELECT MAX(calories) AS max_calories_all
FROM products;


-- 9. Показати середню калорійність овочів та фруктів.
SELECT AVG(calories) AS avg_calories_all
FROM products;


-- 10. Показати фрукт з мінімальною калорійністю.
SELECT *
FROM products
WHERE kind = 'Fruit'
ORDER BY calories ASC
LIMIT 1;


-- 11. Показати фрукт з максимальною калорійністю.
SELECT *
FROM products
WHERE kind = 'Fruit'
ORDER BY calories DESC
LIMIT 1;


-- Додаткова статистика по кожному типу (окремо фрукти і окремо овочі):
SELECT kind,
       MIN(calories) AS min_calories,
       MAX(calories) AS max_calories,
       AVG(calories) AS avg_calories
FROM products
GROUP BY kind;
