# Decisiones — 04-regulatorio

> Decisiones específicas de este módulo. Las cross-módulo viven en `00-core/06-Decisiones/`.

## Plantilla

```
### NNNN — Título corto · YYYY-MM-DD
- **Decisión:**
- **Por qué:**
- **Alternativas descartadas:**
- **Implicaciones:**
```

## Historial

### 0001 — Stand-by correo ICA hasta renovar matrícula · 2026-05-25
- **Decisión:** no enviar el correo formal a `gerencia.cmarca@ica.gov.co` hasta que la sociedad tenga matrícula mercantil al día (T15).
- **Por qué:** el certificado de Cámara advierte literalmente que la sociedad no ha renovado en 2025 ni 2026. Mandar consulta formal a ICA citando NIT con matrícula en mora expone un flanco — pueden bajar la prioridad del caso o exigir subsanar antes de proceder.
- **Alternativas descartadas:**
  - Mandar el correo igual sin mencionar el tema → riesgo si ICA verifica.
  - Mandar el correo mencionando la renovación en curso → pone foco en el problema desde la primera comunicación.
- **Implicaciones:** el borrador completo está listo en `04-regulatorio/ica/correo-consulta-2026-05-25.md` con el NIT real (900.798.798-8). Se envía apenas T15 esté cerrado (24-48 h post-renovación).

### 0002 — No mencionar Duflo por nombre en el correo a ICA · 2026-05-25
- **Decisión:** el borrador del correo al ICA cita "comprador único en la región" en lugar de "Duflo".
- **Por qué:** información comercial no agrega valor regulatorio y reduce exposición innecesaria.
- **Implicaciones:** misma política para otros trámites públicos (Cormacarena, Banco Agrario): no exponer nombre del comprador salvo que lo soliciten formalmente.

### 0003 — Evaluar agregar CIIU 0145 al objeto social en próxima renovación · 2026-05-25
- **Decisión:** en la renovación de matrícula (T15) considerar agregar CIIU 0145 (Cría de aves de corral) al objeto social registrado.
- **Por qué:** actualmente la sociedad tiene CIIU 0141 (bovino), 0129 (cultivos permanentes), 0161/0162 (apoyo). No tiene avícola explícito. ICA puede objetar incoherencia entre objeto social y actividad solicitada.
- **Implicaciones:** confirmar costo adicional de modificación del objeto social al renovar. Coordinar con contadora antes de presentar.

---

## 2026-06-06

### D04 · Plan maestro Trueno · póliza ANTES de carta a Mesa Corzo
- **Decisión:** No mandar carta de acercamiento al abogado de Cesia hasta tener la póliza de caución (Art. 590 CGP) emitida en mano.
- **Por qué:** Sin póliza emitida la carta es bluff (probabilidad aceptación ~35%). Con póliza en mano, Mesa ve que NO podemos ser presionados con el embargo (probabilidad ~55%). Además, el "no alborotar el avispero" tiene fecha de caducidad: cuando radicamos al juez Mesa se entera obligatoriamente.
- **Implicación:** semanas 1-6 trabajamos la póliza en silencio. Semana 6 con póliza emitida + carta. Si Cesia rechaza → semana 8 radicamos póliza al juez + paquete defensa simultáneo.
- **Ver:** `predios/el-trueno/proceso-legal/plan-maestro-estrategia.md`

### D05 · Monto real Cesia ~$100M, no $150-300M
- **Decisión:** El techo realista de negociación es ~$100M COP (capital de las 2 fincas según perito no oficial: $50.24M c/u), no los $150-300M que pensábamos.
- **Por qué:** Información de papá (llamada 2026-06-06): el embargo oficial $160.9M tiene ~$60M de aire (intereses + costas inflados). Lo que realmente exige Mesa Corzo es el capital de las dos fincas.
- **Implicación:** Carta a Mesa ofrece $20-40M (techo $50M), no $40-60M como pensábamos antes. PENDIENTE T47: confirmar con Leonardo si la nulidad parcial del 15-mar-2024 blinda contra el cobro de la 2da finca.

### D06 · Paquete defensa de 4 documentos + insumos papá
- **Decisión:** Estructurar paquete de defensa con 4 borradores legales + 1 archivo de insumos:
  1. Denuncia penal Fiscalía (Arts. 286/289/453 CP) contra Agustín Mesa Corzo
  2. Queja Defensoría del Pueblo (vulneración debido proceso William Iván)
  3. Memorial Corte Constitucional (hechos sobrevinientes)
  4. Carta acercamiento Mesa Corzo (PIEZA CLAVE)
  + 0. Elementos defensa de papá (bienes retenidos + mejoras + prediales 2000-2011)
- **Por qué:** Auto del 15-mar-2024 declara probada la manipulación documental → arma de leverage muy fuerte. La carta es lo que se manda; el resto son amenazas reales listas para radicar.
- **Ver:** `predios/el-trueno/proceso-legal/paquete-defensa/`

### D07 · Cotizar 3 corredores de seguros (NO aseguradoras directo)
- **Decisión:** Pedir cotización a 3 perfiles distintos de corredores:
  1. Contacto de Leonardo (a definir)
  2. Delima Marsh o Aon (corredor multinacional grande)
  3. Correcol o Proseguros (corredor nicho judicial)
- **Por qué:** Las aseguradoras (Sura, Liberty, etc.) no venden póliza Art. 590 directo. Los corredores estructuran la contragarantía y negocian la prima. Tener 3 cotizaciones evita aceptar la primera oferta.
- **Criterio de decisión:** NO ganar por prima sino por contragarantía mínima exigida (es lo difícil de cumplir con T15/B4 atrasadas).

### D08 · Restaurar T15 a "pending" para probar fix de bug
- **Decisión:** T15 (Cámara) queda como pending en data.json aunque papá ya la hizo, para que pueda probarla mañana y verificar el fix del bug de refresh.
- **Por qué:** El bug donde tareas marcadas como hechas reaparecían al refrescar fue arreglado en PR #21. Necesitamos probar el fix con una tarea real.

---

## 2026-06-11

### D09 · Aprovechar Decreto 0243/2026 para amnistía predial Trueno
- **Decisión:** antes de pagar T25 (predial $72.9M acumulado 2018-2026), Juan + Leonardo visitan Alcaldía Puerto Gaitán para evaluar amnistía bajo Decreto Legislativo 0243 de 2026.
- **Por qué:**
  - Decreto Legislativo 0243 de 2026 (Emergencia Económica) otorga facultades excepcionales a alcaldes para adoptar amnistías tributarias territoriales.
  - Comparable: Medellín redujo 70% intereses por mora.
  - Ahorro potencial estimado: ~$32M COP sobre los $72.9M (44% menos).
- **Implicación:** T25 queda en espera de T76 (averiguar) y T77 (carta Leonardo si no hay decreto local).
- **Plazo:** antes 30-jun-2026 (vencimiento original predial).
