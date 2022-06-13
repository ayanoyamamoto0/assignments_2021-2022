# Select database
USE flights;


# Create airports table
CREATE TABLE airports (
	airport_code VARCHAR(3) NOT NULL,
    counrty VARCHAR(20) NOT NULL,
    city VARCHAR(20) NOT NULL,
    airport_name VARCHAR(50) NOT NULL,
    utc TIME NOT NULL,
    PRIMARY KEY (airport_code),
    UNIQUE (airport_code)
);


# Create routes table
CREATE TABLE routes (
	flight_number VARCHAR(6) NOT NULL,
    from_airport_code VARCHAR(3) NOT NULL,
    to_airport_code VARCHAR(3) NOT NULL,
    PRIMARY KEY (flight_number),
    UNIQUE (flight_number),
    FOREIGN KEY (from_airport_code) REFERENCES airports (airport_code),
    FOREIGN KEY (to_airport_code) REFERENCES airports (airport_code)
);


# Create schedules table
CREATE TABLE schedules (
	schedule_id SMALLINT NOT NULL AUTO_INCREMENT,
	flight_date DATE NOT NULL,
	flight_number VARCHAR(6) NOT NULL,
	departure_time TIME NOT NULL,
	arrival_time TIME NOT NULL,
	base_price FLOAT NOT NULL,
	PRIMARY KEY (schedule_id),
	UNIQUE (schedule_id),
	FOREIGN KEY (flight_number) REFERENCES routes (flight_number)
);


# Create classes table
CREATE TABLE classes (
	class_name VARCHAR(15) NOT NULL,
	price_multiplier FLOAT NOT NULL,
	PRIMARY KEY (class_name),
	UNIQUE (class_name)
);


# Create seats table
CREATE TABLE seats (
	seat_number VARCHAR(3) NOT NULL,
    class_name VARCHAR(15) NOT NULL,
    PRIMARY KEY (seat_number),
    UNIQUE (seat_number),
    FOREIGN KEY (class_name) REFERENCES classes (class_name)
);


# Create availabilities table
CREATE TABLE availabilities2 (
	schedule_id SMALLINT NOT NULL,
    seat_number VARCHAR(3) NOT NULL,
    availability TINYINT(1) NOT NULL,
    PRIMARY KEY (schedule_id, seat_number),
    FOREIGN KEY (schedule_id) REFERENCES schedules(schedule_id),
    FOREIGN KEY (seat_number) REFERENCES seats(seat_number)
    );


# Create view to display flight details included the screenshot
CREATE VIEW flight_details AS
	SELECT sc.flight_date AS flight_date,
		DAYNAME(sc.flight_date) AS dayname,
		sc.flight_number AS flight_number,
		r.from_airport_code AS from_airport_code,
		from_airports.city AS from_city,
		r.to_airport_code AS to_airport_code,
		to_airports.city AS to_city,
		sc.departure_time AS departure_time,
		sc.arrival_time AS arrival_time,
		CAST(TIMEDIFF((sc.arrival_time - to_airports.utc),(sc.departure_time - from_airports.utc)) AS TIME) AS duration,
		CAST((sc.base_price * c.price_multiplier) AS DECIMAL (7,2)) AS price,
		se.class_name AS class,
		COUNT(av.availability) AS available_seats
	FROM schedules sc
		JOIN routes r USING (flight_number)
		JOIN availabilities av USING (schedule_id)
		JOIN seats se USING (seat_number)
		JOIN classes c USING (class_name)
		LEFT JOIN airports from_airports ON r.from_airport_code = from_airports.airport_code
		LEFT JOIN airports to_airports ON r.to_airport_code = to_airports.airport_code
	WHERE av.availability = TRUE
	GROUP BY sc.flight_date,
		sc.flight_number,
		se.class_name;


# Create view to display revenues of each scheduled flight
CREATE VIEW flight_revenues AS
	SELECT sc.schedule_id,
		sc.flight_date,
		sc.flight_number,
		CAST(SUM((sc.base_price * c.price_multiplier)) AS DECIMAL(7,2)) AS revenue_per_flight
	FROM availabilities av
		
	WHERE av.availability = FALSE
	GROUP BY sc.flight_date, 
		sc.flight_number;


