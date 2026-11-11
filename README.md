<p align="center">
  <a href="#ru"><img alt="Русский" src="https://img.shields.io/badge/Русский-RU-9b6bff?style=for-the-badge"></a>
  <a href="#en"><img alt="English" src="https://img.shields.io/badge/English-EN-6ea8ff?style=for-the-badge"></a>
</p>

<h1 align="center">PypsCFG</h1>

<p align="center">
  <b>Subscription Aggregator · агрегатор подписок</b><br>
  <sub>VLESS · VMess · Trojan · Hysteria2 · TUIC — чистые списки TXT + Base64, автообновление каждые 4 часа</sub>
</p>

<p align="center">
  <a href="https://github.com/AmazingCoderA/PypsCFG/stargazers"><img alt="Stars" src="https://img.shields.io/github/stars/AmazingCoderA/PypsCFG?style=for-the-badge&logo=github&label=STARS&color=9b6bff"></a>
  <a href="https://github.com/AmazingCoderA/PypsCFG/forks"><img alt="Forks" src="https://img.shields.io/github/forks/AmazingCoderA/PypsCFG?style=for-the-badge&logo=github&label=FORKS&color=6ea8ff"></a>
  <img alt="Updated" src="https://img.shields.io/github/last-commit/AmazingCoderA/PypsCFG?style=for-the-badge&logo=github&label=UPDATED&color=4de8ff">
  <img alt="License" src="https://img.shields.io/github/license/AmazingCoderA/PypsCFG?style=for-the-badge&label=LICENSE&color=34d399">
</p>

<p align="center">
  <a href="https://raw.githubusercontent.com/AmazingCoderA/PypsCFG/main/output/BlackList.txt"><img alt="BlackList" src="https://img.shields.io/badge/⬛_BlackList-TXT-111827?style=for-the-badge"></a>
  <a href="https://raw.githubusercontent.com/AmazingCoderA/PypsCFG/main/output/WhiteList.txt"><img alt="WhiteList" src="https://img.shields.io/badge/⬜_WhiteList-TXT-1e293b?style=for-the-badge"></a>
  <a href="https://raw.githubusercontent.com/AmazingCoderA/PypsCFG/main/output/FavoriteSubBlack.txt"><img alt="FavoriteSubBlack" src="https://img.shields.io/badge/⭐_Favorite-TXT-9b6bff?style=for-the-badge"></a>
  <a href="https://raw.githubusercontent.com/AmazingCoderA/PypsCFG/main/output/LiteBlackList.txt"><img alt="LiteBlackList" src="https://img.shields.io/badge/🪶_Lite_BlackList-TXT-334155?style=for-the-badge"></a>
  <a href="https://raw.githubusercontent.com/AmazingCoderA/PypsCFG/main/output/LiteWhiteList.txt"><img alt="LiteWhiteList" src="https://img.shields.io/badge/🪶_Lite_WhiteList-TXT-475569?style=for-the-badge"></a>
  <a href="https://raw.githubusercontent.com/AmazingCoderA/PypsCFG/main/output/merged_all.txt"><img alt="merged_all" src="https://img.shields.io/badge/🧩_merged__all-TXT-4de8ff?style=for-the-badge"></a>
</p>

<p align="center">
  <a href="https://raw.githubusercontent.com/AmazingCoderA/PypsCFG/main/output/BlackListChecked.txt"><img alt="Checked" src="https://img.shields.io/badge/✅_Checked_lists-TXT-22c55e?style=for-the-badge"></a>
  <a href="https://raw.githubusercontent.com/AmazingCoderA/PypsCFG/main/output/BlackFiltredHy2VlessTrojan.txt"><img alt="Super-filter" src="https://img.shields.io/badge/⚡_Super--filter-Hy2_·_VLESS_·_Trojan-f59e0b?style=for-the-badge"></a>
  <a href="https://raw.githubusercontent.com/AmazingCoderA/PypsCFG/main/output/WhiteFiltredHy2VlessTrojan.txt"><img alt="White super-filter" src="https://img.shields.io/badge/🌸_White_super--filter-Reality_·_TLS-ec4899?style=for-the-badge"></a>
  <a href="https://raw.githubusercontent.com/AmazingCoderA/PypsCFG/main/output/merged_all_Checked.txt"><img alt="merged_all_Checked" src="https://img.shields.io/badge/🧪_merged__all__Checked-TXT-0ea5e9?style=for-the-badge"></a>
