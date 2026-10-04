#!/usr/bin/env python3
"""Genera news.json para el Pregón del día:
  items    -> 5 noticias de geopolítica (medios liberales clásicos / escuela austriaca)
  politica -> 5 noticias de política (liberal clásico / derecha)
  diarias  -> 10 noticias: guerra, Iglesia católica, política de EE. UU., Argentina y Perú (2 de cada una)
Corre a diario en GitHub Actions. Si una fuente falla se prueba la siguiente y, al final,
Google News como respaldo. Si una sección queda vacía se conserva la del día anterior."""
import json, os, re, sys, html, urllib.request, urllib.parse
import xml.etree.ElementTree as ET
from datetime import datetime, timezone, timedelta
from email.utils import parsedate_to_datetime

UTC = timezone.utc
UA = {"User-Agent": "Mozilla/5.0 (compatible; CalendarioMedievalBot/2.0)"}
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "news.json")

# fuente: (idioma, [enlaces alternos: se usa el primero que responda])
GEO = {
    "Mises Institute": ("en", ["https://mises.org/feed/blog.rss", "https://mises.org/rss.xml", "https://mises.org/feed"]),
    "Antiwar.com": ("en", ["https://original.antiwar.com/feed/", "https://www.antiwar.com/blog/feed/"]),
    "Libertarian Institute": ("en", ["https://libertarianinstitute.org/feed/"]),
    "Cato Institute": ("en", ["https://www.cato.org/rss/recent-opeds", "https://www.cato.org/rss/commentary"]),
    "AIER": ("en", ["https://www.aier.org/feed/"]),
    "FEE": ("en", ["https://fee.org/feed/"]),
    "Reason": ("en", ["https://reason.com/feed/"]),
    "Ron Paul Institute": ("en", ["https://ronpaulinstitute.org/feed/"]),
}
POL = {
    "National Review": ("en", ["https://www.nationalreview.com/feed/"]),
    "The Daily Signal": ("en", ["https://www.dailysignal.com/feed/"]),
    "Washington Examiner": ("en", ["https://www.washingtonexaminer.com/feed", "https://www.washingtonexaminer.com/tag/politics/feed"]),
    "Law & Liberty": ("en", ["https://lawliberty.org/feed/"]),
    "City Journal": ("en", ["https://www.city-journal.org/feed", "https://www.city-journal.org/rss"]),
    "Cato Institute": ("en", ["https://www.cato.org/rss/recent-opeds", "https://www.cato.org/rss/commentary"]),
    "Reason": ("en", ["https://reason.com/feed/"]),
    "FEE": ("en", ["https://fee.org/feed/"]),
    "Instituto Juan de Mariana": ("es", ["https://juandemariana.org/feed"]),
    "Libertad Digital": ("es", ["https://www.libertaddigital.com/rss/"]),
}

def gnews(q, lang):
    """Respaldo: búsqueda en Google News (RSS)."""
    if lang == "en":
        p = "hl=en-US&gl=US&ceid=US:en"
    else:
        p = "hl=es-419&gl=AR&ceid=AR:es-419"
    return f"https://news.google.com/rss/search?q={urllib.parse.quote(q + ' when:2d')}&{p}"

