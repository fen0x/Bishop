# Bishop

Choose your preferred language:

[![English](https://img.shields.io/badge/🇬🇧English-blue?style=flat-square)](./README.md)
[![Italiano](https://img.shields.io/badge/🇮🇹Italian-green?style=flat-square)](./README-it.md)
[![Polski](https://img.shields.io/badge/🇵🇱Polski-red?style=flat-square)](./README-pl.md)
[![Deutsch](https://img.shields.io/badge/🇩🇪Deutsch-yellow?style=flat-square)](./README-de.md)
[![Español](https://img.shields.io/badge/🇪🇸Espa%C3%B1ol-orange?style=flat-square)](./README-es.md)
[![Русский](https://img.shields.io/badge/🇷🇺%D0%A0%D1%83%D1%81%D1%81%D0%BA%D0%B8%D0%B9-purple?style=flat-square)](./README-ru.md)

Bishop ist ein Telegram-Bot, der dazu dient, wartende Beiträge aus einem bestimmten Subreddit direkt an Telegram zu senden. Benutzer können Beiträge mit einfachen Befehlen genehmigen oder löschen.

![GitHub Repo stars](https://img.shields.io/github/stars/fen0x/Bishop?style=flat-square) 
![GitHub License](https://img.shields.io/github/license/fen0x/Bishop?style=flat-square) 

## Funktionen

Derzeit unterstützt Bishop zwei Hauptbefehle:

- **/appost**: Genehmigt den gesendeten Beitrag.  
- **/delrule (Regel)**: Löscht den Beitrag basierend auf der angegebenen Regel.  

Das Projekt befindet sich noch in der Alpha-Phase und wird aktiv weiterentwickelt. Da es sich in einem frühen Entwicklungsstadium befindet, können Bugs oder unerwartetes Verhalten auftreten. Feedback und Vorschläge sind willkommen!

## Verwendete Technologien

- Sprache: **Python**  
- Paketverwaltung: **Poetry**  
- Bibliotheken: **Telethon**, **PRAW**  

## Erste Schritte

1. **Repository klonen:**  
   ```bash
   git clone https://github.com/fen0x/Bishop.git
   cd Bishop
   ```

2. **Abhängigkeiten installieren:**  
   Stellen Sie sicher, dass Python und Poetry installiert sind, und führen Sie dann Folgendes aus:  
   ```bash
   poetry install
   ```

3. **Bot konfigurieren:**  
   Bearbeiten Sie die Datei `config.ini.example` mit Ihrem Telegram-Bot-Token und anderen erforderlichen Konfigurationen (z. B. das zu überwachende Subreddit) und benennen Sie sie in `config.ini` um.

4. **Bot starten:**  
   ```bash
   poetry run python main.py
   ```

## Beiträge leisten

Bishop ist Open Source und kostenlos. Wenn Sie einen Beitrag leisten möchten:  

1. Forken Sie das Repository.  
2. Erstellen Sie einen neuen Branch für Ihre Funktion oder Fehlerbehebung.  
3. Reichen Sie eine Pull-Request ein, wenn Sie fertig sind.  

## Lizenz

Dieses Projekt wird unter der MIT-Lizenz vertrieben. Weitere Details finden Sie in der Datei `LICENSE`.  

---

Vielen Dank für Ihr Interesse an Bishop! Wir hoffen, diesen Bot mit der Unterstützung der Community kontinuierlich verbessern zu können.