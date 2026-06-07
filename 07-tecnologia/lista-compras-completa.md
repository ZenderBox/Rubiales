# Lista de compras completa · IoT 2 puntos (casa + galpón)

> **Objetivo:** dejar TODO funcionando antes de la obra. Cuando arranque el galpón, el encargado solo instala lo que ya está en la finca.
>
> **Logística:** Juan tiene empresa de logística propia US ↔ CO → traer todo desde Miami sin restricción de viaje.
>
> **Compras:** TODAS en Amazon US con cuenta business · Tax Exemption activa → -7% sales tax (~$155 USD = ~$620K COP de ahorro adicional).
>
> **Fecha:** 2026-06-07

---

## 🧭 Plan logístico

```
🛫 ETAPA 1 (Juan trae el viernes en MALETA · ≤USD 2.000 DIAN)
   → Lo que se instala el viernes en la casa principal
   → Permite arrancar internet + 1 cámara + Tailscale

📦 ETAPA 2 (envío por empresa logística Juan · 5-10 días)
   → Cámaras del galpón + NVR + AP futuros
   → Llega antes de que arranque la obra del galpón
   → El encargado solo instala
```

---

## 🛫 Etapa 1 · Maleta (este viernes 12-jun)

### En Miami (Juan compra esta semana en Amazon Prime)

| Item | Modelo | Cantidad | USD c/u | Total |
|---|---|---|---|---|
| Raspberry Pi 5 kit | RPi 5 8GB + microSD 128GB + case + power | 1 | $130 | $130 |
| Ubiquiti LiteBeam 5AC Gen2 (enlace 500m) | LBE-5AC-Gen2-US | 2 | $99 | $198 |
| Ubiquiti ETH-SP-G2 (surge protector) | ETH-SP-G2 | 2 | $25 | $50 |
| Cámara IP outdoor | Reolink Argus 4 Pro (battery+solar) | 1 | $150 | $150 |
| Cámara IP indoor (test) | Reolink E1 Pro | 1 | $45 | $45 |
| Cable CAT6 outdoor UV | 30m | 1 | $45 | $45 |
| Adaptadores | PoE injectors + RJ45 + crimpeadora | 1 | $40 | $40 |
| **TOTAL maleta** | | | | **~$658** |

→ Cabe en DIAN sobrado (límite $2.000).

### En Colombia (papá pide hoy, recibe lunes-martes)

| Item | Dónde | COP |
|---|---|---|
| Kit Estándar V4 Starlink | Falabella o Homecenter | $1.349.900 |
| UPS APC Back-UPS Pro 1500VA | Ktronix/Alkosto | $480-600K |
| SIM Claro o Movistar 10GB/mes | Punto Claro/Movistar | $40-60K/mes |
| **TOTAL Colombia** | | **~$1.9M COP** |

---

## 📦 Etapa 2 · Envío logística (antes del arranque del galpón)

### Cámaras CCTV (4 galpón + 2 casa principal + 1 perímetro)

| Item | Modelo | Cantidad | USD c/u | Total |
|---|---|---|---|---|
| Cámara PoE outdoor 5MP | Reolink RLC-510A o RLC-810A | 6 (4 galpón + 2 casa) | $60 | $360 |
| Cámara solar perimetral | Reolink Argus 4 Pro adicional | 1 | $150 | $150 |
| NVR + switch PoE 8 puertos | Reolink RLN8-410 (con 2TB HDD) | 1 | $260 | $260 |
| **Subtotal cámaras** | | | | **$770** |

### Red / WiFi para 2 puntos

| Item | Modelo | Cantidad | USD c/u | Total |
|---|---|---|---|---|
| Access Point WiFi outdoor | TP-Link EAP235-Wall o EAP610-Outdoor | 2 (1 casa + 1 galpón) | $80 | $160 |
| Switch PoE adicional | TP-Link TL-SG1008P (8 puertos PoE) | 1 | $70 | $70 |
| UPS adicional galpón | APC Back-UPS 1500VA | 1 | $200 | $200 |
| **Subtotal red** | | | | **$430** |

### Sensores IoT galpón

| Item | Modelo | Cantidad | USD c/u | Total |
|---|---|---|---|---|
| Sensor temperatura/humedad WiFi | Shelly H&T Gen3 | 3 (zonas distintas galpón) | $25 | $75 |
| Enchufe inteligente WiFi | Shelly Plug S | 2 (control ventiladores) | $20 | $40 |
| Sensor nivel agua pozo | Shelly Flood o WiFi water | 1 | $40 | $40 |
| **Subtotal sensores** | | | | **$155** |

