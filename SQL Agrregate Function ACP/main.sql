CREATE TABLE IF NOT EXISTS MOST_SELLED_CARS_OF_2020_TO_2024 (
    VEHICLE_ID TEXT,
    VEHICLE_NAME TEXT,
    SUPPLIER_ID TEXT,
    CATEGORY_ID TEXT,
    UNIT TEXT,
    PRICE REAL
);

INSERT INTO MOST_SELLED_CARS_OF_2020_TO_2024 (VEHICLE_ID, VEHICLE_NAME, SUPPLIER_ID, CATEGORY_ID, UNIT, PRICE) VALUES
    ('2020', 'Toyota Corolla', '20', 'Compact car (C segment)', '3', 20595),
    ('2021', 'Toyota RAV4', '21', 'Compact crossover SUV', '2', 27565),
    ('2022', 'Toyota Corolla', '22', 'Compact car (C segment)', '4', 25000),
    ('2023', 'Tesla Model Y', '23', 'Electric compact SUV', '1', 45630),
    ('2024', 'Tesla Model Y', '24', 'Electric compact SUV', '5', 44630);

-- Display all records
SELECT * FROM MOST_SELLED_CARS_OF_2020_TO_2024;

-- Count total suppliers
SELECT COUNT(SUPPLIER_ID) AS SUPPLIER_COUNT
FROM MOST_SELLED_CARS_OF_2020_TO_2024;

-- Calculate average price
SELECT AVG(PRICE) AS AVERAGE_PRICE
FROM MOST_SELLED_CARS_OF_2020_TO_2024;

-- Calculate total price
SELECT SUM(PRICE) AS TOTAL_PRICE
FROM MOST_SELLED_CARS_OF_2020_TO_2024;
