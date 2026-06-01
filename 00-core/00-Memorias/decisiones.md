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

## 2026-05-27

### D11 · Raza definitiva · Babcock Brown
- **Decisión:** la raza para Fase 1 es **Babcock Brown** (Hendrix Genetics, distribuida por San Marino en Colombia).
- **Por qué:**
  - Evidencia familiar real: lote actual del papá en semana 40, no se ha enfermado una sola vez.
  - Comparativo: lotes anteriores de Hy-Line se enfermaron 2 veces a edades similares.
  - Babcock está oficialmente diseñada para climas cálidos tropicales — Puerto Gaitán 28-30°C.
  - Métricas oficiales casi idénticas a ISA/Hy-Line (viabilidad 94%, pico 96%, huevo 63.8g, 417 huevos/gallina alojada).
- **Alternativas descartadas:** ISA Brown, Hy-Line Brown (las 3 son Hendrix; sin diferencia significativa en tabla, sí en rusticidad operativa local).
- **Implicación:** **el Plan Maestro debe actualizarse** (decía ISA/Hy-Line). El correo a ICA y Duflo mencionan "ISA Brown o Hy-Line Brown" — aceptable porque el correo dice "línea X o Y", deja apertura. Documentos comerciales y técnicos futuros: Babcock Brown.

### D12 · Proveedor de pollas · San Marino (Cumaral, Meta)
- **Decisión:** San Marino es el proveedor de pollas de 16 semanas. Sede de entrega: Cumaral, Meta — planta Villa Claudia.
- **Por qué:**
  - Único proveedor que ofrece pollas de 16 semanas (Colaves vende de 1 día; no nos sirve sin levante).
  - Ubicación crítica: ~4-5 h al predio (Puerto Gaitán). Vs Girón (12+ h) implica menos estrés post-traslado y menor mortalidad.
  - Precio competitivo $26.500/polla, con margen de rebaja.
  - Lotes mensuales recurrentes (15 de cada mes: jul, ago, sep) — flexibilidad de cantidad.
  - Servicios complementarios: ayudan con camión especializado + canastas plásticas.
  - Plan vacunal completo provisto (14 aplicaciones, día 1 a semana 15) — buena referencia técnica.
- **Alternativas descartadas:** Colaves (1 día, no 16 sem), Toscana (no acepta visitas).
- **Implicación:** **NOTA importante** — San Marino dice expresamente "no se hace responsable del cumplimiento del protocolo sanitario". Después de semana 16 las aves son responsabilidad nuestra → necesitamos veterinario en sitio o programa de visitas (T22).

### D13 · Lote target · 15 de septiembre 2026
- **Decisión:** apuntar al lote del **15 de septiembre 2026** de San Marino. Descartado 15-jul y 15-ago.
- **Por qué:**
  - 15-jul (7 sem desde 27-may): heroico. Galpón (6-8 sem) + Cormacarena + ICA bioseguridad + sistemas + sanitización + adaptación = imposible.
  - 15-ago (10 sem): ajustado pero realista. Riesgo medio.
  - **15-sep (14 sem): holgado.** Permite margen para bloqueadores que aún no resolvemos (Cormacarena, banco, matrícula).
- **Implicación:** primera postura comercial estimada para **enero-febrero 2027** (semanas 20-25 de las aves). Cuando José Munera (Duflo) responda, podemos darle fecha concreta de arranque.

### D14 · Capacidad Fase 1 · TBD entre 2.000 y 5.000
- **Decisión:** **rango abierto** entre 2.000 (plan original) y 5.000. La decisión final depende de cotización del galpón (T20: cotizar 3 escenarios — 2K, 3K, 5K).
- **Por qué:**
  - 2.000 = plan original conservador (USD 10K Juan alcanza).
  - 5.000 = mejor amortización de costos fijos del galpón (terreno, agua, electricidad, vacunación cubren más aves).
  - San Marino ofrece flexibilidad: vende del lote 10K "lo que necesitemos".
  - Galpón más grande = más capital pero mejor unit economics.
- **Implicación:** T20 mide cotización 2K/3K/5K antes de pedir el lote a San Marino. Decisión final antes de finales de junio 2026 (para tener 10 sem de construcción).

### D15 · Plan vacunal · usar como referencia el de San Marino
- **Decisión:** adoptar el plan vacunal de San Marino (14 aplicaciones, día 1 a semana 15) como base, **a aplicar desde semana 16 en adelante por veterinario contratado** (las vacunas pre-semana 16 las aplica San Marino en su planta).
- **Por qué:** cubre todas las enfermedades críticas para zona Llanos (Newcastle, Marek, Bronquitis, Gumboro, Salmonella, Coriza, Pasterella, Viruela). La Triple Oleosa de semana 15 (ND+BI+EDS) ya estaría aplicada al recibir las pollas.
- **Implicación:** verificar al recibir las aves cuáles vacunas vienen aplicadas (certificado del lote) — si alguna falta, T22 veterinario la aplica antes de postura.