</p>

<p align="center">
  <img alt="Python" src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white">
  <img alt="GitHub Actions" src="https://img.shields.io/badge/GitHub_Actions-auto--update-2088FF?style=for-the-badge&logo=githubactions&logoColor=white">
  <img alt="Format" src="https://img.shields.io/badge/Format-TXT_%2B_Base64-8ea3c8?style=for-the-badge">
  <img alt="Protocols" src="https://img.shields.io/badge/VLESS_·_VMess_·_Trojan_·_Hy2_·_TUIC-supported-b28cff?style=for-the-badge">
</p>

---

# PypsCFG — Агрегатор подписок / Subscription Aggregator

<p align="center">
  <a href="#ru">Русский</a> •
  <a href="#en">English</a>
</p>

---

<a name="ru"></a>
## 🇷🇺 PypsCFG — Агрегатор подписок

### ℹ️ О проекте
**PypsCFG** — репозиторий, который собирает и регулярно обновляет подписки из разных источников в одном месте.

Автоматически:
- 📥 забирает списки из указанных источников
- 🧹 чистит «мусор» и пустые строки
- 🚫 удаляет `ss://` и `ssr://`
- ♻️ убирает дубли
- 📦 генерирует итоговые файлы `TXT` и `Base64`
- 🔄 обновляет результат через GitHub Actions

Подходит, если нужны одна/несколько удобных ссылок на **уже обработанные** списки.

> 📋 Источники разные. Если хотите увидеть авторов — смотрите входные файлы в корне репозитория: ссылки косвенно указывают на исходные проекты/авторов. Я лишь агрегирую, миксую и фильтрую.  
> ☢️ Ответственность за использование не несу — используйте во благо.  
> ⚫⚪ Не используйте whitelist-подписки, если у вас уже включены и нормально работают blacklists.

---

### ⚙️ Как это работает
Во входных файлах в корне репозитория указываются источники/конфиги:

- `BlackList`
- `WhiteList`
- `FavoriteSubBlack`
- `LiteBlackList`
- `LiteWhiteList`

Внутри этих файлов можно писать:
- URL на подписки
- готовые конфиги построчно

Если источник отдаёт **Base64**, он автоматически декодируется.  
Если источник отдаёт обычный текст — обрабатывается как есть.

---

### 🧩 Что фильтруется
Сохраняются только конфиги с протоколами:
- `vless://`
- `vmess://`
- `trojan://`
- `hysteria2://`
- `hy2://`
- `tuic://`

Удаляются:
- `ss://`
- `ssr://`
- пустые строки
- значительная часть дублей/повторов

---

### 📊 Типы списков
| Список | Назначение | Обновление | Формат |
| --- | --- | --- | --- |
| `BlackList` | основной чёрный список | часто | TXT + Base64 |
| `WhiteList` | основной белый список | часто | TXT + Base64 |
| `FavoriteSubBlack` | отдельная подборка | часто | TXT + Base64 |
| `LiteBlackList` | облегчённый чёрный список | часто | TXT + Base64 |
| `LiteWhiteList` | облегчённый белый список | часто | TXT + Base64 |
| `*Checked` | версии после проверки endpoint | реже | TXT + Base64 |
| `merged_all` | общий объединённый список | часто | TXT + Base64 |
| `merged_all_Checked` | общий checked-список | реже | TXT + Base64 |
| `BlackFiltredHy2VlessTrojan` | супер-фильтр (Vless Reality/Trojan/Hy2) | **каждые 4 часа** | TXT + Base64 |
| `WhiteFiltredHy2VlessTrojan` | белый супер-фильтр (Reality/TLS) | **каждые 4 часа** | TXT + Base64 |
| `BlackHy2Trojan` | только Hy2 и Trojan | **каждые 4 часа** | TXT + Base64 |
| `WhiteHy2Trojan` | белый список Hy2 и Trojan | **каждые 4 часа** | TXT + Base64 |

---

### 🔄 Автообновление
Два режима обновления:
- ⚡ **быстрое обновление** — обычная сборка без тяжёлой проверки: **каждые 4 часа**
- ✅ **checked-обновление** — сборка с многопоточной TCP-проверкой endpoint: **каждые 12 часов**

> Примечание: TCP-check проверяет доступность хоста/порта, но не гарантирует «полную работоспособность» конкретного протокола/узла.

