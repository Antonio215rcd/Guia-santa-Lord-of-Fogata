# Calendario Medieval

Sitio estático para GitHub Pages. Incluye un calendario por años, un Pomodoro, una radio con muchas emisoras, una voz de bienvenida, un botón a la página de Hábitos y un **Pregón del día** con 20 noticias en tres pestañas (más una cuarta con tus newsletters en PDF), que se renueva solo gracias a un bot de GitHub Actions:

| Pestaña | Cuántas | Qué trae |
|---|---|---|
| 🌍 Geopolítica | 5 (4 en inglés y 1 en español) | Medios de la tradición liberal clásica y de la escuela austriaca |
| ⚖️ Política | 5 | Medios de ideología liberal clásica / derecha |
| 🗞️ Diarias | 10 | 2 de cada tema: guerra, Iglesia católica, política de EE. UU., política argentina y política peruana |

Por defecto el calendario cubre **2026–2030**. Más abajo se explica cómo ampliarlo.

---

## Índice

1. [Archivos del proyecto](#1-archivos-del-proyecto)
2. [Antes de empezar: 4 reglas para no atascarte](#2-antes-de-empezar-4-reglas-para-no-atascarte)
3. [Crear el repositorio](#3-crear-el-repositorio)
4. [Subir los archivos](#4-subir-los-archivos)
5. [Activar GitHub Pages](#5-activar-github-pages)
6. [Permisos del bot](#6-permisos-del-bot)
7. [Probar el bot a mano](#7-probar-el-bot-a-mano)
8. [Traducir las noticias (opcional)](#8-traducir-las-noticias-opcional)
9. [El Pregón del día: cómo funciona y cómo personalizarlo](#9-el-pregón-del-día-cómo-funciona-y-cómo-personalizarlo)
10. [Pomodoro, bienvenida, radio, Hábitos y tamaño en PC](#10-pomodoro-bienvenida-radio-hábitos-y-tamaño-en-pc)
11. [Añadir o quitar años del calendario](#11-añadir-o-quitar-años-del-calendario)
12. [Qué limpia el script](#12-qué-limpia-el-script)
13. [Cambiar la hora del bot (y por qué a veces se retrasa)](#13-cambiar-la-hora-del-bot-y-por-qué-a-veces-se-retrasa)
14. [Mantenimiento mensual (página de aviso)](#14-mantenimiento-mensual-página-de-aviso)
15. [Problemas frecuentes](#15-problemas-frecuentes)
16. [Newsletters en PDF (pestaña 📬)](#16-newsletters-en-pdf-pestaña-)

---

## 1. Archivos del proyecto

| Archivo | Para qué sirve | Dónde va en el repo |
|---|---|---|
| bienvenida.mp3 | La voz de bienvenida que suena al abrir la página (unos 2 segundos) | raíz, junto a index.html |
| mantenimiento.html | Página de aviso para los días de mantenimiento. **No va en el repo tal cual**: se guarda en tu PC y se sube temporalmente con el nombre `index.html` (sección 14) | tu PC |
| index.html | La página (calendario, Pomodoro, radio, oráculo, Hábitos y Pregón). Pesa unos 900 KB porque lleva las voces del Pomodoro incrustadas | raíz |
| news.json | Lo escribe el bot en cada ejecución | raíz |
| README.md | Estas instrucciones | raíz |
| noticias.py | Busca, limpia y elige las 20 noticias | carpeta scripts |
| noticias.yml | Lo ejecuta GitHub automáticamente | carpeta .github/workflows |
| newsletters.yml | Actualiza la lista de newsletters cuando subes un PDF | carpeta .github/workflows |
| newsletters/ | Carpeta donde subes los PDF de la newsletter (y `lista.json`, que escribe el bot) | raíz |

Estructura final que debe quedar en el repo:

```
index.html
bienvenida.mp3
news.json
README.md
scripts/noticias.py
.github/workflows/noticias.yml
.github/workflows/newsletters.yml
newsletters/lista.json
newsletters/.gitkeep
```

Ojo: en el zip los archivos ya vienen en esas carpetas, pero al subirlos a GitHub las dos carpetas hay que crearlas a mano (pasos 4b y 4c). No pongas copias sueltas de `noticias.py` o `noticias.yml` en la raíz: no hacen nada.

---

## 2. Antes de empezar: 4 reglas para no atascarte

Estos son los fallos más comunes. Léelos antes de subir nada.

**Regla 1. Escribe las rutas a mano. No las copies de ningún sitio.**
Si copias un nombre desde un texto con formato de código, puede llevarse una comilla invertida pegada. El resultado son carpetas y archivos llamados `` `scripts `` o `` noticias.yml` ``, que GitHub no reconoce. Escribe siempre el nombre con el teclado.

**Regla 2. Comprueba que el archivo pegado esté completo.**
Al copiar y pegar un archivo largo, a veces se corta. Después de guardar, abre el archivo y mira el contador de líneas que aparece arriba:

| Archivo | Líneas que debe tener |
|---|---|
| scripts/noticias.py | **286** |
| .github/workflows/noticias.yml | **35** |
| .github/workflows/newsletters.yml | **41** |

Si `noticias.py` muestra bastantes menos líneas, está cortado y el bot fallará a los pocos segundos con "exit code 1". Pégalo de nuevo, entero.

**Regla 3. La carpeta .github no se puede subir con "Upload files".**
GitHub ignora las carpetas que empiezan por punto al subir archivos. Hay que crear ese archivo a mano (paso 4c).

**Regla 4. GitHub no descomprime zips.**
Sube los archivos sueltos, no el zip.

---

## 3. Crear el repositorio

1. Entra en github.com e inicia sesión.
2. Pulsa **+ → New repository**.
3. Ponle un nombre (por ejemplo `calendario-medieval`), déjalo en **Public** y pulsa **Create repository**.

---

## 4. Subir los archivos

### 4a. Archivos de la raíz (subida normal)

1. En el repo, pulsa **Add file → Upload files**.
2. Sube `index.html`, `bienvenida.mp3`, `news.json` y `README.md`.
3. Pulsa **Commit changes**.

### 4b. El script (se crea a mano)

1. Pulsa **Add file → Create new file**.
2. En el nombre escribe **con el teclado**: `scripts/noticias.py`
   (al escribir la `/` se crea la carpeta sola).
3. Abre el archivo `noticias.py`, selecciona todo su contenido, cópialo y pégalo en el editor.
4. Pulsa **Commit changes**.
5. Abre el archivo y comprueba que ponga **286 lines** (regla 2).

### 4c. El workflow (se crea a mano)

1. Pulsa **Add file → Create new file**.
2. En el nombre escribe **con el teclado**: `.github/workflows/noticias.yml`
3. Abre el archivo `noticias.yml`, copia todo su contenido y pégalo en el editor.
4. Pulsa **Commit changes**.
5. Abre el archivo y comprueba que ponga **35 lines** (regla 2).

### Comprobación

En la pantalla principal del repo deben verse las carpetas `.github` y `scripts`, sin ningún símbolo extra delante. Si ves `` `scripts `` o `` `.github ``, tienen la comilla: ver el paso de abajo.

### Cómo arreglar un nombre con comilla

1. Abre el archivo con el nombre mal escrito y pulsa el lápiz (**Edit**).
2. En la ruta de arriba, borra todo el nombre y escríbelo a mano bien.
3. Pulsa **Commit changes**. GitHub mueve el archivo solo y la carpeta mala desaparece.

> Si usas un ordenador con Git, puedes subir todo de una vez con `git push` desde la carpeta del proyecto. Ahí sí se respeta `.github`.

---

## 5. Activar GitHub Pages

1. Ve a **Settings → Pages**.
2. En **Source** elige **Deploy from a branch**.
3. Selecciona la rama `main` y la carpeta `/ (root)`. Pulsa **Save**.
4. En uno o dos minutos la página estará en:
   `https://TU-USUARIO.github.io/NOMBRE-DEL-REPO/`

Cada vez que cambies un archivo, GitHub vuelve a publicar la página solo. Lo verás en **Actions** como "pages build and deployment".

---

## 6. Permisos del bot

1. Ve a **Settings → Actions → General**.
2. En **Actions permissions**, comprueba que esté marcado **Allow all actions and reusable workflows**.
3. Baja hasta **Workflow permissions** y marca **Read and write permissions**.
4. Pulsa **Save**.

Sin el permiso de escritura, el bot genera las noticias pero falla al guardarlas (error 403 en "Guardar cambios").

---

## 7. Probar el bot a mano

1. Ve a la pestaña **Actions**.
2. Si aparece un botón verde "I understand my workflows, go ahead and enable them", púlsalo.
3. En el menú de la izquierda, debajo de **All workflows**, debe aparecer **Noticias diarias**. Púlsalo.
4. Pulsa **Run workflow → Run workflow**.
5. Recarga a los 10 o 15 segundos. Verás una ejecución con círculo amarillo (en marcha).
6. Cuando termine:
   - **Verde**: todo bien. Abre `news.json` y verás un commit nuevo de `noticias-bot` con el mensaje "Noticias del día".
   - **Rojo**: entra en la ejecución, pulsa **actualizar** y mira qué paso tiene la ✗ roja.

Al terminar, abre el paso **Generar news.json** y mira el log: cada fuente dice `OK` o `ERR`, y la última línea resume el resultado, por ejemplo:

```
Listo: 5 geopolítica, 5 política, 10 diarias.
```

Es normal que alguna fuente salga con `ERR` (hay páginas que bloquean a los bots). El script prueba la siguiente y, si siguen faltando noticias, usa Google News de respaldo. Si falla a los pocos segundos, casi seguro `noticias.py` está cortado (regla 2).

El aviso amarillo "Node.js 20 is deprecated" es solo una advertencia de GitHub. Se puede ignorar.

**Importante:** el `news.json` que viene en el zip es de antes de las pestañas nuevas. Hasta la primera ejecución del bot, "Política" y "Diarias" mostrarán "Esta sección se llena con la próxima actualización automática". Es normal.

A partir de ahí el bot corre solo, a las horas que indique el `cron` (por defecto, cada 4 horas, en el minuto 11 UTC). Puede retrasarse o saltarse alguna ejecución; ver la sección 13.

---

## 8. Traducir las noticias (opcional)

Por defecto, las notas en inglés se quedan en inglés. Para que se traduzcan al español:

1. Ve a **Settings → Secrets and variables → Actions → New repository secret**.
2. Nombre: `ANTHROPIC_API_KEY`
3. Valor: tu clave de API de Anthropic.
4. Pulsa **Add secret**.

Solo se traducen las noticias que vienen en inglés; las que ya están en español se dejan como están. Las traducidas llevan la etiqueta "traducido" en la tarjeta. Si la traducción falla en alguna ejecución, esas noticias quedan en inglés y el bot sigue adelante.

Si no configuras la clave, todo funciona igual.

---

## 9. El Pregón del día: cómo funciona y cómo personalizarlo

### En la página

Pulsa **📰 Tablón**. Verás cuatro pestañas con el número de elementos de cada una (la cuarta, **📬 Newsletter**, es la de tus PDF: sección 16). En **Diarias** las tarjetas aparecen agrupadas por tema (⚔️ Guerra, ⛪ Iglesia católica, 🇺🇸 Política de EE. UU., 🇦🇷 Política argentina, 🇵🇪 Política peruana).

Son medios con una línea editorial propia, no cobertura neutral: conviene contrastar con otras fuentes.

### Caja del Servicio Meteorológico Nacional

Arriba de las pestañas hay una tarjeta fija con el enlace al Servicio Meteorológico Nacional de Argentina (https://www.smn.gob.ar/). No depende del bot ni de `news.json`: siempre está. Para cambiar el enlace o el texto, busca en `index.html` (Ctrl+F) `smn.gob.ar`.

### Caja de Newsletter (Instituto Juan de Mariana)

**Estado actual: oculta.** Para mostrarla, busca `MOSTRAR_IJM` en `index.html` (Ctrl+F) y cambia `false` por `true`.

(Esta tarjeta es solo el **enlace para suscribirse**. Los PDF que tú guardes aparecen aparte, en la pestaña **📬 Newsletter**: sección 16.)

Debajo de la caja del clima hay otra tarjeta fija, **📬 Newsletter · Instituto Juan de Mariana**, que abre la página oficial del Instituto en la zona de suscripción (`https://juandemariana.org/#newsletter_box`). La persona escribe su correo **allí**, en el formulario del propio Instituto, así que el correo no pasa por esta página: no se recibe, no se guarda y no hace falta ningún servidor. Si el enlace no te deja justo en el formulario, baja hasta el pie de la página del Instituto, donde dice "Suscríbete a nuestra newsletter". Para cambiar el texto o el enlace, busca `newsletter_box` en `index.html` (Ctrl+F).

Una casilla para escribir el correo directamente en esta página no se incluyó a propósito: haría falta enviar esos correos al formulario del Instituto (con su permiso y su código de formulario) o guardarlos aquí, con lo cual esta página pasaría a manejar datos personales de otras personas.

### De dónde salen las noticias

| Sección | Fuentes (se usa el primer enlace que responda) |
|---|---|
| Geopolítica | En inglés: Mises Institute, Antiwar.com, Libertarian Institute, Cato Institute, AIER, FEE, Reason, Ron Paul Institute. En español: Instituto Juan de Mariana, PanAm Post, El Cato, Libertad Digital |
| Política | National Review, The Daily Signal, Washington Examiner, Law & Liberty, City Journal, Cato Institute, Reason, FEE, Instituto Juan de Mariana, Libertad Digital |
| Guerra | BBC News, Al Jazeera, DW |
| Iglesia católica | Vatican News (español e inglés), Catholic News Agency, Aleteia |
| Política de EE. UU. | Fox News, NY Post, The Hill, NPR |
| Política argentina | Infobae, La Nación, Clarín, Perfil |
| Política peruana | Infobae Perú, El Comercio, RPP, La República |

Si una sección no llega a su cantidad con esas fuentes, el script completa con una búsqueda en Google News.

**La nota en español de Geopolítica:** el script reserva siempre un lugar para 1 nota en español entre las 5. Si ninguna fuente en español responde ese día, la busca en Google News en español. Las notas en español llevan la etiqueta "en español" y no se traducen.

### Cambiar cantidades o fuentes

Todo está en `scripts/noticias.py`. Para encontrar cada bloque usa la lupa del editor (Ctrl+F):

| Quieres cambiar | Busca | Qué tocar |
|---|---|---|
| Fuentes de geopolítica | `GEO = {` | Añade, quita o cambia líneas del bloque |
| Fuentes de política | `POL = {` | Igual |
| Fuentes y cantidad de cada tema diario | `CATS = [` | El número después de la etiqueta es cuántas noticias de ese tema (por defecto 2) |
| Cuántas de geopolítica y de política | `seccion(GEO, 5` y `seccion(POL, 5` | Cambia el 5. En la de geopolítica, el `1` que sigue es cuántas deben ser en español |
| Palabras que debe tener una nota para entrar | `GEO_KW`, `POL_KW`, `KW_WAR`, `KW_POLES` | Añade o quita palabras separadas por `|` |

Cada fuente se escribe así: nombre, idioma (`"en"` o `"es"`) y una lista de enlaces RSS alternativos:

```python
"Nombre del medio": ("es", ["https://ejemplo.com/rss", "https://ejemplo.com/feed"]),
```

El idioma importa porque solo se traducen las de `"en"`. Si cambias las cantidades, la página se ajusta sola (los números de las pestañas se calculan), pero el texto explicativo al pie del tablón dice "5 de geopolítica (4 en inglés y 1 en español)… 5 de política… y 10 de actualidad": búscalo en `index.html` (Ctrl+F: `Cada día:`) y actualízalo.

> Escribe los enlaces y nombres a mano o copia solo el contenido, sin las comillas de código (regla 1).

### Formato de news.json

Por si quieres revisarlo a mano: tiene tres listas (`items` para geopolítica, `politica` y `diarias`) y la fecha de la última actualización (`actualizado`). Cada noticia lleva `titulo`, `resumen`, `fuente`, `url` y `fecha`; las que están en español llevan además `idioma` ("es") y las diarias llevan `cat`, el tema.

---

## 10. Pomodoro, bienvenida, radio, Hábitos y tamaño en PC

### Tamaño en PC y en el celular

En pantallas de **900 px de ancho o más** (computadora) la página usa botones, años, días del calendario, textos y Pomodoro más grandes. En el celular se queda el tamaño compacto. Si quieres cambiar los tamaños, busca en `index.html` (Ctrl+F) el comentario `Escritorio: botones y controles más grandes`: es un único bloque `@media(min-width:900px)` donde cada línea es un elemento (`#years button`, `.d`, `#pmt`, etc.) y el número de `font-size` o `padding` es el que manda.

En esas pantallas anchas, el **Tablón** y la **Radio** se abren en una ventana mucho más grande (hasta unos 1100 px, y 1400 px en pantallas de 1400 px o más), las emisoras se ordenan en **dos columnas** y cada noticia es un **rectángulo horizontal largo**, de ancho completo: el título y la fuente a la izquierda, el resumen a la derecha. Los tamaños de letra de las noticias están en las dos líneas siguientes a ese comentario: `font-size:29px` (título), `24px` (resumen) y `16px` (fuente); súbelos o bájalos a gusto. Para cambiar el tamaño, busca en `index.html` (Ctrl+F) el comentario `Escritorio: Tablón y Radio más grandes` y cambia los números de `max-width` (ancho) y `max-height` (alto).

### Pomodoro

- **▶ Iniciar / ↺ Reiniciar / ⚙ Tiempo:** arrancar, volver a empezar la fase y configurar los minutos de enfoque, descanso corto y descanso largo.
- **⏭ Saltar:** pasa a la siguiente fase sin esperar. Si estabas en Enfoque, cuenta como pomodoro hecho.
- **− y +:** restan o suman un pomodoro al contador de hoy (🍅), por si te olvidaste de iniciar uno o quieres corregirlo.
- **Descanso largo:** cada 4 pomodoros completados.
- **Voces:** al iniciar un Enfoque suena una voz, al terminarlo suena otra, y cada 8 pomodoros suena una especial. Están incrustadas en el archivo, así que funcionan sin internet. Si el navegador no deja reproducirlas, suena un pitido.
- **🔊 Voz (control de volumen):** al lado del contador hay una barra para regular el volumen de las voces, del pitido y de la bienvenida. Va de 0 (silencio) a 100. Está pensada para los niveles bajos: el 50 suena bastante más bajo que antes (un cuarto del volumen original) y el 20 es muy suave. Al soltar la barra suena una muestra a ese volumen. El nivel se guarda en el navegador, así que no hay que volver a ponerlo. Con la barra en 0 no suena nada. Para cambiar cuál suena en cada momento, busca `const VOZ=` en `index.html` e intercambia las tres líneas.
- **Memoria:** el contador de pomodoros se guarda en el navegador y se reinicia cada día. Si cierras la página por error, el temporizador retoma donde estaba.

### Radio

Se abre con el botón de la radio. Las emisoras vienen en categorías:

🎷 Jazz · 🎻 Clásica · 📚 Para estudiar · 📰 Noticias EE. UU. · 🌍 Internacional · 🇪🇸 En español · 🇦🇷 Argentina (noticias y música) · 🏎️ Eurobeat y Eurodance · 👽 Rarezas

- Cada emisora tiene varios enlaces de respaldo: si uno falla, prueba el siguiente solo.
- Si el sonido se corta o se queda mudo, la página reconecta sola (hasta 5 veces). Si la conexión es lenta y hay entrecortes, cambia a otro enlace.
- Algunas emisoras (como las de Corea del Norte) usan un formato que Chrome y Firefox no reproducen directamente: la página descarga un reproductor auxiliar (hls.js) solo cuando hace falta. Para eso necesita internet.
- Algunas emisoras muestran debajo un "¿Se corta? Abrir en:" con enlaces a sus páginas oficiales.
- Hay emisoras que pueden estar fuera del aire el día que las pruebes; es normal.
- Para agregar una emisora, busca la categoría en `index.html` (por ejemplo `Rarezas`) y añade una línea con el mismo formato que las demás: nombre y una lista de enlaces.

> Dentro de visores o vistas previas las emisoras suelen bloquearse. Ábrela desde GitHub Pages o desde el archivo en tu navegador.

### Voz de bienvenida

Al abrir la página suena `bienvenida.mp3`. Para cambiarla, reemplaza ese archivo por otro audio MP3 con **el mismo nombre**.

- **Los navegadores bloquean el sonido automático.** Chrome, Edge, Firefox y Safari no dejan sonar un audio en el instante de abrir una página, hasta que tocas algo. Por eso la página lo intenta al abrir y, si el navegador lo bloquea (lo más común), suena **con tu primer clic, toque o tecla**. Solo suena una vez por apertura.
- Mientras suena aparece arriba a la derecha el botón **⏹ Detener bienvenida**.
- Si inicias el Pomodoro mientras suena la bienvenida, esta se corta para no encimar las voces.
- El volumen de la bienvenida es el de la barra **🔊 Voz** del Pomodoro. Con la barra en 0 no suena.
- Si prefieres que no suene más, deja la barra en 0 o borra `bienvenida.mp3` del repo (la página sigue funcionando igual).

### Botón ❤️ Donar (Cafecito)

**Estado actual: oculto.** Para mostrarlo, busca `MOSTRAR_DONAR` en `index.html` (Ctrl+F) y cambia `false` por `true`. Lo mismo vale para el cartel de la página de mantenimiento (`mantenimiento.html`).

En la barra de botones de arriba, después de ⚔️ Hábitos, hay un botón **❤️ Donar**. Abre una ventana del mismo tamaño que el Tablón y la Radio, con el mensaje de que el proyecto se mantiene gracias a los aportes y un botón que lleva a https://cafecito.app/lionheartd. Se cierra con **Cerrar** o tocando fuera de la ventana. La página de mantenimiento (sección 14) trae un cartel con el mismo mensaje y enlace.

Para cambiar el enlace o el texto, busca `cafecito.app` en `index.html` y en `mantenimiento.html` (Ctrl+F). Para quitarlo de la página principal, borra la línea del botón `id="donb"` y el bloque `<div id="donar">` hasta su cierre.

### Botón ⚔️ Hábitos

Lleva a otra página tuya (la de hábitos). La dirección está en `index.html`, en una sola línea: busca `HABITOS_URL` y cambia el enlace entre comillas.

---

## 11. Añadir o quitar años del calendario

Los años están definidos en `index.html`, en dos líneas seguidas. El calendario calcula los meses y los días con el año elegido, así que no hay que tocar nada más.

Las dos líneas (están hacia la línea 249; en el editor usa la lupa o Ctrl+F y busca `const YEARS`):

```js
const YEARS=[2026,2027,2028,2029,2030];
let year=YEARS.includes(new Date().getFullYear())?new Date().getFullYear():YEARS[0],sel=null,store={};
```

La segunda línea ya viene preparada: abre el año actual si está en la lista y, si no, el **primero de la lista** (`YEARS[0]`). Por eso puedes quitar años sin tocar esa línea, y por eso la lista debe estar siempre **ordenada de menor a mayor**.

### 11a. Añadir años

1. Abre `index.html` y pulsa el lápiz (**Edit**).
2. En la línea `const YEARS=` añade los años que quieras, separados por comas. Por ejemplo, hasta 2040:

```js
const YEARS=[2026,2027,2028,2029,2030,2031,2032,2033,2034,2035,2036,2037,2038,2039,2040];
```

3. Opcional: cambia el título de la pestaña en la línea 7:

```html
<title>Calendario Medieval 2026 · 2040</title>
```

4. Pulsa **Commit changes**.
5. En uno o dos minutos la página mostrará los botones nuevos (recarga con Ctrl+F5 si no los ves).

Los botones saltan de línea solos, así que puedes añadir los años que quieras sin tocar el diseño.

### 11b. Quitar años (por ejemplo, ya pasó el 2026)

1. Abre `index.html` y pulsa el lápiz (**Edit**).
2. En `const YEARS=` borra el año que ya no quieras. Por ejemplo, para quitar el 2026:

```js
const YEARS=[2027,2028,2029,2030];
```

3. Opcional: actualiza el título de la línea 7.
4. Pulsa **Commit changes**.

### Con qué año abre la página

| Fecha de hoy | Año con el que abre |
|---|---|
| Año que está en la lista (por ejemplo 2029) | Ese año, marcado en rojo |
| Año que no está en la lista (por ejemplo 2026 ya quitado, o 2035) | El primero de la lista (por ejemplo 2027) |

### Qué pasa con los eventos que ya guardaste

- Tus eventos se guardan en el navegador de cada dispositivo (no en GitHub), por fecha y año.
- Si quitas un año, sus eventos **no se borran**, pero no podrás verlos mientras ese año no esté en la lista. Si vuelves a añadir el año, reaparecen.
- Antes de quitar un año con eventos importantes, pulsa **⬇ Respaldo** en la página para guardar una copia. Con **⬆ Cargar** la recuperas.

> Escribe la lista a mano o copia solo el contenido del bloque, sin las comillas de código (regla 1).

---

## 12. Qué limpia el script

- Descarta notas fuera de tema: en geopolítica, política, guerra, Argentina y Perú solo entran notas que contengan palabras del tema (por ejemplo "ceasefire", "Congreso", "gobierno"). Las de Iglesia católica y política de EE. UU. vienen de secciones ya temáticas de cada medio.
- Reserva un lugar para 1 nota en español entre las 5 de geopolítica.
- Quita duplicados: la misma nota (mismo enlace o mismo título) no aparece dos veces, ni siquiera en secciones distintas.
- Prefiere notas de los últimos 4 días. Si no hay ninguna tan reciente, usa las más nuevas que encuentre.
- Máximo 1 noticia por medio dentro de cada tema (2 solo si faltan para completar).
- Arregla los textos con símbolos raros (`&nbsp;` y similares) que algunos medios incluyen y que rompen la lectura del feed.
- Si una sección no encuentra nada nuevo, conserva la que ya tenía en `news.json` y lo avisa en el log con la palabra `AVISO`.
- Si **ninguna** fuente responde, la ejecución sale en rojo para que te enteres, y el `news.json` anterior queda intacto.

---

## 13. Cambiar la hora del bot (y por qué a veces se retrasa)

En `.github/workflows/noticias.yml` está esta línea:

```yaml
- cron: "11 */4 * * *"   # cada 4 horas, en el minuto 11 (UTC)
```

Los números son **minuto hora día-del-mes mes día-de-la-semana**, y la hora es siempre **UTC**. Lo que escribas después del `#` es solo un comentario: GitHub lo ignora (ponle un espacio antes del `#` y no lo metas dentro de las comillas).

Ejemplos:

| Quieres | Escribe |
|---|---|
| Una vez al día, 9:11 UTC | `11 9 * * *` |
| Dos veces al día (9:11 y 21:11 UTC) | `11 9,21 * * *` |
| Cada 6 horas (4 veces al día) | `11 */6 * * *` |
| Cada 4 horas (6 veces al día) | `11 */4 * * *` |
| Cada 3 horas (8 veces al día) | `11 */3 * * *` |
| Cada 2 horas (12 veces al día) | `11 */2 * * *` |

### Pasar de UTC a tu hora

Resta o suma la diferencia de tu zona. Ejemplo para Argentina y Uruguay (UTC-3, sin cambio de verano):

| UTC | Tu hora |
|---|---|
| 9:11 | 6:11 a.m. |
| 21:11 | 6:11 p.m. |

Para Perú (UTC-5, sin cambio de verano) resta 5 horas. En España, la diferencia es +1 en invierno y +2 en verano.

### Problema: el bot se ejecuta tarde, o directamente no se ejecuta

Esto **no es un error de tu configuración**. Pasa seguido:

- GitHub avisa en su documentación de que las tareas programadas (`schedule`) pueden retrasarse cuando hay mucha carga en sus servidores, y que no garantiza la hora exacta.
- Las horas en punto (`0 9`, `0 11`, `0 21`) son las más saturadas, porque mucha gente programa sus tareas justo a esa hora.
- En repositorios nuevos o con poca actividad, el retraso suele ser mayor, y a veces una ejecución se salta del todo.
- No hay forma de arreglarlo desde el archivo: la puntualidad depende de GitHub.
- Además, GitHub **desactiva las tareas programadas** de un repositorio público si pasan 60 días sin actividad. Si un día el bot deja de correr, entra en **Actions → Noticias diarias** y pulsa el botón para volver a habilitarlo.

### Estrategia recomendada: ejecuciones frecuentes + botón manual de respaldo

Como no se puede garantizar una hora exacta, la forma más fiable es no depender de una sola ejecución. El proyecto ya viene así:

1. **Ejecuciones más seguidas.** Con `11 */4 * * *`, si una se retrasa o se salta, otra llega poco después. Es gratis: en un repositorio público, GitHub Actions no tiene coste, y cada ejecución dura menos de un minuto.
2. **Minuto distinto de 0.** Se usa el `11` para esquivar la hora en punto.
3. **Botón manual de respaldo.** Si ves que las noticias están viejas y necesitas algo fresco ya, ve a **Actions → Noticias diarias → Run workflow → Run workflow**. Es lo más rápido y siempre funciona, aunque todo lo demás falle.
4. **Si todo falla,** revisa que la última ejecución en Actions no salga en rojo, y que **Settings → Actions → General** siga con **Allow all actions** y **Read and write permissions** (secciones 6 y 7).

### Qué cambia al ejecutar más seguido

El tablón se actualiza cuando los medios publican notas nuevas. Si en una ejecución las noticias elegidas son las mismas que ya estaban, no se guarda ningún cambio y no se crea ningún commit. Eso significa que ejecutar más veces no llena el repositorio de commits inútiles, y que el tablón siempre muestra lo más reciente que encontró el bot.

- Si prefieres menos movimiento, usa menos ejecuciones (y acepta que una pueda retrasarse).
- Si prefieres que siempre haya noticias recientes, usa más ejecuciones.

### Alternativa avanzada: un disparador externo

Servicios como cron-job.org pueden pedirle a GitHub que lance el workflow a una hora exacta, y suelen ser más puntuales que `schedule`. Requiere crear un token de GitHub y configurar el servicio, así que solo vale la pena si necesitas puntualidad estricta. Para uso normal, la estrategia de arriba es suficiente.

### Cómo saber si una actualización fue manual o programada

1. Ve a **Actions → Noticias diarias**.
2. Cada ejecución indica "Manually run by..." (manual) o "Scheduled" (programada), y la hora.
3. En la página, la línea "Actualizado" muestra la hora de la última ejecución que guardó noticias, convertida a la hora de tu dispositivo.

### Cuándo empieza a valer un cambio de horario

Un cambio en el `cron` vale desde el siguiente horario programado. No dispara una ejecución en el momento.

---

## 14. Mantenimiento mensual (página de aviso)

`mantenimiento.html` es una página de aviso para los días en que vayas a modificar el calendario (por ejemplo, un par de horas una vez al mes). Cuando la subes en lugar del `index.html` normal, quien entra ve:

- Un cartel de **🛠️ Reino en mantenimiento**, con el motivo y la hora estimada de regreso (con cuenta regresiva).
- Un aviso de **⚠️ Haz tu respaldo lo antes posible**, con el botón **⬇ Descargar respaldo**. Funciona aunque el calendario no esté disponible: lee los mismos eventos que el calendario guarda en el navegador. Si el navegador no deja descargar, el botón **📋 Copiar como texto** los copia al portapapeles.
- Instrucciones para recuperar todo cuando vuelva la página: **⬆ Cargar** (o el botón **📋 Texto**). El archivo tiene el mismo formato que el ⬇ Respaldo normal, así que el calendario lo reconoce.
- Se vuelve a comprobar sola cada 5 minutos y, cuando el `index.html` normal ya está de vuelta, abre el calendario sin que nadie haga nada.

### Paso a paso

**Antes de empezar**

1. Guarda una copia de tu `index.html` actual en tu PC. (GitHub también guarda el historial en **Commits**, pero así es más fácil.)
2. Abre `mantenimiento.html` con el Bloc de notas (o cualquier editor de texto). Arriba del script hay dos líneas para editar:
   - `MOTIVO`: lo que quieres contar, por ejemplo "Estamos agregando una sección nueva".
   - `VUELVE`: la hora estimada de regreso **con zona horaria**, por ejemplo `"2026-11-01T20:00:00-03:00"` (Argentina: `-03:00`; Perú: `-05:00`). Si la dejas vacía, dice "Volvemos en unas horas".
3. Haz una copia de ese archivo y renómbrala exactamente **`index.html`** (que la extensión sea `.html` de verdad, no `index.html.txt`).
4. En el repo: **Add file → Upload files**, sube ese `index.html` a la raíz y confirma que reemplazas el anterior. Espera uno o dos minutos y abre la página con Ctrl+F5: debe verse el cartel.

**Durante el mantenimiento**

5. Trabaja en tu PC con tu `index.html` de verdad y pruébalo abriéndolo en el navegador.

**Al terminar**

6. Sube tu `index.html` nuevo a la raíz del repo, reemplazando el de mantenimiento. Espera uno o dos minutos y abre con Ctrl+F5.
7. Comprueba que los eventos siguen ahí.

### Cosas que conviene saber

- **El mantenimiento no borra los eventos.** Viven en el navegador de cada persona mientras la dirección de la página siga siendo la misma. Si algún día cambias el nombre del repositorio o del usuario, la dirección cambia y los eventos dejan de verse; ahí el respaldo es lo que salva todo.
- El botón de descarga respalda los **eventos del calendario**. No incluye el contador de pomodoros ni el volumen de la voz.
- Solo cambia el archivo `index.html`. El resto (`news.json`, `bienvenida.mp3`, el bot de noticias) sigue funcionando durante el mantenimiento.
- Mientras esté la página de aviso no se ve el Pregón, la radio ni el Pomodoro, porque es otra página.

---

## 15. Problemas frecuentes

| Problema | Causa probable | Solución |
|---|---|---|
| No aparece "Noticias diarias" en Actions | Falta `.github/workflows/noticias.yml`, está en una carpeta con comilla, o no está en la rama principal | Repite el paso 4c y la sección "Cómo arreglar un nombre con comilla" |
| Carpetas o archivos con una comilla (`` `scripts ``) | Copiaste el nombre en vez de escribirlo | Renómbralos escribiendo la ruta a mano |
| El workflow falla a los pocos segundos ("exit code 1") | `noticias.py` está cortado | Pégalo entero; debe tener 286 líneas |
| Falla en "Generar news.json" después de un rato, con "ERROR: ninguna fuente entregó noticias nuevas" | Todas las fuentes fallaron (corte de red o bloqueo) | Vuelve a lanzarlo con **Run workflow**; el `news.json` anterior no se pierde |
| Falla en "Guardar cambios" (error 403) | Falta el permiso de escritura | Paso 6: Read and write permissions |
| Falla en "Guardar cambios" con un error de `push` o `rebase` | Cambiaste un archivo a la vez que corría el bot | Vuelve a lanzar el bot con **Run workflow** |
| Al guardar sale "has committed since you started editing" | Abriste el editor y el archivo cambió después (el bot guarda `news.json` con frecuencia) | Copia tu texto, recarga la página, abre el editor otra vez, pega y guarda |
| Sale el aviso "You have unsaved changes" | Intentaste salir sin guardar | Pulsa **Cancelar** y guarda con **Commit changes** |
| La página no carga | Pages no está activado o aún publica | Revisa el paso 5 y espera un par de minutos |
| El Pregón dice "No se pudo cargar el tablón" | Abriste `index.html` como archivo local: el navegador bloquea leer `news.json` | Ábrelo desde la dirección de GitHub Pages |
| Una pestaña dice "Esta sección se llena con la próxima actualización" | Todavía no corrió el bot con la versión nueva, o esa sección no encontró nada | Lanza el bot con **Run workflow** y mira en el log qué fuentes dieron `ERR` |
| Una sección tiene menos noticias de las esperadas | Pocas notas del tema pasaron el filtro o varias fuentes fallaron | Mira el log; añade más fuentes en `noticias.py` (sección 9) |
| Las noticias salen en inglés | No hay clave de traducción, o la traducción falló | Paso 8; si ya la pusiste, revisa en el log el mensaje "Traducción falló". La de "en español" no se traduce porque ya viene en español |
| Una emisora de la radio no suena | Está fuera del aire o el navegador bloqueó el audio | Toca otra emisora, o toca de nuevo la misma. Si tampoco suena ninguna, ábrela desde GitHub Pages, no desde una vista previa |
| Las emisoras de Corea del Norte no cargan | Necesitan el reproductor auxiliar hls.js, que se baja de internet | Comprueba tu conexión; esas emisoras suelen estar fuera del aire |
| El Pomodoro no dice la voz, solo pita | El navegador bloqueó el audio hasta que toques la página | Toca cualquier botón de la página una vez y vuelve a iniciar |
| La bienvenida no suena al abrir la página | El navegador bloquea el sonido automático hasta que tocas la página | Es normal: suena con tu primer clic, toque o tecla |
| La bienvenida nunca suena | Falta `bienvenida.mp3` en la raíz del repo, tiene otro nombre, o la barra 🔊 Voz está en 0 | Sube el archivo con ese nombre exacto, junto a `index.html`, y sube la barra |
| La voz del Pomodoro asusta por lo fuerte | Volumen demasiado alto | Baja la barra 🔊 Voz (con 20 o 30 suena muy suave); queda guardado |
| La pestaña 📬 dice "Aún no hay newsletters" aunque el PDF está subido | El bot no corrió (la lista sigue vacía: ábrela, debe mostrar el nombre del PDF), o el navegador guardó la versión vieja | Recarga con Ctrl+F5. Si sigue igual: **Actions → Newsletters → Run workflow**. Comprueba que el PDF esté dentro de la carpeta `newsletters` (no en la raíz) y que termine en `.pdf` |
| El contador 🍅 se puso en 0 | Cambió el día (se reinicia a diario) o cambiaste de navegador o dispositivo | Es normal. Usa **+** para corregirlo si hace falta |
| El botón Hábitos lleva a un sitio equivocado | `HABITOS_URL` tiene otro enlace | Cambia el enlace en `index.html` (sección 10) |
| Las noticias no cambian | Los medios no publicaron nada nuevo, o alguna fuente falló | Mira el log en Actions: cada fuente indica `OK` o `ERR` |
| Los años nuevos no aparecen | Cambio sin guardar o Pages aún publica | Comprueba el commit en `index.html`, espera un par de minutos y recarga con Ctrl+F5 |
| El bot se ejecutó horas más tarde de lo programado, o no se ejecutó | GitHub retrasa o se salta tareas programadas, sobre todo en horas en punto y en repos con poca actividad | Usa ejecuciones frecuentes (`11 */4 * * *`), un minuto distinto de 0, y el botón **Run workflow** como respaldo (sección 13) |
| El bot dejó de correr del todo después de semanas | GitHub desactiva los workflows programados tras 60 días sin actividad en el repo | Actions → Noticias diarias → botón para habilitarlo de nuevo |
| La hora de "Actualizado" no cambió aunque el bot corrió | Las noticias elegidas fueron las mismas y no hubo nada que guardar | Es normal. Mira en Actions si la ejecución salió en verde |
| No sé si una actualización fue manual o programada | La página solo muestra la hora | En Actions, cada ejecución dice "Manually run" o "Scheduled" |
| Quité un año de la lista y mis eventos desaparecieron | No se borraron: solo están ocultos mientras ese año no esté en la lista | Vuelve a añadir el año a `YEARS` y reaparecen. Antes de quitar años, usa **⬇ Respaldo** |
| La lista de años quedó desordenada y abre en un año raro | El primer año de la lista es el que se abre por defecto | Ordena `YEARS` de menor a mayor |

---

## 16. Newsletters en PDF (pestaña 📬)

Esta sección explica **todo** lo de las newsletters: cómo funciona, cómo dejarlo andando por primera vez, cómo subir una cada vez, cómo borrarla y qué hacer si algo falla.

### 16.1 Qué es y cómo funciona

El Tablón tiene una cuarta pestaña, **📬 Newsletter**, que muestra los PDF que guardes en la carpeta `newsletters` del repositorio. La subida es manual: tú descargas la newsletter como PDF, la subes y aparece en la página.

El recorrido completo es este:

1. **Subes un PDF** a la carpeta `newsletters` en GitHub.
2. GitHub ve que hay un PDF nuevo y lanza solo el bot **Newsletters** (el archivo `newsletters.yml`).
3. El bot hace una lista con los nombres de todos los PDF de la carpeta y la guarda en `newsletters/lista.json`.
4. La página lee esa lista y dibuja una tarjeta por cada PDF, de la más nueva a la más vieja.
5. **Respaldo:** si `lista.json` está vacío o no se puede leer, la página le pregunta directamente a GitHub qué PDF hay en la carpeta. Así el PDF aparece aunque el bot falle.

Las piezas son estas:

| Pieza | Para qué sirve | Quién la toca |
|---|---|---|
| `newsletters/` (carpeta) | Aquí guardas los PDF | Tú |
| `newsletters/*.pdf` | Cada newsletter | Tú |
| `newsletters/lista.json` | La lista de PDF | El bot (tú no la toques) |
| `newsletters/.gitkeep` | Archivo vacío que mantiene viva la carpeta aunque no haya PDF | Nadie |
| `.github/workflows/newsletters.yml` | El bot que escribe la lista | Se crea una sola vez |
| `index.html` | Dibuja la pestaña 📬 | Ya viene incluida |

### 16.2 Puesta en marcha (una sola vez)

**Paso 1. Crea la carpeta y la lista inicial.**
En el repo pulsa **Add file → Create new file**. En el nombre escribe **a mano** `newsletters/lista.json` (al escribir la `/` se crea la carpeta). Como contenido pega exactamente esto y pulsa **Commit changes**:

```
{"archivos":[]}
```

**Paso 2. Crea el bot a mano.**
Es la parte donde más gente se atasca, porque la carpeta `.github` **no se puede subir con "Upload files"** (regla 3). Pulsa **Add file → Create new file**, escribe **a mano** el nombre `.github/workflows/newsletters.yml`, pega todo el contenido de abajo y pulsa **Commit changes**:

```yaml
name: Newsletters
on:
  push:
    paths:
      - "newsletters/**.pdf"
  workflow_dispatch:
permissions:
  contents: write
concurrency:
  group: newsletters
  cancel-in-progress: false
jobs:
  listar:
    runs-on: ubuntu-latest
    timeout-minutes: 5
    steps:
      - uses: actions/checkout@v4
      - name: Generar newsletters/lista.json
        run: |
          python3 - <<'PY'
          import json, os
          nombres = sorted(
              (f for f in os.listdir("newsletters") if f.lower().endswith(".pdf")),
              reverse=True,
          )
          with open("newsletters/lista.json", "w", encoding="utf-8") as fh:
              json.dump({"archivos": nombres}, fh, ensure_ascii=False, indent=1)
              fh.write("\n")
          PY
      - name: Guardar cambios
        run: |
          git config user.name "noticias-bot"
          git config user.email "noticias-bot@users.noreply.github.com"
          git add newsletters/lista.json
          if git diff --staged --quiet; then
            echo "Sin cambios que guardar."
            exit 0
          fi
          git commit -m "Lista de newsletters"
          git pull --rebase origin "$GITHUB_REF_NAME"
          git push origin "HEAD:$GITHUB_REF_NAME"
```

Después abre el archivo y comprueba que ponga **41 lines** (regla 2). Si pone menos, se cortó al pegar: pégalo de nuevo, entero. Si cambias algo sin querer, el bot deja de funcionar.

**Paso 3. Permisos.**
El bot necesita escribir en el repo. Revisa el paso 6 de este README (**Read and write permissions**). Si el bot de noticias ya te funciona, este también.

**Paso 4. Sube el `index.html` actual.**
Tiene que ser la versión que trae la pestaña 📬 Newsletter. Si en el Tablón solo ves tres pestañas, el `index.html` del repo es viejo.

**Paso 5. Pruébalo a mano.**
Crear el bot **no lo activa solo**, porque el bot solo se lanza cuando se sube un PDF. La primera vez hay que lanzarlo tú:

1. Pestaña **Actions**. A la izquierda debe aparecer **Newsletters**. (Si no aparece, mira la tabla del apartado 16.6.)
2. Pulsa **Newsletters → Run workflow → Run workflow**.
3. Espera a que termine en verde.
4. Abre `newsletters/lista.json`: debe mostrar el nombre de tu PDF dentro de `archivos`.
5. Abre tu página, pulsa **📰 Tablón → 📬 Newsletter** y recarga con **Ctrl+F5**.

### 16.3 Subir una newsletter (lo que haces cada vez)

1. **Guarda la newsletter como PDF.** En Gmail: abre el correo, toca los tres puntos, **Imprimir** y elige **Guardar como PDF**. En el celular: Compartir, Imprimir, Guardar como PDF.
2. **Ponle un nombre correcto** (reglas abajo).
3. En GitHub abre la carpeta `newsletters`.
4. Pulsa **Add file → Upload files**, arrastra o elige el PDF y pulsa **Commit changes**. Desde el celular funciona igual en la web de GitHub.
5. **Espera 1 o 2 minutos.** En **Actions** verás correr el bot **Newsletters**.
6. Cuando termine en verde, abre el Tablón, pulsa **📬 Newsletter** y recarga si hace falta.

**Cómo nombrar el PDF**

- Sin espacios, sin tildes y sin ñ. Usa guiones o guiones bajos. (Con espacios o ñ el archivo puede no abrirse bien. A ti te pasó: al quitar los espacios funcionó.)
- Termina siempre en `.pdf`.
- Va **dentro** de la carpeta `newsletters`, no en la raíz.
- Empieza con la fecha, en cualquiera de estos dos formatos, y después, si quieres, un título.

| Nombre del archivo | Fecha que muestra | Título que muestra |
|---|---|---|
| `2026-10-08_Nombre-del-tema.pdf` | 2026-10-08 | Nombre del tema |
| `7-10-26-Keating-no-ensenaba-poesia.pdf` | 2026-10-07 | Keating no ensenaba poesia |
| `2026-10-08.pdf` | 2026-10-08 | Newsletter |
| `sin-fecha.pdf` | (ninguna) | sin fecha |

El formato corto `D-M-AA` se lee **día-mes-año**: `7-10-26` es el 7 de octubre de 2026. La página ordena por esa fecha, de la más nueva a la más vieja; las que no tienen fecha van al final. El título sale del nombre cambiando los guiones por espacios, así que no tendrá tildes.

### 16.4 Borrar o reemplazar una newsletter

- **Borrar:** abre el PDF dentro de `newsletters`, pulsa los tres puntos (**⋯**) y **Delete file**. Si la tarjeta no desaparece en un par de minutos, ve a **Actions → Newsletters → Run workflow** para que la lista se actualice.
- **Renombrar:** GitHub no renombra archivos subidos desde el navegador de forma cómoda. Lo más simple es subir el PDF con el nombre nuevo y borrar el viejo.
- **Reemplazar el contenido:** sube un PDF con **el mismo nombre**; GitHub te pregunta si reemplaza.

### 16.5 Cosas que conviene saber

- **No toques `lista.json`.** Lo escribe el bot. Si alguna vez se descuadra, ve a **Actions → Newsletters → Run workflow**.
- **Parche de emergencia:** si necesitas que un PDF aparezca ya y el bot no responde, edita `lista.json` a mano con el nombre exacto: `{"archivos":["7-10-26-Keating-no-ensenaba-poesia.pdf"]}`. Con el respaldo de la página normalmente ni hace falta.
- **El respaldo de la página** solo funciona abierto desde la dirección de GitHub Pages (`usuario.github.io/...`), con el repositorio público. GitHub limita esas consultas (60 por hora por conexión), de sobra para uso normal, y la página solo las hace cuando la lista está vacía.
- **La vista previa de GitHub** a veces no muestra los PDF y dice "Unable to render code block". No es un error del archivo: usa el botón de descarga (⬇) o ábrelo desde tu página.
- **Tamaño:** desde la web de GitHub puedes subir archivos de hasta 25 MB.
- **Repositorio público:** cualquiera puede ver los PDF si tiene el enlace. La newsletter del Instituto Juan de Mariana es pública, pero conviene no subir correos con datos personales: por ejemplo, el enlace de "darse de baja" lleva tu dirección de correo. Sube solo lo que puedas compartir.
- **Si no abre el PDF en el celular,** pulsa el enlace de nuevo: algunos navegadores lo descargan en lugar de mostrarlo.
- **Cambiar el nombre de la fuente:** hoy cada tarjeta dice "Instituto Juan de Mariana". Para cambiarlo, busca en `index.html` (Ctrl+F) `fuente:"Instituto Juan de Mariana"` y cambia el texto. (La tarjeta de enlace para suscribirse al Instituto es otra cosa: está oculta por ahora, ver `MOSTRAR_IJM`.)

### 16.6 Si algo falla

| Problema | Causa probable | Solución |
|---|---|---|
| En Actions no aparece **Newsletters** | El archivo no está en la ruta exacta `.github/workflows/newsletters.yml`, o tiene una comilla en el nombre | Repite el paso 2 de 16.2 escribiendo la ruta a mano |
| Aparece un cartel rojo "Invalid workflow file" | Se pegó mal o quedó cortado | Comprueba que tenga **41 líneas** y pégalo de nuevo entero |
| El bot sale en rojo en "Guardar cambios" (error 403) | Falta el permiso de escritura | Paso 6: **Read and write permissions** |
| Subí el PDF y el bot no se lanzó | El PDF no está dentro de `newsletters`, no termina en `.pdf`, o el bot se creó después de subir el PDF | Revisa la ruta y el nombre; lanza el bot a mano con **Run workflow** |
| `lista.json` sigue en `{"archivos":[]}` | El bot no corrió | **Actions → Newsletters → Run workflow** |
| La pestaña dice "Aún no hay newsletters" | La lista está vacía y la página tampoco pudo leer la carpeta | Recarga con Ctrl+F5; lanza el bot; comprueba que abres la página desde `github.io`, no desde un archivo local |
| Solo veo tres pestañas, sin 📬 | El `index.html` del repo es una versión vieja | Sube el `index.html` actual |
| Aparece la tarjeta pero el PDF no abre | El nombre cambió o tiene espacios o ñ, o la lista quedó vieja | Usa nombres sin espacios ni ñ y lanza el bot a mano |
| El PDF se descarga en vez de abrirse | El navegador o el celular lo decide así | Es normal; abre el archivo descargado |
| La fecha sale mal (7-10 como 10 de julio) | El formato corto es día-mes-año | Usa `AAAA-MM-DD` si prefieres evitar dudas |
| Una newsletter no queda primera aunque es la más nueva | No empieza con fecha | Ponle la fecha al principio del nombre |
| Carpeta o archivo con una comilla (`` `newsletters ``) | Copiaste el nombre en vez de escribirlo (regla 1) | Renómbralo a mano con el lápiz de **Edit** |

---

## Resumen rápido (checklist)

- [ ] Repo público creado
- [ ] `index.html`, `news.json` y `README.md` subidos a la raíz
- [ ] `scripts/noticias.py` creado a mano (286 líneas)
- [ ] `.github/workflows/noticias.yml` creado a mano (35 líneas)
- [ ] Sin comillas raras en ningún nombre
- [ ] Pages activado en la rama `main`, carpeta raíz
- [ ] Read and write permissions activado
- [ ] Probado con **Run workflow** y salió en verde
- [ ] Revisado el log: las fuentes principales salen `OK` y la última línea dice `Listo: 5 geopolítica, 5 política, 10 diarias.`
- [ ] Pregón abierto desde GitHub Pages: se ven las 4 pestañas (la de Newsletter puede estar vacía al principio)
- [ ] Pestaña Geopolítica con 5 notas, una "en español"
- [ ] Probados la radio (una emisora suena), el Pomodoro (⏭ Saltar, − y +) y el botón ⚔️ Hábitos
- [ ] En PC (pantalla ancha) los botones se ven grandes
- [ ] `bienvenida.mp3` subido y la voz suena con el primer clic; la barra 🔊 Voz regula el volumen
- [ ] (Opcional) `ANTHROPIC_API_KEY` configurada para traducir
- [ ] Tener `mantenimiento.html` guardado en la PC para los días de mantenimiento (sección 14)
- [ ] `.github/workflows/newsletters.yml` creado a mano (41 líneas) y `newsletters/lista.json` creado
- [ ] Probado **Actions → Newsletters → Run workflow** en verde; `lista.json` muestra el nombre del PDF
- [ ] Pestaña 📬 Newsletter visible en el Tablón y el PDF abre desde la tarjeta
- [ ] PDF con nombre sin espacios, tildes ni ñ, y con la fecha al principio
- [ ] Saber usar **Run workflow** como respaldo manual si una ejecución programada no llega
