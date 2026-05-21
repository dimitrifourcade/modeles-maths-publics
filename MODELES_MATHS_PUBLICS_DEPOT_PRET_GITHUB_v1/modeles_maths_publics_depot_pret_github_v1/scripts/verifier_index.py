#!/usr/bin/env python3
"""Vérifie rapidement la structure de index.json."""
from __future__ import annotations
import json
from pathlib import Path

index_path = Path(__file__).resolve().parents[1] / "index.json"
data = json.loads(index_path.read_text(encoding="utf-8"))

assert data.get("schema") == "maths_espace_prof.modeles_externes.v1", "schema invalide"
modeles = data.get("modeles")
assert isinstance(modeles, list), "modeles doit être une liste"

ids = []
for i, modele in enumerate(modeles, start=1):
    for champ in ["id", "titre", "type_document", "niveau", "chapitre", "statut", "fichiers"]:
        assert champ in modele, f"modèle {i}: champ manquant {champ}"
    ids.append(modele["id"])
    assert isinstance(modele["fichiers"], list) and modele["fichiers"], f"modèle {modele['id']}: fichiers vide"
    for fichier in modele["fichiers"]:
        for champ in ["nom", "type", "role", "url"]:
            assert champ in fichier, f"modèle {modele['id']}: fichier incomplet ({champ})"

assert len(ids) == len(set(ids)), "identifiants dupliqués"
print(f"OK — {len(modeles)} modèles, {len(set(ids))} identifiants uniques.")