---

### 🔗 Ссылки

#### GitHub Raw
<details>
<summary>Показать ссылки GitHub Raw</summary>

**Обычные списки**
- BlackList.txt — <https://raw.githubusercontent.com/AmazingCoderA/PypsCFG/main/output/BlackList.txt>
- BlackList.b64 — <https://raw.githubusercontent.com/AmazingCoderA/PypsCFG/main/output/BlackList.b64>
- WhiteList.txt — <https://raw.githubusercontent.com/AmazingCoderA/PypsCFG/main/output/WhiteList.txt>
- WhiteList.b64 — <https://raw.githubusercontent.com/AmazingCoderA/PypsCFG/main/output/WhiteList.b64>
- FavoriteSubBlack.txt — <https://raw.githubusercontent.com/AmazingCoderA/PypsCFG/main/output/FavoriteSubBlack.txt>
- FavoriteSubBlack.b64 — <https://raw.githubusercontent.com/AmazingCoderA/PypsCFG/main/output/FavoriteSubBlack.b64>
- LiteBlackList.txt — <https://raw.githubusercontent.com/AmazingCoderA/PypsCFG/main/output/LiteBlackList.txt>
- LiteBlackList.b64 — <https://raw.githubusercontent.com/AmazingCoderA/PypsCFG/main/output/LiteBlackList.b64>
- LiteWhiteList.txt — <https://raw.githubusercontent.com/AmazingCoderA/PypsCFG/main/output/LiteWhiteList.txt>
- LiteWhiteList.b64 — <https://raw.githubusercontent.com/AmazingCoderA/PypsCFG/main/output/LiteWhiteList.b64>
- merged_all.txt — <https://raw.githubusercontent.com/AmazingCoderA/PypsCFG/main/output/merged_all.txt>
- merged_all.b64 — <https://raw.githubusercontent.com/AmazingCoderA/PypsCFG/main/output/merged_all.b64>

**Checked-списки** (после проверки)
- BlackListChecked.txt — <https://raw.githubusercontent.com/AmazingCoderA/PypsCFG/main/output/BlackListChecked.txt>
- BlackListChecked.b64 — <https://raw.githubusercontent.com/AmazingCoderA/PypsCFG/main/output/BlackListChecked.b64>
- WhiteListChecked.txt — <https://raw.githubusercontent.com/AmazingCoderA/PypsCFG/main/output/WhiteListChecked.txt>
- WhiteListChecked.b64 — <https://raw.githubusercontent.com/AmazingCoderA/PypsCFG/main/output/WhiteListChecked.b64>
- FavoriteSubBlackChecked.txt — <https://raw.githubusercontent.com/AmazingCoderA/PypsCFG/main/output/FavoriteSubBlackChecked.txt>
- FavoriteSubBlackChecked.b64 — <https://raw.githubusercontent.com/AmazingCoderA/PypsCFG/main/output/FavoriteSubBlackChecked.b64>
- LiteBlackListChecked.txt — <https://raw.githubusercontent.com/AmazingCoderA/PypsCFG/main/output/LiteBlackListChecked.txt>
- LiteBlackListChecked.b64 — <https://raw.githubusercontent.com/AmazingCoderA/PypsCFG/main/output/LiteBlackListChecked.b64>
- LiteWhiteListChecked.txt — <https://raw.githubusercontent.com/AmazingCoderA/PypsCFG/main/output/LiteWhiteListChecked.txt>
- LiteWhiteListChecked.b64 — <https://raw.githubusercontent.com/AmazingCoderA/PypsCFG/main/output/LiteWhiteListChecked.b64>
- merged_all_Checked.txt — <https://raw.githubusercontent.com/AmazingCoderA/PypsCFG/main/output/merged_all_Checked.txt>
- merged_all_Checked.b64 — <https://raw.githubusercontent.com/AmazingCoderA/PypsCFG/main/output/merged_all_Checked.b64>

