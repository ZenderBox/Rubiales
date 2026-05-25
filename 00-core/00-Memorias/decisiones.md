# Decisiones estratégicas — Proyecto Avícola Rubiales

Registro de decisiones tomadas, con fecha, contexto y razón. Para no re-discutir lo ya cerrado.

---

## 2026-05-25

### D01 · Aporte de capital inicial USD 10.000 desde Miami
- **Decisión:** Juan transfiere USD 10.000 desde Miami al Banco Agrario como aporte de capital arranque.
- **Por qué:** desbloquear el proyecto financieramente sin esperar Finagro.
- **Pendiente:** estructurar legalmente el aporte (préstamo de socio vs. aumento de capital) — definir con contadora/abogado.

### D02 · Tramitar permiso ICA por Mosquera (Tibaitatá) en lugar de Villavicencio
- **Decisión:** intentar primero la vía Mosquera.
- **Por qué:** papá ya tiene contacto verbal previo en Mosquera. Eficiencia y conocidos.
- **Riesgo:** que territorialmente deba hacerse en Villavicencio (territorio Meta). Validar por correo (T04).

### D03 · Constructor galpón — ingenieros de la zona, NO Moreno Vargas
- **Decisión:** descartar Moreno Vargas como opción principal; ir con ingenieros locales.
- **Por qué:** Moreno Vargas hace obras civiles de mayor escala — no es el fit para un galpón avícola. Ingenieros locales conocen la zona, materiales y costos reales.

### D04 · Compra de plántulas plátano por tandas
- **Decisión:** las 8.888 plántulas de Dominico Hartón NO se compran de una sola vez.
- **Estrategia:** compra escalonada para tener producción constante de 9 toneladas/mes una vez en operación.
- **Razón:** plátano no aguanta llegar todo al mismo tiempo y producir todo al mismo tiempo — se desfasa la cosecha.

### D05 · Secuencia: visita presencial a Duflo ANTES del correo formal
- **Decisión:** primero visitar Duflo en persona, luego el correo de seguimiento.
- **Por qué:** relación se construye en persona; el correo formaliza lo conversado.

### D06 · Free-range en Rubiales — viable y legal
- **Decisión:** ratificar el modelo free-range.
- **Por qué:** investigación regulatoria 2026-05-25 confirma que NO está prohibido. Ver `regulatorio-ica.md`.
- **Sello a perseguir:** Resolución ICA 16409 de 2024 (Bienestar Animal) desde Fase 1.

### D07 · Sistema de gestión del proyecto = MiramarBox (working name)
- **Decisión:** clonar el patrón modular de ZenderBox WMS para gestionar el proyecto agropecuario.
- **Nombre provisional:** MiramarBox (hereda nombre de la sociedad). Pendiente decisión final entre MiramarBox / FincaBox / CampoBox / otro.
- **Repo:** `https://github.com/ZenderBox/Rubiales` (se renombra cuando se decida el nombre final).
- **Por qué:** el patrón ZenderBox ya probó funcionar — disciplina de memorias, módulos numerados, comandos `/guardar-*`. Replicarlo evita inventar.
- **Estructura:** 7 módulos numerados con `00-Memorias/` cada uno (ver `README.md`).

### D08 · Workflow: branch + PR siempre, owner mergea
- **Decisión:** ningún commit directo a `main`. Toda sesión de trabajo termina con `/guarda-finca` que crea branch + PR; Juan revisa y mergea.
- **Por qué:** trazabilidad de cambios, control del owner, mismo flujo que ZenderBox.
- **Implicación:** `/guarda-finca` nunca usa `git add .` ni hace merge.

### D09 · Drive para pesados — pospuesto
- **Decisión:** por ahora todo en git. No abrir Drive hasta que aparezca el primer archivo >10MB (video del galpón, foto hi-res, escaneo grande).
- **Por qué:** los PDFs actuales (1-3 MB) y fotos WhatsApp (200 KB) caben sin friction en git. Drive agrega un punto más de gestión que no necesitamos todavía.
- **Cuando aparezca:** crear carpeta `MiramarBox/` en Drive y dejar `LINKS.md` por módulo apuntando.

### D10 · DOCX duplicados se mantienen en 00-core/editables/
- **Decisión:** los `.docx` (Plan Maestro, Setup Técnico, Anexo Planos, Hoja Visita) viven en `00-core/editables/`. Los `.pdf` viven en sus módulos respectivos.
- **Por qué:** los DOCX sirven para seguir editando; los PDF son para compartir. Separarlos evita confundir cuál es la fuente de verdad.

---

## Decisiones del documento Plan Maestro (pre-existentes)

- Arranque con **2.000 gallinas** ISA Brown (Fase 1).
- Modelo integrado plátano + gallinas en 8 ha, 4 potreros de 2 ha, rotación cada 2 semanas.
- Comprador único Fase 1–2: **Duflo**.
- Escenario constructivo recomendado para arranque: **B (bienestar animal)**, no el premium de exportación.
