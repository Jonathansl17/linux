#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Genera README.md a partir de linux-commands.txt

Reglas de parseo:
- Una línea que empieza con "--" inicia una sección (H2) con ese título.
- Líneas con "comando: descripción" se renderizan en una tabla Markdown.
- Líneas sin ":" se renderizan como bullets (útil para notas/ejemplos).
- El archivo README.md se reescribe solo si hay cambios reales.
"""

import os
import re
from typing import Dict, List, Tuple


ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "linux-commands.txt")
DST = os.path.join(ROOT, "README.md")


# --------- Utilidades ---------


def _anchor_from_title(title: str) -> str:
    """Crea un anchor tipo GitHub para el índice."""
    return re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")


def _strip(line: str) -> str:
    return line.rstrip("\n").strip()


def _escape_pipes(s: str) -> str:
    return s.replace("|", "\\|")


# --------- Parseo ---------


def parse_sections(lines: List[str]) -> List[Dict]:
    """
    Devuelve lista de secciones:
    [
      {"title": str, "rows": [(cmd, desc), ...], "bullets": [str, ...]}
    ]
    """
    sections: List[Dict] = []
    current: Dict = None

    for raw in lines:
        line = _strip(raw)

        if not line:
            continue

        # Nueva sección
        if line.startswith("--"):
            title = _strip(line[2:])
            if not title:
                title = "Sección"
            current = {"title": title, "rows": [], "bullets": []}
            sections.append(current)
            continue

        # Si no hay sección todavía, crea una por defecto
        if current is None:
            current = {"title": "General", "rows": [], "bullets": []}
            sections.append(current)

        # Línea tipo "comando: descripción" (usa ": " para no romper
        # comandos que contengan ":" sin espacio, como docker nombre:tag)
        if ": " in line:
            cmd, desc = line.split(": ", 1)
            cmd, desc = _strip(cmd), _strip(desc)
            if cmd and desc:
                current["rows"].append((cmd, desc))
            else:
                current["bullets"].append(line)
        else:
            current["bullets"].append(line)

    return sections


# --------- Render ---------


def render_markdown(sections: List[Dict], sort_rows: bool = False) -> str:
    """
    Genera el contenido Markdown del README.
    sort_rows=True para ordenar los comandos alfabéticamente dentro de cada sección.
    """
    out: List[str] = []

    # Título
    out.append("# Linux Commands — Cheatsheet Automático\n")
    out.append("_Generado automáticamente desde `linux-commands.txt`._\n")
    out.append(
        "> Edita **solo** `linux-commands.txt`. "
        "El `README.md` se regenera en cada push (GitHub Actions) "
        "o al ejecutar el script.\n"
    )

    # Índice
    out.append("## Índice\n")
    for s in sections:
        out.append(f"- [{s['title']}](#{_anchor_from_title(s['title'])})")
    out.append("")

    # Secciones
    for s in sections:
        out.append(f"## {s['title']}\n")

        rows: List[Tuple[str, str]] = s["rows"]
        bullets: List[str] = s["bullets"]

        if sort_rows:
            rows = sorted(rows, key=lambda x: x[0].lower())

        if rows:
            out.append("| Comando | Descripción |")
            out.append("|---|---|")
            for cmd, desc in rows:
                out.append(f"| `{_escape_pipes(cmd)}` | {_escape_pipes(desc)} |")
            out.append("")

        if bullets:
            for b in bullets:
                out.append(f"- {b}")
            out.append("")

    return "\n".join(out)


# --------- Main ---------


def main():
    if not os.path.exists(SRC):
        raise SystemExit(f"No existe {SRC}. Crea el archivo primero.")

    with open(SRC, "r", encoding="utf-8") as f:
        lines = f.readlines()

    sections = parse_sections(lines)

    # Puedes poner sort_rows=True si quieres orden alfabético
    md = render_markdown(sections, sort_rows=False)

    prev = ""
    if os.path.exists(DST):
        with open(DST, "r", encoding="utf-8") as f:
            prev = f.read()

    if md.strip() != prev.strip():
        with open(DST, "w", encoding="utf-8") as f:
            f.write(md)
        print(f"Regenerado {DST}")
    else:
        print("README.md ya está actualizado; no hay cambios.")


if __name__ == "__main__":
    main()
