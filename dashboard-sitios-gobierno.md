# DASHBOARD DE OPACIDAD — Gobierno del Estado de Morelos

**Expediente editorial — 45 Digital Noticias**
**Inicio del expediente:** 2026-05-19
**Última actualización:** 2026-05-19
**Estado:** abierto, en construcción

> **Tesis editorial del expediente.** Las autoridades responden a cada cuestionamiento con la misma fórmula: *"pidan la información por transparencia"*. Pero la Ley General de Transparencia (Art. 65) obliga a publicarla **proactivamente**, sin necesidad de solicitud. Este dashboard documenta, sitio por sitio, dónde se incumple esa obligación en Morelos — y cómo el desmantelamiento del IMIPE en 2026 convirtió la opacidad en política de Estado.

---

## 1. Bitácora de verificación

| # | Fecha | Sitios revisados | Hallazgos clave |
|---|---|---|---|
| 001 | 2026-05-19 | 29 dominios y subdominios estatales | 11 funcionan, 7 cascarones, 7 caídos, 2 inseguros, 1 extinto, 1 inexistente (18 con defunción operativa). Confirmado: el órgano sustituto del IMIPE *no tiene portal* a 13 días de su decreto. |

---

## 2. Inventario técnico — estado de sitios oficiales

### 2.1. Sitios funcionales (cargan y muestran contenido sustantivo)

| Institución | URL probada | Estado | Tipo de sujeto obligado | Observaciones |
|---|---|---|---|---|
| Portal principal del Estado | https://www.morelos.gob.mx | ✅ OK | Poder Ejecutivo | Funcional |
| Congreso del Estado | https://www.congresomorelos.gob.mx | ✅ OK | Poder Legislativo | Funcional |
| ESAF (Auditoría Superior) | https://esaf-morelos.gob.mx | ✅ OK | Órgano técnico del Legislativo | Funcional |
| Tribunal Superior de Justicia | https://tsjmorelos.gob.mx | ✅ OK | Poder Judicial | Funcional |
| Tribunal de Justicia Administrativa | https://tjamorelos.gob.mx | ✅ OK | Órgano jurisdiccional | Funcional |
| Fiscalía General del Estado | https://www.fiscaliamorelos.gob.mx | ✅ OK | Órgano constitucional autónomo | Funcional (sólo con dominio independiente, no con subdominios `*.morelos.gob.mx`) |
| Denuncia Digital de la Fiscalía | https://denuncia.fiscaliamorelos.gob.mx | ✅ OK | Sistema de la Fiscalía | Funcional |
| Periódico Oficial *Tierra y Libertad* (listado) | https://periodico.morelos.gob.mx/ejemplares | ✅ OK | Publicaciones oficiales | Listado de ejemplares carga; la home no (ver 2.2) |
| IMPEPAC | https://impepac.mx → https://jornada.impepac.mx | ✅ OK | Órgano autónomo electoral | Carga vía redirect 302 hacia un subdominio "jornada", patrón inusual |
| Avisos de Privacidad | https://avisosprivacidad.morelos.gob.mx | ✅ Carga | Anexo Contraloría | Funcional pero sin información sustantiva |

### 2.2. Sitios con carga parcial, contenido nulo o decorativo

