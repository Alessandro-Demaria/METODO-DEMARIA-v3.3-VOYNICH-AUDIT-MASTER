# METODO DEMARIA® Release v3.2 (Audit-Master)
### Computational Analysis and Vector Topology of the Voynich Manuscript (Beinecke MS 408)

[![Validation Suite - Metodo Demaria](https://github.com/Alessandro-Demaria/METODO-DEMARIA-v3.3-VOYNICH-AUDIT-MASTER/actions/workflows/validate.yml/badge.svg)](https://github.com/Alessandro-Demaria/METODO-DEMARIA-v3.3-VOYNICH-AUDIT-MASTER/actions/workflows/validate.yml)

**Autore, Responsabile Scientifico e Inventore Unico**: Avv. Alessandro Demaria (Molochio, RC)[cite: 7]  
**Concept DOI Madre (Archivio Permanente)**: [10.5281/zenodo.22789343](https://doi.org/10.5281/zenodo.22789343)[cite: 7]  
**DOI Ufficiale Release v3.2 (Audit-Master)**: [10.5281/zenodo.23199718](https://doi.org/10.5281/zenodo.23199718)[cite: 7]  
**DOI Trattato Voynich-Summa**: [10.5281/zenodo.22999135](https://doi.org/10.5281/zenodo.22999135)[cite: 7]  
**Licenza del Trattato e dei Dati**: Creative Commons Attribution 4.0 International (CC BY 4.0)[cite: 7]  
**Licenza Codebase Pubblica**: MIT License  
**Privativa Industriale e Segreto Algoritmico**: Art. 98 D.Lgs. 30/2005 (Codice della Proprieta Industriale)[cite: 17]  
**Marchio Registrato e Metodologia**: METODO DEMARIA®[cite: 7]  
**Contatti Ufficiali**: metodo.demaria@gmail.com | avv.alessandrodemaria@pec.it[cite: 7]  

---

## 1. PREMESSA EPISTEMOLOGICA E CAMBIO DI PARADIGMA

La presente Release v3.2 (Audit-Master) del METODO DEMARIA® formalizza e consolida il cambio di paradigma epistemologico nello studio dei corpora simbolici storici non decifrati, con specifico riferimento al Manoscritto Voynich (Beinecke MS 408)[cite: 8].

Rigettando l'ipotesi linguistico-fonetica tradizionale (Symbol-to-Sound / Symbol-to-Meaning), il METODO DEMARIA® formalizza il modello vettoriale e cibernetico (Symbol-to-Vector / Symbol-to-State): il corpus grafico costituisce un Instruction Set deterministico e calcolabile, concepito per la regolazione e il monitoraggio di uno spazio degli stati all'interno di un sistema temporizzato ad anello chiuso (Closed-Loop Timed Automaton)[cite: 8].

---

## 2. RECAP BENCHMARK EMPIRICI FROZEN (RELEASE v3.2)

- **Corpus Analizzato**: 35.483 EVA tokens validati su 227 folii unici[cite: 7, 8].
- **Coerenza Sintattica Grezza Reale Osservata (Craw)**: 0.685281 (68.53%)[cite: 7, 8].
- **Model 1 (Global Null Model - Monte Carlo N=10.000)**: Mean C_null = 0.676538, Z-Score = +4.3541, p-value < 0.000001[cite: 8, 15].
- **Model 2 (Intra-Folio Null Model - Monte Carlo N=10.000)**: Mean C_null = 0.682928, Z-Score = +1.1882, p-value = 0.123400[cite: 8, 15].
- **Model 3 (Intra-Line Null Model / Smoking Gun - Monte Carlo N=10.000)**: Mean C_null = 0.676567, Z-Score = +4.3958, p-value < 0.000001 (Vincolo Sintattico di Rigo)[cite: 7, 8, 15].
- **Isomorphic Double Randomization Test**: Double Null Mean = 0.711419, Z-Score = -0.7961, Empirical p-value = 0.664300[cite: 7, 8, 16].
- **Stress Test di Sensibilita al Rumore Sintattico**: 94.85% di ritenzione del segnale al 10.0% di rumore sintattico inoculato (Craw' = 0.650001)[cite: 7, 8, 16].
- **Holdout Stability (Out-of-Sample)**: Delta C inferiore al 2.59%[cite: 16].

---

## 3. STRUTTURA DEL REPOSITORY DI LABORATORIO (FILE FROZEN & HASH SHA-256)

### Codebase Python Vettorizzata Pure-Array (7 Moduli Integrati)
1. `core_parser1.py`: Parser deterministico dell'alfabeto EVA e mappatura biunivoca sulle regole della quadrupla degli stati minimi (Alpha: 10.00%, Beta: 54.99%, Delta: 19.51%, Gamma: 15.50%)[cite: 14].
2. `core_matrix2.py`: Gestore C-native della Matrice Canonica 4x4 e calcolo della Coerenza Sintattica Grezza (Craw = 0.685281) su coordinata di rigo pergamenaceo[cite: 7, 14].
3. `utils_preflight3.py`: Checker d'integrita crittografica SHA-256 e verifica di immutabilita del dataset master[cite: 15].
4. `audit_nullmodels4.py`: Motore stocastico Monte Carlo per l'audit dei tre modelli nulli gerarchici (N=10.000, Seed 42)[cite: 8, 15].
5. `audit_doublerand5.py`: Test avversariale di doppia randomizzazione isomorfa (N=10.000, Seed 42)[cite: 8, 16].
6. `audit_robustness6.py`: Test di sensibilita e resilienza al rumore sintattico inoculato (0.0% -> 30.0%)[cite: 8, 16].
7. `batch_runner7.py`: Orchestratore Master unificato per la riesecuzione automatica dell'intera suite e l'esportazione dei report[cite: 15].

### Dataset, Report e Impronte Crittografiche SHA-256
- `METODO_DEMARIA_VOYNICH_AUDIT_MASTER_v3.2_SIGILLATO.zip`: `adc04fdfbaeaef650877b8b9f84e1e486c730599e8a6abffa903979f7f0dc06e`[cite: 7, 18]
- `voynich_eva_tokens_extended.csv`: `dec87e784290ad5b404bd5ed0110349a2f379c7fb386adb0bca2d7a4b1890999`[cite: 7, 18]
- `audit_master_summary_results.csv`: `e3e4020ac6fe93cca79cfa393b773061d0b5f06c0f3c0c96d96f06efca1c2ca0`[cite: 18]
- `robustness_test_results.csv`: `d96a6ca9efe82a7cdbd5386dfe5627af728e6a5c6ba6b2c4de825d647b504812`[cite: 18]

### Apparato Iconografico Scientifico
- `METODO DEMARIA Release v3.2 - Tavola 1`: Automa Temporizzato ad Anello Chiuso, Matrice Canonica 4x4 ed Equazione dell'Invariante di Armonia.
- `METODO DEMARIA Release v3.2 - Tavola 2`: Topologia di Rigo Pergamenaceo e Tripartizione Sintattica (Smoking Gun)[cite: 13, 15].
- `METODO DEMARIA Release v3.2 - Tavola 3`: Diagnostica Computazionale, Z-Score dei Modelli Nulli e Curva di Resilienza al Rumore[cite: 15, 16].

---

## 4. ESECUZIONE RAPIDA (QUICK START)

Per rieseguire l'intero audit e verificare in modo deterministico la baseline di laboratorio (Seed 42)[cite: 15]:

```bash
# Esecuzione dell'Orchestratore Master v3.2
python batch_runner7.py
```

---

## 5. NOTE LEGALI, PATERNITA E SEGRETO INDUSTRIALE (ART. 98 CPI)

1. **Diritto d'Autore (L. 633/1941)**: La struttura teorica del METODO DEMARIA®, i trattati scientifici, i dataset quantitativi, la codebase di laboratorio, il design del dispositivo analogico Volvelle e la formalizzazione dell'Invariante di Armonia costituiscono opera d'ingegno originale tutelata ai sensi della Legge 22 aprile 1941 n. 633 e delle Convenzioni Internazionali WIPO / Berna[cite: 17].
2. **Marchio Registrato (D.Lgs. 30/2005)**: La denominazione, il logo e la metodologia METODO DEMARIA® costituiscono marchio registrato ai sensi del D.Lgs. 10 febbraio 2005, n. 30 (Codice della Proprieta Industriale)[cite: 17].
3. **Segreto Industriale (Art. 98 CPI)**: Gli algoritmi di simulazione avanzata, i motori commerciali backend, le matrici proprietarie dell'Invariante di Armonia (Phi_alpha) e la struttura analitica del motore di calcolo C* **rimangono coperti da Segreto Industriale ed esclusiva proprieta dell'Autore Avv. Alessandro Demaria (Art. 98 D.Lgs. 30/2005 - CPI)**[cite: 17]. La messa a disposizione della presente suite risponde ai requisiti di trasparenza Open Science e riproducibilita popperiana, senza concedere alcuna licenza d'uso o di sfruttamento commerciale sulla codebase proprietaria e sul motore sottostante[cite: 17].

© METODO DEMARIA DEPOSITATO - Tutti i diritti riservati (L. 633/1941, D.Lgs. 30/2005, Art. 98 CPI)[cite: 17].
