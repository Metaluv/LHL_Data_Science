/* SQL Exercise
====================================================================
We will be working with database chinook.db
You can download it here: https://drive.google.com/file/d/0Bz9_0VdXvv9bWUtqM0NBYzhKZ3c/view?usp=sharing&resourcekey=0-7zGUhDz0APEfX58SA8UKog

 The Chinook Database is about an imaginary video and music store. Each track is stored using one of the digital formats and has a genre. The store has also some playlists, where a single track can be part of several playlists. Orders are recorded for customers, but are called invoices. Every customer is assigned a support employee, and Employees report to other employees.
*/


-- MAKE YOURSELF FAIMLIAR WITH THE DATABASE AND TABLES HERE





--==================================================================
/* TASK I
Which artists did not make any albums at all? Include their names in your answer.
*/
SELECT artists.ArtistID, Name FROM artists
    WHERE artists.ArtistId NOT IN (SELECT albums.ArtistId FROM albums)


/* TASK II
Which artists recorded any tracks of the Latin genre?
*/
SELECT DISTINCT artists.Name FROM artists
JOIN albums ON artists.ArtistId = albums.ArtistId
JOIN tracks ON albums.AlbumId = tracks.AlbumId
JOIN genres ON tracks.GenreId = genres.GenreId
WHERE genres.Name LIKE 'Latin'
 
    


/* TASK III
Which video track has the longest length?
*/
SELECT name, MediaTypeId from media_types

SELECT tracks.TrackId, tracks.Name FROM tracks
JOIN media_types ON tracks.MediaTypeId = media_types.MediaTypeId
WHERE media_types.Name LIKE 'Protected MPEG-4 video file'
ORDER BY tracks.Milliseconds DESC

/* TASK IV
Find the names of customers who live in the same city as the top employee (The one not managed by anyone).
*/

SELECT customers.FirstName, customers.LastName FROM employees
JOIN customers ON employees.City = customers.City
WHERE employees.ReportsTo ISNULL

/* TASK V
Find the managers of employees supporting Brazilian customers.
*/
SELECT DISTINCT managers.FirstName, managers.LastName from employees
JOIN employees as managers ON employees.ReportsTo = managers.EmployeeId
JOIN customers ON employees.EmployeeId = customers.SupportRepId
WHERE customers.Country LIKE '%Brazil%'

/* TASK VI
Which playlists have no Latin tracks?
*/

SELECT DISTINCT playlist_track.PlaylistId FROM playlist_track
JOIN tracks ON playlist_track.TrackId = tracks.TrackId
JOIN genres ON tracks.GenreId = genres.GenreId
WHERE genres.name <> 'Latin'