| Institución | URL probada | Estado | Lo que muestra | Implicación |
|---|---|---|---|---|
| **Transparencia Morelos (portal original)** | https://transparenciamorelos.mx | ⚠️ Carga | Único mensaje: **"Sitio No Vigente"** | Sin archivo migrado, sin redirección a sucesor — la memoria de transparencia se evapora |
| **Portal local de Transparencia** | https://transparencia.morelos.gob.mx | ⚠️ Carga | Página de **login** + eslogan *"Más allá de la obligación, hacia una transparencia proactiva"* | Vitrina vacía. No hay obligaciones de Art. 65 publicadas para el ciudadano común |
| **IMIPE (extinto)** | https://imipe.org.mx | ⚠️ Carga | Contenido del antiguo instituto + banner *aviso_cierre_imipe.jpg* | Información congelada; ningún indicador de durabilidad |
| **Compras Morelos / Contratos** | https://compras.morelos.gob.mx | 🔒 Bloquea | HTTP 403 Forbidden / 429 Too Many Requests intermitentes | Bloqueo activo a consultas externas — donde deben estar contratos y licitaciones |
| **CDH Morelos** | https://cdhmorelos.org.mx | ⚠️ Carga | Sólo cabecera "CDHMORELOS", sin contenido | Sitio cascarón |
| **Periódico Oficial (home)** | https://periodico.morelos.gob.mx | ⚠️ Carga | *"Cargando información, por favor espere"* indefinido | Home rota; sólo es navegable por URLs internas conocidas |

### 2.3. Sitios oficiales que NO existen o están caídos

| Institución | URL esperada | Error | Implicación |
|---|---|---|---|
| **Secretaría Anticorrupción y Buen Gobierno** | anticorrupcion.morelos.gob.mx | ECONNREFUSED | Sin subdominio propio. Sólo ruta dentro del portal del Estado |
| **"Transparencia para el Pueblo de Morelos"** (sustituto del IMIPE, decreto 2026-05-06) | sin URL pública conocida | n/d | **Sin portal a 13 días de su creación** |
| **Fiscalía Especializada en Combate a la Corrupción** | fiscaliaanticorrupcion.morelos.gob.mx | ECONNREFUSED | Servidor sin respuesta — referenciado por buscadores |
| Fiscalía General (variantes oficiales) | fiscalia.morelos.gob.mx, fge.morelos.gob.mx | ECONNREFUSED | Variantes inválidas; sólo opera bajo dominio independiente |
| Sistema de Administración Tributaria estatal | sat.morelos.gob.mx | ECONNREFUSED | Caído |
| CEAGUA — Comisión Estatal del Agua | ceagua.morelos.gob.mx | ECONNREFUSED | Caído |
| Secretaría de Salud (subdominio) | salud.morelos.gob.mx | ECONNREFUSED | Caído como subdominio independiente |
| Portal de Servicios | servicios.morelos.gob.mx | ECONNREFUSED | Caído |
| IEBEM — Educación Básica | iebem.edu.mx | SSL inválido | Navegadores marcan inseguro |
| **"Transparencia para el Pueblo"** (homólogo federal) | transparencia.gob.mx | SSL inválido | El sustituto del INAI a nivel nacional tampoco tiene certificado válido |

---

## 3. Mapa de incumplimiento — Art. 65 LGTAIP

> La Ley General de Transparencia y Acceso a la Información Pública obliga a **publicar proactivamente** las siguientes fracciones. No hace falta solicitud: deben estar disponibles, en formato abierto, en el portal del sujeto obligado y en la Plataforma Nacional de Transparencia.

| Fracción Art. 65 | Obligación | Dónde debería estar | Estado al 2026-05-19 |
|---|---|---|---|
| **XXI** | Gastos en comunicación social y publicidad oficial | Portal de transparencia local + portal del sujeto obligado | ⚠️ No localizable en portal local (es página de login) |
| **XXV** | Concesiones, contratos, convenios, permisos | compras.morelos.gob.mx | 🔒 Bloqueado |
| **XXVI** | Procedimientos de contrataciones (adjudicaciones, invitaciones, licitaciones) | compras.morelos.gob.mx | 🔒 Bloqueado |
| **XXX** | Padrón de proveedores y contratistas | compras.morelos.gob.mx | 🔒 Bloqueado |
| Federal complementario | Programa Anual de Comunicación Social 2025 (Ley General de Comunicación Social, Art. 9) | Coordinación General de Comunicación Social del Estado | ❓ No publicado en portal visible |
| Federal complementario | Padrón Nacional de Medios Impresos (PNMI) — verificación de OEM Morelos | pnmi.segob.gob.mx | ⏳ Pendiente de verificar (federal, sí carga) |