**Супер-фильтры**
- BlackFiltredHy2VlessTrojan.txt — <https://raw.githubusercontent.com/AmazingCoderA/PypsCFG/main/output/BlackFiltredHy2VlessTrojan.txt>
- BlackFiltredHy2VlessTrojan.b64 — <https://raw.githubusercontent.com/AmazingCoderA/PypsCFG/main/output/BlackFiltredHy2VlessTrojan.b64>
- WhiteFiltredHy2VlessTrojan.txt — <https://raw.githubusercontent.com/AmazingCoderA/PypsCFG/main/output/WhiteFiltredHy2VlessTrojan.txt>
- WhiteFiltredHy2VlessTrojan.b64 — <https://raw.githubusercontent.com/AmazingCoderA/PypsCFG/main/output/WhiteFiltredHy2VlessTrojan.b64>
- BlackHy2Trojan.txt — <https://raw.githubusercontent.com/AmazingCoderA/PypsCFG/main/output/BlackHy2Trojan.txt>
- BlackHy2Trojan.b64 — <https://raw.githubusercontent.com/AmazingCoderA/PypsCFG/main/output/BlackHy2Trojan.b64>
- WhiteHy2Trojan.txt — <https://raw.githubusercontent.com/AmazingCoderA/PypsCFG/main/output/WhiteHy2Trojan.txt>
- WhiteHy2Trojan.b64 — <https://raw.githubusercontent.com/AmazingCoderA/PypsCFG/main/output/WhiteHy2Trojan.b64>

</details>

#### jsDelivr (быстрее в некоторых регионах)
<details>
<summary>Показать ссылки jsDelivr</summary>

> Примечание: у jsDelivr бывает кэширование, обновление может приходить с задержкой.

**Обычные списки**
- BlackList.txt — <https://cdn.jsdelivr.net/gh/AmazingCoderA/PypsCFG@main/output/BlackList.txt>
- BlackList.b64 — <https://cdn.jsdelivr.net/gh/AmazingCoderA/PypsCFG@main/output/BlackList.b64>
- WhiteList.txt — <https://cdn.jsdelivr.net/gh/AmazingCoderA/PypsCFG@main/output/WhiteList.txt>
- WhiteList.b64 — <https://cdn.jsdelivr.net/gh/AmazingCoderA/PypsCFG@main/output/WhiteList.b64>
- FavoriteSubBlack.txt — <https://cdn.jsdelivr.net/gh/AmazingCoderA/PypsCFG@main/output/FavoriteSubBlack.txt>
- FavoriteSubBlack.b64 — <https://cdn.jsdelivr.net/gh/AmazingCoderA/PypsCFG@main/output/FavoriteSubBlack.b64>
- LiteBlackList.txt — <https://cdn.jsdelivr.net/gh/AmazingCoderA/PypsCFG@main/output/LiteBlackList.txt>
- LiteBlackList.b64 — <https://cdn.jsdelivr.net/gh/AmazingCoderA/PypsCFG@main/output/LiteBlackList.b64>
- LiteWhiteList.txt — <https://cdn.jsdelivr.net/gh/AmazingCoderA/PypsCFG@main/output/LiteWhiteList.txt>
- LiteWhiteList.b64 — <https://cdn.jsdelivr.net/gh/AmazingCoderA/PypsCFG@main/output/LiteWhiteList.b64>
- merged_all.txt — <https://cdn.jsdelivr.net/gh/AmazingCoderA/PypsCFG@main/output/merged_all.txt>
- merged_all.b64 — <https://cdn.jsdelivr.net/gh/AmazingCoderA/PypsCFG@main/output/merged_all.b64>

**Супер-фильтры**
- BlackFiltredHy2VlessTrojan.txt — <https://cdn.jsdelivr.net/gh/AmazingCoderA/PypsCFG@main/output/BlackFiltredHy2VlessTrojan.txt>
- BlackFiltredHy2VlessTrojan.b64 — <https://cdn.jsdelivr.net/gh/AmazingCoderA/PypsCFG@main/output/BlackFiltredHy2VlessTrojan.b64>
- WhiteFiltredHy2VlessTrojan.txt — <https://cdn.jsdelivr.net/gh/AmazingCoderA/PypsCFG@main/output/WhiteFiltredHy2VlessTrojan.txt>
- WhiteFiltredHy2VlessTrojan.b64 — <https://cdn.jsdelivr.net/gh/AmazingCoderA/PypsCFG@main/output/WhiteFiltredHy2VlessTrojan.b64>
- BlackHy2Trojan.txt — <https://cdn.jsdelivr.net/gh/AmazingCoderA/PypsCFG@main/output/BlackHy2Trojan.txt>
- BlackHy2Trojan.b64 — <https://cdn.jsdelivr.net/gh/AmazingCoderA/PypsCFG@main/output/BlackHy2Trojan.b64>
- WhiteHy2Trojan.txt — <https://cdn.jsdelivr.net/gh/AmazingCoderA/PypsCFG@main/output/WhiteHy2Trojan.txt>
- WhiteHy2Trojan.b64 — <https://cdn.jsdelivr.net/gh/AmazingCoderA/PypsCFG@main/output/WhiteHy2Trojan.b64>

