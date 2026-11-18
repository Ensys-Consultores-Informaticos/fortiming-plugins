# Envío al directorio de Claude: qué poner en cada paso

Valores preparados para los dos formularios de <https://claude.ai/directory/manage>. Primero el conector y después el plugin. Lo marcado con **(tú)** es una decisión o un dato que no se puede rellenar desde aquí.

Quién puede enviar: una cuenta de pago de claude.ai. En un plan Team o Enterprise tiene que ser un propietario (*Owner*) de la organización, y la ficha queda a nombre de esa organización.

## Antes de abrir el portal

| Hace falta | Estado |
|---|---|
| Conector funcionando en `https://mcp.fortiming.com/ensysia/api/mcp` | Hecho. Probado como conector personalizado el 17-nov-2026 |
| Las 63 tools con título y anotaciones | Hecho |
| Repositorio del plugin en GitHub | Hecho, privado. Tiene que ser público para publicar |
| Página pública de documentación del conector | **Falta.** Hay un borrador en `DOCUMENTACION-PUBLICA.md` para publicarlo en la web |
| Política de privacidad con dirección propia | **(tú)** La web trata la privacidad dentro de `/aviso-legal/` y de `/servicios/terminos-y-condiciones/`; no hay una página aparte |
| Contacto de soporte | **(tú)** La web tiene `https://fortiming.com/contacto/` y `https://fortiming.com/soporte/` |
| Icono | Hay un SVG en `GesiaQuattro/Recursos/iconos svg/generales/fortiming.svg`. El portal dirá qué formato y tamaño admite |
| Haber ejecutado todas las tools | Hecho el 18-nov-2026: las 63 llamadas desde Claude por el conector personalizado, contra producción. Las 58 de lectura responden con datos; las 5 de escritura, en modo de comprobación (`dry_run`), sin grabar nada |

## Formulario 1: conector (*MCP connector*)

### 1. Connection

- Elegir el conector personalizado que ya existe, «MCP general ForTiming», o pegar `https://mcp.fortiming.com/ensysia/api/mcp`.
- **No** marcar «Users connect to different URLs». Todas las empresas usan la misma dirección, y así basta con la etiqueta *Community*.

### 2. Tools

Se cargan solas del servidor: 58 de lectura y 5 de escritura. No debe marcar ninguna como falta de título o de anotación.

### 3. Listing

| Campo | Valor |
|---|---|
| Nombre (máx. 100) | ForTiming |
| Frase corta (máx. 200) | Consulta y registra desde Claude tus partes de tiempo, proyectos, presupuestos, registro de jornada, ausencias y notas de gasto de ForTiming. |
| Categorías (de 1 a 5) | **(tú)** Las más cercanas a productividad, gestión de proyectos y recursos humanos |
| Documentación | **(tú)** La dirección donde publiques `DOCUMENTACION-PUBLICA.md` |
| Política de privacidad | **(tú)** |
| Contacto de soporte | **(tú)** |
| Icono | El de ForTiming |
| Dirección de la ficha (*slug*) | `fortiming`. No se puede cambiar una vez publicada |

Descripción (máx. 2.000 caracteres):

> ForTiming es la aplicación de control horario y gestión de tiempos de Ensys Consultores. Este conector permite preguntar a Claude por los datos de tu empresa en ForTiming y registrar horas sin salir de la conversación.
>
> Qué puedes consultar: partes de tiempo y horas por persona, proyecto, cliente o actividad; presupuestos, desviaciones y márgenes de los proyectos; registro de jornada, fichajes, retrasos e informe de registro de jornada; ausencias, vacaciones y calendario laboral; notas de gasto y su estado de liquidación; empleados, departamentos y centros de trabajo.
>
> Qué puedes hacer: crear, modificar y borrar partes de tiempo, y cerrar o reabrir proyectos. Antes de escribir, Claude enseña el cambio y espera tu confirmación.
>
> Claude ve y hace lo mismo que tu usuario en ForTiming: se aplican tus permisos. El inicio de sesión se hace en ForTiming con OAuth; Claude no ve tu contraseña. El conector no devuelve el DNI, y el correo, las tarifas y los comentarios de las ausencias solo se incluyen cuando los pides.
>
> Requiere una cuenta de ForTiming en una empresa con el acceso por API activado.

Versión en inglés, por si el portal o los revisores la piden:

- *One-liner:* Query and log your ForTiming time entries, projects, budgets, attendance records, absences and expense reports from Claude.
- *Description:* ForTiming is the time-tracking and workforce management application by Ensys Consultores. This connector lets you ask Claude about your company's ForTiming data and log time without leaving the conversation. Read: time entries and hours by person, project, client or activity; project budgets, variances and margins; attendance records, clock-ins, late arrivals and the statutory working-time report; absences, holidays and work calendar; expense reports; employees, departments and work centres. Write: create, edit and delete time entries, and close or reopen projects; Claude always shows the change and waits for confirmation first. Claude acts with the signed-in user's own ForTiming permissions. Sign-in uses OAuth on ForTiming; Claude never sees the password. National ID numbers are never returned, and email, hourly rates and absence comments are only included on request. Requires a ForTiming account in a company with API access enabled.

