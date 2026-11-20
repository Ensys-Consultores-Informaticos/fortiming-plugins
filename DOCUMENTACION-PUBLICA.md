# Conectar ForTiming con Claude

Borrador de la página pública de documentación del conector, para publicarla en la web de ForTiming. El directorio de Claude pide su dirección en la ficha. Revisar lo marcado con **(confirmar)** antes de publicar.

---

## Qué es

El conector de ForTiming permite usar tus datos de ForTiming desde una conversación con Claude: consultar horas, proyectos, presupuestos, registro de jornada, ausencias y notas de gasto, y registrar partes de tiempo.

## Requisitos

- Una cuenta de usuario de ForTiming.
- Que tu empresa tenga activado el acceso por API. **(confirmar qué necesita exactamente una empresa)**
- Una cuenta de Claude en un plan que admita conectores.

No hay que instalar nada, registrar ninguna aplicación ni configurar claves.

## Cómo conectarlo

1. En Claude, abre **Configuración → Conectores**.
2. Busca **ForTiming** en el directorio y pulsa **Conectar**. Si todavía no aparece, elige **Agregar → Conector personalizado** y escribe esta dirección:

   ```
   https://mcp.fortiming.com/ensysia/api/mcp
   ```

3. Se abre la pantalla de acceso de ForTiming. Inicia sesión con tu usuario de siempre.
4. ForTiming te enseña los permisos que pide Claude. Acéptalos.

La dirección es la misma para todas las empresas.

## Qué puede hacer Claude

Claude ve y hace lo mismo que tu usuario en ForTiming: se aplican tus permisos.

**Consultar**

- Partes de tiempo y horas por persona, proyecto, cliente o actividad.
- Presupuestos, desviaciones y márgenes de los proyectos.
- Registro de jornada: fichajes, retrasos e informe de registro de jornada.
- Ausencias, vacaciones y calendario laboral.
- Notas de gasto y su estado de liquidación.
- Empleados, departamentos y centros de trabajo.

**Escribir**

- Crear, modificar y borrar partes de tiempo.
- Cerrar y reabrir proyectos.

Antes de escribir, Claude enseña el cambio y espera tu confirmación.

**Lo que no hace**

No ficha, no corrige fichajes y no valida jornadas ni ausencias. Eso se hace en la aplicación de ForTiming.

## Ejemplos

- «¿Cuántas horas he imputado esta semana y qué me falta?»
- «Apunta 3 horas de hoy al proyecto Alfa, actividad Análisis.»
- «¿Cómo va el proyecto Alfa frente a su presupuesto?»
- «¿Quién de mi equipo tiene horas sin imputar este mes?»
- «¿Qué notas de gasto están pendientes de liquidar?»

## Permisos

Al conectar, ForTiming pide tu consentimiento para estos permisos:

| Área | Qué incluye | Acceso |
|---|---|---|
| Organización | Empleados, departamentos, calendario y ausencias | Lectura |
| Tiempos | Partes de tiempo, proyectos y presupuestos | Lectura y escritura |
| Registro de jornada | Fichajes y jornadas | Lectura |
| Gastos | Notas de gasto | Lectura |

## Datos y privacidad

- El inicio de sesión se hace en ForTiming. Claude no ve tu contraseña.
- Los datos viajan entre Claude y tu cuenta de ForTiming a través de `mcp.fortiming.com`, con tu sesión y tus permisos.
- El conector no devuelve el DNI. El correo electrónico, las tarifas por hora y los comentarios de las ausencias solo se incluyen cuando los pides expresamente.
- El tratamiento que hace Claude de la conversación se rige por las condiciones de Anthropic. El de ForTiming, por su política de privacidad: **(confirmar dirección)**.

## Desconectar

En Claude, **Configuración → Conectores → ForTiming → Desconectar**. Puedes volver a conectarlo cuando quieras.

## Soporte

**(confirmar)** <https://fortiming.com/contacto/>
