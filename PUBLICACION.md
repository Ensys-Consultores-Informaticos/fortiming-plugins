# Publicación del plugin de ForTiming

Pasos para enviar el plugin a los directorios de Claude y de ChatGPT, y lo que falta antes de poder hacerlo. Escrito el 17-nov-2026.

## Antes de enviar

| Pendiente | Dónde se resuelve |
|---|---|
| `mcp.fortiming.com` no existe todavía en DNS. Es la URL que declara `fortiming/.mcp.json` | Guía `doc/despliegue-mcp-fortiming-com.md` del repositorio EnsysIA |
| Este repositorio está solo en local, sin commit ni remoto | Crear el repositorio en GitHub, en la organización de Ensys, y subirlo |
| Licencia. El manifiesto dice `"license": "Propietario"`, como el plugin de Gesia | Decidir si vale así o si hace falta un fichero `LICENSE` con el texto |
| Requisitos de la ficha: el README dice que la empresa necesita «el acceso por API activado» | Confirmar qué necesita exactamente una empresa para conectar |
| Documentación pública del conector y política de privacidad | Web de ForTiming |
| Cuenta de prueba con datos para los revisores | Entorno de pruebas |
| Probar los cinco procedimientos con datos reales | Claude Code y claude.ai, con el plugin cargado |

## Directorio de Claude

Son dos envíos separados desde <https://claude.ai/directory/manage>, con una cuenta de la organización de Ensys:

1. **Conector.** Enviar nuevo > *MCP connector*, con la URL `https://mcp.fortiming.com/ensysia/api/mcp`.
2. **Plugin.** Enviar nuevo > *Plugin bundle*:
   - *Repository*: la URL de este repositorio en GitHub.
   - *Plugin path*: `fortiming`.
   - Pulsar *Validate* y corregir lo que salga como bloqueante.

Como el plugin declara la misma URL que el conector, quien tenga los dos ve un solo juego de tools.

El repositorio puede ser privado mientras se valida y se revisa, pero tiene que ser público para publicar.

Lo que comprueba la validación y ya se cumple:

- El nombre `fortiming` es propio del producto y está en minúsculas.
- El manifiesto tiene `description`, `author`, `version` y `license`.
- El README de `fortiming/` tiene más de 40 palabras y dice qué hace el plugin, cómo se usa y qué datos envía.
- El conector se declara con `type: "http"` y una URL `https://`.
- No hay ejecutables, scripts, hooks ni claves: solo Markdown y JSON.

## Directorio de ChatGPT y Codex

Todo lo necesario está en la carpeta `openai/`, aparte de la del plugin de Claude para no generar versiones nuevas en el directorio de Claude:

- `openai/ENVIO-OPENAI.md`: pasos, valores del formulario, casos de prueba y lo que falta antes de enviar.
- `openai/plugin.json`: manifiesto con los datos del listado de OpenAI.
- `openai/empaquetar.py`: genera el zip que se sube al portal.
- `web/conector-chatgpt.html`: página pública para `fortiming.com/conector-chatgpt/`.

## Documentación de referencia

- Estructura de un plugin: <https://claude.com/docs/plugins/build>
- Lista de comprobación previa: <https://claude.com/docs/plugins/pre-submission-checklist>
- Envío de un plugin: <https://claude.com/docs/plugins/submit>
- Envío de un conector: <https://claude.com/docs/connectors/building/submission>
- Empaquetado para OpenAI: <https://developers.openai.com/plugins/build/plugins>
- Enviar a OpenAI un plugin de Claude: <https://developers.openai.com/plugins/guides/submit-claude-plugin>