### 4. Use cases

Casos de uso principales:

1. Imputar horas: «Apunta 3 horas de hoy al proyecto Alfa» o «rellena las horas que me faltan esta semana».
2. Seguimiento de proyectos: horas, personas, presupuesto consumido, margen y gastos de un proyecto o de un cliente.
3. Revisión de equipo: quién tiene horas sin imputar, jornadas pendientes de validar, fichajes abiertos y ausencias.
4. Registro de jornada: horas fichadas frente a previstas, retrasos e informe de registro de jornada de un periodo.
5. Control de presupuestos y gastos: proyectos excedidos, proyectos sin actividad y notas de gasto pendientes de liquidar.

Qué necesita el usuario antes de conectar: **(tú, confirmar)** una cuenta de usuario de ForTiming en una empresa con el acceso por API activado. No hay que registrar ninguna aplicación ni configurar claves.

Lee o escribe: las dos cosas.

### 5. Company

- Empresa: Ensys Consultores Informáticos, S.L.
- Web: **(tú)** `https://fortiming.com` o la de Ensys.
- Contacto para la revisión: **(tú)** un correo que se lea; ahí llegan los avisos de Anthropic.

### 6. Authentication

- *Authentication requirement:* obligatoria. Ninguna tool funciona sin cuenta. No elegir «Required when the server asks».
- *Authentication methods:* OAuth, con la identidad publicada de Claude (CIMD). El servidor también admite registro dinámico.
- **No** introducir identificador ni secreto de cliente: no hace falta que Anthropic guarde credenciales.

### 7. Data handling

- De quién es el API: propio. El conector llama al API de ForTiming, de Ensys.
- Datos de salud: **(tú)** El conector devuelve ausencias, entre ellas las bajas médicas (tipo y fechas), y sus comentarios solo si se piden. Lee la pregunta exacta del portal y responde con eso presente.
- Contenido patrocinado: no.

### 8. Test & launch

Pide confirmar que has ejecutado todas las tools, con MCP Inspector o como conector personalizado. No se ponen credenciales en el portal. Si Anthropic lo sube a revisión *Verified*, un revisor pedirá por correo una cuenta de prueba: tiene que estar en producción, tener datos y entrar sin segundo factor.

### 9. Compliance

Siete aceptaciones, todas obligatorias **(tú)**: normas del directorio, uso de API propio, transacciones financieras, generación de medios con IA, inyección de instrucciones, recogida de datos de la conversación y documentación pública. La última exige que la página de documentación esté publicada para la fecha de publicación.

### 10. Review and submit

Repasar y enviar. Si avisa de respuestas demasiado cortas, ampliarlas antes: esos avisos llegan al revisor.

## Formulario 2: plugin (*Plugin bundle*)

Enviar después del conector y desde la misma organización, para poder emparejarlos.

### 1. Source

| Campo | Valor |
|---|---|
| Repository | `Ensys-Consultores-Informaticos/fortiming-plugins` |
| Plugin path | `fortiming` |
| Branch or tag | vacío (sigue `main`) |

Pulsar *Validate*. Como el repositorio es privado, el portal pedirá:

- Conectar tu cuenta de GitHub en claude.ai, en la organización desde la que envías.
- Instalar la aplicación de GitHub de Claude en el repositorio.
- Aceptar que el código se sube a Anthropic para analizarlo.

### 2. Listing details

Sale de `fortiming/.claude-plugin/plugin.json` y de `fortiming/README.md`. Para cambiar algo se edita el repositorio y se valida otra vez.

### 3. Data handling

| Pregunta | Respuesta |
|---|---|
| ¿Lee o guarda datos personales? | Lee datos de empleados a través del conector de ForTiming. El plugin no guarda nada |
| ¿Envía datos a servicios distintos de sus conectores declarados? | No |
| ¿Cuánto tiempo conserva los datos? | No conserva datos |
| ¿Pensado para menores de 18 años? | No |

### 4. Compliance

Correo de contacto y cuatro aceptaciones **(tú)**.

### 5. Review and submit

Dejar «GitHub push webhook». Tras enviar, configurar las actualizaciones automáticas (*Set up push updates*); hace falta ser administrador del repositorio en GitHub.

### Para publicar

Cuando la versión pase los controles: hacer público el repositorio en GitHub, pulsar *Check for new commits* y después *Publish*.

## Después

- Emparejar el plugin con el conector desde el portal.
- Con cada cambio del plugin, subir `version` en `plugin.json`.
- Dudas con el conector: `mcp-review@anthropic.com`. Con el plugin: `directory@anthropic.com`.
