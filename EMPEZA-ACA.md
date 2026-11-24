# Karina, empeza aca

Esta carpeta es tu proyecto: el sistema agentico de ARDIC. Yami ya corrio la primera parte de La Maquinaria por vos: leyo tu Workbook, armo el **plan completo** y dejo funcionando el **orquestador** con el primer agente (Administrativo), probado con datos de ejemplo. Vos revisas, aprobas y seguis.

## 1. Bajar el proyecto (una sola vez)

1. Acepta la invitacion al repositorio que te llega por mail desde GitHub.
2. En Claude Code, abri una carpeta nueva en el Escritorio o en Documentos (NO adentro de otro proyecto) y pedile:

   > Clona este repositorio en esta carpeta: https://github.com/yamilasolgala/sistema-agentico-ardic y abri esa carpeta como proyecto.

   Si te pide iniciar sesion en GitHub, hacelo en el navegador. No pegues claves en el chat.

## 2. Cada vez que te sientes a trabajar

1. Abri la carpeta en Claude Code.
2. Pedile: "Traeme los ultimos cambios del repositorio" (eso es hacer *pull*).
3. Escribi `/session-start`. Claude te cuenta donde quedaron.

## 3. Tu primera sesion

1. Pedile a Claude: "Explicame el plan de design/design_summary.md". Si algo no te cierra, decile y lo corrige.
2. Abri `planning/questions.md` y contestale a Claude las preguntas (archivo de pendientes de entrega, cotizaciones, proveedor de IA).
3. Para ver el orquestador andando: pedile "corre `docs/primera-corrida.md` y explicame que paso".
4. Cuando apruebes el plan, escribi `/start-execution`. Recien ahi construye, empezando por que funcione con tus archivos reales.

## 4. Para guardar tu trabajo

Al terminar, pedile: "Guarda los cambios y subilos al repositorio" (*commit* y *push*).

## Reglas que no se rompen

- Tus datos reales (clientes, precios, OCs) van en `data/real/`. Esa carpeta nunca se sube a GitHub.
- Las claves (API keys) nunca van en el chat ni en un archivo del repositorio.
- Nada sale hacia un cliente sin tu OK.
- Una cosa a la vez.
