# Modul_9.4
Zadanie z modułu 9.4

Obsługa API

GET http://localhost:5000/api/library/albums/ - zwraca wszystkie albumy w formacie JSON
POST http://localhost:5000/api/library/albums/ - dodaje nowy album do listy - zapytanie oczekuje danych w formacie JSON*
DELETE http://localhost:5000/api/library/albums/ - usuwa wszystkie albumy

GET http://localhost:5000/api/library/albums/{numer id} - zwraca pojedyńczy album w formacie JSON
PUT http://localhost:5000/api/library/albums/{numer id} - aktualizuje album o podanym numerze ID - zapytanie oczekuje danych w formacie JSON*
DELETE http://localhost:5000/api/library/albums/{numer id} - usuwa album o wybranym numerze ID

*struktura obiektu:
{
    "album_name": 	(oczekiwany string, pole wymagane),
    "author_name": 	(oczekiwany string),
    "genre": 		(oczekiwany string),
    "release_year": 	(oczekiwany integer)
}
