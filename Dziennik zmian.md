# Prosty Kalkulator w Pythonie 🧮

Projekt prostego kalkulatora konsolowego stworzony w języku Python. Program umożliwia wykonywanie podstawowych operacji matematycznych.

## 📂 Struktura plików
W tym repozytorium znajdują się dwie wersje programu:

* `kalkulator_v1.py` - Pierwotna, podstawowa wersja kalkulatora.
* `kalkulator_v2.py` - **Rozbudowana wersja** z nowymi funkcjami (aktualna).

---

## 📝 Dziennik Zmian (Modyfikacje)

Poniżej znajduje się lista modyfikacji wprowadzonych względem pierwotnej wersji programu.

### Aktualizacja do wersji 2.0:
W pliku `kalkulator_v2.py` wprowadzono następujące ulepszenia:

1.  **Dodano funkcję potęgowania:**
    * Zaimplementowano nowy operator `^`.
    * Użytkownik może teraz podnosić pierwszą liczbę do potęgi drugiej liczby.
    
2.  **Wprowadzono pętlę działania (`while True`):**
    * Kalkulator nie wyłącza się po jednym obliczeniu.
    * Dodano komendę `exit`, która pozwala bezpiecznie zakończyć działanie programu.

3.  **Poprawiono obsługę błędów:**
    * Dodano blok `try-except`, który zapobiega awarii programu, gdy użytkownik wpisze tekst zamiast liczby.
    * Dodano czytelniejsze komunikaty błędów (np. przy dzieleniu przez zero).

---

## 🚀 Jak uruchomić?

Aby uruchomić nową wersję kalkulatora, wpisz w terminalu:

```bash
python kalkulator_v2.py
