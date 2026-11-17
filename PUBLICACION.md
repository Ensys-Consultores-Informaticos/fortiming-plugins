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

El portal de OpenAI acepta el formato de plugin de Claude y lo convierte, pero no lee `.mcp.json`: el servidor MCP se envía aparte, como punto de acceso remoto, en el mismo borrador.

1. Crear el plugin en el portal de OpenAI, opción *With MCP*, con la URL `https://mcp.fortiming.com/ensysia/api/mcp`.
2. Añadir en el mismo borrador los procedimientos de `fortiming/skills/`.
3. Verificar el dominio: el portal da un token que hay que servir en `https://mcp.fortiming.com/.well-known/openai-apps-challenge`. EnsysIA ya tiene la ruta; los pasos están en la guía de despliegue.

El punto *UserInfo* de OpenID Connect no es obligatorio para enviar el plugin (comprobado el 17-nov-2026 en la documentación de autenticación de OpenAI). Solo hace falta para una función de ChatGPT Enterprise, las restricciones por dominio del espacio de trabajo, que usa el correo verificado del usuario. La pasarela de EnsysIA no lo ofrece ni anuncia los ámbitos `openid` y `email`, y así debe seguir mientras no se desarrolle: ChatGPT pide por defecto todos los ámbitos de OpenID Connect que el servidor anuncie.

La cuenta de prueba para los revisores de OpenAI tiene que entrar sin segundo factor ni códigos por correo o SMS.

## Documentación de referencia

- Estructura de un plugin: <https://claude.com/docs/plugins/build>
- Lista de comprobación previa: <https://claude.com/docs/plugins/pre-submission-checklist>
- Envío de un plugin: <https://claude.com/docs/plugins/submit>
- Envío de un conector: <https://claude.com/docs/connectors/building/submission>
- Empaquetado para OpenAI: <https://developers.openai.com/plugins/build/plugins>
- Enviar a OpenAI un plugin de Claude: <https://developers.openai.com/plugins/guides/submit-claude-plugin>
