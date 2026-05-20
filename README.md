# El Cementerio de la Transparencia — Morelos 2026

**Expediente editorial de 45 Digital Noticias.**
Auditoría visual e interactiva de los sitios oficiales del gobierno del estado de Morelos al **19 de mayo de 2026**.

---

## Qué es

Un inventario, sitio por sitio, de las páginas web del gobierno estatal de Morelos y del aparato federal de transparencia que las regula — documentando cuáles funcionan, cuáles son cáscaras decorativas, cuáles están caídas y cuáles nunca tuvieron portal.

El expediente parte de una observación simple: la Ley General de Transparencia y Acceso a la Información Pública obliga a publicar **48 fracciones de información de oficio**, sin necesidad de que nadie las pida. En la práctica, los portales donde esa información debería estar muestran un eslogan, una pantalla de login o un error de servidor.

## Quién es responsable

Documenta el período del primer año y medio de gobierno de **Margarita González Saravia** (toma de protesta: 1 de octubre de 2024), durante el cual se ejecutó el desmantelamiento local del órgano garante autónomo —el **IMIPE**— y su sustitución por una dependencia subordinada al Ejecutivo. El expediente se publica un día antes de la emisión del programa del **20 de mayo de 2026**.

## Cómo navegarlo

Abre [cementerio-transparencia.html](cementerio-transparencia.html) en cualquier navegador moderno. Es un archivo único, autocontenido, sin dependencias externas más allá de las fuentes de Google.

Siete secciones, accesibles desde el menú superior:

| Pestaña | Qué encontrarás |
|---|---|
| **Apertura** | Manifiesto editorial y marcador vivo con conteos en tiempo real |
| **Análisis** | La columna *"El timo de la transparencia"* (~950 palabras) |
| **Cementerio** | 16 lápidas clickeables — cada una con expediente, captura de evidencia y línea legal incumplida |
| **Tabla maestra** | Los 29 sitios auditados, con filtros por estado y buscador |
| **Comparativa** | IMIPE (autónomo) vs. "Transparencia para el Pueblo de Morelos" (subordinado) |
| **Cronología** | Quince meses del desmantelamiento, marzo 2025 → mayo 2026 |
| **Glosario** | LGTAIP, Art. 70, padrón de proveedores, adjudicación directa, etc., en lenguaje claro |
| **Fuentes** | Toda la evidencia documental — prensa, organismos, datos abiertos |

## Lo que contiene este repositorio

```
_expediente-opacidad-morelos/
├── README.md                       ← este archivo
├── LICENSE                         ← CC BY-NC 4.0
├── cementerio-transparencia.html   ← pieza principal, autocontenida
├── dashboard-sitios-gobierno.md    ← bitácora de trabajo (datos crudos, pendientes)
├── datos/
│   └── plan_apertura_TP.csv        ← evidencia primaria: el plan que Transparencia para el Pueblo
│                                      no cumplió (descargado de datos.gob.mx el 19 may 2026)
└── evidencia/
    ├── README.md                   ← cómo nombrar capturas
    ├── *.png                       ← 29 capturas con slug (las que el HTML lee automáticamente)
    └── raw/                        ← respaldo de las capturas originales con su URL completa
```

## Datos clave del expediente

- **29 sitios oficiales auditados.** 11 funcionan. 18 no le sirven al ciudadano (7 cascarones, 7 caídos, 2 inseguros, 1 extinto, 1 inexistente).
- **El nuevo órgano garante local, "Transparencia para el Pueblo de Morelos"**, no tiene portal funcional al día de la auditoría — el decreto que lo creó es del 6 de mayo de 2026.
- **El órgano garante federal homólogo** (también llamado "Transparencia para el Pueblo") opera con certificado de seguridad inválido; los navegadores marcan el sitio como inseguro.
- **El único dataset que publica el organismo federal en datos.gob.mx** es un Plan de Apertura — un papel donde se compromete a publicar nueve tipos de datasets durante 2026. Al 19 de mayo de 2026, fecha en que ese plan se vence por primera vez, ningún dataset prometido aparece publicado.

## Fuentes primarias

- [Plataforma Nacional de Transparencia](https://www.plataformadetransparencia.org.mx/)
- [Datos.gob.mx — Transparencia para el Pueblo](https://www.datos.gob.mx/organization/tp)
- [Artículo 19 — denuncia 99.6% de recursos desechados](https://articulo19.org/transparencia-para-el-pueblo-niega-el-derecho-de-acceso-a-la-informacion/)
- [Cauce Legal — La extinción del IMIPE: retroceso democrático](https://revistacaucelegal.com/2025/12/15/la-extincion-del-imipe-retroceso-democratico/)

## Cómo citar

> *Cementerio de la Transparencia — Morelos 2026*. 45 Digital Noticias.
> Disponible en GitHub. Última verificación: 19 de mayo de 2026.

## Licencia

[CC BY-NC 4.0](LICENSE) — Atribución, no comercial.
Puedes reproducir, citar y modificar este material, siempre con crédito a *45 Digital Noticias* y sin uso comercial.

## Contacto

Para correcciones, contraargumentos documentados o aportaciones de evidencia, abre un *Issue* en este repositorio o escribe al programa.

---

*45 Digital Noticias.*
