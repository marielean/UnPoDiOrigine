# Usa un'immagine Python ufficiale come immagine base
FROM python:3.8

# Imposta la directory di lavoro nel container
WORKDIR /usr/src/app

# Copia il file delle dipendenze e installale
COPY requirements.txt ./
# Crea un ambiente virtuale per isolare le dipendenze
RUN python -m venv .venv
RUN .venv/bin/python -m pip install --upgrade pip
RUN .venv/bin/pip install --no-cache-dir -r requirements.txt

# Copia il resto del codice sorgente del progetto nel container
COPY . .

# Espone la porta 8000
EXPOSE 8000

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]