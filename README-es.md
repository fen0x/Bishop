# Bishop

Choose your preferred language:

[![English](https://img.shields.io/badge/🇬🇧English-blue?style=flat-square)](./README.md)
[![Italiano](https://img.shields.io/badge/🇮🇹Italian-green?style=flat-square)](./README-it.md)
[![Polski](https://img.shields.io/badge/🇵🇱Polski-red?style=flat-square)](./README-pl.md)
[![Deutsch](https://img.shields.io/badge/🇩🇪Deutsch-yellow?style=flat-square)](./README-de.md)
[![Español](https://img.shields.io/badge/🇪🇸Espa%C3%B1ol-orange?style=flat-square)](./README-es.md)
[![Русский](https://img.shields.io/badge/🇷🇺%D0%A0%D1%83%D1%81%D1%81%D0%BA%D0%B8%D0%B9-purple?style=flat-square)](./README-ru.md)

Bishop es un bot de Telegram diseñado para enviar publicaciones en cola desde un subreddit específico directamente a Telegram. Los usuarios pueden aprobar o eliminar publicaciones con comandos simples.

![GitHub Repo stars](https://img.shields.io/github/stars/fen0x/Bishop?style=flat-square) 
![GitHub License](https://img.shields.io/github/license/fen0x/Bishop?style=flat-square) 

## Funciones

Actualmente, Bishop admite dos comandos principales:

- **/appost**: aprueba la publicación enviada.  
- **/delrule (regla)**: elimina la publicación según la regla especificada.  

El proyecto aún se encuentra en fase alfa y está en desarrollo activo. Debido a su etapa temprana, pueden surgir errores o comportamientos inesperados. ¡Los comentarios y sugerencias son bienvenidos!

## Tecnologías utilizadas

- Lenguaje: **Python**  
- Gestión de bibliotecas: **Poetry**  
- Bibliotecas: **Telethon**, **PRAW**  

## Cómo empezar

1. **Clona el repositorio:**  
   ```bash
   git clone https://github.com/fen0x/Bishop.git
   cd Bishop
   ```

2. **Instala las dependencias:**  
   Asegúrate de tener instalado Python y Poetry, luego ejecuta:  
   ```bash
   poetry install
   ```

3. **Configura el bot:**  
   Edita el archivo `config.ini.example` con el token de tu bot de Telegram y otras configuraciones necesarias (por ejemplo, el subreddit a monitorear) y cámbiale el nombre a `config.ini`.

4. **Ejecuta el bot:**  
   ```bash
   poetry run python main.py
   ```

## Contribuir

Bishop es de código abierto y gratuito. Si deseas contribuir:  

1. Haz un fork del repositorio.  
2. Crea una nueva rama para tu función o corrección de errores.  
3. Envía un pull request cuando termines.  

## Licencia

Este proyecto se distribuye bajo la licencia MIT. Consulta el archivo `LICENSE` para obtener más detalles.  

---

¡Gracias por tu interés en Bishop! Esperamos mejorar continuamente este bot con la ayuda de la comunidad.