## Zadanie 1 – Proste testy jednostkowe

W pliku znajduje się funkcja `is_even(n)`, która sprawdza, czy liczba jest parzysta.

Twoim zadaniem jest zaimplementowanie dwóch prostych testów:
- `test_is_even_with_even_number()` – test sprawdzający działanie funkcji dla liczby parzystej,
- `test_is_even_with_odd_number()` – test sprawdzający działanie funkcji dla liczby nieparzystej.

---

## Zadanie 2 – Testy sparametryzowane

W pliku znajduje się funkcja `is_prime(n)`, która sprawdza, czy liczba jest pierwsza.

Twoim zadaniem jest napisanie testów sparametryzowanych dla tej funkcji. Uwzględnij przypadki zarówno liczb pierwszych, jak i złożonych.

---

## Zadanie 3 – Testowanie wyjątków

Masz za zadanie przetestować funkcję `withdraw(balance, amount)` sprawdzającą poprawność wypłaty z konta bankowego.

Zaimplementuj trzy testy:
- `test_withdraw_success()` – test poprawnej wypłaty,
- `test_withdraw_negative_amount()` – test rzucania wyjątku przy podaniu ujemnej kwoty,
- `test_withdraw_insufficient_funds()` – test rzucania wyjątku przy próbie wypłaty większej niż dostępny stan konta.

---

## Zadanie 4 – Rozdzielenie logiki na funkcje

Masz daną funkcję `process_order(user, order)`

Rozdziel tę funkcję na trzy osobne.

---

## Zadanie 5 – Mockowanie bazy danych

Masz przetestować funkcję `user_exists(db, email)` 

Zaimplementuj dwa testy:
- `test_user_exists_found()` – baza zwraca użytkownika,
- `test_user_exists_not_found()` – baza nie znajduje użytkownika.

---

## Zadanie 6 – Test-Driven Development (TDD)

Na podstawie gotowych testów napisz funkcję `romanToInt(s: str) -> int`

Twoim celem jest tak napisać funkcję, by **wszystkie testy przechodziły**.
"""