**Checked-списки**
- BlackListChecked.txt — <https://cdn.jsdelivr.net/gh/AmazingCoderA/PypsCFG@main/output/BlackListChecked.txt>
- BlackListChecked.b64 — <https://cdn.jsdelivr.net/gh/AmazingCoderA/PypsCFG@main/output/BlackListChecked.b64>
- WhiteListChecked.txt — <https://cdn.jsdelivr.net/gh/AmazingCoderA/PypsCFG@main/output/WhiteListChecked.txt>
- WhiteListChecked.b64 — <https://cdn.jsdelivr.net/gh/AmazingCoderA/PypsCFG@main/output/WhiteListChecked.b64>
- FavoriteSubBlackChecked.txt — <https://cdn.jsdelivr.net/gh/AmazingCoderA/PypsCFG@main/output/FavoriteSubBlackChecked.txt>
- FavoriteSubBlackChecked.b64 — <https://cdn.jsdelivr.net/gh/AmazingCoderA/PypsCFG@main/output/FavoriteSubBlackChecked.b64>
- LiteBlackListChecked.txt — <https://cdn.jsdelivr.net/gh/AmazingCoderA/PypsCFG@main/output/LiteBlackListChecked.txt>
- LiteBlackListChecked.b64 — <https://cdn.jsdelivr.net/gh/AmazingCoderA/PypsCFG@main/output/LiteBlackListChecked.b64>
- LiteWhiteListChecked.txt — <https://cdn.jsdelivr.net/gh/AmazingCoderA/PypsCFG@main/output/LiteWhiteListChecked.txt>
- LiteWhiteListChecked.b64 — <https://cdn.jsdelivr.net/gh/AmazingCoderA/PypsCFG@main/output/LiteWhiteListChecked.b64>
- merged_all_Checked.txt — <https://cdn.jsdelivr.net/gh/AmazingCoderA/PypsCFG@main/output/merged_all_Checked.txt>
- merged_all_Checked.b64 — <https://cdn.jsdelivr.net/gh/AmazingCoderA/PypsCFG@main/output/merged_all_Checked.b64>

</details>

---

### 🛠️ Как использовать свои источники
1. Сделайте fork репозитория
2. Добавьте свои ссылки/конфиги во входные файлы в корне (`BlackList`, `WhiteList`, и т.д.)
3. При необходимости поправьте GitHub Actions (расписание/проверки)
4. Используйте сгенерированные ссылки из `output/`

---

<a name="en"></a>
## 🇬🇧 PypsCFG — Subscription Aggregator

### ℹ️ About
**PypsCFG** is a repository that aggregates and regularly updates subscriptions from multiple sources in one place.

It automatically:
- 📥 pulls lists from provided sources
- 🧹 removes junk and empty lines
- 🚫 drops `ss://` and `ssr://`
- ♻️ deduplicates entries
- 📦 generates clean `TXT` + `Base64` outputs
- 🔄 updates everything via GitHub Actions

Useful if you want one or a few ready-to-use links to **pre-processed** subscription lists.

> 📋 Sources are public and come from different places. If you want original authors/projects — check the input files in the repository root. I only collect, merge, and filter.  
> ☢️ Use at your own risk and responsibility.  
> ⚫⚪ Please don’t use whitelist subscriptions if your blacklists are already enabled and working as intended.

---

### ⚙️ How it works
Input files (in the repository root):
- `BlackList`
- `WhiteList`
- `FavoriteSubBlack`
- `LiteBlackList`
- `LiteWhiteList`

Each input file can contain:
- subscription URLs
- raw configs, one per line

If a source returns **Base64**, it is auto-decoded.  
If it returns plain text, it is processed as-is.

---

### 🧩 Filtering rules
Only these protocols are kept:
- `vless://`
- `vmess://`
- `trojan://`
- `hysteria2://`
- `hy2://`
- `tuic://`

