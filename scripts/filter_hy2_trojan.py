"""Фильтр: только Hysteria2/Hy2 и Trojan.

Собирает исходники (локальные файлы + URL-подписки внутри них),
декодирует Base64, фильтрует протоколы.
"""
import base64
import re
import urllib.request
from pathlib import Path

BLACK_SOURCES = [
    "BlackList",
    "FavoriteSubBlack",
    "LiteBlackList",
    "https://cdn.jsdelivr.net/gh/EtoNeYaProject/EtoNeYaProject.github.io@refs/heads/main/youtube",
]

WHITE_SOURCES = ["WhiteList", "LiteWhiteList"]

OUTPUT_DIR = Path("output")
OUTPUT_DIR.mkdir(exist_ok=True)

ALLOWED_PREFIXES = ("trojan://", "hysteria2://", "hy2://")


def looks_like_base64_blob(text: str) -> bool:
    s = "".join(text.strip().split())
    if not s or len(s) < 16 or "://" in text:
        return False
    return re.fullmatch(r"[A-Za-z0-9+/=]+", s) is not None


def try_decode_base64_text(text: str) -> str:
    s = "".join(text.strip().split())
    s += "=" * ((4 - len(s) % 4) % 4)
    try:
        out = base64.b64decode(s).decode("utf-8", errors="ignore")
        if "://" in out or "\n" in out:
            return out
    except Exception:
        pass
    return text


def fetch_text(url: str) -> str:
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "Mozilla/5.0 PypsCFG-Hy2Trojan", "Accept": "*/*"},
    )
    with urllib.request.urlopen(req, timeout=25) as r:
        return r.read().decode("utf-8", errors="ignore")


def read_source(source: str) -> str:
    source = source.strip()
    if source.startswith("http"):
        try:
            return fetch_text(source)
        except Exception as e:
            print(f"[FETCH FAIL] {source} -> {e}")
            return ""

    path = Path(source)
    if path.exists():
        return path.read_text(encoding="utf-8", errors="ignore")
    return ""


def score(line: str) -> int:
    low = line.lower()
    if "trojan://" in low:
        return 100
    if "hysteria2://" in low or "hy2://" in low:
        return 80
    return 0


def collect_lines(content: str):
    """Сначала простой список строк, затем загрузка URL-подписок внутри."""
    lines = []
    for x in content.replace("\r", "\n").split("\n"):
        x = x.strip()
        if x and not x.startswith("#"):
            lines.append(x)

    for line in list(lines):
        if not line.startswith("http"):
            continue
        try:
            sub = fetch_text(line)
            if looks_like_base64_blob(sub):
                sub = try_decode_base64_text(sub)
        except Exception as e:
            print(f"[FETCH FAIL] {line} -> {e}")
            continue
        for y in sub.replace("\r", "\n").split("\n"):
            y = y.strip()
            if y and not y.startswith("#"):
                lines.append(y)
    return lines


def process(sources):
    links = set()

    for src in sources:
        content = read_source(src)
        if not content:
            continue

        for line in collect_lines(content):
            low = line.lower()
            if low.startswith(ALLOWED_PREFIXES):
                links.add(line.split()[0])

    return sorted(links, key=score, reverse=True)


def save(name, links):
    txt = OUTPUT_DIR / f"{name}.txt"
    b64 = OUTPUT_DIR / f"{name}.b64"

    data = "\n".join(links) + ("\n" if links else "")

    txt.write_text(data, encoding="utf-8")
    b64.write_text(base64.b64encode(data.encode()).decode(), encoding="utf-8")

    print(f"{name}: {len(links)} links")


def main():
    black = process(BLACK_SOURCES)
    white = process(WHITE_SOURCES)

    save("BlackHy2Trojan", black)
    save("WhiteHy2Trojan", white)

    print("DONE")


if __name__ == "__main__":
    main()
