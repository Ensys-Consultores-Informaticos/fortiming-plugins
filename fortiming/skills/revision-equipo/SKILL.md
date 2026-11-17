---
name: revision-equipo
description: Repasa el estado del equipo de un responsable en ForTiming con las horas sin imputar, las jornadas pendientes de validar, los fichajes abiertos, las ausencias y las vacaciones. Úsalo cuando el usuario pida un repaso de su equipo o de un departamento, pregunte quién no ha rellenado los partes, quién está ausente o qué tiene pendiente de aprobar.
---

# Revisión del equipo

Reúne en un solo repaso lo que un responsable suele mirar de su equipo, usando el conector de ForTiming.

## 1. Fijar el grupo y el periodo

- **Grupo.** Por defecto, el equipo del usuario: las personas que supervisa directamente. Se pide con `mi_equipo=True`. Si el usuario nombra un departamento, localízalo con `buscar_departamento` y usa su identificador; el departamento incluye sus subdepartamentos.
- **Periodo.** Si no lo dice, la semana en curso, de lunes a hoy. Dilo en la respuesta.

Si el usuario no supervisa a nadie, su equipo es su departamento. Alguna consulta con `mi_equipo=True` sale entonces vacía y con un aviso: repítela con el `idDepartamento` que devuelve `perfil_usuario`.

## 2. Consultar

| Qué se revisa | Tool | Parámetros |
|---|---|---|
| Horas sin imputar | `resumen_partes_incompletos` | rango de fechas, `mi_equipo=True` |
| Jornadas pendientes de validar | `dim_registro_jornada_por_filtro` | `mi_equipo=True`, `estado="PENDIENTE_SUPERVISOR"`, `registro="resumido"` |
| Fichajes sin cerrar | `dim_registro_jornada_por_filtro` | `mi_equipo=True`, `solo_fichajes_abiertos=True`, `excluir_hoy=True`, `registro="detalle"` |
| Quién está ausente hoy | `dim_ausencias` | `mi_equipo=True`, `vigentes_a` con la fecha de hoy |
| Ausencias pendientes de aprobar | `dim_ausencias` | `mi_equipo=True`, `estado="SOLICITADO"`, sin fechas |
| Saldo de vacaciones, solo si lo pide | `saldo_vacaciones` | `mi_equipo=True` |

Para un departamento, cambia `mi_equipo=True` por el filtro de departamento de cada tool.

## 3. Responder

Un apartado por cada revisión, con los nombres de las personas y el dato que importa:

1. **Horas sin imputar.** Quién y cuántas horas le faltan.
2. **Jornadas por validar.** Quién y qué días.
3. **Fichajes abiertos.** Quién y qué día.
4. **Ausencias.** Quién está ausente hoy, y qué solicitudes esperan aprobación.

Si un apartado no tiene nada, dilo en una línea («Sin fichajes abiertos») en lugar de omitirlo: el responsable necesita saber que se ha mirado.

## Límites

- Validar jornadas y aprobar o rechazar ausencias se hace en la aplicación de ForTiming; desde aquí solo se consulta.
- El comentario de una ausencia y su motivo de rechazo pueden contener datos personales o de salud. Pídelos (`incluir_comentarios=True`) solo si el usuario los solicita expresamente.
- Las consultas devuelven lo que el usuario puede ver en ForTiming según sus permisos.