### Cables y accesorios

| Item | Cantidad | USD |
|---|---|---|
| Cable CAT6 outdoor 100m UV | 1 | $80 |
| Soportes/monturas cámaras | 8 | $60 |
| Conectores RJ45 outdoor + tools | kit | $30 |
| Tarjetas microSD 64GB (cámaras Reolink) | 4 | $40 |
| **Subtotal accesorios** | | **$210** |

### Total Etapa 2 (envío logística)

| Categoría | USD |
|---|---|
| Cámaras (7 + NVR) | $770 |
| Red + WiFi + UPS galpón | $430 |
| Sensores IoT | $155 |
| Cables y accesorios | $210 |
| **TOTAL Miami Etapa 2** | **~$1.565** |

---

## 💰 Costo total proyecto completo

| Etapa | Origen | Costo |
|---|---|---|
| Etapa 1 maleta · Miami | USD | ~$658 (~$2.6M COP) |
| Etapa 1 Colombia · Falabella/Ktronix | COP | ~$1.9M |
| Etapa 2 logística · Miami | USD | ~$1.565 (~$6.2M COP) |
| **Hardware total** | | **~$10.7M COP** (~USD 2.680) |
| Plan Starlink Lite × 12 meses | | ~$1.9M COP |
| SIM backup × 12 meses | | ~$600K COP |
| **TOTAL año 1 completo** | | **~$13.2M COP** (~USD 3.300) |

→ **Ahorro vs comprar todo retail Colombia: ~$5-7M COP** (40-50%).

---

## 📍 Distribución final en la finca

### 📦 Casa principal (instalar viernes)
- Antena Starlink al techo
- Router Gen 3 Starlink (interno)
- Raspberry Pi 5 conectado al router (Tailscale gateway)
- UPS APC 1500VA (sostiene Starlink + router 1-2h)
- **Cámaras casa:**
  - 1× Reolink E1 Pro indoor (sala/comedor)
  - 1× Reolink Argus 4 Pro solar (perímetro casa, exterior)
  - 2× Reolink RLC-510A PoE (esquinas casa, conectadas al switch PoE del NVR) — instalar después con el NVR
- 1× Ubiquiti LiteBeam #1 (provisional poste, apuntando a donde irá el galpón)
- 1× Access Point WiFi outdoor TP-Link (futuro · cubre patio)

### 📦 Galpón (futuro · todo listo en cajas)
- 1× Ubiquiti LiteBeam #2 (transmisor enlace 500m, instalar en el techo galpón cuando esté hecho)
- 1× Reolink NVR + switch PoE 8 puertos (en sala del galpón o casa del cuidador)
- 4× Reolink RLC-510A PoE (esquinas galpón + entrada + cara productiva)
- 1× Reolink Argus 4 Pro solar (perímetro futuro · cultivos plátano)
- 1× Access Point WiFi outdoor TP-Link (cubre galpón + casa cuidador)
- 1× UPS APC 1500VA (sostiene NVR + switch + router)
- 3× Shelly H&T (sensor temperatura/humedad)
- 2× Shelly Plug S (control eléctrico ventiladores/luces)
- 1× Shelly Flood (sensor pozo de agua)

---

## 🛠️ Instalación cuando arranque la obra

El encargado de la obra del galpón solo necesita:

1. **Tubo galvanizado + mástil** para el LiteBeam del galpón (lo compra él · ~$100K COP)
2. **Pasar canaleta** desde el rack del NVR a las 4 ubicaciones de cámaras PoE
3. **Apuntar el LiteBeam** al de la casa principal (Juan asiste por video desde Miami)
4. **Conectar todo** a la red eléctrica + UPS
5. **Tomar fotos** del cableado final para futuro mantenimiento

→ Todo el conocimiento técnico de configuración se hace remoto desde Miami via Tailscale.

---

## ✅ Acciones para HOY

1. **Juan** · Pedir lista Etapa 1 maleta en Amazon Prime (~$658) → llega Miami 1-2 días
2. **Juan** · Pedir lista Etapa 2 logística para iniciar envío (~$1.565) → llega Colombia 5-10 días
3. **Juan** · Pasar lista Colombia a papá por WhatsApp para que pida Falabella + Ktronix
4. **Juan** · Confirmar dirección de envío para empresa logística
5. **Papá** · Ir a Claro/Movistar a comprar la SIM con plan datos
