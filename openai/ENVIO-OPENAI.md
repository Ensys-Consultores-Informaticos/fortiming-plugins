# Envío de ForTiming al directorio de ChatGPT

Guía para enviar el plugin de ForTiming al portal de OpenAI (vale para ChatGPT y Codex). Preparada el 18-nov-2026 a partir de la documentación de OpenAI de ese día:

- Enviar un plugin de Claude: <https://developers.openai.com/plugins/guides/submit-claude-plugin>
- Requisitos del envío: <https://developers.openai.com/apps-sdk/deploy/submission>
- Autenticación: <https://developers.openai.com/apps-sdk/build/auth>

Es el mismo servidor MCP y los mismos procedimientos que el plugin de Claude, que ya está en el directorio de Claude. La aprobación de Anthropic no vale para OpenAI: hay que pasar su revisión.

## Estado

| Hace falta | Estado |
|---|---|
| Servidor MCP en `https://mcp.fortiming.com/ensysia/api/mcp` | Hecho. En producción, con OAuth 2.1, PKCE `S256`, `iss` en la respuesta (RFC 9207), CIMD y registro dinámico |
| Redirecciones de ChatGPT admitidas por la pasarela | Hecho. `https://chatgpt.com/connector_platform_oauth_redirect` y `https://chatgpt.com/connector/oauth/*` (`back_ensysia/ensysia/mcp/oauth.py` de EnsysIA) |
| Anotaciones de las 63 tools (`readOnlyHint`, `destructiveHint`, `openWorldHint`) | Hecho |
| Paquete del plugin | Hecho: `python openai/empaquetar.py` genera `fortiming-openai-1.0.0.zip` |
| Manifiesto con los datos del listado | Hecho: `openai/plugin.json` |
| Ruta de verificación de dominio en EnsysIA | Hecho. Sirve la variable `OPENAI_APPS_CHALLENGE` |
| Ruta de verificación en Nginx | Hecho en `gqc`, el servidor de entrada (comprobado el 20-nov-2026: el 404 sin token lo da EnsysIA). Sin comprobar en el resto de servidores. Está en `GesiaQuattro-doc/entornos/nginx/.../apps/ensysia.conf` |
| Página pública `https://fortiming.com/conector-chatgpt/` | Hecho. Publicada y comprobada el 20-nov-2026. El HTML está en `web/conector-chatgpt.html` |
| Ámbitos OAuth que se piden al conectar | **Falta desplegar.** Producción pide los ocho de ForTiming. EnsysIA anuncia ya solo los cinco que usan las tools (cambio del 20-nov-2026), y hay que desplegarlo antes de grabar el vídeo y de enviar: la pantalla de consentimiento no debe enseñar permisos de escritura que el plugin no usa |
| Cuenta de prueba para los revisores, sin segundo factor | Creada el 20-nov-2026. **Falta** ejecutar con ella los casos de prueba en chatgpt.com |
| Vídeo de demostración | **Falta** |
| Organización de OpenAI verificada y permiso para enviar | **Falta comprobar** |

## 1. Antes de abrir el portal

### Cuenta y organización de OpenAI

- Envía el propietario (*owner*) de la organización de OpenAI o alguien con el permiso **Apps Management Write**, que da el propietario.
- La organización tiene que estar verificada como empresa (*business verification*, en la configuración de la organización). Esa verificación da la identidad de desarrollador que se elige al subir: **Ensys Consultores Informáticos, S.L.** Es el nombre que verá la gente.

### Nginx

Ya está desplegado en `gqc`, que es el servidor de entrada de `mcp.fortiming.com` (comprobado el 20-nov-2026). Queda opcional subirlo al resto para que la configuración siga siendo igual: desplegar `apps/ensysia.conf` con `sync_conf.bat` (carpeta `GesiaQuattro-doc/entornos/nginx/produccion`) y después, en cada servidor:

```bash
sudo nginx -t && sudo systemctl reload nginx
```

Comprobación: sin token, el 404 tiene que venir de EnsysIA (cuerpo vacío), no de Nginx (página HTML):

```bash
curl -si https://mcp.fortiming.com/.well-known/openai-apps-challenge
```

### Página pública

Publicada el 20-nov-2026. Si cambia `web/conector-chatgpt.html`, hay que volver a pegarlo en WordPress como se hizo con la de Claude: página «Conectar ForTiming con ChatGPT», bloque **HTML personalizado** con todo lo que va desde `<div class="ft-app">`, enlace permanente `conector-chatgpt`. OpenAI exige que las direcciones públicas funcionen y sean del mismo editor que envía.

### Cuenta de prueba para los revisores

OpenAI exige una cuenta que entre **sin segundo factor, sin códigos por correo o SMS, sin enlaces mágicos y sin red privada**, y con **datos de ejemplo**, no reales. Propuesta:

- Una empresa de demostración en producción (servidor `gqc` o el que corresponda), con el módulo API activado.
- Un usuario con rol de responsable (para que funcionen «mi equipo» y los presupuestos) y otro par de empleados que supervise.
- Proyectos con presupuesto, alguno excedido, partes de tiempo del mes en curso y del anterior, fichajes, alguna ausencia y alguna nota de gasto.
- Los nombres de proyecto y actividad que se usen en los casos de prueba de abajo tienen que existir en esa empresa.

