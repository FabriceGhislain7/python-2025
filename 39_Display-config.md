# Specifiche tecniche del display

Tipo: TFT LCD touch capacitivo

Dimensioni: 3,5 pollici

Risoluzione: 480x320 pixel

Interfaccia: SPI (collegamento tramite GPIO)

Controller touch: XPT2046

> Compatibilità: Raspberry Pi 2, 3, 4, Zero, Zero W

# Passaggi per l'installazione

1. Installazione dei prerequisiti (git github)
Assicurati che il tuo Raspberry Pi sia aggiornato e abbia installato `git` e `python3-pip`. Apri il terminale e digita i seguenti comandi:
```bash
sudo apt-get update
sudo apt-get install -y git python3-pip  # -y per confermare automaticamente l'installazione
```
Installazione github cli
```bash
sudo apt-get install -y gh
```

2. Collegamento del display
- **Spegni il Raspberry Pi**
- Collega il display direttamente ai pin GPIO del Raspberry Pi, assicurandoti che i pin siano allineati correttamente.

3. Abilitazione dell'interfaccia SPI
- Avvia il Raspberry Pi collegato SSH.

Apri il terminale e digita:
```bash
sudo raspi-config
```
- Naviga su **Interface Options → SPI → Yes** per abilitare l'interfaccia SPI.
- Riavvia il Raspberry Pi:
```bash
sudo reboot
```
4. Installazione dei driver
Assicurati che il Raspberry Pi sia connesso a Internet.
Apri il terminale e digita i seguenti comandi:
```bash
sudo rm -rf LCD-show  # Rimuove eventuali vecchie versioni del driver
git clone https://github.com/goodtft/LCD-show.git  # Clona il repository dei driver
chmod -R 755 LCD-show  # Imposta i permessi corretti
cd LCD-show/  # Entra nella cartella dei driver
sudo ./LCD35-show  # Installa il driver per il display 3.5"
```
Il Raspberry Pi si riavvierà automaticamente e il display dovrebbe mostrare l'interfaccia grafica.

>  Nota: Dopo l'installazione, l'output video sarà diretto al display touch, disattivando l'uscita HDMI. Per ripristinare l'output su HDMI, esegui:

```bash
cd LCD-show/  # Entra nella cartella dei driver
sudo ./LCD-hdmi  # Ripristina l'output su HDMI
```
5. Configurazione del touch screen

- Calibrazione del touch (opzionale)

Se noti che il tocco non è preciso o è invertito:

- Installa il calibratore:
```bash
sudo apt-get update
sudo apt-get install -y xserver-xorg-input-evdev
```
6. Calibrazione del touch screen
Per calibrare il touch screen, puoi utilizzare il pacchetto `xinput-calibrator`. Esegui i seguenti comandi:
```bash
sudo apt-get update
sudo apt-get install -y xinput-calibrator
```
Esegui la calibrazione:
```bash
DISPLAY=:0.0 xinput_calibrator  # Avvia il calibratore
# se il calibratore non si avvia, prova a eseguire:
ssh -X pi@<indirizzo_ip_del_raspberry>  # Avvia il Raspberry Pi con l'opzione X11 forwarding
```
Segui le istruzioni sullo schermo per calibrare il touch.

Se la calibrazione con `xinput_calibrator` non funziona, puoi provare a utilizzare il comando `evtest` per verificare gli eventi del touch screen:
```bash
sudo apt-get update
sudo apt-get install -y evtest
sudo evtest  # Avvia evtest per monitorare gli eventi del touch
```
# Crea il file di calibrazione
Apri un terminale:

```bash
sudo nano /etc/X11/xorg.conf.d/99-calibration.conf
```
Se la cartella non esiste, creala:
```bash
sudo mkdir -p /etc/X11/xorg.conf.d/
```
2. Inserisci il contenuto

- Nel file 99-calibration.conf, incolla:

```bash
Section "InputClass"
    Identifier      "calibration"
    MatchProduct    "ADS7846 Touchscreen"
    Option          "Calibration"   "170 3800 3900 200"
    Option          "SwapAxes"      "1"
EndSection
```
Spiegazione dei valori:

"170 3800 3900 200" sono i valori minX, maxX, maxY, minY.

"SwapAxes" "1" serve se il touchscreen è ruotato di 90° (molto comune)

# Verifica del funzionamento con Python
Per testare il corretto funzionamento del display e del touch screen, puoi eseguire un semplice script Python che rileva gli eventi touch.

Istruzioni:

> Assicurati di avere Pygame installato:

1. Crea l'ambiente virtuale e installa Pygame:

Crea la cartella del progetto
```bash
mkdir /touchscreen_test
cd /touchscreen_test
```

```bash
python3 -m venv venv
source venv/bin/activate
```
```bash
sudo apt-get install python3-pygame
```

Ecco un esempio:

```python
import pygame
import sys

# Inizializza Pygame
pygame.init()

# Imposta la dimensione dello schermo
screen = pygame.display.set_mode((480, 320))
pygame.display.set_caption("Test Touch")

# Colori
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Riempie lo schermo di bianco
screen.fill(WHITE)
pygame.display.update()

# Loop principale
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Ottiene la posizione del tocco
            pos = pygame.mouse.get_pos()
            # Disegna un cerchio rosso nella posizione toccata
            pygame.draw.circle(screen, RED, pos, 5)
            pygame.display.update()

pygame.quit()
sys.exit()
```
2. Salva lo script in un file, ad esempio test_touch.py.
3. Esegui lo script:

```bash
python3 test_touch.py
```

4. Tocca lo schermo; dovresti vedere dei cerchi rossi apparire nei punti toccati