# clave, etiqueta, cuántas, filtro de palabras, fuentes, respaldo (consulta, idioma)
KW_WAR = r"war|wars|attacks?|strikes?|missiles?|drones?|troops|ceasefire|invasion|offensive|bomb\w*|military|army|ukrain\w*|russia\w*|gaza|israel\w*|iran\w*|hamas|hezbollah|guerra|ataque\w*|misil\w*|bombardeo\w*|tropas|alto el fuego|ofensiva|ejército|ejercito"
KW_POLES = r"gobierno|congreso|president\w*|ministr\w*|elecci\w*|senad\w*|diputad\w*|partido|ley|leyes|fiscal\w*|candidat\w*|pol[ií]tic\w*|poder|JNE|reforma|decreto|gabinete|oposici\w*|oficialismo"
CATS = [
    ("guerra", "⚔️ Guerra", 2, KW_WAR, {
        "BBC News": ("en", ["https://feeds.bbci.co.uk/news/world/rss.xml"]),
        "Al Jazeera": ("en", ["https://www.aljazeera.com/xml/rss/all.xml"]),
        "DW": ("en", ["https://rss.dw.com/rdf/rss-en-all"]),
    }, ("war OR guerra conflict ceasefire", "en")),
    ("catolica", "⛪ Iglesia católica", 2, None, {
        "Vatican News": ("es", ["https://www.vaticannews.va/es.rss.xml"]),
        "Vatican News (EN)": ("en", ["https://www.vaticannews.va/en.rss.xml"]),
        "Catholic News Agency": ("en", ["https://www.catholicnewsagency.com/feeds/rss/news.xml", "https://www.catholicnewsagency.com/rss/news.xml"]),
        "Aleteia": ("es", ["https://es.aleteia.org/feed/"]),
    }, ("Iglesia católica Vaticano papa", "es")),
    ("eeuu", "🇺🇸 Política de EE. UU.", 2, None, {
        "Fox News": ("en", ["https://moxie.foxnews.com/google-publisher/politics.xml"]),
        "NY Post": ("en", ["https://nypost.com/politics/feed/"]),
        "The Hill": ("en", ["https://thehill.com/homenews/feed/", "https://thehill.com/feed/"]),
        "NPR": ("en", ["https://feeds.npr.org/1014/rss.xml"]),
    }, ("US politics Congress White House", "en")),
    ("argentina", "🇦🇷 Política argentina", 2, KW_POLES, {
        "Infobae": ("es", ["https://www.infobae.com/arc/outboundfeeds/rss/category/politica/"]),
        "La Nación": ("es", ["https://www.lanacion.com.ar/arc/outboundfeeds/rss/category/politica/?outputType=xml"]),
        "Clarín": ("es", ["https://www.clarin.com/rss/politica/"]),
        "Perfil": ("es", ["https://www.perfil.com/feed/politica", "https://www.perfil.com/feed"]),
    }, ("política Argentina gobierno Congreso", "es")),
    ("peru", "🇵🇪 Política peruana", 2, KW_POLES, {
        "Infobae Perú": ("es", ["https://www.infobae.com/arc/outboundfeeds/rss/category/peru/"]),
        "El Comercio": ("es", ["https://elcomercio.pe/arc/outboundfeeds/rss/category/politica/?outputType=xml"]),
        "RPP": ("es", ["https://rpp.pe/feed/politica"]),
        "La República": ("es", ["https://larepublica.pe/rss/politica"]),
    }, ("política Perú Congreso gobierno", "es")),
]
GEO_KW = r"war|wars|ukraine|russia\w*|china|chinese|taiwan|iran\w*|israel\w*|gaza|nato|sanctions?|tariffs?|empire|foreign policy|military|middle east|venezuela\w*|pentagon|geopolit\w*|brics|treaty|sovereignty|syria\w*|north korea\w*|cuba\w*|argentin\w*|milei|european union|trade war|ceasefire|invasion|nuclear|diplomacy|embargo"
POL_KW = r"congress|senate|house|elections?|vote\w*|president\w*|trump|democrat\w*|republican\w*|gop|supreme court|law|laws|bill|tax\w*|budget|government|policy|regulation|immigration|liberal\w*|conservative\w*|governor|federal|milei|gobierno|congreso|elecciones|impuestos|ley|pol[ií]tic\w*"

_cache = {}

def get(url):
    if url not in _cache:
        with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=25) as r:
            _cache[url] = r.read()
    return _cache[url]

def strip(t):
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", t or ""))).strip()

def cut(t, n=220):
    return t if len(t) <= n else t[:n].rsplit(" ", 1)[0].rstrip(".,;:") + "…"

def parse_date(s):
    if not s:
        return None
    try:
        d = parsedate_to_datetime(s)
    except Exception:
        try:
            d = datetime.fromisoformat(s.strip().replace("Z", "+00:00"))
        except Exception:
            return None
    return d if d.tzinfo else d.replace(tzinfo=UTC)

def local(tag):
    return tag.rsplit("}", 1)[-1]

def parse(xml, fuente, lang):
    out = []
    # algunas fuentes traen entidades HTML sin declarar (&nbsp;) que rompen el XML
    xml = re.sub(r"&(?!(?:amp|lt|gt|quot|apos|#\d+|#x[0-9a-fA-F]+);)", "&amp;", xml.decode("utf-8", "replace")).encode("utf-8")
    for node in ET.fromstring(xml).iter():
        if local(node.tag) not in ("item", "entry"):
            continue
        d = {}
        for c in node:
            k = local(c.tag)
            if k == "link":
                if c.get("href") and c.get("rel", "alternate") == "alternate":
                    d.setdefault("link", c.get("href"))
                elif c.text and c.text.strip():
                    d.setdefault("link", c.text.strip())
            elif k in ("pubDate", "published", "updated", "date"):
                d.setdefault("date", c.text)
            elif k == "source":
                d.setdefault("source", strip(c.text))
            elif k in ("title", "description", "summary", "encoded", "content"):
                d.setdefault(k, c.text or "")
        link, title = d.get("link", ""), strip(d.get("title"))
        if not title or not link.startswith("http"):
            continue
        src = d.get("source") or fuente
        if d.get("source") and title.endswith(" - " + src):      # Google News: "Titular - Medio"
            title = title[: -len(src) - 3].rstrip()
        resumen = strip(d.get("description") or d.get("summary") or d.get("encoded") or d.get("content"))
        if resumen[:25].lower() == title[:25].lower():            # Google repite el titular
            resumen = ""
        out.append({"titulo": title, "resumen": cut(resumen), "fuente": src, "url": link,
                    "lang": lang, "dt": parse_date(d.get("date"))})
    return out

