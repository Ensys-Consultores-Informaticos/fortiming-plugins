---
name: informe-proyecto
description: Prepara un informe de situación de un proyecto, centro de coste o cliente de ForTiming con sus horas, personas, actividades, evolución mensual, presupuesto, margen y gastos. Úsalo cuando el usuario pregunte cómo va un proyecto, cuántas horas lleva, quién ha trabajado en él o si se está pasando del presupuesto.
---

# Informe de situación de un proyecto

En ForTiming un proyecto es un centro de coste. Este procedimiento reúne en un solo informe lo que ForTiming sabe de uno, usando el conector de ForTiming.

## 1. Localizar el proyecto

- Por nombre o código: `buscar_centro_coste`. Devuelve el `idCentroCoste`.
- Por cliente: `buscar_cliente`. Devuelve el `idCliente`, que agrupa todos sus proyectos. Si no encuentra el cliente, devuelve centros de coste sugeridos: muchos nombres comerciales son el proyecto de otro cliente.

Si hay varias coincidencias, enseña las opciones y pregunta cuál es.

## 2. Fijar el periodo

Si el usuario no da fechas, usa los últimos 12 meses y dilo en el informe. Con el proyecto como filtro, las consultas admiten hasta 5 años, así que se puede pedir todo el histórico en una llamada.

## 3. Consultar

Usa el mismo rango y el mismo `id_centro_coste` (o `id_cliente`) en todas las llamadas:

| Dato | Tool | Parámetros propios |
|---|---|---|
| Horas por persona | `horas_por_persona` | |
| Horas por actividad | `horas_por_actividad` | |
| Evolución mensual | `horas_por_centro_coste` | `granularidad="mes"` |
| Consumo del presupuesto | `cumplimiento_presupuesto` | |
| Margen | `margen_presupuesto` | |
| Gastos | `resumen_gastos` | |

No descargues los partes uno a uno para sumarlos: estas consultas ya devuelven los totales.

Si una consulta falla por falta de permisos (el margen y los gastos piden permiso de gastos), sigue con las demás y di en el informe qué apartado falta y por qué.

## 4. Redactar el informe

Con este orden, y omitiendo los apartados sin datos:

1. **Cabecera.** Proyecto, cliente y periodo analizado.
2. **Horas.** Total y las personas con más horas.
3. **Actividades.** Reparto de las horas por actividad.
4. **Evolución.** Horas por mes y si la tendencia sube o baja.
5. **Presupuesto.** Horas presupuestadas, consumidas y restantes, con el porcentaje de consumo.
6. **Margen.** Margen inicial, operativo y final.
7. **Gastos.** Total y los tipos principales.
8. **Observaciones.** Lo que merece atención: presupuesto excedido, meses sin actividad, márgenes negativos.

## Cómo leer los datos

- Un proyecto **sin presupuesto** trae el porcentaje de consumo y las horas restantes vacíos. Di que no tiene presupuesto; sus horas no son un exceso.
- Un proyecto **sin honorarios** trae `sin_honorarios=true` y los márgenes en porcentaje vacíos. No digas que el margen es 0: usa los márgenes en importe.
- Las tarifas por hora de las personas solo se incluyen si el usuario las pide expresamente.
- Si una respuesta trae `truncado=true`, no la trates como completa: acota la consulta o dilo.