**Lectura editorial.** Cuatro de las fracciones del Art. 65 directamente relacionadas con la pauta publicitaria oficial están bloqueadas, ausentes o vacías en los portales del Estado de Morelos. La obligación legal no se traduce en información consultable.

---

## 4. Cronología institucional 2025-2026

| Fecha | Hecho | Fuente |
|---|---|---|
| 2025-03 | DOF publica reforma federal que ordena a Congresos locales extinguir órganos garantes de transparencia en 90 días | DOF / Verificado |
| 2025-12-13 | Congreso de Morelos aprueba extinción del IMIPE (14 a favor, 4 en contra) y crea la Secretaría Anticorrupción y Buen Gobierno | La Jornada, Proceso |
| 2026-01-27 | Decreto de extinción del IMIPE publicado en *Tierra y Libertad* | Periódico Oficial |
| 2026-05-06 | Decreto que crea "Transparencia para el Pueblo de Morelos" como dependencia de la Secretaría Anticorrupción | Diario de Morelos, La Unión |
| 2026-05-13 | Crítica especializada (Cauce Legal, La Unión): pérdida de autonomía, presupuesto **27 → 5 mdp** (–81 %), titular sin requisito acreditado | Revista Cauce Legal |
| 2026-05-18 | Trascendido nacional sin firma señala supuesta investigación de EU a la gobernadora González Saravia | Infobae, Quadratín, TV Azteca, El Sol de Cuernavaca |
| 2026-05-18 | Gobierno de Morelos desmiente el trascendido el mismo día | Comunicado oficial |
| 2026-05-19 | **Verificación técnica del expediente**: el portal sustituto no existe; 10 dominios oficiales caídos; el portal local de transparencia es sólo un login | Este dashboard |

---

## 5. Datos críticos del rediseño institucional 2026

| Variable | IMIPE (hasta enero 2026) | "Transparencia para el Pueblo" (desde mayo 2026) | Cambio |
|---|---|---|---|
| Naturaleza jurídica | Órgano constitucional autónomo | Dependencia de la Secretaría Anticorrupción del Ejecutivo | Pierde autonomía constitucional |
| Patrimonio | Propio | Asignado por el Ejecutivo | Pierde patrimonio propio |
| Toma de decisión sobre reservas | Colegiada (5 comisionados) | Unipersonal (titular única) | De 5 a 1 |
| Presupuesto anual | 27 mdp | 5 mdp | –81 % |
| Portal web | imipe.org.mx (vigente como archivo) | Sin portal | Sin sustituto operativo |
| Titular | Comisionados con requisitos de experiencia comprobables | Alejandra Fernández Hernández — **señalada por carecer del requisito legal** de experiencia comprobable | Pérdida de perfil técnico |

---

## 6. Pendientes — qué falta documentar

- [ ] Solicitar formalmente, vía PNT, a la Coordinación General de Comunicación Social: Programa Anual 2025, padrón de proveedores, contratos firmados con monto y vigencia, criterios de adjudicación.
- [ ] Solicitar lo mismo a la Oficina de la Gubernatura (es la unidad con el gasto más alto según la infografía de Morelos Rinde Cuentas 2025).
- [ ] Recuperar la **Cuenta Pública 2024** publicada por ESAF y extraer partidas 3611 (Difusión por radio, TV y otros) y 3621 (Difusión de mensajes comerciales).
- [ ] Solicitar a Morelos Rinde Cuentas (`contacto@morelosrindecuentas.org.mx`, 777 106 00 89) el dataset detrás de la infografía 2025.
- [ ] Verificar si OEM (El Sol de Cuernavaca, El Sol de Cuautla, El Sol de México) está en el Padrón Nacional de Medios Impresos.
- [ ] Capturar pantallas de evidencia técnica de cada sitio caído (con marca temporal) para anexo probatorio de columna.
- [ ] Probar subdominios adicionales no verificados (DIF Morelos, Secretaría de Cultura, Secretaría de Movilidad, Coordinación de Comunicación Social, organismos descentralizados restantes).
- [ ] Documentar el patrón de redirección `impepac.mx → jornada.impepac.mx` (es atípico para un órgano electoral).
- [ ] Hacer ping y `whois` a los dominios caídos para confirmar si están **desregistrados** o sólo **sin servidor**.

