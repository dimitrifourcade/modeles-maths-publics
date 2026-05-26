#!/usr/bin/env python3
"""
Extraction automatique des archives ZIP déposées dans documents_a_classer/.

But : rendre les PDF/fichiers utiles contenus dans les archives accessibles comme de vrais fichiers publics GitHub,
afin que le site Netlify et ChatGPT puissent les traiter comme des PDF ordinaires.
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import shutil
import zipfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List

ROOT = Path(__file__).resolve().parents[1]
ARCHIVES_ROOT = ROOT / "documents_a_classer"
OUT_ROOT = ROOT / "documents_extraits_archives"
INDEX_PATH = ROOT / "index_archives_extraites.json"

USEFUL_EXTENSIONS = {
    ".pdf", ".tex", ".md", ".txt", ".json", ".png", ".jpg", ".jpeg", ".webp", ".svg",
    ".docx", ".pptx", ".xlsx", ".csv"
}
MAX_FILE_SIZE = 95 * 1024 * 1024  # éviter de committer des fichiers proches de la limite GitHub classique


def slugify(value: str) -> str:
    value = value.replace("\\", "/").split("/")[-1]
    value = re.sub(r"\.[A-Za-z0-9]+$", "", value)
    value = value.lower()
    value = re.sub(r"[^a-z0-9._-]+", "_", value)
    value = re.sub(r"_+", "_", value).strip("._-")
    return value or "archive"


def safe_name(value: str) -> str:
    value = value.replace("\\", "/").split("/")[-1]
    value = re.sub(r"[^A-Za-z0-9À-ÿ._ -]+", "_", value).strip(" ._")
    return value or "fichier"


def category_for(ext: str) -> str:
    ext = ext.lower()
    if ext == ".pdf":
        return "pdf"
    if ext == ".tex":
        return "latex"
    if ext in {".png", ".jpg", ".jpeg", ".webp", ".svg"}:
        return "images"
    if ext in {".md", ".txt", ".json", ".csv"}:
        return "textes"
    if ext in {".docx", ".pptx", ".xlsx"}:
        return "office"
    return "autres"


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def raw_url_for(path: Path) -> str:
    repo = os.environ.get("GITHUB_REPOSITORY", "dimitrifourcade/modeles-maths-publics")
    branch = os.environ.get("GITHUB_REF_NAME", "main")
    return f"https://raw.githubusercontent.com/{repo}/{branch}/{rel(path)}"


def github_url_for(path: Path) -> str:
    repo = os.environ.get("GITHUB_REPOSITORY", "dimitrifourcade/modeles-maths-publics")
    branch = os.environ.get("GITHUB_REF_NAME", "main")
    return f"https://github.com/{repo}/blob/{branch}/{rel(path)}"


def extract_one_archive(archive: Path) -> List[Dict[str, object]]:
    archive_slug = slugify(archive.name)
    target_root = OUT_ROOT / archive_slug
    if target_root.exists():
        shutil.rmtree(target_root)
    target_root.mkdir(parents=True, exist_ok=True)

    extracted: List[Dict[str, object]] = []
    manifest = {
        "archive_name": archive.name,
        "archive_path": rel(archive),
        "archive_size": archive.stat().st_size,
        "archive_sha256": sha256_file(archive),
        "date_extraction": datetime.now(timezone.utc).isoformat(),
        "fichiers": []
    }

    try:
        with zipfile.ZipFile(archive) as zf:
            for info in zf.infolist():
                if info.is_dir():
                    continue
                internal = info.filename.replace("\\", "/")
                name = safe_name(internal)
                ext = Path(name).suffix.lower()
                if ext not in USEFUL_EXTENSIONS:
                    continue
                if info.file_size > MAX_FILE_SIZE:
                    continue
                if "__MACOSX/" in internal or internal.split("/")[-1].startswith("."):
                    continue

                category = category_for(ext)
                out_dir = target_root / category
                out_dir.mkdir(parents=True, exist_ok=True)
                out_path = out_dir / name
                if out_path.exists():
                    stem, suffix = out_path.stem, out_path.suffix
                    out_path = out_dir / f"{stem}_{len(list(out_dir.glob(stem + '*')))+1}{suffix}"

                with zf.open(info) as src, out_path.open("wb") as dst:
                    shutil.copyfileobj(src, dst)

                item = {
                    "name": out_path.name,
                    "path": rel(out_path),
                    "ext": ext.lstrip("."),
                    "size": out_path.stat().st_size,
                    "sha256": sha256_file(out_path),
                    "raw_url": raw_url_for(out_path),
                    "github_url": github_url_for(out_path),
                    "archive_name": archive.name,
                    "archive_path": rel(archive),
                    "internal_path": internal,
                    "category": category,
                    "source": "archive_extraite"
                }
                extracted.append(item)
                manifest["fichiers"].append(item)
    except zipfile.BadZipFile:
        manifest["erreur"] = "Archive ZIP illisible"

    (target_root / "manifest_archive.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    (target_root / "README.md").write_text(
        f"# Fichiers extraits de `{archive.name}`\n\n"
        "Ce dossier est généré automatiquement par GitHub Actions.\n\n"
        "Les fichiers utiles contenus dans l’archive sont publiés ici pour obtenir des liens publics directs.\n",
        encoding="utf-8"
    )
    return extracted


def main() -> None:
    OUT_ROOT.mkdir(parents=True, exist_ok=True)
    archives = sorted(ARCHIVES_ROOT.rglob("*.zip")) if ARCHIVES_ROOT.exists() else []
    all_items: List[Dict[str, object]] = []
    for archive in archives:
        all_items.extend(extract_one_archive(archive))

    index = {
        "schema": "maths_espace_prof.archives_extraites.v1",
        "version": datetime.now(timezone.utc).isoformat(),
        "source_archives": "documents_a_classer/**/*.zip",
        "dossier_sortie": "documents_extraits_archives/",
        "nombre_fichiers": len(all_items),
        "fichiers": all_items,
        "note": "Fichier généré automatiquement. Les PDF extraits disposent d'une URL raw GitHub directe."
    }
    INDEX_PATH.write_text(json.dumps(index, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Archives analysées : {len(archives)}")
    print(f"Fichiers utiles extraits : {len(all_items)}")


if __name__ == "__main__":
    main()
