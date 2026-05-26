# MEMORIAS — Proyecto Avícola Rubiales

Registro de contexto, decisiones y aprendizajes. Útil para retomar el proyecto después de pausas o para ponerlo en contexto a alguien nuevo (papá, banco, contratista, asesor).

Última actualización: 2026-05-03

---

## Contexto base del proyecto

- **Sociedad:** Sociedad Agropecuaria Miramar — Jaime Acuña e Hijos.
- **Socios:** Juan Acuña 64% · Alejandro Acuña 33% · Jaime Acuña (gestor y representante legal).
- **Ubicación:** Finca propia de 2.000 ha en Rubiales, Puerto Gaitán, Meta.
- **Modelo:** Avícola free-range integrada con cultivo de plátano Dominico Hartón en 8 ha.
- **Comprador:** Duflo — confirmado para absorber producción de huevo, plátano y eventualmente pollo.
- **Financiación objetivo:** Crédito Finagro $200M.

## Por qué este proyecto es diferente

1. Tierra propia de 2.000 ha — el espacio free-range no cuesta.
2. Comprador confirmado antes de producir — Duflo absorbe el 100% de la fase 2.
3. Sinergia gallinas ↔ plátano: gallinaza fertiliza, plátano da sombra, costo de insumos casi cero.
4. Modelo modular: cada sección nueva replica la primera sin rediseño.

## Plan por fases

| Fase | Gallinas | Utilidad/mes | Mercado |
|------|---------:|-------------:|---------|
| 1 — Validar | 2.000 | $7.9M | Duflo (29% demanda) |
| 2 — Cubrir Duflo | 7.000 | $27M | Duflo (100%) |
| 3 — Renegociar + maíz propio | 7.000 | $46M | Duflo $17–18k |
| 4 — Diversificar | 10.000+ | $60M+ | Duflo + Villavo + Bogotá |
| 5 — Exportar | 10.000+ | $93M+ | Ecuador, Panamá, Caribe (USD) |

## Documentos del proyecto

1. **Plan Maestro** (`Proyecto Rubiales-Finagro200M.pdf`) — para dueño y banco.
2. **Setup Técnico** (`SetupTecnico_Rubiales.pdf`) — para maestro de obra, agrónomo, electricista. **Estado: borrador, pendiente revisión de papá.**
3. **Anexo Planos Visuales** (`Anexo2_Planos_Visuales_Rubiales.pdf`) — 7 planos para contratistas.
4. **Hoja de Visita** (`HojaVisita_Gallinas_ParaPapa.pdf`) — contactos y preguntas para 3 proveedores de pollitas.
5. **Guías técnicas:** Babcock Brown y Hy-Line Brown — referencia nutricional.

## Decisiones tomadas

- **2026-05-03** — Estructura de 3 documentos + hoja de visita validada. Cada uno tiene audiencia clara.
- Recomendación estratégica del Setup Técnico: arrancar con **Escenario B (bienestar animal)**, expandir a **C (exportación)** en el galpón 2 cuando ya haya flujo de caja.
- Galpón: 12 m ancho, 3.20 m al alero, 4.80 m al caballete, ventilación natural por caballete (sin ventiladores eléctricos para 2.000 gallinas).
- Sistema de agua: pozo → bomba → tanque elevado → gravedad a 220 chupos nipple en 4 líneas.
- Sistema eléctrico: híbrido solar + planta.

## Riesgos identificados

- **Bioseguridad en free-range clima cálido** — riesgo #1, falta plan específico.
- **Margen 29% agresivo** — Finagro lo va a estresar, hace falta análisis de sensibilidad.
- **Cronograma desfasado** — fechas originales (jul-ago 2025) ya pasaron.
- **Colaves vende pollitas de 1 día, no de 16 semanas** — verificar si tienen aliado de levante.

## Proveedores en evaluación

| Proveedor | Ubicación | Línea | Notas |
|-----------|-----------|-------|-------|
| Colaves | Girón, Santander | ISA Brown, Shaver Black | Vende de 1 día — preguntar por levante |
| San Marino | Girón, Santander | — | Visitar mismo día que Colaves |
| Toscana | — | — | Solo WhatsApp, no acepta visitas. $26k negociable |

