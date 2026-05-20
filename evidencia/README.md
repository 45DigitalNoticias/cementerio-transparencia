# Carpeta de evidencia — capturas de pantalla

Aquí van las capturas de los sitios oficiales documentados en el cementerio.

## Cómo nombrar los archivos

Cada lápida del cementerio busca su captura por **slug**. El nombre del archivo debe coincidir exactamente con el slug listado abajo, en formato `.png` o `.jpg`.

| Slug del archivo | Sitio | URL probada |
|---|---|---|
| `imipe.png` | IMIPE (extinto, archivo congelado) | imipe.org.mx |
| `transparencia-para-el-pueblo.png` | "Transparencia para el Pueblo" (sin portal) | n/d |
| `transparencia-morelos-gob.png` | Portal de Transparencia (login + slogan) | transparencia.morelos.gob.mx |
| `compras-morelos.png` | Compras Morelos (bloqueado 403/429) | compras.morelos.gob.mx |
| `transparenciamorelos-mx.png` | transparenciamorelos.mx ("Sitio No Vigente") | transparenciamorelos.mx |
| `anticorrupcion.png` | Secretaría Anticorrupción (sin subdominio) | anticorrupcion.morelos.gob.mx |
| `fiscalia-anticorrupcion.png` | Fiscalía Especializada Anticorrupción | fiscaliaanticorrupcion.morelos.gob.mx |
| `ceagua.png` | CEAGUA | ceagua.morelos.gob.mx |
| `salud-subdominio.png` | Secretaría de Salud (subdominio) | salud.morelos.gob.mx |
| `sat-morelos.png` | Sistema Tributario Estatal | sat.morelos.gob.mx |
| `servicios-morelos.png` | Portal de Servicios | servicios.morelos.gob.mx |
| `cdh-morelos.png` | Comisión de Derechos Humanos | cdhmorelos.org.mx |
| `periodico-home.png` | Periódico Oficial (home rota) | periodico.morelos.gob.mx |
| `iebem.png` | IEBEM (SSL inválido) | iebem.edu.mx |
| `avisos-privacidad.png` | Avisos de Privacidad GEM | avisosprivacidad.morelos.gob.mx |
| `transparencia-gob-mx.png` | "Transparencia para el Pueblo" federal | transparencia.gob.mx |

Para los sitios que no responden ("ECONNREFUSED"), basta una captura del navegador con su mensaje genérico de "No se puede acceder a este sitio" — esa imagen ES la evidencia.

## Recomendaciones de captura

- Resolución mínima 1280 px de ancho para que se vea bien en el modal.
- Capturar la URL completa visible en la barra del navegador.
- Si es posible, dejar fecha/hora visible (reloj del sistema en la barra de tareas, o un timestamp con marca de agua).
- Formato `.png` preferido (más limpio para texto); `.jpg` también funciona.

## Cómo lo lee la página

`cementerio-transparencia.html` busca automáticamente `evidencia/{slug}.png` para cada lápida cuando se abre su modal. Si la imagen no existe, muestra una nota que dice "Captura pendiente — añadir a `evidencia/{slug}.png`".
