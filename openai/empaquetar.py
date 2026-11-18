"""
Genera el zip del plugin de ForTiming para el portal de OpenAI (ChatGPT y Codex).

Reúne en un solo paquete, sin tocar la carpeta del plugin de Claude:
- plugin.json         <- openai/plugin.json (manifiesto con extensions.com.openai)
- skills/             <- fortiming/skills/ (los mismos procedimientos que en Claude)
- assets/icon.png     <- fortiming/.claude-plugin/icon.png
- assets/logo.png     <- el mismo icono

No incluye fortiming/.mcp.json: OpenAI no lo lee. El servidor MCP se da en el
portal, con la opción «With MCP».

Uso, desde la raíz del repositorio:
    python openai/empaquetar.py
Deja fortiming-openai-<versión>.zip en la raíz (excluido de git por *.zip).
"""
import json
import zipfile
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
MANIFIESTO = RAIZ / "openai" / "plugin.json"
SKILLS = RAIZ / "fortiming" / "skills"
ICONO = RAIZ / "fortiming" / ".claude-plugin" / "icon.png"

LIMITES = {"displayName": 30, "shortDescription": 30, "longDescription": 4000}


def comprobar(manifiesto: dict) -> None:
    interfaz = manifiesto["extensions"]["com.openai"]["interface"]
    for campo, maximo in LIMITES.items():
        largo = len(interfaz[campo])
        assert largo <= maximo, f"{campo}: {largo} caracteres (máximo {maximo})"
    prompts = interfaz["defaultPrompt"]
    assert len(prompts) <= 3, "defaultPrompt: máximo 3"
    assert len(set(prompts)) == len(prompts), "defaultPrompt: repetidos"
    for p in prompts:
        assert len(p) <= 128, f"defaultPrompt de {len(p)} caracteres: {p}"
        assert "@" not in p, f"defaultPrompt con mención: {p}"
    for campo in ("websiteURL", "supportURL", "privacyPolicyURL", "termsOfServiceURL"):
        url = interfaz[campo]
        assert url.startswith("https://") and len(url) <= 1024, f"{campo}: {url}"
    assert manifiesto.get("description"), "falta description"


def main() -> None:
    manifiesto = json.loads(MANIFIESTO.read_text(encoding="utf-8"))
    comprobar(manifiesto)
    skills = sorted(p for p in SKILLS.rglob("*") if p.is_file())
    assert any(p.name == "SKILL.md" for p in skills), "no hay skills"

    destino = RAIZ / f"fortiming-openai-{manifiesto['version']}.zip"
    with zipfile.ZipFile(destino, "w", zipfile.ZIP_DEFLATED) as z:
        z.write(MANIFIESTO, "plugin.json")
        for p in skills:
            z.write(p, (Path("skills") / p.relative_to(SKILLS)).as_posix())
        z.write(ICONO, "assets/icon.png")
        z.write(ICONO, "assets/logo.png")

    with zipfile.ZipFile(destino) as z:
        for nombre in z.namelist():
            print(nombre)
    print(f"\n{destino.name}: {destino.stat().st_size} bytes")


if __name__ == "__main__":
    main()
