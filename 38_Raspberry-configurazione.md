# CONFIGURAZIONE RASPBERRY PI

Installazione di Raspberry Pi OS Lite
- Scaricare l'immagine di Raspberry Pi OS Lite dal sito ufficiale di Raspberry Pi.
- Configurare la connessione Wi-Fi e le impostazioni di base (come il nome host) durante il primo avvio.
- Scegliere se si desidera utilizzare SSH per accedere al Raspberry Pi senza un monitor.
- Abilitare SSH per accedere al Raspberry Pi da remoto.
- Scegliere se si desidera accedere con SSH password o chiave pubblica.
- Utilizzare Raspberry Pi Imager per scrivere l'immagine su una scheda SD.
- Inserire la scheda SD nel Raspberry Pi e accenderlo.

 # Visual studio code

 Scaricare l estensione Remote - SSH per Visual Studio Code.
- Aprire Visual Studio Code e accedere al Raspberry Pi tramite SSH.
```bash
ssh pi@<IP_ADDRESS>
# oppure
ssh pi@<HOSTNAME>
ssh allievo@rasp0-a.local
```
In modo da verificare che la connessione SSH funzioni correttamente.
```bash
ssh -v nomedispositivo
```
Il comando ssh pi@<IP_ADDRESS> consente di accedere al Raspberry Pi tramite SSH.
oppure utilizzare il comando ssh pi@<HOSTNAME> se si è configurato un nome host.

> In questo caso il nome host è raspberrypi ed pi è l utente predefinito.

# Configurare il Raspberry Pi in Visual Studio Code
- Premere `CTRL + SHIFT + P` per aprire il menu dei comandi.
- Digitare "Apri file di configurazione SSH" e selezionare il file di configurazione SSH.
- Aggiungere la seguente riga al file di configurazione SSH:
```
Host raspberrypi
    HostName <IP_ADDRESS>
    User pi
```
- Sostituire `<IP_ADDRESS>` con l'indirizzo IP del Raspberry Pi.

# Connettersi al Raspberry Pi
- Digitare "Remote-SSH: Connect to Host" e selezionare il Raspberry Pi dall'elenco.
- Selezionare "Apri cartella" e scegliere la cartella in cui si desidera lavorare.

# Verificare l ip che è stato assegnato al raspberry
- Per verificare l'indirizzo IP del Raspberry Pi, utilizzare il comando `hostname -I`.
```bash
hostname -I
```
- Oppure usare il comando `ip a` per visualizzare le informazioni di rete.
```bash
ip a
```
- Per visualizzare le informazioni di rete, utilizzare il comando `ifconfig`.
```bash
ifconfig
ip addr
ip route
ip link
ip neigh
```
# Aggiornare il Raspberry Pi
- Per aggiornare il Raspberry Pi, utilizzare i seguenti comandi:
```bash
# aggiornare l'elenco dei pacchetti disponibili
sudo apt update
# aggiornare i pacchetti installati
sudo apt upgrade
# eseguire il reboot del raspberry
sudo reboot
```
- Per installare i pacchetti necessari, utilizzare il comando `sudo apt install` seguito dal nome del pacchetto.
```bash
sudo apt install nome_pacchetto
```

# Navigare tra i files
- è possibile navigare tra i vari files del raspberry in modo da selezionare la cartella root di Visual Studio Code.
- Per navigare tra i files, utilizzare il comando `cd` seguito dal percorso della cartella desiderata.
- Per creare una nuova cartella, utilizzare il comando `mkdir` seguito dal nome della cartella.

