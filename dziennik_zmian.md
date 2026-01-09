# Dokumentacja Projektu: Kalkulator

W tym repozytorium znajdują się dwie wersje kalkulatora napisanego w Pythonie. Poniżej opisano różnice między nimi oraz wprowadzone modyfikacje.

## 📂 Pliki w projekcie

* **`kalkulator_v1.py`** – Pierwotna, podstawowa wersja programu. Obsługuje tylko pojedyncze działania (+, -, *, /).
* **`kalkulator_v2.py`** – Rozbudowana wersja z nowymi funkcjami (szczegóły poniżej).

---

## 📝 Dziennik Zmian (Changelog)

W pliku `kalkulator_v2.py` wprowadzono następujące modyfikacje względem oryginału:

### 1. Nowa funkcja matematyczna: Potęgowanie
* **Co zmieniono:** Dodano obsługę operatora `^`.
* **Jak to działa:** Program pobiera dwie liczby i wykonuje działanie potęgowania (liczba1 do potęgi liczba2) przy użyciu składni `**`.

### 2. Praca w pętli (Ciągłe działanie)
* **Co zmieniono:** Cały kod zamknięto w pętli `while True`.
* **Cel:** W starej wersji program kończył się po jednym wyniku. Teraz pozwala na wykonywanie wielu obliczeń bez konieczności ponownego uruchamiania.

### 3. Komenda wyjścia
* **Co zmieniono:** Dodano instrukcję warunkową sprawdzającą, czy użytkownik wpisał słowo `exit`.
* **Cel:** Umożliwia bezpieczne i kontrolowane zakończenie działania pętli i programu.

### 4. Zabezpieczenie przed błędami (Error Handling)
* **Co zmieniono:** Dodano blok `try...except`.
* **Cel:** Jeśli użytkownik wpisze litery zamiast cyfr, stara wersja wyrzucała błąd systemowy. Nowa wersja wyświetla przyjazny komunikat "Proszę wpisywać tylko liczby" i pozwala spróbować ponownie.
