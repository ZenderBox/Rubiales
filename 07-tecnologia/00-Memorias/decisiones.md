# Decisiones — 07-tecnologia

> Por qué cada equipo / proveedor. Para no re-discutir lo ya cerrado.

## 2026-06-07

### D01 · Crear módulo 07-tecnologia
- **Decisión:** infraestructura tech vive en un módulo cross propio (no en 01-galpon ni 06-proveedores).
- **Por qué:** la red Starlink + IoT atraviesa galpón, plátano, energía, regulatorio. Tener un solo dueño técnico evita decisiones contradictorias.
- **Owner técnico:** Juan.

### D02 · Starlink como internet base (no fibra ni 4G)
- **Decisión:** Starlink es la primera opción.
- **Por qué:**
  - Fibra: no hay cobertura en vereda Santa Helena (Puerto Gaitán rural).
  - 4G/5G: cobertura irregular, latencia alta para videollamadas con Juan.
  - Starlink: 100% cobertura satelital + latencia LEO razonable (40-60ms típico).
- **Verificación pendiente:** confirmar disponibilidad Residential en coordenadas exactas (deep-research en curso).

### D03 · IoT-ready desde día 1
- **Decisión:** dimensionar la red para 5-15 dispositivos IoT desde el arranque.
- **Por qué:** cambiar router/red después es más caro que comprar bien una vez.

### D04 · UPS obligatorio para Starlink + router
- **Decisión:** UPS de mínimo 800VA para el rack de red.
- **Por qué:** la finca tiene cortes frecuentes de energía. Sin UPS, la conectividad se cae con cada bajón → cámaras pierden grabación, sensores desincronizan.

### D05 · Etapa 1 = Starlink en casa principal · Etapa 2 = mover al galpón con enlace PtP
- **Decisión Juan + papá:** este viernes 12-jun se instala Starlink en la **casa principal** (electricidad estable, casa ya existe).
- **Por qué:** el galpón aún no está construido. Esperar para el Starlink retrasa todo el proyecto IoT. La casa principal funciona como base inicial mientras se levanta el galpón.
- **Etapa 2 (cuando arranque el galpón):** se evalúa **mover el Starlink al galpón** (mejor vista al cielo, más cerca de cámaras/sensores críticos) + agregar **enlace Ubiquiti LiteBeam 5AC 500m** para que la casa principal mantenga internet.
- **Decisión final del punto del Starlink:** se toma en sitio durante el viaje del viernes (verificar vista al cielo, obstáculos, ubicación de techos).

### D06 · NO comprar Ubiquiti 500m en esta etapa
- **Decisión:** no traer Ubiquiti LiteBeam ahora. Solo cuando arranque el galpón.
- **Por qué:** ahorra ~\$1.6M COP de hardware que no se usaría hasta Fase B. Si en el viaje del viernes papá identifica un escenario donde ya conviene (ej. galpón arranca pronto), se compra después.

### D11 · NO SIM celular backup · sin señal en la finca
- **Decisión:** se elimina la SIM Claro/Movistar del plan. Juan confirmó que la señal celular en la finca es **prácticamente cero**.
- **Implicación:** Starlink es el ÚNICO acceso a internet. NO hay backup si Starlink falla (mantenimiento, lluvia muy fuerte sostenida, falla del satélite).
- **Mitigación:** (a) UPS robusto para que el Starlink sobreviva cortes eléctricos, (b) montar la antena con vista al cielo despejada (sin árboles tapando), (c) si pasa algo, Tailscale + Reolink Cloud siguen guardando localmente en NVR/microSD hasta que vuelva la conexión.
- **Plan futuro Fase 2:** si la criticidad aumenta, evaluar **segundo kit Starlink** como redundancia (overkill para Fase 1, justificable cuando haya 5K-10K aves productivas).
- **Ahorro:** $40-60K COP/mes (~$500-720K COP/año).

### D10 · Comprar TODO en Amazon US con Tax Exemption · cuenta business
- **Decisión:** todas las compras Miami se hacen en Amazon US con la cuenta business de Juan que tiene Tax Exemption activa.
- **Por qué:** ahorra 7% de sales tax Florida sobre cada compra. Sobre el total proyecto ($2.220 USD) son ~$155 USD = ~$620K COP adicionales de ahorro.
- **Reglas:** (a) usar cuenta Amazon Business con cert tax exempt vinculado, (b) NO usar cuenta personal, (c) verificar al checkout que diga "Tax: $0.00".

### D09 · Aprovechar empresa de logística propia · adelantar CCTV galpón completo
- **Decisión:** comprar TODO el hardware del proyecto IoT (Etapa 1 maleta + Etapa 2 envío logística) en USA, dejar listo en Colombia ANTES de que arranque la obra del galpón.
- **Por qué:** Juan tiene empresa de logística propia US ↔ CO → costo de envío bajo. Hardware tech en Colombia tiene markup 50-100% vs USA. Aún con IVA 19% el ahorro es ~$5-7M COP en el proyecto completo.
- **Alcance:** Etapa 2 incluye: 7 cámaras (4 galpón + 2 casa + 1 perímetro solar), 1 NVR Reolink RLN8-410, 2 access points outdoor, switch PoE, 2 UPS, sensores Shelly (H&T, Plug, Flood), cables y monturas. Total Etapa 2: ~USD 1.565.
- **Resultado:** cuando arranque la obra del galpón, el encargado solo INSTALA hardware ya en sitio. Toda la configuración técnica se hace remota desde Miami via Tailscale.

### D08 · Juan viaja con papá el viernes · compras divididas Colombia + Miami
- **Decisión:** Juan viaja a Colombia esta semana y va con papá el viernes a la finca → aprovechar para traer hardware desde Miami (~USD 680 = ~$2.7M COP en mercancía).
- **Implicación clave:** Etapa 2 (enlace 500m) se adelanta al primer viaje. La finca queda completamente IoT-ready desde el viernes 12-jun en vez de esperar meses.
- **Miami (Juan):** Raspberry Pi 5 + 2× Ubiquiti LiteBeam + surge protectors + cámaras Reolink + cable outdoor + adaptadores. Ahorro real ~$1.2M COP vs comprar Colombia.
- **Colombia (papá):** Kit Starlink Falabella + UPS APC + SIM backup. El kit Starlink DEBE comprarse en Colombia (cuenta atada a país).
- **DIAN:** modalidad viajero permite USD 2.000 libre · $680 cabe sobrado.

### D07 · Plan Residencial LITE (no Standard ni Business) · comprar en Falabella
- **Decisión:** Plan **Residencial Lite COP $160.000/mes**. Hardware comprado en **Falabella Colombia** (COP $1.349.900, vs $1.599.000 en starlink.com directo).
- **Validación:** cobertura confirmada por starlink.com con dirección Puerto Gaitán Meta ("Fast, reliable internet available at: Puerto Gaitán, Meta, Colombia").
- **Por qué NO Business:** cobra por gigas (50GB/500GB/1TB) · 15 IoT no llegan a 200GB/mes · kit Performance $6.257K = overkill para finca · ahorro $5-10M COP/año yendo Personal.
- **Por qué NO Standard:** Lite es suficiente para Etapa 1 (1 cámara + uso esporádico). Si se queda corto, se sube a Standard con un click en la app Starlink, sin penalidad ni cambio de hardware.
- **Misterio del "$250.000 USD" resuelto:** era el Kit Performance del plan Business ($6.257K COP / $6.519K total checkout) que la UI mostraba con `$`.
- **Total año 1:** $1.349.900 hardware + $1.920.000 (12 meses Lite) = **~$3.27M COP** (~USD 815).
