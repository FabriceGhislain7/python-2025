# CLOUD COMPUTING

Il **cloud computing** è un modello di fornitura di risorse informatiche (come server, archiviazione, database, reti, software e analisi) attraverso Internet. È progettato per offrire accesso on-demand a risorse scalabili, eliminando la necessità di investimenti iniziali significativi in hardware o infrastruttura.

---

## **Principi Fondamentali**

1. **Accesso On-Demand**:  
   * Gli utenti possono accedere alle risorse informatiche senza necessità di interazioni manuali con i fornitori.  
2. **Multitenancy**:  
   * Le risorse sono condivise tra più utenti (o tenant) mantenendo la separazione dei dati.  
3. **Elasticità**:  
   * È possibile scalare le risorse in modo dinamico in base alle esigenze.  
4. **Pay-as-you-go**:  
   * Si paga solo per le risorse effettivamente utilizzate.  
5. **Disponibilità globale**:  
   * Le risorse sono accessibili da qualsiasi luogo con una connessione Internet.

---

## **Modelli di Servizio del Cloud**

1. **IaaS (Infrastructure as a Service)**:  
   * Fornisce infrastruttura virtualizzata come server, reti e storage.  
   * Esempi: **Amazon EC2**, **Google Compute Engine**, **Microsoft Azure Virtual Machines**.  
2. **PaaS (Platform as a Service)**:  
   * Fornisce piattaforme per lo sviluppo, il test e la distribuzione di applicazioni.  
   * Esempi: **Google App Engine**, **Heroku**, **Microsoft Azure App Services**.  
3. **SaaS (Software as a Service)**:  
   * Fornisce software pronto all'uso accessibile via browser.  
   * Esempi: **Google Workspace (Gmail, Drive)**, **Microsoft 365**, **Salesforce**.

---

## **Modelli di Distribuzione del Cloud**

1. **Public Cloud**:  
   * Risorse condivise e accessibili pubblicamente su Internet.  
   * Esempi: **AWS**, **Google Cloud Platform**, **Microsoft Azure**.  
2. **Private Cloud**:  
   * Risorse dedicate a un singolo cliente.  
   * Esempi: **VMware Cloud**, **OpenStack**.  
3. **Hybrid Cloud**:  
   * Combina risorse di cloud pubblico e privato.  
   * Esempio: Un'azienda può mantenere i dati sensibili in un private cloud e utilizzare il public cloud per applicazioni non critiche.  
4. **Community Cloud**:  
   * Risorse condivise tra organizzazioni con interessi comuni.

---

## **Vantaggi del Cloud Computing**

1. **Scalabilità**:  
   * Adatta rapidamente le risorse in base alla domanda.  
2. **Flessibilità**:  
   * Supporta una varietà di tecnologie e piattaforme.  
3. **Riduzione dei Costi**:  
   * Elimina l'investimento iniziale in hardware.  
4. **Accesso Globale**:  
   * Permette di lavorare ovunque.  
5. **Manutenzione Delegata**:  
   * Gli aggiornamenti e la manutenzione sono gestiti dal fornitore.  
6. **Affidabilità**:  
   * Data center ridondanti garantiscono alta disponibilità.

---

## **Svantaggi e Rischi**

1. **Dipendenza dal Fornitore**:  
   * Legame con una specifica piattaforma o infrastruttura (vendor lock-in).  
2. **Sicurezza**:  
   * Potenziale rischio di accesso non autorizzato ai dati.  
3. **Interruzioni del Servizio**:  
   * Possibili downtime del fornitore.  
4. **Costi Ricorrenti**:  
   * Costi operativi continui che possono aumentare rapidamente.

---

## **Principali Provider di Cloud**

### **Amazon Web Services (AWS)**

* Servizi popolari:  
  * Amazon EC2 (server virtuali)  
  * Amazon S3 (archiviazione)  
  * Amazon Lambda (serverless computing)

### **Google Cloud Platform (GCP)**

* Servizi popolari:  
  * Google Compute Engine (IaaS)  
  * Google Kubernetes Engine (GKE)  
  * BigQuery (analisi dati)

### **Microsoft Azure**

* Servizi popolari:  
  * Azure Virtual Machines  
  * Azure Functions (serverless)  
  * Azure DevOps (strumenti CI/CD)

### **IBM Cloud**

* Noti per soluzioni basate su **AI** e **blockchain**.

### **Oracle Cloud**

* Specializzato per soluzioni di database.

---

## **Esempi Pratici di Utilizzo del Cloud**

1. **Archiviazione e Backup**:  
   * Utilizzare Amazon S3 o Google Cloud Storage per archiviare file e backup.  
2. **Applicazioni Serverless**:  
   * Eseguire funzioni con AWS Lambda o Google Cloud Functions senza gestire server.  
3. **Big Data e Analisi**:  
   * Utilizzare servizi come Google BigQuery per analisi su larga scala.  
4. **Hosting di Applicazioni**:  
   * Usare Heroku o Azure App Services per distribuire applicazioni web.  
5. **CI/CD (Continuous Integration/Continuous Deployment)**:  
   * Automazione delle pipeline di sviluppo con strumenti come Jenkins o Azure DevOps.

---

## **Best Practices nel Cloud Computing**

1. **Sicurezza**:  
   * Configurare correttamente i permessi.  
   * Utilizzare crittografia per i dati in transito e a riposo.  
   * Monitorare accessi e attività con audit log.  
2. **Monitoraggio**:  
   * Usare strumenti come AWS CloudWatch per monitorare le risorse.  
3. **Gestione dei Costi**:  
   * Implementare tag per il tracciamento.  
   * Spegnere risorse non utilizzate.  
4. **Backup**:  
   * Pianificare backup regolari e testarli.  
5. **Ridondanza**:  
   * Utilizzare più regioni per alta disponibilità.

---

## **Strumenti per Cloud Computing**

1. **Terraform**:  
   * Infrastruttura come codice per gestire risorse cloud.  
2. **Kubernetes**:  
   * Orchestrazione di container su larga scala.  
3. **Ansible**:  
   * Automazione della configurazione e gestione.  
4. **Docker**:  
   * Containerizzazione per ambienti isolati.  
5. **CloudFormation**:  
   * Gestione delle risorse su AWS.

---

## **Futuro del Cloud Computing**

* **Edge Computing**:  
  * Sposta l'elaborazione vicino alla sorgente dei dati (IoT, 5G).  
* **AI e Machine Learning**:  
  * Servizi integrati per sviluppare modelli (es. AWS SageMaker, Google AI).  
* **Cloud Ibrido**:  
  * Maggiore adozione per combinare flessibilità e sicurezza.  
* **Quantum Computing**:  
  * Sviluppo di piattaforme cloud per calcolo quantistico (es. IBM Quantum).

Il cloud computing rappresenta una delle tecnologie chiave per il presente e il futuro della trasformazione digitale.