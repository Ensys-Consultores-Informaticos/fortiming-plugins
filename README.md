# Plugins de ForTiming

Repositorio de los plugins de ForTiming para asistentes de IA. Hoy contiene uno, `fortiming`, que une el conector de ForTiming (el servidor MCP) con los procedimientos que indican al asistente cómo usarlo.

El mismo plugin sirve para Claude (chat, Cowork y Claude Code) y para ChatGPT y Codex: el portal de OpenAI lee el formato de plugin de Claude y lo convierte.

## Estructura

```
.claude-plugin/marketplace.json   Catálogo: permite añadir este repositorio como origen de plugins
fortiming/                        El plugin. Es la carpeta que se envía a los directorios
  .claude-plugin/plugin.json      Manifiesto: nombre, versión y descripción
  .mcp.json                       El conector: URL del servidor MCP de ForTiming
  README.md                       Texto de la ficha en el directorio
  skills/                         Un procedimiento por carpeta, en SKILL.md
PUBLICACION.md                    Pasos para publicar y lo que falta
```

Quien instala el plugin recibe solo la carpeta `fortiming/`. Lo que es del repositorio y no del plugin (este fichero, `PUBLICACION.md`) queda fuera.

## Procedimientos

| Carpeta | Para qué sirve |
|---|---|
| `imputar-horas` | Crear, corregir y borrar partes de tiempo |
| `informe-proyecto` | Informe de situación de un proyecto o cliente |
| `revision-equipo` | Repaso del equipo de un responsable |
| `seguimiento-presupuestos` | Cartera de proyectos con presupuesto y cierre de proyectos |
| `registro-jornada` | Fichajes, retrasos e informe de registro de jornada |

Los procedimientos solo dicen en qué orden usar las tools del conector y cómo presentar el resultado. Los nombres de las tools y de sus parámetros salen del servidor MCP, en el repositorio EnsysIA (`back_ensysia/ensysia/mcp/tools/fortiming/`): si allí cambia un nombre, hay que cambiarlo aquí.

## Probar el plugin

En Claude Code, desde la raíz del repositorio:

```bash
claude plugin validate ./fortiming
```

```bash
claude --plugin-dir ./fortiming
```

En claude.ai y en Cowork: comprimir la carpeta `fortiming` en un zip y subirlo en **Personalizar > Plugins > Añadir > Subir plugin**. Después, conectar ForTiming desde la pestaña **Conectores** del plugin.

Para que varias personas prueben la misma copia, añadir este repositorio como origen de plugins con su URL de GitHub.

## Publicar una versión

1. Cambiar lo que haga falta en `fortiming/`.
2. Subir `version` en `fortiming/.claude-plugin/plugin.json`.
3. Subir los cambios a la rama que siguen los directorios.

Los pasos del primer envío están en `PUBLICACION.md`.
