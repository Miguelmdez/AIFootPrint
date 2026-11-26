# Agenda de contactos (Vue) – E4b

SPA hecha con **Vue 2.6.10** para gestionar una agenda de contactos: mostrar, crear y borrar contactos (nombre, email y teléfono).

**Web publicada:** https://agenda-iw-bi-05.netlify.app/

Grupo **IW-BI-05**: Eneko, Jürgen, Miguel, Andoni y Cesar.

## Cómo ejecutarla

No necesita instalación ni servidor: basta con abrir `index.html` en el navegador. Vue va incluido en `js/vue.js`.

## Estructura

```
agendaVue/
├── index.html        Página única: plantilla de Vue, metadatos y datos estructurados
├── css/estilos.css   Estilos (incluye diseño adaptable a móvil)
├── js/vue.js         Librería Vue 2.6.10
├── js/app.js         Lógica de la agenda (instancia de Vue)
└── img/og-image.png  Imagen de vista previa para redes sociales (1200×630)
```

## Funcionalidades

- Listado de contactos con contador y enlaces `mailto:` y `tel:`.
- Alta de contactos con validación de nombre, email y teléfono.
- Borrado con confirmación.
- Persistencia en `localStorage`: los contactos se conservan al recargar.

## Opción 1: web semántica y capacidades sociales

| Técnica | Dónde | Vocabulario |
|---|---|---|
| Microdata | Cada contacto de la lista | `schema.org/Person` |
| RDFa | Pie de página (grupo autor) | `schema.org/Organization` + `Person` |
| JSON-LD | `<head>`: la aplicación y la lista de contactos (se actualiza al añadir o borrar) | `WebApplication`, `ItemList` |
| Open Graph y Twitter Card | Metaetiquetas del `<head>` | Tarjeta de vista previa al compartir |
| Botones de compartir | Sección «Comparte la agenda» | Enlaces a Twitter/X y Facebook |

## Validación

- HTML: [validador del W3C](https://validator.w3.org/): sin errores.
- CSS: [validador CSS del W3C](https://jigsaw.w3.org/css-validator/): sin errores.
- Datos estructurados: [validator.schema.org](https://validator.schema.org/): sin errores.

> Las etiquetas de cierre `</body>` y `</html>` se omiten a propósito (son opcionales en HTML5): Netlify añade al final del archivo el script de su insignia, y así la página publicada también pasa la validación.