Automatically removed:
- `ss://`
- `ssr://`
- empty lines
- many duplicates/repeats

---

### 📊 Output lists
| List | Purpose | Update rate | Format |
| --- | --- | --- | --- |
| `BlackList` | main blacklist | frequent | TXT + Base64 |
| `WhiteList` | main whitelist | frequent | TXT + Base64 |
| `FavoriteSubBlack` | curated/selected list | frequent | TXT + Base64 |
| `LiteBlackList` | lightweight blacklist | frequent | TXT + Base64 |
| `LiteWhiteList` | lightweight whitelist | frequent | TXT + Base64 |
| `*Checked` | lists after endpoint checking | less frequent | TXT + Base64 |
| `merged_all` | fully merged list | frequent | TXT + Base64 |
| `merged_all_Checked` | merged list after checks | less frequent | TXT + Base64 |
| `BlackFiltredHy2VlessTrojan` | super-filter (Vless Reality/Trojan/Hy2) | **every 4 hours** | TXT + Base64 |
| `WhiteFiltredHy2VlessTrojan` | white super-filter (Reality/TLS) | **every 4 hours** | TXT + Base64 |
| `BlackHy2Trojan` | only Hy2 and Trojan | **every 4 hours** | TXT + Base64 |
| `WhiteHy2Trojan` | white list of Hy2 and Trojan | **every 4 hours** | TXT + Base64 |

---

### 🔄 Auto update
Two update modes:
- ⚡ **fast update** — regular build without heavy checks: **every 4 hours**
- ✅ **checked update** — build with multi-threaded TCP endpoint checks: **every 12 hours**

> Note: TCP checks validate host/port reachability, but do not guarantee full protocol-level functionality.

---

### 🔗 Links

#### GitHub Raw
<details>
<summary>Show GitHub Raw links</summary>

**Regular lists**
- BlackList.txt — <https://raw.githubusercontent.com/AmazingCoderA/PypsCFG/main/output/BlackList.txt>
- BlackList.b64 — <https://raw.githubusercontent.com/AmazingCoderA/PypsCFG/main/output/BlackList.b64>
- WhiteList.txt — <https://raw.githubusercontent.com/AmazingCoderA/PypsCFG/main/output/WhiteList.txt>
- WhiteList.b64 — <https://raw.githubusercontent.com/AmazingCoderA/PypsCFG/main/output/WhiteList.b64>
- FavoriteSubBlack.txt — <https://raw.githubusercontent.com/AmazingCoderA/PypsCFG/main/output/FavoriteSubBlack.txt>
- FavoriteSubBlack.b64 — <https://raw.githubusercontent.com/AmazingCoderA/PypsCFG/main/output/FavoriteSubBlack.b64>
- LiteBlackList.txt — <https://raw.githubusercontent.com/AmazingCoderA/PypsCFG/main/output/LiteBlackList.txt>
- LiteBlackList.b64 — <https://raw.githubusercontent.com/AmazingCoderA/PypsCFG/main/output/LiteBlackList.b64>
- LiteWhiteList.txt — <https://raw.githubusercontent.com/AmazingCoderA/PypsCFG/main/output/LiteWhiteList.txt>
- LiteWhiteList.b64 — <https://raw.githubusercontent.com/AmazingCoderA/PypsCFG/main/output/LiteWhiteList.b64>
- merged_all.txt — <https://raw.githubusercontent.com/AmazingCoderA/PypsCFG/main/output/merged_all.txt>
- merged_all.b64 — <https://raw.githubusercontent.com/AmazingCoderA/PypsCFG/main/output/merged_all.b64>

