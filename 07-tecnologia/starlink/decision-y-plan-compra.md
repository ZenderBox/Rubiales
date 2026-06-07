# Starlink · Decisión + plan de compra

> **Investigación:** deep-research multi-fuente · 8 hallazgos verificados (107 agentes, 342 web searches).
> **Fecha:** 2026-06-07
> **Objetivo:** internet operativo en la finca el **viernes 12-jun**.

---

## 🎯 Recomendación final

**Comprar el Kit Estándar V4 en COLOMBIA vía Falabella + plan Residencial Estándar.**

| Item | Valor | Fuente |
|---|---|---|
| Kit Estándar V4 (Falabella) | **COP $1.349.900** (~USD 335) | falabella.com.co/falabella-co/product/73053329 |
| Plan Residencial Estándar | **COP $250.000/mes** | starlink.com/co + 5 fuentes |
| Velocidad típica | Hasta 400 Mbps | Confirmado |
| Datos | **Ilimitados con prioridad alta** | Confirmado |
| **Costo total año 1** | **~COP 4.350.000** (~USD 1.080) | |

→ Entra **perfecto** en budget: hardware <USD 800 ✅ · mensual =COP 250K tope ✅

---

## ❌ Por qué NO comprar en USA

El "precio absurdo" que Juan vio ($250.000 con dirección Rubiales) era **el precio COP renderizado con `$`** que la UI confunde con USD.

- Precio real Colombia: **COP $1.599.000** (precio lista) / **$1.349.900** (Falabella con descuento)
- Precio Miami: USD $50/mes solo es válido si el kit se queda en USA
- **Si traés kit USA → forzás plan Roam ~USD $165/mes (~COP $660K/mes) = 2.6× más caro**
- Aduana: DIAN permite USD $2.000 libre por viajero → legalmente OK, **pero económicamente malo**

---

## 📅 Cronograma para el viernes 12-jun

| Día | Acción | Owner |
|---|---|---|
| **Sábado 7 (HOY)** | Verificar cobertura en starlink.com/map · pedir kit en Falabella | Juan |
| Domingo 8 | (Falabella procesa) | — |
| Lunes 9 / Martes 10 | Falabella entrega en Bogotá | Papá recibe |
| Miércoles 11 | Activar cuenta starlink.com con el kit (revisar serial) | Juan |
| Jueves 11 | Papá empaca kit + UPS + cámara prueba para viaje | Papá |
| **Viernes 12** | Viaje a la finca · instalar antena · primera conexión | Papá (+Juan remoto por celular) |

---

## ⚠️ Bandera roja crítica: CGNAT

Starlink Residential usa **CGNAT** (IPs 100.x.x.x). El add-on "IP pública" fue **discontinuado en mayo 2024**.

**Implicación:** las cámaras IP del galpón **NO se pueden acceder con port forwarding clásico** desde Miami.

**Solución obligatoria:** instalar **Tailscale** (gratis para uso personal) en:
- Un mini-PC o Raspberry Pi en la finca (o el router si soporta)
- El celular y laptop de Juan en Miami
- → acceso a las cámaras como si estuvieran en LAN local

Alternativas: Cloudflare Tunnel, ZeroTier.

---

## 🔍 Verificación pendiente antes de comprar

1. **Cobertura específica Puerto Gaitán:** ir a https://starlink.com/map y poner "Vereda Santa Helena, Puerto Gaitán, Meta" o coordenadas GPS de la finca → confirmar "Available".
   - Riesgo: bajo (Llanos Orientales tiene cobertura), pero **no cero**.
2. **Stock real en Falabella:** confirmar entrega Bogotá lunes/martes antes de pagar.

---

## 📦 Lo que viene en el kit

- Antena Standard V4 (rectangular)
- Base de pie incluida
- Router Gen 3 (WiFi 6, 2 puertos Ethernet) ← **importante: soporta bypass mode**
- Cable antena-router (15m)
- Fuente de poder
- Consumo: 50-100W (necesita UPS para cortes)

---

## 🛠️ Componentes adicionales semana 8-12 jun

