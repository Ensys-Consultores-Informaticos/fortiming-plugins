---
name: registro-jornada
description: Consulta el registro de jornada de ForTiming con las horas fichadas frente a las previstas, los retrasos, los fichajes abiertos o corregidos y el informe de registro de jornada de un periodo. Úsalo cuando el usuario pregunte por fichajes, entradas y salidas, quién llega tarde, la jornada de un mes o pida el informe para una inspección de trabajo.
---

# Registro de jornada

El registro de jornada recoge los fichajes de entrada y salida: las horas de presencia. No son las horas imputadas a proyectos, que están en los partes de tiempo; no mezcles unas con otras. Este procedimiento usa el conector de ForTiming.

## 1. Elegir la consulta

| Lo que pide el usuario | Tool |
|---|---|
| Los fichajes de una persona | `dim_registro_jornada` con su `id_personal` |
| Los fichajes de un equipo o departamento | `dim_registro_jornada_por_filtro` |
| Totales por mes, o un rango de varios meses | `resumen_jornada_mensual_por_filtro` |
| El informe formal de un periodo, persona a persona | `informe_registro_jornada` |
| A qué hora debe entrar o salir alguien | `horario_previsto` |

Para «mi jornada», obtén el `idPersonal` del usuario con `perfil_usuario`. Para otra persona, `buscar_personal`. Para «mi equipo», `mi_equipo=True`.

Para rangos largos de un grupo, usa el resumen mensual en lugar de pedir el detalle diario y sumarlo.

## 2. Preguntas frecuentes

- **Horas fichadas frente a previstas.** En las filas de resumen, `horasOrdinarias` es la jornada prevista y `horasJornada` la real. La diferencia es real menos prevista.
- **Retrasos.** `incluir_horario_previsto=True` añade el horario previsto a cada día. `retraso_minimo=N` deja solo los días con N minutos de retraso o más.
- **Quién llega tarde habitualmente.** `dim_registro_jornada_por_filtro` con `agrupar_por="persona"` devuelve los contadores por persona, sin el detalle diario.
- **Fichajes sin cerrar.** `solo_fichajes_abiertos=True` y `excluir_hoy=True`.
- **Fichajes corregidos.** `solo_fichajes_modificados=True`. Quien corrige un fichaje es siempre la propia persona; el responsable solo valida o rechaza.
- **El último fichaje.** Sin fechas, con `orden="desc"` y `limite=1`.

## 3. El informe de registro de jornada

`informe_registro_jornada` devuelve, persona a persona, los tramos, las horas y el estado de validación de cada día, que es lo que exige el artículo 34.9 del Estatuto de los Trabajadores. Trae además las incidencias del periodo: fichajes abiertos, días laborables sin registro, días sin validar y fichajes corregidos.

Al presentarlo, pon primero el periodo y las personas incluidas, después un resumen de incidencias y, por último, el detalle.

## Límites

- El registro de jornada es de solo lectura: fichar, corregir un fichaje y validar o rechazar jornadas se hace en la aplicación de ForTiming.
- Las consultas devuelven lo que el usuario puede ver en ForTiming según sus permisos.
