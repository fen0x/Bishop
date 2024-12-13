# Bishop

Choose your preferred language:

[![English](https://img.shields.io/badge/🇬🇧English-blue?style=flat-square)](./README.md)
[![Italiano](https://img.shields.io/badge/🇮🇹Italian-green?style=flat-square)](./README-it.md)
[![Polski](https://img.shields.io/badge/🇵🇱Polski-red?style=flat-square)](./README-pl.md)
[![Deutsch](https://img.shields.io/badge/🇩🇪Deutsch-yellow?style=flat-square)](./README-de.md)
[![Español](https://img.shields.io/badge/🇪🇸Espa%C3%B1ol-orange?style=flat-square)](./README-es.md)
[![Русский](https://img.shields.io/badge/🇷🇺%D0%A0%D1%83%D1%81%D1%81%D0%BA%D0%B8%D0%B9-purple?style=flat-square)](./README-ru.md)

Bishop to bot Telegramowy stworzony do wysyłania oczekujących postów z określonego subreddita bezpośrednio do Telegrama. Użytkownicy mogą zatwierdzać lub usuwać posty za pomocą prostych komend.

![GitHub Repo stars](https://img.shields.io/github/stars/fen0x/Bishop?style=flat-square) 
![GitHub License](https://img.shields.io/github/license/fen0x/Bishop?style=flat-square) 

## Funkcje

Obecnie Bishop obsługuje dwie główne komendy:

- **/appost**: zatwierdza wysłany post.  
- **/delrule (reguła)**: usuwa post na podstawie określonej reguły.  

Projekt jest nadal w fazie alfa i aktywnie rozwijany. Ze względu na wczesny etap rozwoju mogą występować błędy lub nieoczekiwane zachowania. Opinie i sugestie są mile widziane!

## Wykorzystane technologie

- Język: **Python**  
- Zarządzanie bibliotekami: **Poetry**  
- Biblioteki: **Telethon**, **PRAW**  

## Jak zacząć

1. **Sklonuj repozytorium:**  
   ```bash
   git clone https://github.com/fen0x/Bishop.git
   cd Bishop
   ```

2. **Zainstaluj zależności:**  
   Upewnij się, że Python i Poetry są zainstalowane, a następnie uruchom:  
   ```bash
   poetry install
   ```

3. **Skonfiguruj bota:**  
   Edytuj plik `config.ini.example`, wprowadzając token swojego bota Telegramowego oraz inne niezbędne konfiguracje (np. subreddit do monitorowania) i zmień jego nazwę na `config.ini`.

4. **Uruchom bota:**  
   ```bash
   poetry run python main.py
   ```

## Współtworzenie projektu

Bishop jest projektem open source i jest darmowy. Jeśli chcesz pomóc w rozwoju:  

1. Forknij repozytorium.  
2. Utwórz nowy branch dla swojej funkcji lub poprawki błędu.  
3. Wyślij pull request po zakończeniu pracy.  

## Licencja

Ten projekt jest dystrybuowany na licencji MIT. Szczegóły znajdują się w pliku `LICENSE`.  

---

Dziękujemy za zainteresowanie projektem Bishop! Mamy nadzieję, że dzięki wsparciu społeczności uda nam się go nieustannie udoskonalać.