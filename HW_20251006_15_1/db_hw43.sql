-- Модуль 15. Вступ до теорії баз даних
-- Тема: Вступ до теорії баз даних. Частина 1
-- #====================================================================================
-- Завдання 1
-- Створіть базу даних під назвою Birds. Розташування залишається на ваш вибір.
-- #====================================================================================
-- Завдання 2
-- Переназвіть базу даних із першого завдання. Нове ім’я для бази даних Cats.
-- #====================================================================================
-- Завдання 3
-- Видаліть базу даних Cats.
-- #====================================================================================
-- Завдання 4
-- Створіть однотабличну базу даних «Овочі та фрукти»,
-- яка зберігатиме таку інформацію:
-- ■ Назва;
-- ■ Тип (овоч або фрукт);
-- ■ Колір;
-- ■ Калорійність;
-- ■ Короткий опис.
-- #====================================================================================
-- Завдання 5
-- Створіть наступні запити для таблиці з інформацією про
-- овочі та фрукти із попереднього завдання:
-- ■ Відображення всієї інформації з таблиці овочів та фруктів;
-- ■ Відображення усіх овочів;
-- ■ Відображення усіх фруктів;
-- ■ Відображення усіх назв овочів та фруктів;
-- ■ Відображення усіх кольорів. Кольори мають бути унікальними;
-- ■ Відображення фруктів певного кольору;
-- ■ Відображення овочів певного кольору.

CREATE DATABASE BIRDS;
ALTER DATABASE BIRDS RENAME TO CATS;
DROP DATABASE CATS;
CREATE DATABASE FRUITS_VEGETABLES;

INSERT INTO FRUITS_VEGETABLES
(FRUIT_VEGETABLE_NAME, TYPE_FRUIT_VAGETABLE, FRUIT_VEGETABLE_COLOR, FRUIT_VEGETABLE_CALS, FRUIT_VEGETABLE_ABOUT)
VALUES
('Apple', 'Fruit', 'Red', 52, 'Sweet and juicy fruit'),
('Banana', 'Fruit', 'Yellow', 89, 'Soft tropical fruit'),
('Orange', 'Fruit', 'Orange', 47, 'Citrus rich in vitamin C'),
('Strawberry', 'Fruit', 'Red', 33, 'Small and sweet berry'),
('Watermelon', 'Fruit', 'Green/Red', 30, 'Refreshing summer fruit'),
('Pear', 'Fruit', 'Green', 57, 'Soft and juicy fruit'),
('Peach', 'Fruit', 'Orange', 39, 'Sweet fuzzy fruit'),
('Grape', 'Fruit', 'Purple', 69, 'Small sweet berries'),
('Pineapple', 'Fruit', 'Yellow', 50, 'Tropical juicy fruit'),
('Kiwi', 'Fruit', 'Brown/Green', 41, 'Tangy and vitamin-rich fruit'),
('Tomato', 'Vegetable', 'Red', 18, 'Common salad vegetable'),
('Cucumber', 'Vegetable', 'Green', 16, 'Cool and crunchy vegetable'),
('Carrot', 'Vegetable', 'Orange', 41, 'Rich in beta-carotene'),
('Potato', 'Vegetable', 'Brown', 77, 'Starchy root vegetable'),
('Onion', 'Vegetable', 'White', 40, 'Used in cooking for flavor'),
('Broccoli', 'Vegetable', 'Green', 34, 'Healthy green vegetable'),
('Spinach', 'Vegetable', 'Green', 23, 'Leafy and iron-rich'),
('Cabbage', 'Vegetable', 'Green', 25, 'Common leafy vegetable'),
('Eggplant', 'Vegetable', 'Purple', 25, 'Soft and spongy vegetable'),
('Pepper', 'Vegetable', 'Red', 31, 'Colorful and sweet vegetable');

SELECT * FROM FRUITS_VEGETABLES;
SELECT * FROM FRUITS_VEGETABLES WHERE TYPE_FRUIT_VAGETABLE = 'Vegetable';
SELECT * FROM FRUITS_VEGETABLES WHERE TYPE_FRUIT_VAGETABLE = 'Fruit';
SELECT FRUIT_VEGETABLE_NAME FROM FRUITS_VEGETABLES;
SELECT DISTINCT FRUIT_VEGETABLE_COLOR FROM FRUITS_VEGETABLES;

SELECT FRUIT_VEGETABLE_NAME, FRUIT_VEGETABLE_COLOR
FROM FRUITS_VEGETABLES
WHERE FRUIT_VEGETABLE_COLOR = 'Red'
AND TYPE_FRUIT_VAGETABLE = 'Fruit';

SELECT FRUIT_VEGETABLE_NAME, FRUIT_VEGETABLE_COLOR
FROM FRUITS_VEGETABLES
WHERE FRUIT_VEGETABLE_COLOR = 'Green'
AND TYPE_FRUIT_VAGETABLE = 'Vegetable';