# ForTiming

Consulta y registra los datos de ForTiming desde una conversación: partes de tiempo, proyectos y presupuestos, registro de jornada, ausencias y notas de gasto.

ForTiming es la aplicación de control horario y gestión de tiempos de Ensys Consultores. Este plugin une el conector de ForTiming con cinco procedimientos que indican al asistente cómo hacer las tareas más habituales.

## Qué puedes pedir

- **Imputar horas.** «Apunta 3 horas de hoy al proyecto Alfa, actividad Análisis» o «rellena las horas que me faltan de esta semana». El asistente enseña lo que va a grabar y espera tu confirmación.
- **Informe de un proyecto.** «¿Cómo va el proyecto Alfa?» Devuelve horas, personas, actividades, evolución mensual, presupuesto, margen y gastos.
- **Revisión del equipo.** «Repasa mi equipo»: horas sin imputar, jornadas pendientes de validar, fichajes abiertos y ausencias.
- **Seguimiento de presupuestos.** «¿Qué proyectos se pasan de presupuesto?» o «¿qué proyectos llevan dos meses sin horas?»
- **Registro de jornada.** «¿Quién ha llegado tarde este mes?» o «prepara el informe de registro de jornada de octubre».

También puedes preguntar cualquier otra cosa sobre tus datos de ForTiming: el conector ofrece más de cincuenta consultas.

## Requisitos

- Una cuenta de usuario de ForTiming en una empresa con el acceso por API activado.
- Iniciar sesión en ForTiming la primera vez que se usa el conector. El asistente abre la pantalla de acceso de ForTiming y pide tu consentimiento.

No hay que instalar nada ni configurar claves.

## Qué puede hacer y qué no

El asistente ve y hace lo mismo que tu usuario en ForTiming: se aplican tus permisos.

- **Consulta** personal, departamentos, proyectos, partes de tiempo, presupuestos, registro de jornada, ausencias, vacaciones y notas de gasto.
- **Escribe** solo partes de tiempo (crear, modificar y borrar) y el cierre o la reapertura de proyectos. Antes de escribir enseña el cambio y espera tu confirmación.
- **No** ficha, no corrige fichajes y no valida jornadas ni ausencias: eso se hace en la aplicación de ForTiming.

## Datos

El plugin no guarda ni envía datos por su cuenta: solo contiene instrucciones. Los datos viajan entre el asistente y tu cuenta de ForTiming a través del conector, en `mcp.fortiming.com`, con tu sesión y tus permisos.

El conector no devuelve el DNI. El correo electrónico, las tarifas por hora y los comentarios de las ausencias solo se incluyen cuando los pides expresamente.

## Soporte

Ensys Consultores Informáticos, S.L. · <https://fortiming.com>

## English summary

ForTiming is a time-tracking and workforce management application by Ensys Consultores. This plugin bundles the ForTiming connector with five skills: logging time entries, project status reports, team review, budget tracking and attendance records. It requires a ForTiming user account in a company with API access enabled; sign-in uses OAuth. The plugin stores no data: everything is exchanged between the assistant and the user's ForTiming account through `mcp.fortiming.com`, under the user's own permissions. Write operations are limited to time entries and closing or reopening projects, and always ask for confirmation first.
