# Aprendizajes y contexto operativo

Cosas que aprendimos sobre el terreno, sobre el papá, sobre los proveedores y sobre la operación. Para no tropezar dos veces con la misma piedra.

---

## Contexto operativo del papá (Jaime)

- Papá es el gestor en campo. Vive cerca de la finca y maneja las relaciones presenciales (ICA, Cormacarena, constructores, vendedores).
- Le funciona el contacto verbal/telefónico antes que el correo. Cuando hay que formalizar algo, el correo va después de la conversación.
- Tiene buen criterio para descartar proveedores que no encajan (ej. Moreno Vargas — sabe distinguir obra civil grande vs. galpón).
- Tiende a olvidar nombres de contactos nuevos en el momento (ej. constructor del galpón). **Lección:** después de cada llamada con papá, pedirle explícitamente los nombres y guardarlos en `contactos.md`.

## Sobre el mercado avícola colombiano

- Colaves vende pollitas de 1 día, no de 16 semanas. Importante preguntar siempre por servicio de levante.
- Toscana no recibe visitas — todo por WhatsApp/llamada. Precio referencia ~$26.000/unidad.
- San Marino y Colaves están ambas en Girón (Santander) — un solo viaje cubre las dos.
- En Colombia NO hay un sello oficial "free-range". La certificación seria es la Resolución 16409 de 2024 del ICA (Bienestar Animal). Internacional: Certified Humane (HFAC).

## Sobre regulación / trámites

- **Cormacarena es el cuello de botella real.** Sin permiso de agua no hay ICA, sin ICA no hay venta legal. Es la tarea más crítica del proyecto.
- ICA Mosquera vs. Villavicencio: territorialmente Meta debería ir por Villavicencio, pero papá tiene contacto previo en Mosquera. Vale la pena intentar Mosquera primero (T04 semana actual).
- El traslado de ganado en Colombia ya está permitido nuevamente (mayo 2026). Relevante para futuro de la finca, no para el componente avícola.

## Sobre estructura financiera

- El aporte inicial de USD 10.000 desde Miami requiere primero reactivar el Banco Agrario.
- Banco Agrario pide declaraciones de renta + estado financiero de la contadora para reactivar.
- **Lección operativa:** los trámites bancarios desde Miami requieren tiempo de escaneo y envío — meterlos siempre en el camino crítico.

## Sobre el roadmap del proyecto

- Las muestras de plátano y patilla salen en 15 días (≈ 9 jun 2026) — usar ese hito como referencia para construir el roadmap completo hacia atrás.
- El proyecto tiene 3 cuellos de botella simultáneos: capital (banco), agua (Cormacarena), ICA. Los tres pueden tramitarse en paralelo pero hay dependencias.

## Sobre el workflow de PRs (regla crítica)

**Problema observado en 2 ocasiones (PR #5 y PR #6):** se mergeó un PR mientras Claude estaba pusheando commits adicionales a la misma branch. Resultado: los commits posteriores quedaron huérfanos (en la branch pero no en main), y hubo que recuperarlos con un PR de fix (#7 y antes).

**Regla operativa de ahora en adelante:**
- Claude debe terminar TODOS los pushes a una branch ANTES de avisar al owner.
- Claude debe decir explícitamente "PR #X listo · podés mergear" al owner.
- El owner NO mergea hasta esa señal.
- Si después del merge hace falta agregar algo, va en una branch nueva — no en la branch ya mergeada.

Este patrón es propio de un flujo solo/colaborativo (un dev + un revisor). Sin esta disciplina los commits se pierden silenciosamente.

## Sobre Cloudflare Pages

- El UI nuevo de Cloudflare mezcla Workers y Pages — el flujo de "Crear aplicación" puede empujar al de Workers en vez de Pages. Para forzar Pages: link de abajo "¿Busca implementar Pages? Comenzar".
- Para repo en organización GitHub (no cuenta personal): al autorizar la app de Cloudflare en GitHub, seleccionar **la organización** (no la cuenta personal). Si seleccionás cuenta personal, no ve los repos de la org.
- **Build output directory** es el campo crítico para proyectos no-en-root. Para nuestro repo: `00-core/dashboard`.
- **Production branch** debe ser `main`, no la branch inicial del repo (suele cargarse el default que ve primero — en nuestro caso fue `setup/initial-structure`, que estaba vacía).

## Sobre el sistema MiramarBox

- El patrón ZenderBox WMS (módulos numerados + `00-Memorias/` + comandos `/guardar-*`) se traduce 1:1 a un proyecto agropecuario. No hace falta inventar arquitectura nueva.
- El bootstrap de un repo nuevo en GitHub requiere un commit inicial en `main` para que se pueda abrir PR. Una vez sembrado, todo el resto va por branch + PR.
- El comando `/guarda-finca` se modela como `/guardar` del WMS: detectar módulo → actualizar memorias → branch + commit + push + PR. Owner mergea. Nunca push directo a main.
- Decisión arquitectónica clave: empezar con markdown plano + HTML estático. Postgres / n8n / WhatsApp solo cuando el manual duela (Fase F4-F5 del roadmap del sistema). Replicar la evolución por dolor que funcionó en ZenderBox.
