/* SQL Exercise
====================================================================
We will be working with database imdb.db
You can download it here: https://drive.google.com/file/d/1E3KQDdGJs4a0i1RoYb8DEq0PFxCgI6cN/view?usp=sharing
*/


-- MAKE YOURSELF FAMILIAR WITH THE DATABASE AND TABLES HERE





--==================================================================
/* TASK I
 Find the id's of movies that have been distributed by “Universal Pictures”.
*/

SELECT movie_distributors.movie_id FROM movie_distributors
    JOIN movies ON movie_distributors.movie_id = movies.movie_id
    JOIN distributors ON movie_distributors.distributor_id = distributors.distributor_id
    WHERE distributors.name LIKE 'Universal Pictures';

/* TASK II
 Find the name of the companies that distributed movies released in 2006.
*/

SELECT distributors.name FROM movie_distributors
    JOIN movies ON movie_distributors.movie_id = movies.movie_id
    JOIN distributors ON movie_distributors.distributor_id = distributors.distributor_id
    WHERE movies.year = 2006;

/* TASK III
Find all pairs of movie titles released in the same year, after 2010.
hint: use self join on table movies.
*/

SELECT movies.title , same_year_movies.title FROM movies 
    JOIN movies same_year_movies ON same_year_movies.year = movies.year
    WHERE movies.year > 2010
    AND movies.title <> same_year_movies.title

/* TASK IV
 Find the names and movie titles of directors that also acted in their movies.
*/



SELECT people.name as director, movies.title FROM directors
    JOIN people ON people.person_id = directors.person_id
    JOIN movies ON movies.movie_id = directors.movie_id
    WHERE directors.person_id IN (
        SELECT person_id FROM roles
        WHERE roles.movie_id = movies.movie_id
    )
    GROUP BY director


/* TASK V
Find ALL movies realeased in 2011 and their aka titles.
hint: left join
*/

SELECT movies.title, aka_titles.title as aka_title FROM movies
    LEFT JOIN aka_titles ON aka_titles.movie_id = movies.movie_id
    WHERE movies.year = 2011


/* TASK VI
Find ALL movies realeased in 1976 OR 1977 and their composer's name.
*/

SELECT movies.title, people.name FROM movies
    LEFT JOIN composers ON composers.movie_id = movies.movie_id
    LEFT JOIN people ON people.person_id = composers.person_id
    WHERE movies.year = 1976 OR movies.year = 1977


/* TASK VII
Find the most popular movie genres.
*/

SELECT AVG(movies.rating) as avg_rating, genres.label FROM movies
    JOIN movie_genres ON movie_genres.movie_id = movies.movie_id
    JOIN genres ON genres.genre_id = movie_genres.genre_id
GROUP BY genres.label
ORDER BY avg_rating DESC

/* TASK VIII
Find the people that achieved the 10 highest average ratings for the movies 
they cinematographed.
*/

SELECT people.name, AVG(movies.rating) as avg_rating FROM cinematographers
    JOIN movies ON movies.movie_id = cinematographers.movie_id
    JOIN people ON people.person_id = cinematographers.person_id
GROUP BY people.name
ORDER BY avg_rating DESC
LIMIT 10



/* TASK IX
Find all countries which have produced at least one movie with a rating higher than
8.5.
hint: subquery
*/

SELECT countries.name FROM movies
    JOIN movie_countries ON movie_countries.movie_id = movies.movie_id
    JOIN countries ON countries.country_id = movie_countries.country_id
    WHERE rating > 8.5
GROUP BY countries.name


/* TASK X
Find the highest-rated movie, and report its title, year, rating, and country. There
can be ties; if so, you should report for each of them.
*/
SELECT title, year, rating, cname 
    FROM (
        SELECT title, year, rating, countries.name as cname,
            RANK() OVER (ORDER BY rating DESC) as posn
            FROM movies
            JOIN movie_countries ON movie_countries.movie_id = movies.movie_id
            JOIN countries ON countries.country_id = movie_countries.country_id
    ) as ranked
WHERE ranked.posn = 1


/* STRETCH BONUS
Find the pairs of people that have directed at least 5 movies and whose 
careers do not overlap (i.e. The release year of a director's last movie is 
lower than the release year of another director's first movie).
*/
/* step1: get directors that have directed 5 or more movies */
SELECT people.name, COUNT(*) as movie_count FROM directors
    JOIN people ON people.person_id = directors.person_id
    GROUP BY directors.person_id
    HAVING movie_count >= 5
   
/* step2: add first movie year and last movie year to query */ 