- Per visualizzare i file e le cartelle presenti nella cartella corrente, utilizzare il comando `ls`.
```bash
ls -l /
```
# WHOAMI
- Per visualizzare l'utente corrente, utilizzare il comando `whoami`.
```bash
whoami
```
- Per visualizzare il percorso della cartella corrente, utilizzare il comando `pwd`.
```bash
pwd
```
cd /home/pi (nome utente dato in configurazione)
# Creare una nuova cartella
- Per creare una nuova cartella, utilizzare il comando `mkdir` seguito dal nome della cartella.
```bash
mkdir nome_cartella
```
# Permessi e proprietà
Ogni cifra è Owner-Group-Others:
- 7 = rwx
- 6 = rw-
- 5 = r-x
- 4 = r--
```bash
# rwx (7) per owner, r-x (5) per group, r-- (4) per others
chmod 754 eseguibile
```
Dopo aver creato un file, puoi verificare permessi e proprietario con:
```bash
ls -l nomefile
```
# Se devi cambiare proprietario o permessi
```bash
sudo chown allievo:allievo nomefile      # diventi proprietario tu
chmod 644 nomefile                       # rw-r--r-- per file testuali
chmod +x script.sh                       # rende eseguibile uno script
```
Se invece il proprietario non è allievo o i permessi non ti permettono di scrivere:
```bash
sudo chown allievo:allievo /home/allievo
chmod 755 /home/allievo
```
La rotta dove creare la folder con i progetti di visual studio code su raspberry è
```bash
/home/pi/.vscode-server/data/Machine
```
# Comandi linux utili
- `ls`: elenca i file e le cartelle nella directory corrente.
- `cd`: cambia la directory corrente.
- `mkdir`: crea una nuova directory.
- `rm`: rimuove file o directory.
- `cp`: copia file o directory.
- `mv`: sposta o rinomina file o directory.
- `nano`: apre un editor di testo per modificare file.
- `cat`: visualizza il contenuto di un file.
- `chmod`: cambia i permessi di un file o directory.
- `chown`: cambia il proprietario di un file o directory.
- `sudo`: esegue un comando come superutente.
- `apt-get`: gestisce i pacchetti software su Debian e Ubuntu.
- `apt update`: aggiorna l'elenco dei pacchetti disponibili.
- `apt upgrade`: aggiorna i pacchetti installati.
- `apt install`: installa un pacchetto software.
- `apt remove`: rimuove un pacchetto software.
- `ifconfig`: visualizza le informazioni di rete.
- `ping`: verifica la connettività di rete.
- `ssh`: accede a un altro computer tramite SSH.
- `scp`: copia file tra computer tramite SSH.

# cat
- Il comando `cat` viene utilizzato per visualizzare il contenuto di un file.
- Per visualizzare gli utenti presenti nel sistema, utilizzare il comando `cat /etc/passwd`.
```bash
cat /etc/passwd
```
- Per visualizzare i gruppi presenti nel sistema, utilizzare il comando `cat /etc/group`.
```bash
cat /etc/group
```
# Nano
- `nano`: è un editor di testo da riga di comando.
- Per aprire un file con nano, utilizzare il comando `nano` seguito dal nome del file.
```bash
nano nome_file.txt
```
- Per salvare le modifiche, premere `CTRL + O`, quindi `Invio`.
- Per uscire da nano, premere `CTRL + X`.
- Per copiare e incollare il testo, utilizzare `CTRL + K` per tagliare e `CTRL + U` per incollare.
- Per cercare una parola o una frase, premere `CTRL + W` e digitare la parola o la frase da cercare.

# Impostare la configurazione di rete con Nano
- Per configurare la rete, utilizzare il comando `sudo nano /etc/dhcpcd.conf`.
- Aggiungere le seguenti righe alla fine del file:
```bash
interface wlan0
static ip_address=<IP_ADDRESS>/24 (oppure senza /24 se non si conosce la subnet mask)
static routers=<ROUTER_IP>
static domain_name_servers=<DNS_IP>
```
- Sostituire `<IP_ADDRESS>` con l'indirizzo IP desiderato per il Raspberry Pi, `<ROUTER_IP>` con l'indirizzo IP del router e `<DNS_IP>` con l'indirizzo IP del server DNS.
- Salvare le modifiche e uscire da nano.
- Riavviare il Raspberry Pi per applicare le modifiche alla configurazione di rete.
```bash
sudo reboot
```
# Configurare il Raspberry Pi per l'accesso remoto
- Per abilitare SSH, utilizzare il comando `sudo raspi-config`.
- Selezionare "Interfacing Options" e quindi "SSH".
- Selezionare "Yes" per abilitare SSH.

