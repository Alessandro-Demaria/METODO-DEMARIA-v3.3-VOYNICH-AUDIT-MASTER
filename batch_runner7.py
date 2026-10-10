"""
METODO DEMARIA v3.3 - MAGISTER
DOI UFFICIALE DI RELEASE: 10.5281/zenodo.23242996
Modulo: batch_runner7.py (Elemento 7 del Motore - Master Orchestrator)
Descrizione: Single Source of Truth per l'orchestrazione batch unificata dell'intera suite.
             Applica la distruzione incondizionata delle colonne di stato pre-esistenti nel CSV
             e forza il re-parsing deterministico di tutti i 35.483 token EVA per garantire l'allineamento
             invariabile ed incondizionato alla baseline Craw = 0.786597 (78.66%).
Autore, Responsabile Scientifico e Inventore Unico: Avv. Alessandro Demaria
"""

import sys
import os
import time
import pandas as pd
from typing import Dict, Any

from utils_preflight3 import PreFlightChecker
from core_parser1 import EVAParser
from core_matrix2 import TransitionMatrixManager
from audit_nullmodels4 import HierarchicalNullModelsAudit
from audit_doublerand5 import IsomorphicDoubleRandomizationAudit
from audit_robustness6 import RobustnessStressTestAudit


class MasterBatchRunner:
    """
    Orchestratore Master della suite computazionale METODO DEMARIA v3.3 - MAGISTER.
    Coordina l'intera pipeline di verifica, parsing, calcolo stocastico C-native e reportistica.
    """

    def __init__(
        self,
        dataset_path: str = None,
        summary_report_path: str = "audit_master_summary_results.csv",
        robustness_report_path: str = "robustness_test_results.csv"
    ):
        if dataset_path is None:
            base_dir = os.path.dirname(os.path.abspath(__file__))
            self.dataset_path = os.path.join(base_dir, "voynich_eva_tokens_extended.csv")
        else:
            self.dataset_path = dataset_path

        self.summary_report_path = summary_report_path
        self.robustness_report_path = robustness_report_path

    def run_full_pipeline(self, seed: int = 42) -> Dict[str, Any]:
        """
        Esegue la pipeline completa di calcolo e audit scientifico con topologia di rigo esplicita
        sfruttando l'architettura vettoriale One-Shot Pure-Array.
        """
        start_time = time.time()
        print("=" * 80)
        print("   METODO DEMARIA v3.3 - MAGISTER - MASTER AUDIT SUITE")
        print("   DOI UFFICIALE DI RELEASE: 10.5281/zenodo.23242996")
        print("   Autore, Responsabile Scientifico e Inventore Unico: Avv. Alessandro Demaria")
        print("=" * 80)

        # 1. PRE-FLIGHT CHECK CRITTOGRAFICO SHA-256
        print("\n[STEP 1/6] Avvio Pre-Flight Check e Verifica Integrità SHA-256...")
        checker = PreFlightChecker(dataset_path=self.dataset_path)
        preflight_results = checker.run_preflight_check(enforce_hard_stop=True)
        status_pf = preflight_results["status"]
        sha_pf = preflight_results["computed_sha256"]
        tokens_pf = preflight_results["total_tokens_processed"]
        print(f" -> Status Pre-Flight: {status_pf}")
        print(f" -> SHA-256 Rilevato : {sha_pf}")
        print(f" -> Token Processati : {tokens_pf}")

        # 2. CARICAMENTO DATASET ED ELIMINAZIONE INCONDIZIONATA DEL BIAS DI STATO PRE-ESISTENTE
        print("\n[STEP 2/6] Caricamento Dataset ed Esecuzione Forzata Parsing EVA...")
        df = pd.read_csv(self.dataset_path)
        
        token_col = "EVA_Token" if "EVA_Token" in df.columns else ("token" if "token" in df.columns else df.columns[0])

        # RICOSTRUZIONE TOPOLOGICA PUNTUALE DI FOGLIO E RIGO PERGAMENACEO
        if "line_id" not in df.columns:
            if "Folio" in df.columns:
                clean_folio = df["Folio"].astype(str).str.replace('"', '', regex=False).str.strip()
                extracted_line = clean_folio.str.extract(r'([f\d\w]+\.\d+)')[0]
                df["line_id"] = extracted_line.fillna(clean_folio.str.split(',').str[0])
            else:
                df["line_id"] = "L_" + (df.index // 10).astype(str)

        if "folio" not in df.columns:
            if "Folio" in df.columns:
                clean_folio = df["Folio"].astype(str).str.replace('"', '', regex=False).str.strip()
                df["folio"] = clean_folio.str.extract(r'(f\d+[rv])')[0].fillna(clean_folio.str.split('.').str[0])
            else:
                df["folio"] = df["line_id"].astype(str).str.split('_').str[0].str.split('.').str[0]

        # RIMOZIONE COSTRIVILE ED ELIMINAZIONE DI QUALSIASI COLONNA DI STATO PRE-ESISTENTE
        for col in ["assigned_state", "state", "assigned_states", "State"]:
            if col in df.columns:
                df.drop(columns=[col], inplace=True)

        # CALCOLO DETERMINISTICO ED ESCLUSIVO TRAMITE CORE_PARSER1 (Garantisce Craw = 0.786597)
        parsed = [EVAParser.parse_token(str(t)) for t in df[token_col]]
        df["assigned_state"] = [p[0] for p in parsed]
        df["applied_rule"] = [p[1] for p in parsed]

        # 3. MISURAZIONE C_RAW REALE OSSERVATA SU RIGO
        print("\n[STEP 3/6] Calcolo Coerenza Sintattica Grezza Reale (Craw) su Rigo...")
        matrix_mgr = TransitionMatrixManager()
        c_observed = matrix_mgr.calculate_c_raw_by_lines(df, state_column="assigned_state", line_column="line_id")
        c_perc = c_observed * 100.0
        print(f" -> Coerenza Sintattica Grezza Reale (Craw): {c_observed:.6f} ({c_perc:.2f}%)")

        # 4. FASE 1 - MODELLI NULLI GERARCHICI MONTE CARLO (N=10.000)
        print("\n[STEP 4/6] Esecuzione Fase 1: Modelli Nulli Gerarchici (N=10.000, Seed 42)...")
        null_audit = HierarchicalNullModelsAudit(
            df, 
            matrix_manager=matrix_mgr, 
            state_column="assigned_state", 
            folio_column="folio", 
            line_column="line_id"
        )
        phase1_results = null_audit.run_full_hierarchical_audit(n_iterations=10000, seed=seed)
        
        m1 = phase1_results["global_null_model"]
        m2 = phase1_results["intra_folio_null_model"]
        m3 = phase1_results["intra_line_null_model"]

        z1, p1 = m1["z_score"], m1["p_value"]
        z2, p2 = m2["z_score"], m2["p_value"]
        z3, p3 = m3["z_score"], m3["p_value"]

        print(f" -> Model 1 (Global Null)    : Z = {z1:+.4f} | p = {p1:.6f}")
        print(f" -> Model 2 (Intra-Folio Null): Z = {z2:+.4f} | p = {p2:.6f}")
        print(f" -> Model 3 (Intra-Line Null) : Z = {z3:+.4f} | p = {p3:.6f} [PROVA REGINA]")

        # 5. FASE 2 - ISOMORPHIC DOUBLE RANDOMIZATION TEST (N=10.000)
        print("\n[STEP 5/6] Esecuzione Fase 2: Double Randomization Test Isomorfo (N=10.000, Seed 42)...")
        double_audit = IsomorphicDoubleRandomizationAudit(
            df, 
            matrix_manager=matrix_mgr, 
            state_column="assigned_state", 
            line_column="line_id"
        )
        phase2_results = double_audit.run_double_randomization_test(n_iterations=10000, seed=seed)
        z_dbl = phase2_results["z_score"]
        p_dbl = phase2_results["p_value_empirical"]
        print(f" -> Double Null Z-Score      : {z_dbl:+.4f}")
        print(f" -> Empirical p-value        : {p_dbl:.6f}")

        # 6. FASE 3 - ROBUSTNESS & STRESS TEST (N=1.000 per livello)
        print("\n[STEP 6/6] Esecuzione Fase 3: Robustness & Stress Test (0% - 30% Rumore)...")
        robust_audit = RobustnessStressTestAudit(
            df, 
            matrix_manager=matrix_mgr, 
            state_column="assigned_state", 
            line_column="line_id"
        )
        phase3_results = robust_audit.run_stress_test(n_iterations_per_level=1000, seed=seed)
        
        for level_res in phase3_results["stress_test_levels"]:
            n_p = level_res["noise_level_percent"]
            c_m = level_res["c_raw_mean"]
            c_r = level_res["coherence_retention_percent"]
            print(f" -> Rumore {n_p:4.1f}%: Craw' = {c_m:.6f} | Ritenzione = {c_r:6.2f}%")

        elapsed_time = time.time() - start_time
        print(f"\nPipeline completata con successo in {elapsed_time:.2f} secondi.")

        # 7. ESPORTAZIONE REPORT CSV
        self._export_reports(c_observed, phase1_results, phase2_results, phase3_results)

        return {
            "c_observed": c_observed,
            "phase1": phase1_results,
            "phase2": phase2_results,
            "phase3": phase3_results,
            "execution_time_seconds": elapsed_time
        }

    def _export_reports(
        self,
        c_observed: float,
        p1: Dict[str, Any],
        p2: Dict[str, Any],
        p3: Dict[str, Any]
    ):
        """
        Esporta i risultati sintetici ed analitici dell'Audit nei report CSV ufficiali.
        """
        summary_data = [
            {"Metric_Name": "Observed_Craw", "Value": c_observed, "Z_Score": None, "p_value": None, "Notes": "Coerenza Sintattica Reale"},
            {"Metric_Name": "Model_1_Global_Null", "Value": p1["global_null_model"]["c_null_mean"], "Z_Score": p1["global_null_model"]["z_score"], "p_value": p1["global_null_model"]["p_value"], "Notes": "Permutazione Totale Corpus"},
            {"Metric_Name": "Model_2_Intra_Folio_Null", "Value": p1["intra_folio_null_model"]["c_null_mean"],