Las credenciales se escriben en el formulario **Review details** del portal, nunca en el zip.

### Ámbitos OAuth

La pantalla de consentimiento de ForTiming tiene que enseñar solo estos permisos, que son los de la tabla de la página pública:

- Leer datos de organización.
- Leer y escribir datos de partes de tiempo.
- Leer datos de notas de gastos.
- Leer datos de registro de jornada.

Si enseña también la escritura de organización, de notas de gastos o de registro de jornada, el servidor al que apunta `mcp.fortiming.com` no tiene desplegado el cambio de EnsysIA. Comprobación:

```bash
curl -s https://mcp.fortiming.com/.well-known/oauth-protected-resource
```

`scopes_supported` debe traer `read_organizacion`, `read_tiempos`, `write_tiempos`, `read_gastos` y `read_fichaje`, y ninguno más.

### Vídeo de demostración

OpenAI pide un enlace a un vídeo (`demo_recording_url`) que los revisores puedan abrir: conectar ForTiming desde ChatGPT, iniciar sesión y recorrer dos o tres de los casos de prueba, incluida una escritura con su confirmación.

Se graba en chatgpt.com, con la cuenta de prueba, de una sola toma. Duración: unos 3 minutos, 5 como máximo.

| # | Tiempo | Qué se ve | Qué demuestra |
|---|---|---|---|
| 1 | 0:00 | Abrir la aplicación ForTiming en ChatGPT y pulsar **Conectar** | Instalación |
| 2 | 0:15 | Pantalla de acceso de ForTiming: usuario de prueba, contraseña y entrar | Acceso sin segundo factor |
| 3 | 0:35 | Pantalla de permisos de ForTiming, aceptar y vuelta a ChatGPT ya conectado | OAuth y consentimiento |
| 4 | 0:50 | «¿Cuántas horas he imputado esta semana y qué me falta por imputar?» | Lectura personal |
| 5 | 1:20 | «¿Qué proyectos se están pasando del presupuesto de horas este año?» | Lectura analítica |
| 6 | 1:50 | «Apunta 2 horas de hoy al proyecto Sample Project 1, actividad Analysis». Esperar a que enseñe el parte y pida confirmación, y responder «Sí, grábalo» | Escritura con confirmación |
| 7 | 2:30 | «Ficha mi entrada ahora» | Límite: no ficha y remite a ForTiming |
| 8 | 2:50 | Configuración → ForTiming → **Desconectar** | Desconexión |

Al grabar:

- Desplegar las llamadas a las tools en los pasos 4 a 6. En el 6 tiene que distinguirse la vista previa (`dry_run`) de la grabación real.
- Solo datos de la empresa de prueba en pantalla: sin otras pestañas, marcadores ni datos reales. Ventana limpia a 1920×1080.
- Usar una ventana privada, para que ForTiming pida las credenciales y no reutilice una sesión abierta.
- Los prompts van en español, que es el idioma del producto. Añadir rótulos o subtítulos breves en inglés en cada paso, porque los revisores leen inglés.
- Antes de grabar, borrar el parte del paso 6 si se creó en los ensayos, para que las horas pendientes del paso 4 sean coherentes.
- Subirlo a un sitio que se abra sin iniciar sesión, por ejemplo YouTube como «no listado».

## 2. En el portal

1. Abrir el portal de plugins de OpenAI y pulsar **Create plugin** → **With MCP**.
2. **Servidor MCP:** `https://mcp.fortiming.com/ensysia/api/mcp`. Solo admite un servidor por plugin.
3. **Paquete:** subir el zip que genera, desde la raíz de este repositorio:

   ```bash
   python openai/empaquetar.py
   ```

   Lleva `plugin.json`, las cinco skills y el icono. No lleva el `.mcp.json` del plugin de Claude: OpenAI no lo lee.
4. **Verificación de dominio.** El portal da un token y lo busca en `https://mcp.fortiming.com/.well-known/openai-apps-challenge`:
   1. En `gqc`, añadir a `/etc/ensysia.env`:

      ```ini
      OPENAI_APPS_CHALLENGE=<token que da el portal>
      ```

   2. `sudo systemctl restart ensysia`.
   3. Comprobar que la respuesta es `200` y el cuerpo es solo el token:

      ```bash
      curl -s https://mcp.fortiming.com/.well-known/openai-apps-challenge
      ```

   4. Pulsar verificar en el portal.

   Si en el futuro `mcp.fortiming.com` apunta a otro servidor, el token tiene que estar también en ese.
5. **Autenticación:** OAuth, con registro **CIMD** (el que OpenAI prefiere; el servidor lo anuncia con `client_id_metadata_document_supported`). Si el portal no lo ofrece, registro dinámico (DCR), que también funciona. **No** dar identificador ni secreto de cliente: la pasarela no los necesita y el secreto del programa general no debe salir de los servidores.
6. Si el portal enseña una dirección de retorno distinta de las dos de ChatGPT que ya admite la pasarela, avisar: hay que añadirla en `oauth.py` de EnsysIA y desplegar.
7. Probar la conexión desde el propio portal con la cuenta de prueba.

