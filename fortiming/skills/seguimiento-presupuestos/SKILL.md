---
name: seguimiento-presupuestos
description: Revisa los presupuestos de los proyectos de ForTiming con su consumo de horas, sus desviaciones, su margen y los proyectos excedidos o sin actividad. Úsalo cuando el usuario pregunte qué proyectos se pasan de presupuesto, cuál es el margen, cómo va el cumplimiento presupuestario o qué proyectos se pueden cerrar.
---

# Seguimiento de presupuestos

Repasa la cartera de proyectos con presupuesto, usando el conector de ForTiming. Para el detalle de un solo proyecto, el procedimiento adecuado es el informe de proyecto.

## 1. Fijar el periodo

Si el usuario no da fechas, usa el año en curso, del 1 de enero a hoy, y dilo en la respuesta.

## 2. Consultar

| Pregunta | Tool | Parámetros |
|---|---|---|
| Qué proyectos están excedidos o al límite | `cumplimiento_presupuesto` | `estado="excedido,ajustado"`, `solo_activos=True` |
| Dónde hay más desviación en horas o en importe | `desviacion_presupuesto` | |
| Qué proyectos tienen peor margen | `margen_presupuesto` | `limite=10`; el orden por defecto pone primero el peor margen |
| Qué proyectos abiertos llevan tiempo sin horas | `centros_inactivos` | `dias=60`, `solo_abiertos=True` |

Haz solo las consultas que la pregunta necesita. Las tres de presupuesto admiten hasta 5 años en una llamada.

## 3. Responder

Empieza por la conclusión: cuántos proyectos están excedidos y cuál preocupa más. Después, una tabla por pregunta con el proyecto, el cliente y las cifras, ordenada de peor a mejor.

## Cómo leer los datos

- **Estados del cumplimiento.** `por_debajo` es menos del 95 % consumido, `ajustado` entre el 95 y el 100 %, y `excedido` más del 100 %.
- **Proyectos sin presupuesto.** Traen el consumo y las horas restantes vacíos. Sus horas no son un exceso.
- **Totales.** Los que terminan en `_con_presupuesto` o `_con_honorarios` cuentan solo los proyectos que los tienen; los `_global` cuentan todos. Para las horas o el coste real de la cartera, usa los globales.
- **Proyectos sin honorarios.** Traen `sin_honorarios=true` y el margen en porcentaje vacío. Usa el margen en importe; no digas que es 0.
- **Margen.** El margen final descuenta los gastos reales no repercutibles, así que pide permiso de gastos. Si falta, dilo.

## Cerrar proyectos

Si el usuario pide cerrar proyectos terminados o sin actividad:

1. Llama a `cerrar_centros_coste` con todos los `ids_centro_coste` en una sola llamada y `dry_run=True`. No cierra nada: devuelve el impacto de cada cierre.
2. Enseña ese impacto: horas imputadas, último parte, partes posteriores a la fecha de cierre, presupuesto y gastos sin liquidar.
3. Repite con `dry_run=False` solo cuando el usuario lo confirme expresamente.

Un proyecto con partes posteriores al cierre o con gastos sin liquidar no se cierra. Usa `forzar=True` solo si el usuario lo pide después de ver el motivo. Un cierre se deshace con `reabrir_centros_coste`, que sigue los mismos pasos.