## 2026-05-28

### D16 · Dashboard publicado en Cloudflare Pages
- **Decisión:** dashboard del proyecto vive en `https://rubiales.pages.dev` (Cloudflare Pages, plan free).
- **Por qué:** repo GitHub privado no permite GitHub Pages gratis. Cloudflare Pages sí soporta repos privados y auto-redeploya en cada push a `main`. URL no indexada (solo quien tiene el link la ve).
- **Setup:** cuenta Cloudflare `Juan.acuna@zenderbox.com`, app GitHub instalada en org ZenderBox con acceso solo a `Rubiales`. Branch de producción: `main`. Build output directory: `00-core/dashboard`.
- **Implicación:** cualquier merge a main = dashboard se actualiza para papá automáticamente. Cero infraestructura propia. Para Fase 2 (auth con magic link / dominio propio) — ver T24/T25 cuando registremos `agropecuariamiramar.co`.

### D17 · Rebrand provisional a "Miramar"
- **Decisión:** el brand del dashboard pasa de "Zender Ranch" a **"Miramar"** (prefix "Mira" + accent "mar", sin separador).
- **Por qué:** "Miramar" es el nombre legal de la sociedad y la identidad que llevamos a Duflo/ICA. Mantener brand interno = brand externo evita confusiones de marca.
- **Pendiente:** la decisión final del nombre del proyecto (MiramarBox / Miramar / otro) sigue abierta para cuando se registre dominio. Ver T12.

### D18 · Estrategia plátano · 4 tandas escalonadas
- **Decisión:** las 8 ha de plátano Dominico Hartón se siembran en **4 tandas mensuales** (sep, oct, nov, dic 2026), una por potrero de 2 ha.
- **Por qué:** sembrar las 8 ha el mismo día = cosechar las 8 ha el mismo mes = un mes con mucha producción, los demás cero. Escalonar = cosechar continuamente = producción constante 9 ton/mes.
- **Cronograma:** P03-P06 (siembra) → P07 primera cosecha sep-2027 → P08 producción constante jun-2028.
- **Pendiente validar con agrónomo:** marco de siembra exacto (4×3m o 3×3m), riego complementario en seca, mano de obra local con experiencia plátano.

## 2026-06-01

### D19 · Stack técnico de Miramar · n8n+Postgres+EC2 separado en cuenta AWS de ZenderHub
- **Decisión:** replicar el stack del WMS (Ubuntu + Postgres + n8n + nginx) pero en una **instancia EC2 dedicada a Miramar dentro de la cuenta AWS de ZenderHub** (no ZenderBox, no compartida).
- **Por qué:** reusa el conocimiento operacional ya pago de Juan, separa negocios para compliance/sucesión, Postgres > SQLite para crecer, n8n permite flows visuales sin escribir backend custom.
- **Alternativas descartadas:** (1) Cloudflare puro · curva nueva y D1 limita queries; (2) Stack idéntico compartido con WMS · acoplaba contabilidades y operaciones.
- **Implicación:** $20/mes de infraestructura (vs $0-5 de Cloudflare) que se justifican porque este es el sistema operacional de la familia para 10 años. ADR completa: `00-core/06-Decisiones/0001-stack-tecnico-miramar-2026-06-01.md`.

### D20 · F0 completada · servidor Miramar arriba
- **Decisión operativa:** terminar F0 con el dashboard estático corriendo sobre el server propio antes de meter dinámica (F1).
- **Resultado:** EC2 `miramar-n8n` (us-east-2 · `18.226.86.66`) corriendo Postgres 16 + Docker + n8n + nginx. Dashboard sirve `http://18.226.86.66/`. Cloudflare Pages (`rubiales.pages.dev`) sigue activa de respaldo hasta tener DNS + SSL nuevo.
- **Detalles operacionales:** ver `00-core/00-Memorias/servidor-miramar.md`. Credenciales en 1Password vault Miramar.
- **Implicación:** F0 cierra cuando esté DNS subdominio + SSL. F1 (DB schema + API) arranca después.

---

## Decisiones del documento Plan Maestro (pre-existentes)

- Arranque con **2.000 gallinas** ISA Brown (Fase 1).
- Modelo integrado plátano + gallinas en 8 ha, 4 potreros de 2 ha, rotación cada 2 semanas.
- Comprador único Fase 1–2: **Duflo**.
- Escenario constructivo recomendado para arranque: **B (bienestar animal)**, no el premium de exportación.