## 3. Datos del listado

Ya están en `openai/plugin.json`. Para cambiarlos se edita ese fichero y se vuelve a generar el zip. El script comprueba los límites.

| Campo | Valor | Límite |
|---|---|---|
| `displayName` | ForTiming | 30 |
| `shortDescription` | Horas, proyectos y jornada | 30 |
| `longDescription` | La de Claude, cambiando «Claude» por «el asistente» | 4.000 |
| `developerName` | Ensys Consultores Informáticos, S.L. | |
| `category` | Productivity | |
| `capabilities` | Read, Write | |
| `websiteURL` | `https://fortiming.com/conector-chatgpt/` | |
| `supportURL` | `https://fortiming.com/contacto/` | |
| `privacyPolicyURL` | `https://fortiming.com/aviso-legal/` | |
| `termsOfServiceURL` | `https://fortiming.com/servicios/terminos-y-condiciones/` | |
| `defaultPrompt` | Tres preguntas de ejemplo | 3 × 128 |
| `logo`, `composerIcon` | El icono del calendario rojo, PNG de 1024 px | |
| `brandColor` | `#C75555` (contraste 4,3:1 con blanco y 3,7:1 con `#212121`; el mínimo es 2:1) | |

Países (`publication.countries`): sin restringir, salvo que se decida limitar a España e Hispanoamérica.

## 4. Casos de prueba

OpenAI pide cinco positivos y tres negativos, ejecutados antes con la cuenta de prueba. El proyecto «Sample Project 1» y la actividad «Analysis» del caso 3 existen en la empresa de prueba, que tiene los datos en inglés.

### Positivos

| # | Descripción | Prompt | Tools | Comportamiento esperado |
|---|---|---|---|---|
| 1 | Horas imputadas por el usuario | ¿Cuántas horas he imputado esta semana? | `perfil_usuario`, `resumen_horas_trabajadas` | Da el total de horas de la semana en curso y el número de partes |
| 2 | Horas pendientes de imputar | ¿Qué horas me faltan por imputar esta semana? | `perfil_usuario`, `pendiente_imputacion` | Lista los días con horas pendientes frente a la jornada prevista y el total que falta |
| 3 | Registrar horas con confirmación | Apunta 2 horas de hoy al proyecto Sample Project 1, actividad Analysis | `buscar_centro_coste`, `buscar_actividad`, `crear_partes_tiempo` | Primero enseña el parte que va a crear (`dry_run`) y pide confirmación; solo al confirmar lo graba y devuelve su identificador |
| 4 | Proyectos excedidos | ¿Qué proyectos se están pasando del presupuesto de horas este año? | `cumplimiento_presupuesto` | Lista los proyectos con estado excedido, con horas presupuestadas, trabajadas y porcentaje de consumo |
| 5 | Saldo de vacaciones | ¿Cuántos días de vacaciones me quedan este año? | `saldo_vacaciones` | Da los días que corresponden, los disfrutados, los pendientes de aprobar y los disponibles |

### Negativos

| # | Prompt | Comportamiento esperado |
|---|---|---|
| 1 | Ficha mi entrada ahora | No llama a ninguna tool de escritura. Explica que fichar se hace en la aplicación de ForTiming |
| 2 | Valida las jornadas pendientes de mi equipo | No valida nada. Puede listar las jornadas pendientes y explica que la validación se hace en ForTiming |
| 3 | Dame el DNI de todos los empleados | No lo da. Explica que el plugin no devuelve el DNI |

## 5. Resto del formulario

- **Notas de versión** (`release_notes`): «Primera versión: consulta de partes de tiempo, proyectos, presupuestos, registro de jornada, ausencias y notas de gasto de ForTiming, y registro de partes de tiempo con confirmación.»
- **Declaraciones de cumplimiento:** las acepta quien envía.

## Riesgo a vigilar: UserInfo

La guía de envío de plugins de Claude dice, entre los requisitos de OAuth, que el servidor exponga un punto **UserInfo** con `email` y `email_verified`, y que anuncie los ámbitos `openid` y `email`. La guía de autenticación, en cambio, lo limita a las restricciones por dominio de ChatGPT Enterprise («the UserInfo Endpoint is required for workspace domain restrictions»).

La pasarela de EnsysIA no tiene UserInfo y no anuncia esos ámbitos, a propósito: ChatGPT pide por defecto los ámbitos OpenID que el servidor anuncie, y anunciarlos sin implementarlos rompería el inicio de sesión. Si el portal o los revisores lo exigen, es desarrollo nuevo en EnsysIA (y probablemente en ForTiming, para dar el correo verificado del usuario), no un ajuste de configuración.

## Después de la aprobación

- Publicar desde el portal.
- Con cada cambio en las skills o en `openai/plugin.json`, subir `version` y volver a generar y subir el zip. Solo puede haber una revisión abierta a la vez.
