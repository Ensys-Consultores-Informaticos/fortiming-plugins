---
name: imputar-horas
description: Registra, corrige o borra partes de tiempo en ForTiming. Úsalo cuando el usuario quiera imputar horas a un proyecto o centro de coste, rellenar las horas que le faltan de un día o de una semana, cambiar la duración de un parte o deshacer partes recién creados.
---

# Imputar horas en ForTiming

Un parte de tiempo son las horas que una persona imputa un día a un centro de coste (proyecto, trabajo o encargo) y a una actividad. Este procedimiento usa el conector de ForTiming.

## 1. Reunir los datos

Cada parte necesita persona, fecha, centro de coste, actividad y duración.

- **Persona.** Por defecto, el usuario. Para imputar por otra persona, localízala con `buscar_personal`; ForTiming solo lo permite a quien tiene permisos de gestión.
- **Fecha.** Convierte «hoy», «ayer» o «el lunes» a `YYYY-MM-DD`.
- **Centro de coste.** `buscar_centro_coste` con el nombre o, si el usuario da códigos, con todos ellos en `codigos`.
- **Actividad.** `buscar_actividad` con el nombre.
- **Duración.** En minutos: 1 h son 60 y 1,5 h son 90.

Si una búsqueda devuelve varias coincidencias, enseña las opciones y pregunta. No elijas una por tu cuenta ni inventes un identificador.

## 2. Si pide rellenar lo que le falta

1. Obtén su `idPersonal` con `perfil_usuario`.
2. Llama a `pendiente_imputacion` con ese `id_personal`, el rango de fechas y `solo_pendientes=True`. Devuelve, día a día, la jornada prevista, lo fichado y lo ya imputado.
3. Propón un reparto que no supere la jornada prevista de cada día. Si el usuario no ha dicho a qué proyecto y actividad van las horas, pregúntalo.

Si el usuario pide expresamente más horas que la jornada prevista, regístralas: ForTiming solo impide pasar de 24 horas en un día.

## 3. Comprobar antes de grabar

Llama a `crear_partes_tiempo` con todos los partes de la petición en una sola llamada y `dry_run=True`. No graba nada: devuelve cómo quedaría cada parte.

Enseña el resultado en una tabla con fecha, proyecto, actividad y horas, y avisa de lo que venga marcado:

| Estado o aviso | Qué decir al usuario |
|---|---|
| `previsto` | Se grabará. |
| `ya_existe` | Ya hay un parte ese día en el mismo proyecto y actividad. Ofrece sumarle las horas (paso 5). |
| `no_valido` | No se puede grabar. Explica el motivo que trae `mensaje`. |
| `aviso_redondeo` | La empresa redondea las duraciones; di cuántos minutos se grabarán. |
| `avisos_dia` | El día queda por encima de la jornada prevista. Es informativo. |

## 4. Grabar

Solo cuando el usuario confirme expresamente, repite la misma llamada con `dry_run=False`. Después di cuántos partes se han creado y cuántos han dado error, con el motivo de cada error.

## 5. Corregir o deshacer

- **Cambiar un parte.** `modificar_parte_tiempo` con su `id_parte_tiempo` y solo los campos que cambian. Las duraciones son el valor final, no un incremento: para sumar 1 h a un parte de 2 h, pasa `duracion_minutos=180`.
- **Borrar partes.** `borrar_partes_tiempo` con sus `ids_parte_tiempo`. Sirve para deshacer partes recién creados.

Las dos funcionan igual que la creación: primero con `dry_run=True`, se enseña el cambio y se repite con `dry_run=False` cuando el usuario lo confirme.

## Límites

- Como máximo, 100 partes por llamada.
- El registro de jornada (fichajes) no se puede modificar desde aquí: se ficha y se valida en la aplicación de ForTiming.