**Checked lists** (after checking)
- BlackListChecked.txt — <https://raw.githubusercontent.com/AmazingCoderA/PypsCFG/main/output/BlackListChecked.txt>
- BlackListChecked.b64 — <https://raw.githubusercontent.com/AmazingCoderA/PypsCFG/main/output/BlackListChecked.b64>
- WhiteListChecked.txt — <https://raw.githubusercontent.com/AmazingCoderA/PypsCFG/main/output/WhiteListChecked.txt>
- WhiteListChecked.b64 — <https://raw.githubusercontent.com/AmazingCoderA/PypsCFG/main/output/WhiteListChecked.b64>
- FavoriteSubBlackChecked.txt — <https://raw.githubusercontent.com/AmazingCoderA/PypsCFG/main/output/FavoriteSubBlackChecked.txt>
- FavoriteSubBlackChecked.b64 — <https://raw.githubusercontent.com/AmazingCoderA/PypsCFG/main/output/FavoriteSubBlackChecked.b64>
- LiteBlackListChecked.txt — <https://raw.githubusercontent.com/AmazingCoderA/PypsCFG/main/output/LiteBlackListChecked.txt>
- LiteBlackListChecked.b64 — <https://raw.githubusercontent.com/AmazingCoderA/PypsCFG/main/output/LiteBlackListChecked.b64>
- LiteWhiteListChecked.txt — <https://raw.githubusercontent.com/AmazingCoderA/PypsCFG/main/output/LiteWhiteListChecked.txt>
- LiteWhiteListChecked.b64 — <https://raw.githubusercontent.com/AmazingCoderA/PypsCFG/main/output/LiteWhiteListChecked.b64>
- merged_all_Checked.txt — <https://raw.githubusercontent.com/AmazingCoderA/PypsCFG/main/output/merged_all_Checked.txt>
- merged_all_Checked.b64 — <https://raw.githubusercontent.com/AmazingCoderA/PypsCFG/main/output/merged_all_Checked.b64>

**Super-filters**
- BlackFiltredHy2VlessTrojan.txt — <https://raw.githubusercontent.com/AmazingCoderA/PypsCFG/main/output/BlackFiltredHy2VlessTrojan.txt>
- BlackFiltredHy2VlessTrojan.b64 — <https://raw.githubusercontent.com/AmazingCoderA/PypsCFG/main/output/BlackFiltredHy2VlessTrojan.b64>
- WhiteFiltredHy2VlessTrojan.txt — <https://raw.githubusercontent.com/AmazingCoderA/PypsCFG/main/output/WhiteFiltredHy2VlessTrojan.txt>
- WhiteFiltredHy2VlessTrojan.b64 — <https://raw.githubusercontent.com/AmazingCoderA/PypsCFG/main/output/WhiteFiltredHy2VlessTrojan.b64>
- BlackHy2Trojan.txt — <https://raw.githubusercontent.com/AmazingCoderA/PypsCFG/main/output/BlackHy2Trojan.txt>
- BlackHy2Trojan.b64 — <https://raw.githubusercontent.com/AmazingCoderA/PypsCFG/main/output/BlackHy2Trojan.b64>
- WhiteHy2Trojan.txt — <https://raw.githubusercontent.com/AmazingCoderA/PypsCFG/main/output/WhiteHy2Trojan.txt>
- WhiteHy2Trojan.b64 — <https://raw.githubusercontent.com/AmazingCoderA/PypsCFG/main/output/WhiteHy2Trojan.b64>

</details>

#### jsDelivr (faster in some regions)
<details>
<summary>Show jsDelivr links</summary>

> Note: jsDelivr uses caching, updates might be delayed.

**Regular lists**
- BlackList.txt — <https://cdn.jsdelivr.net/gh/AmazingCoderA/PypsCFG@main/output/BlackList.txt>
- BlackList.b64 — <https://cdn.jsdelivr.net/gh/AmazingCoderA/PypsCFG@main/output/BlackList.b64>
- WhiteList.txt — <https://cdn.jsdelivr.net/gh/AmazingCoderA/PypsCFG@main/output/WhiteList.txt>
- WhiteList.b64 — <https://cdn.jsdelivr.net/gh/AmazingCoderA/PypsCFG@main/output/WhiteList.b64>
- FavoriteSubBlack.txt — <https://cdn.jsdelivr.net/gh/AmazingCoderA/PypsCFG@main/output/FavoriteSubBlack.txt>
- FavoriteSubBlack.b64 — <https://cdn.jsdelivr.net/gh/AmazingCoderA/PypsCFG@main/output/FavoriteSubBlack.b64>
- LiteBlackList.txt — <https://cdn.jsdelivr.net/gh/AmazingCoderA/PypsCFG@main/output/LiteBlackList.txt>
- LiteBlackList.b64 — <https://cdn.jsdelivr.net/gh/AmazingCoderA/PypsCFG@main/output/LiteBlackList.b64>
- LiteWhiteList.txt — <https://cdn.jsdelivr.net/gh/AmazingCoderA/PypsCFG@main/output/LiteWhiteList.txt>
- LiteWhiteList.b64 — <https://cdn.jsdelivr.net/gh/AmazingCoderA/PypsCFG@main/output/LiteWhiteList.b64>
- merged_all.txt — <https://cdn.jsdelivr.net/gh/AmazingCoderA/PypsCFG@main/output/merged_all.txt>
- merged_all.b64 — <https://cdn.jsdelivr.net/gh/AmazingCoderA/PypsCFG@main/output/merged_all.b64>