def reunir(fuentes):
    pool = []
    for fuente, (lang, urls) in fuentes.items():
        for u in urls:
            try:
                items = parse(get(u), fuente, lang)
                print(f"OK  {fuente}: {len(items)} entradas")
                pool += items
                break
            except Exception as e:
                print(f"ERR {fuente}: {u} -> {e}")
    return pool

def elegir(pool, n, kw, usados, now, dias=4):
    rx = re.compile(r"\b(" + kw + r")\b", re.I) if kw else None
    c = [i for i in pool if i["url"] not in usados and i["titulo"] not in usados
         and (rx is None or rx.search(i["titulo"] + " " + i["resumen"]))]
    rec = [i for i in c if i["dt"] and now - i["dt"] <= timedelta(days=dias)] or c
    rec.sort(key=lambda i: i["dt"] or datetime.min.replace(tzinfo=UTC), reverse=True)
    pick, fuentes = [], set()
    for i in rec:                          # primero fuentes distintas
        if i["fuente"] not in fuentes:
            pick.append(i); fuentes.add(i["fuente"])
        if len(pick) == n:
            break
    for i in rec:                          # si faltan, completar
        if len(pick) == n:
            break
        if i not in pick:
            pick.append(i)
    for i in pick:
        usados.update((i["url"], i["titulo"]))
    return pick

def seccion(fuentes, n, kw, usados, now, respaldo=None):
    pick = elegir(reunir(fuentes), n, kw, usados, now)
    if len(pick) < n and respaldo:         # Google News solo si faltan
        q, lang = respaldo
        try:
            extra = parse(get(gnews(q, lang)), "Google News", lang)
            print(f"OK  Google News ({q}): {len(extra)} entradas")
            pick += elegir(extra, n - len(pick), kw, usados, now)
        except Exception as e:
            print(f"ERR Google News ({q}) -> {e}")
    return pick

def traducir(items):
    key = os.environ.get("ANTHROPIC_API_KEY")
    todo = [i for i in items if i.get("lang") == "en"]
    if not key or not todo:
        return
    for k in range(0, len(todo), 10):
        lote = todo[k:k + 10]
        datos = [{"id": n, "titulo": i["titulo"], "resumen": i["resumen"]} for n, i in enumerate(lote)]
        prompt = ("Traduce al español neutral estos titulares y resúmenes. Responde SOLO con un array JSON "
                  '[{"id":0,"titulo":"...","resumen":"..."}] con los mismos id, sin explicaciones.\n\n'
                  + json.dumps(datos, ensure_ascii=False))
        try:
            body = json.dumps({"model": "claude-haiku-4-5-20251001", "max_tokens": 6000,
                               "messages": [{"role": "user", "content": prompt}]}).encode()
            req = urllib.request.Request("https://api.anthropic.com/v1/messages", data=body, headers={
                "content-type": "application/json", "x-api-key": key, "anthropic-version": "2023-06-01"})
            txt = json.load(urllib.request.urlopen(req, timeout=90))["content"][0]["text"]
            arr = json.loads(txt[txt.index("["): txt.rindex("]") + 1])
            for t in arr:
                it = lote[int(t["id"])]
                it["titulo"], it["resumen"], it["traducido"] = t["titulo"], t.get("resumen", ""), True
        except Exception as e:
            print("Traducción falló (se dejan en inglés):", e)

def limpiar(i, cat=None):
    dt = i.pop("dt", None)
    i.pop("lang", None)
    i["fecha"] = dt.date().isoformat() if dt else ""
    if cat:
        i["cat"] = cat
    return i

def main():
    now = datetime.now(UTC)
    usados = set()
    geo = seccion(GEO, 5, GEO_KW, usados, now)
    pol = seccion(POL, 5, POL_KW, usados, now, ("conservative OR libertarian politics opinion", "en"))
    dia = []
    for clave, etiqueta, n, kw, fuentes, respaldo in CATS:
        for i in seccion(fuentes, n, kw, usados, now, respaldo):
            i["_cat"] = etiqueta
            dia.append(i)
    todos = geo + pol + dia
    traducir(todos)
    nuevo = {"items": [limpiar(i) for i in geo],
             "politica": [limpiar(i) for i in pol],
             "diarias": [limpiar(i, i.pop("_cat")) for i in dia]}
    try:
        viejo = json.load(open(OUT, encoding="utf-8"))
    except Exception:
        viejo = {}
    for k in nuevo:                         # sección vacía -> se conserva la anterior
        if not nuevo[k]:
            nuevo[k] = viejo.get(k, [])
            print(f"AVISO: sin noticias nuevas en '{k}', se conserva lo anterior.")
    if not todos:
        print("ERROR: ninguna fuente entregó noticias nuevas.")
        if not os.path.exists(OUT):
            json.dump({"actualizado": None, **nuevo}, open(OUT, "w", encoding="utf-8"))
        sys.exit(1)
    nuevo = {"actualizado": now.isoformat(timespec="seconds"), **nuevo}
    json.dump(nuevo, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print(f"Listo: {len(geo)} geopolítica, {len(pol)} política, {len(dia)} diarias.")

if __name__ == "__main__":
    main()
