# Bishop

Choose your preferred language:

[![English](https://img.shields.io/badge/🇬🇧English-blue?style=flat-square)](./README.md)
[![Italiano](https://img.shields.io/badge/🇮🇹Italian-green?style=flat-square)](./README-it.md)
[![Polski](https://img.shields.io/badge/🇵🇱Polski-red?style=flat-square)](./README-pl.md)
[![Deutsch](https://img.shields.io/badge/🇩🇪Deutsch-yellow?style=flat-square)](./README-de.md)
[![Español](https://img.shields.io/badge/🇪🇸Espa%C3%B1ol-orange?style=flat-square)](./README-es.md)
[![Русский](https://img.shields.io/badge/🇷🇺%D0%A0%D1%83%D1%81%D1%81%D0%BA%D0%B8%D0%B9-purple?style=flat-square)](./README-ru.md)

Bishop è un bot di Telegram progettato per inviare post in coda da un subreddit specifico direttamente su Telegram. Gli utenti possono quindi approvare o eliminare i post utilizzando comandi semplici.

![GitHub Repo stars](https://img.shields.io/github/stars/fen0x/Bishop?style=flat-square) 
![GitHub License](https://img.shields.io/github/license/fen0x/Bishop?style=flat-square) 

## Funzionalità

Attualmente, Bishop supporta due comandi principali:

- **/appost**: approva il post inviato.  
- **/delrule (regola)**: elimina il post in base alla regola specificata.

Il progetto è ancora in fase alfa ed è in attivo sviluppo. Essendo nelle sue fasi iniziali, potrebbero verificarsi bug o comportamenti imprevisti. Feedback e suggerimenti sono benvenuti!

## Tecnologie Utilizzate

- Linguaggio: **Python**  
- Gestione delle dipendenze: **Poetry**  
- Librerie: Telethon, PRAW  

## Come Iniziare

1. **Clona il repository:**  
   ```bash
   git clone https://github.com/fen0x/Bishop.git
   cd Bishop
   ```

2. **Installa le dipendenze:**  
   Assicurati di avere Python e Poetry installati, poi esegui:  
   ```bash
   poetry install
   ```

3. **Configura il bot:**  
   Modifica il file `config.ini.example` con il token del tuo bot Telegram e le altre configurazioni necessarie (ad esempio, il subreddit da monitorare) e rinominalo in `config.ini`.

4. **Avvia il bot:**  
   ```bash
   poetry run python main.py
   ```

## Contribuire

Bishop è open source e gratuito. Se desideri contribuire:  

1. Fai un fork del repository.  
2. Crea un nuovo branch per la tua funzionalità o correzione.  
3. Invia una pull request quando hai terminato.  

## Licenza

Questo progetto è distribuito sotto la licenza MIT. Consulta il file `LICENSE` per maggiori dettagli.

---

Grazie per l'interesse in Bishop! Speriamo di migliorare continuamente questo bot con l'aiuto della comunità.

---