Comprar EN COLOMBIA esta semana para el viaje del viernes:

| Componente | Para qué | Budget | Dónde |
|---|---|---|---|
| **UPS 800VA+** | Mantener Starlink + router en cortes (60 min) | COP 250-450K | Ktronix, Alkosto, MercadoLibre |
| **Pole mount Starlink** | Si el techo del galpón no es estable | COP 100-200K | Tienda Starlink Colombia o adaptar |
| **Cámara IP de prueba** (1) | Validar setup el primer día | COP 180-280K | Reolink E1 Pro o TP-Link Tapo C320WS |
| **Cables Ethernet largos** | Conectar router a galpón si está separado | COP 30-50K | Cualquier ferretería técnica |
| **SIM celular backup** | Plan datos cuando Starlink falla | COP 30-60K/mes | Claro o Movistar |

---

## 🌐 Red final propuesta (Fase A)

```
   ☁️ Internet (Starlink LEO)
        │
   📡 Antena Starlink (techo o poste alto)
        │
   🔌 Router Gen 3 Starlink (WiFi 6)
        │
        ├── 📷 Cámara IP de prueba (Tailscale para acceso Miami)
        ├── 📱 Celular papá (WiFi)
        ├── 📱 Celular Guyo (WiFi)
        ├── 🔋 UPS 800VA (alimenta antena + router)
        └── (Fase B: switch + mesh + sensores + más cámaras)
```

---

## 🔮 Setup IoT Fase B (post-arranque del galpón)

- **Router router/mesh adicional**: TP-Link Deco X50 o Ubiquiti UniFi (~COP 700K-1.2M)
- **Switch PoE**: para cámaras que se alimentan por el cable Ethernet (~COP 300K)
- **4-6 cámaras CCTV**: Reolink PoE o Hikvision (~COP 200K c/u)
- **Sensores temperatura/humedad**: Sonoff, Shelly, Aqara
- **Mini-PC para Tailscale + DVR**: Raspberry Pi 5 (~COP 400K) o cualquier viejo

---

## 📚 Fuentes verificadas

- **Oficiales Starlink:**
  - https://www.starlink.com/co (planes Colombia)
  - https://www.starlink.com/support (bypass mode, CGNAT)
  - https://www.starlink.com/map (cobertura)
- **Comparativas Colombia 2025-2026:**
  - https://www.enter.co/colombia/cuanto-cuesta-starlink-en-colombia-en-2026-...
  - https://selectra.com.co/empresas/starlink/internet
  - https://www.infobae.com/tecno/2025/09/11/starlink-presenta-planes-mas-baratos-para-colombia
  - https://conexionsatelital.net/planes-de-starlink-en-colombia/
  - https://www.cronista.com/colombia/actualidad-co/starlink-llega-al-pais-con-prueba-de-30-dias
- **Stock + precios:**
  - https://www.falabella.com.co/falabella-co/brand/STARLINK
  - https://www.falabella.com.co/falabella-co/product/73053329 (Kit Estándar V4)
  - https://www.falabella.com.co/falabella-co/product/72999285/ (Kit Mini)
- **CGNAT + bypass:**
  - https://kb.protectli.com/kb/starlink-bypass-mode-bridge-mode/
- **Aduana (no aplica, pero documentado):**
  - https://www.dian.gov.co/Viajeros-y-Servicios-aduaneros/Paginas/Modalidad-viajeros.aspx

---

## ✅ Acciones para HOY

1. **Juan** · Verificar cobertura en https://starlink.com/map con coords de la finca (5 min)
2. **Juan** · Pedir kit en https://www.falabella.com.co/falabella-co/product/73053329 → envío Bogotá → datos de papá (15 min)
3. **Juan** · En paralelo, mandar a papá comprar UPS 800VA + 1 cámara IP de prueba (lista corta arriba)
4. **Juan** · Crear cuenta starlink.com (no activar plan todavía, solo registrar el correo)
5. **Juan** · Instalar Tailscale en celular y laptop para tener listo el acceso remoto