## Conversaciones y revisiones

*(Anotar aquí cada vez que haya reunión con papá, llamada con proveedor, visita a finca, conversación con Duflo, etc. Formato: fecha — con quién — qué se habló — qué quedó pendiente.)*

- **2026-04-30** — Visita presencial a Duflo S.A.S. Asistieron papá (Jaime) y Juan. Atendió José Munera Benedetti (Gerente de Operaciones). El pitch fue exploratorio: "tenemos finca en la zona, queremos ser proveedores". José compartió a grandes rasgos qué compra Duflo (huevos, plátano, patilla, carne) y de dónde lo trae actualmente (Bogotá y aledañas, 8-10 h de tránsito). **No hubo compromiso formal de compra** — la lectura nuestra es que por costo y logística Duflo nos preferiría si tenemos producción consistente. Esa lectura es la razón por la que estructuramos el proyecto. Mismo día, Juan envió WhatsApp agradeciendo la visita.
- **2026-05-03** — Revisión inicial de la carpeta de documentos. Se crearon Pendientes y Memorias. Próximo paso: cerrar revisión de papá del Setup Técnico.
- **2026-05-25** — Sesión Juan ↔ Claude. Tres bloques de trabajo:
  1. **Pendientes y Memorias estructurados** — 11 tareas activas de la semana + 3 cuellos de botella identificados (Cormacarena, Banco Agrario, ICA Mosquera).
  2. **Investigación regulatoria ICA / free-range** — confirmado que NO está prohibido; ruta de certificación es la Resolución 16409 de 2024 (Bienestar Animal). Documentado en `04-regulatorio/ica/regulatorio-ica.md`.
  3. **Sistema MiramarBox creado** — clon del patrón ZenderBox WMS: 7 módulos numerados, `00-Memorias/` por módulo, workflow branch+PR, comando `/guarda-finca` para cerrar sesiones. Repo en `github.com/ZenderBox/Rubiales` (provisional). PR #1 (estructura inicial) merged.
- **2026-05-26** — Sesión Juan ↔ Claude. Hitos:
  1. **Datos legales sociedad extraídos** — NIT 900.798.798-8, matrícula 02526088. Hallazgo crítico: matrícula vencida desde abril 2024.
  2. **Predios identificados** — El Trueno (991 ha, vereda Rubiales, a nombre del tío William Iván, embargado por Cesia Martinez ~$160.9M COP + Seguros Bolívar 2017) + La Realidad (posesión, sesión dedicada pendiente). Plan Maestro decía 2.000 ha — error histórico, son 991.
  3. **Incidente legal Cesia Martinez registrado** — conflicto familiar largo, caso en Corte Constitucional. Bloquea Fase 2 con Finagro; Fase 1 viable bajo comodato.
  4. **Correo ICA enviado** — consulta exploratoria a Mosquera/Tibaitatá (territorialidad + Resolución 16409). Esperando respuesta.
  5. **Correo Duflo enviado** — warm follow-up a José Munera (Gerente Operaciones · `jose.munera@duflosas.com`) presentando el proyecto y solicitando reunión formal en 2 semanas. Decisión de no exponer Finagro ni embargo en el correo. Enviado desde `juan.acuna@zenderbox.com` para reforzar credibilidad (el correo menciona el rol de CEO de ZenderBox).
  6. **Banco Agrario · primer envío de documentos** — Juan envió declaraciones de renta 2018-2020 + estado financiero (lo que pidió papá) al banco para reactivar la cuenta. ⚠️ Riesgo: las declaraciones son antiguas. Si rechazan, hay que activar T18 (declaraciones 2021-2025 con contadora).
  7. **Dashboard actualizado** — 4 bloqueadores activos (B0 matrícula crítico, B1 Cormacarena, B2 banco esperando respuesta, B3 ICA resuelto-enviado). Predios documentados en `00-core/00-Memorias/predios.md`. Incidente Cesia en `00-core/07-Incidentes/2026-05-25_conflicto-legal-cesia-martinez.md`.

---

*Este archivo es la memoria viva del proyecto. Actualizar después de cada hito, conversación importante o decisión.*
