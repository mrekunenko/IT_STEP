--Створіть наступні запити для бази даних з інформацією про овочі та фрукти з попереднього домашнього завдання:
CREATE DATABASE FRUITS_VEGETABLES;

CREATE TABLE FRUITS_VEGETABLES (
    FRUIT_VEGETABLE_ID INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    FRUIT_VEGETABLE_NAME VARCHAR(50) NOT NULL,
    TYPE_FRUIT_VAGETABLE VARCHAR(20) NOT NULL,
    FRUIT_VEGETABLE_COLOR VARCHAR(30),
    FRUIT_VEGETABLE_CALS INT CHECK (FRUIT_VEGETABLE_CALS >= 0),
    FRUIT_VEGETABLE_ABOUT VARCHAR(255)
);

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

-- ■ Відображення усіх овочів з калорійністю, менше вказаної.
SELECT * FROM FRUITS_VEGETABLES WHERE FRUIT_VEGETABLE_CALS < 50 AND TYPE_FRUIT_VAGETABLE LIKE 'Vegetable';

-- ■ Відображення усіх фруктів з калорійністю у вказаному діапазоні.
SELECT * FROM FRUITS_VEGETABLES WHERE TYPE_FRUIT_VAGETABLE LIKE 'Fruit' AND FRUIT_VEGETABLE_CALS BETWEEN 30 AND 60;

-- ■ Відображення усіх овочів, у назві яких є вказане слово. Наприклад, слово: капуста.
SELECT * FROM FRUITS_VEGETABLES WHERE TYPE_FRUIT_VAGETABLE LIKE 'Vegetable' AND LOWER(FRUIT_VEGETABLE_NAME) LIKE '%cabbage%';

-- ■ Відображення усіх овочів та фруктів, у короткому описі яких є вказане слово. Наприклад, слово: гемоглобін.
SELECT * FROM FRUITS_VEGETABLES WHERE FRUIT_VEGETABLE_ABOUT LIKE '%sweet%';

-- ■ Показати усі овочі та фрукти жовтого або червоного кольору.
SELECT * FROM FRUITS_VEGETABLES WHERE LOWER(FRUIT_VEGETABLE_COLOR) LIKE 'red' OR LOWER(FRUIT_VEGETABLE_COLOR)LIKE 'yellow';

-- ■ Показати кількість овочів.
SELECT TYPE_FRUIT_VAGETABLE, COUNT(*) FROM FRUITS_VEGETABLES WHERE TYPE_FRUIT_VAGETABLE LIKE 'Vegetable' GROUP BY TYPE_FRUIT_VAGETABLE;

-- ■ Показати кількість фруктів.
SELECT TYPE_FRUIT_VAGETABLE, COUNT(*) FROM FRUITS_VEGETABLES WHERE TYPE_FRUIT_VAGETABLE LIKE 'Fruit' GROUP BY TYPE_FRUIT_VAGETABLE;

-- ■ Показати кількість овочів та фруктів заданого кольору.
SELECT FRUIT_VEGETABLE_COLOR, COUNT(*) FROM FRUITS_VEGETABLES WHERE FRUIT_VEGETABLE_COLOR LIKE 'Red' GROUP BY FRUIT_VEGETABLE_COLOR;

-- ■ Показати кількість овочів та фруктів кожного кольору.
SELECT FRUIT_VEGETABLE_COLOR, COUNT(*) FROM FRUITS_VEGETABLES GROUP BY FRUIT_VEGETABLE_COLOR;

-- ■ Показати мінімальну калорійність овочів та фруктів.
SELECT TYPE_FRUIT_VAGETABLE, MIN(FRUIT_VEGETABLE_CALS) FROM FRUITS_VEGETABLES GROUP BY TYPE_FRUIT_VAGETABLE;

-- ■ Показати максимальну калорійність овочів та фруктів.
SELECT TYPE_FRUIT_VAGETABLE, MAX(FRUIT_VEGETABLE_CALS) FROM FRUITS_VEGETABLES GROUP BY TYPE_FRUIT_VAGETABLE;

-- ■ Показати середню калорійність овочів та фруктів.
SELECT TYPE_FRUIT_VAGETABLE, AVG(FRUIT_VEGETABLE_CALS) FROM FRUITS_VEGETABLES GROUP BY TYPE_FRUIT_VAGETABLE;

-- ■ Показати фрукт з мінімальною калорійністю.
SELECT FRUIT_VEGETABLE_NAME, FRUIT_VEGETABLE_CALS
FROM FRUITS_VEGETABLES
WHERE FRUIT_VEGETABLE_CALS = (
    SELECT MIN(FRUIT_VEGETABLE_CALS)
    FROM FRUITS_VEGETABLES
	WHERE TYPE_FRUIT_VAGETABLE = 'Fruit'
) AND TYPE_FRUIT_VAGETABLE LIKE 'Fruit';

-- ■ Показати фрукт з максимальною калорійністю.
SELECT FRUIT_VEGETABLE_NAME, FRUIT_VEGETABLE_CALS
FROM FRUITS_VEGETABLES
WHERE FRUIT_VEGETABLE_CALS = (
    SELECT MAX(FRUIT_VEGETABLE_CALS)
    FROM FRUITS_VEGETABLES
	WHERE TYPE_FRUIT_VAGETABLE = 'Fruit'
) AND TYPE_FRUIT_VAGETABLE LIKE 'Fruit';