---

## 7. Convenciones del expediente

- ✅ — Funcional / Confirmado
- ⚠️ — Parcial / Vacío / Decorativo
- ❌ — Caído / No existe
- 🔒 — Bloqueado o restringido
- ❓ — No confirmado, pendiente de verificación
- ⏳ — En proceso

## 8. Fuentes documentales

- [Congreso de Morelos extingue el IMIPE — La Jornada](https://www.jornada.com.mx/noticia/2025/12/13/estados/congreso-de-morelos-extingue-el-imipe-y-crea-la-secretaria-anticorrupcion)
- [Congreso extingue organismo de transparencia — Proceso](https://www.proceso.com.mx/nacional/estados/2025/12/14/congreso-de-morelos-extingue-el-organismo-de-transparencia-crea-secretaria-anticorrupcion-364669.html)
- [Extinguen el IMIPE — La Jornada Morelos](https://www.lajornadamorelos.mx/seguridad-y-justicia/extinguen-el-imipe-y-crean-secretaria-anticorrupcion-y-de-buen-gobierno/)
- [La extinción del IMIPE: retroceso democrático — Cauce Legal](https://revistacaucelegal.com/2025/12/15/la-extincion-del-imipe-retroceso-democratico/)
- [El nuevo IMIPE y su "autonomía" — Cauce Legal, 2026-05-13](https://revistacaucelegal.com/2026/05/13/el-nuevo-imipe-y-su-autonomia/)
- [El nuevo IMIPE y su 'autonomía' — La Unión de Morelos](https://www.launion.com.mx/opinion/estrategias/noticias/293469-el-nuevo-imipe-y-su-autonomia.html)
- [Nace "Transparencia para el Pueblo" — Diario de Morelos](https://www.diariodemorelos.com/noticias/nace-transparencia-pueblo-nuevo-guardian-cuentas-claras-en-morelos)
- [Crean órgano de transparencia para municipios — La Unión Morelos](https://www.launion.com.mx/morelos/politica/noticias/293233-crean-organo-de-transparencia-para-municipios-y-dependencias-estatales.html)
- [Ahorrará Morelos 22 millones — Punto por Punto](https://puntoporpuntotv.com/ahorrara-morelos-22-millones-de-pesos-con-el-nuevo-instituto-de-transparencia/)
- [Nuevo organismo vigilará 120 oficinas — Infórmate y más](https://www.informateymas.com/gobierno-morelos/nuevo-organismo-vigilara-transparencia-en-120-oficinas-de-morelos/)
- [Transparencia para el Pueblo: el cuestionable órgano que sustituye al INAI — Verificado](https://verificado.com.mx/transparencia-para-el-pueblo-sustituye-al-inai/)
- [Gobierno de Morelos niega medidas migratorias — Infobae](https://www.infobae.com/mexico/2026/05/18/gobierno-de-morelos-niega-que-hayan-medidas-migratorias-contra-la-gobernadora-gonzalez-saravia/)
- [Morelos Rinde Cuentas](https://morelosrindecuentas.org.mx/)
- [Plataforma Nacional de Transparencia](https://www.plataformadetransparencia.org.mx/)
- [Padrón Nacional de Medios Impresos (SEGOB)](https://pnmi.segob.gob.mx/reporte)