# Add index to availability column from availabilities table
ALTER TABLE availabilities ADD INDEX (availability);


# Query 1
# Available seats on one way flight for 1 adult on 5th January 2022
# from city names starting with 'pa' to city names starting with 'du'
SELECT fd.*
FROM flight_details fd
WHERE flight_date = '2022-01-05'
    AND REGEXP_LIKE (from_city, '^pa', 'i')
    AND REGEXP_LIKE (to_city, '^du','i');

# Query 2
# Available seats on return routes ror 2 adults between airport_code DUB and VIE
# with departure dates bewteen 13th-19th January 2022
# and return dates between 20th-26th January 2022
SELECT fd.*
FROM flight_details fd
WHERE (flight_date BETWEEN '2022-01-13' AND '2022-01-19')
	AND from_airport_code = 'DUB'
    AND to_airport_code = 'VIE'
    AND available_seats >= 2
    OR (flight_date BETWEEN '2022-01-20' AND '2022-01-26')
    AND from_airport_code = 'VIE'
    AND to_airport_code = 'DUB'
    AND available_seats >= 2
ORDER BY flight_number ASC;

# Query 3
# From the cheapest to the most expensive days of the week to fly business class
# from airport_code DUB to airport names including 'suarez' or 'suerez'
# according to the average distinct prices of the available seats
SELECT to_airports.airport_name AS to_airport,
	fd.dayname,
    CAST(AVG(DISTINCT(fd.price)) AS DECIMAL(7,2)) AS avg_weekday_price
FROM airports to_airports
	RIGHT JOIN flight_details fd ON fd.to_airport_code = to_airports.airport_code
WHERE fd.class = 'Business'
	AND fd.from_airport_code = 'DUB'
	AND REGEXP_LIKE (to_airports.airport_name, 'su(a|e)rez', 'i')
GROUP BY fd.dayname,
	to_airports.airport_name
ORDER BY avg_weekday_price ASC;

# Query 4
# routes with 90% or higher availabe seats
SELECT sc.flight_date,
	sc.flight_number,
    FORMAT((SUM(av.availability) / COUNT(av.availability))*100, 0) AS percentage_available
FROM schedules sc
	INNER JOIN availabilities av USING (schedule_id)
GROUP BY sc.flight_date,
	sc.flight_number
HAVING percentage_available >= 90;

# Query 5
# Total revenue
SELECT FORMAT(SUM(sc.base_price * c.price_multiplier), 2) AS total_revenue
FROM availabilities av
	LEFT JOIN schedules sc ON av.schedule_id = sc.schedule_id
    LEFT JOIN seats se ON av.seat_number = se.seat_number
    LEFT JOIN classes c ON se.class_name = c.class_name
WHERE av.availability = FALSE;

# Query 6
# Single flight with the highest revenue
SELECT flight_date,
	flight_number,
	MAX(revenue_per_flight)
FROM flight_revenues;

# Query 7
# Top 5 highest revenue routes with city names
SELECT fr.flight_number,
	airport_names.from_airport,
	airport_names.to_airport,
    SUM(fr.revenue_per_flight) AS revenue
FROM flight_revenues fr
	LEFT JOIN(
		SELECT r.flight_number,
			from_airports.airport_name AS from_airport,
			to_airports.airport_name AS to_airport
		FROM routes r
			LEFT JOIN airports from_airports ON r.from_airport_code = from_airports.airport_code
			LEFT JOIN airports to_airports ON r.to_airport_code = to_airports.airport_code
		) AS airport_names ON fr.flight_number = airport_names.flight_number
	GROUP BY flight_number
    ORDER BY revenue DESC
    LIMIT 5;
    
# Query 8
# routes with below average revenue
SELECT *
FROM flight_revenues
WHERE revenue_per_flight < (SELECT AVG(revenue_per_flight) FROM flight_revenues)
ORDER BY revenue_per_flight DESC;