# Test finale
Dentro VS Code terminale integrato (o in SSH shell):

```bash
pwd      # conferma che sei in /home/allievo/VSCodeProjects
ls -la   # verifica che la cartella sia vuota/pronta
```
# Comandi gestione files e folders
touch – crea un file vuoto (o aggiorna la data)
```bash
# Nella tua cartella corrente, crea un file vuoto chiamato "appunti.txt"
touch appunti.txt
```
Se il file “appunti.txt” esiste già, il comando touch aggiorna la data di ultima modifica del file. Puoi usarlo per creare un file vuoto o per aggiornare la data di un file esistente.

Se “appunti.txt” non esiste, lo crea; se esiste, ne aggiorna la data di ultima modifica.

```bash
# Crea (o sovrascrive) "index.html" con il contenuto tra virgolette
echo "<!DOCTYPE html><html><body><h1>Ciao!</h1></body></html>" > index.html
Se vuoi aggiungere testo a un file esistente senza cancellarne il contenuto, usa >>:
```
```bash
echo "Riga aggiunta" >> appunti.txt
```
# Gestione utenti

Creare diversi utenti permette di separare i progetti e le configurazioni.

- Per visualizzare gli utenti presenti nel sistema, utilizzare il comando `cat /etc/passwd`.
```bash
cat /etc/passwd
```
- Per visualizzare i gruppi presenti nel sistema, utilizzare il comando `cat /etc/group`.
```bash
cat /etc/group
```
- Per creare un nuovo gruppo, utilizzare il comando `sudo addgroup` seguito dal nome del gruppo.
```bash
sudo addgroup nome_gruppo
```
- Per creare un nuovo utente, utilizzare il comando `sudo adduser` seguito dal nome dell'utente.
```bash
sudo adduser nome_utente
```
- Per aggiungere l'utente a un gruppo, utilizzare il comando `sudo usermod -aG` seguito dal nome del gruppo e dal nome dell'utente.
```bash
sudo usermod -aG nome_gruppo nome_utente
```
- Per rimuovere un utente, utilizzare il comando `sudo deluser` seguito dal nome dell'utente.
```bash
sudo deluser nome_utente
```
- Per modificare la password di un utente, utilizzare il comando `sudo passwd` seguito dal nome dell'utente.
```bash
sudo passwd nome_utente
```
- Per visualizzare gli utenti inseriti in un gruppo in modo piu sintetico:
```bash
getent group nome_gruppo
```
- Per visualizzare i gruppi a cui appartiene un utente, utilizzare il comando `groups` seguito dal nome dell'utente.
```bash
getent group nome_utente
```
- Per switchare l'utente corrente a un altro utente, utilizzare il comando `su` seguito dal nome dell'utente.
```bash
su nome_utente
su - nome_utente # per passare alla home dell'utente caricando il suo ambiente
```
# Attivita utili
Informazioni di sistema
```bash
uname -a
```
Mostra kernel, architettura e versione del sistema.

Visualizza il carico della CPU ed altre informazioni in tempo reale:
```bash
htop
```
Visualizza memoria libera e usata in formato leggibile.
```bash
free -h
```
Spazio su disco di tutte le partizioni (GB, MB).
```bash
df -h
```
Informazioni sui dispositivi di blocco (dischi, partizioni, USB).
```bash
lsblk
```
Terminare un processo per PID o per nome:
```bash
kill 1234
```
Interfaccia Ncurses per esplorare l’uso del disco:
```bash
ncdu /
```
Si esce con q
# Alias
Definisci scorciatoie in ~/.bashrc o ~/.zshrc:
```bash
alias ll='ls -lah'
alias gs='git status'
```