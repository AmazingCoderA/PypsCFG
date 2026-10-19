"""Super filter: Vless Reality / Trojan / Hy2 only.

Собирает исходники (локальные файлы + URL-подписки внутри них),
декодирует Base64, фильтрует протоколы, сортирует: Reality > Vision > TLS.
"""
import base64
import re
import urllib.request
from pathlib import Path

BLACK_SOURCES = ["BlackList", "FavoriteSubBlack", "LiteBlackList"]
WHITE_SOURCES = ["WhiteList", "LiteWhiteList"]

OUTPUT_DIR = Path("output")
OUTPUT_DIR.mkdir(exist_ok=True)

ALLOWED_PREFIXES = ("vless://", "trojan://", "hysteria2://", "hy2://")


def get_score(line: str) -> int:
    """Приоритет: Reality > Vision > TLS"""
    low = line.lower()
    if "security=reality" in low:
        return 50
    if "flow=xtls-rprx-vision" in low:
        return 30
    if "security=tls" in low or "sni=" in low:
        return 20
    return 0


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
        headers={"User-Agent": "Mozilla/5.0 PypsCFG-SuperFilter", "Accept": "*/*"},
    )
    with urllib.request.urlopen(req, timeout=20) as r:
        return r.read().decode("utf-8", errors="ignore")


def expand_source(source: str):
    """source — имя файла или URL; возвращает список строк-конфигов."""
    source = source.strip()
    text = ""
    if source.startswith("http"):
        try:
            text = fetch_text(source)
        except Exception as e:
            print(f"[FETCH FAIL] {source} -> {e}")
            return []

    if not text:
        path = Path(source)
        if path.exists():
            text = path.read_text(encoding="utf-8", errors="ignore")
        else:
            return []

    lines = []
    for line in text.replace("\r", "\n").split("\n"):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        lines.append(line)

    for line in list(lines):
        if line.startswith("http"):
            # строка внутри файла — это подписка-URL, забираем её содержимое
            try:
                sub = fetch_text(line)
                if looks_like_base64_blob(sub):
                    sub = try_decode_base64_text(sub)
                lines.extend(sub.replace("\r", "\n").split("\n"))
            except Exception as e:
                print(f"[FETCH FAIL] {line} -> {e}")
        else:
            lines.append(line)
    return lines


def process_list(files_list):
    """Сбор, декодирование и фильтрация ссылок"""
    unique_links = set()
    for filename in files_list:
        for sub_line in expand_source(filename):
            sub_line = sub_line.strip()
            low = sub_line.lower()
            if low.startswith(ALLOWED_PREFIXES):
                unique_links.add(sub_line.split()[0])

    # Сортировка по весу (Reality наверх)
    return sorted(unique_links, key=get_score, reverse=True)


def save_files(name_prefix, links):
    """Сохранение .txt и .b64"""
    if not links:
        return
    txt_data = "\n".join(links).strip() + "\n"

    (OUTPUT_DIR / f"{name_prefix}FiltredHy2VlessTrojan.txt").write_text(txt_data, encoding="utf-8")

    b64_data = base64.b64encode(txt_data.encode("utf-8")).decode("ascii")
    (OUTPUT_DIR / f"{name_prefix}FiltredHy2VlessTrojan.b64").write_text(b64_data, encoding="utf-8")


def main():
    black_links = process_list(BLACK_SOURCES)
    save_files("Black", black_links)

    white_links = process_list(WHITE_SOURCES)
    save_files("White", white_links)

    print(f"Готово! Black: {len(black_links)}, White: {len(white_links)}")


if __name__ == "__main__":
    main()