**Super-filters**
- BlackFiltredHy2VlessTrojan.txt — <https://cdn.jsdelivr.net/gh/AmazingCoderA/PypsCFG@main/output/BlackFiltredHy2VlessTrojan.txt>
- BlackFiltredHy2VlessTrojan.b64 — <https://cdn.jsdelivr.net/gh/AmazingCoderA/PypsCFG@main/output/BlackFiltredHy2VlessTrojan.b64>
- WhiteFiltredHy2VlessTrojan.txt — <https://cdn.jsdelivr.net/gh/AmazingCoderA/PypsCFG@main/output/WhiteFiltredHy2VlessTrojan.txt>
- WhiteFiltredHy2VlessTrojan.b64 — <https://cdn.jsdelivr.net/gh/AmazingCoderA/PypsCFG@main/output/WhiteFiltredHy2VlessTrojan.b64>
- BlackHy2Trojan.txt — <https://cdn.jsdelivr.net/gh/AmazingCoderA/PypsCFG@main/output/BlackHy2Trojan.txt>
- BlackHy2Trojan.b64 — <https://cdn.jsdelivr.net/gh/AmazingCoderA/PypsCFG@main/output/BlackHy2Trojan.b64>
- WhiteHy2Trojan.txt — <https://cdn.jsdelivr.net/gh/AmazingCoderA/PypsCFG@main/output/WhiteHy2Trojan.txt>
- WhiteHy2Trojan.b64 — <https://cdn.jsdelivr.net/gh/AmazingCoderA/PypsCFG@main/output/WhiteHy2Trojan.b64>

**Checked lists**
- BlackListChecked.txt — <https://cdn.jsdelivr.net/gh/AmazingCoderA/PypsCFG@main/output/BlackListChecked.txt>
- BlackListChecked.b64 — <https://cdn.jsdelivr.net/gh/AmazingCoderA/PypsCFG@main/output/BlackListChecked.b64>
- WhiteListChecked.txt — <https://cdn.jsdelivr.net/gh/AmazingCoderA/PypsCFG@main/output/WhiteListChecked.txt>
- WhiteListChecked.b64 — <https://cdn.jsdelivr.net/gh/AmazingCoderA/PypsCFG@main/output/WhiteListChecked.b64>
- FavoriteSubBlackChecked.txt — <https://cdn.jsdelivr.net/gh/AmazingCoderA/PypsCFG@main/output/FavoriteSubBlackChecked.txt>
- FavoriteSubBlackChecked.b64 — <https://cdn.jsdelivr.net/gh/AmazingCoderA/PypsCFG@main/output/FavoriteSubBlackChecked.b64>
- LiteBlackListChecked.txt — <https://cdn.jsdelivr.net/gh/AmazingCoderA/PypsCFG@main/output/LiteBlackListChecked.txt>
- LiteBlackListChecked.b64 — <https://cdn.jsdelivr.net/gh/AmazingCoderA/PypsCFG@main/output/LiteBlackListChecked.b64>
- LiteWhiteListChecked.txt — <https://cdn.jsdelivr.net/gh/AmazingCoderA/PypsCFG@main/output/LiteWhiteListChecked.txt>
- LiteWhiteListChecked.b64 — <https://cdn.jsdelivr.net/gh/AmazingCoderA/PypsCFG@main/output/LiteWhiteListChecked.b64>
- merged_all_Checked.txt — <https://cdn.jsdelivr.net/gh/AmazingCoderA/PypsCFG@main/output/merged_all_Checked.txt>
- merged_all_Checked.b64 — <https://cdn.jsdelivr.net/gh/AmazingCoderA/PypsCFG@main/output/merged_all_Checked.b64>

</details>

---

### 🛠️ Using your own sources
1. Fork the repository
2. Add your links/configs to the root input files (`BlackList`, `WhiteList`, etc.)
3. Adjust GitHub Actions if needed (schedule/checking)
4. Use generated links from `output/`
