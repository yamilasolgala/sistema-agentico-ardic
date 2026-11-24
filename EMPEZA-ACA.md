# Karina, empeza aca

Esta carpeta es tu proyecto: el sistema agentico de ARDIC. Yami dejo la base armada (el orquestador y el primer agente de ejemplo). Desde ahora lo seguis vos, con tu Claude, paso a paso.

## 1. Bajar el proyecto (una sola vez)

1. Acepta la invitacion al repositorio que te llega por mail desde GitHub.
2. En Claude Code, abri una carpeta nueva en el Escritorio o en Documentos (NO adentro de otro proyecto) y pedile:

   > Clona este repositorio en esta carpeta: [LINK DEL REPO]. Despues abri esa carpeta como proyecto.

   Si te pide iniciar sesion en GitHub, hacelo en el navegador. No pegues claves en el chat.

## 2. Cada vez que te sientes a trabajar

1. Abri la carpeta en Claude Code.
2. Pedile: "Traeme los ultimos cambios del repositorio" (eso es hacer *pull*).
3. Escribi `/session-start`. Claude te cuenta donde quedaron.

## 3. Primera sesion

1. Lee `Contexto/perfil-karina.md` y `START_PROJECT_PROMPT.md`. Si algo esta mal, decile a Claude que lo corrija.
2. Escribi `/init-agent-system`. Claude te va a hacer preguntas (hay varias ya listadas en `planning/questions.md`) y arma el plan.
3. Cuando el plan te guste, escribi `/start-execution`. Recien ahi construye.

## 4. Para guardar tu trabajo

Al terminar, pedile: "Guarda los cambios y subilos al repositorio" (*commit* y *push*).

## Reglas que no se rompen

- Tus datos reales (clientes, precios, OCs) van en `data/real/`. Esa carpeta nunca se sube a GitHub.
- Las claves (API keys) nunca van en el chat ni en un archivo del repositorio.
- Nada sale hacia un cliente sin tu OK.
- Una cosa a la vez.
