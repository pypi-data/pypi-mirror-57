import datetime
import logging
import os
import re
from .aws_utils import translate

log = logging.getLogger(__name__)


def today_string():
    return datetime.datetime.now().strftime("%Y%m%d%")


def now_string():
    return (
        datetime.datetime.now()
        .isoformat()
        .split(".")[0]
        .replace("-", "")
        .replace(":", "")
    )


def set_path(dct, value, path=None):
    if path is None:
        path = []
    current = dct
    last = path[-1]
    for key in path[:-1]:
        if current.get(key) is None:
            current[key] = {}
        current = current[key]
    current[last] = value


def get_path(dct, path=None):
    if path is None:
        path = []
    current = dct
    last = path[-1]
    for key in path[:-1]:
        if current.get(key) is not None:
            current = current[key]
    return current[last]


def filify(params: dict):
    string = ""
    for key, value in params.items():
        string += "$"
        string += key.replace(".", "-")
        string += "#"
        string += str(value).replace(".", "-")
    return string


def generate_file_name(directory="reports", prefix="", suffix="", ext=""):
    fmt = {
        "prefix": "" if len(prefix) == 0 else "{}_".format(prefix),
        "suffix": "" if len(suffix) == 0 else "_{}".format(suffix),
        "date": datetime.now().isoformat().replace("-", "").replace(":", "")[:15],
        "ext": "" if len(ext) == 0 else ".{}".format(ext),
    }
    return os.path.join(directory, "{prefix}{date}{suffix}{ext}".format(**fmt))


def translate_dataframe_columns(df):
    df = df.copy()
    df.columns = map(
        lambda x: translate(x) if re.search(r"[^\x00-\x7F]", x) else x, df.columns
    )
    return df


def get_trade_search(name):
    regexes = [
        {"pattern": r"[\[\]()\\ /:;\'.,`-]"},
        {"pattern": r"\n"},
        {"pattern": r"co\s*ltd.*"},
        {"pattern": r"(limited)|(\blt?d?)\b"},
        {"pattern": r"\bco?r?p?o?r?a?t?i?o?n?\b"},
        {"pattern": r"\bimp?o?r?t?\b"},
        {"pattern": r"\bexp?o?r?t?\b"},
        {"pattern": r"\binco?r?p?o?r?a?t?e?d?\b"},
        {"pattern": r"\bsha\b"},
        {"pattern": r"\bbldg\b"},
        {"pattern": r"\band\b"},
        {"pattern": r"\bsh\b"},
        {"pattern": r"&"},
        {"pattern": r"\bi\s*e\b"},
        {"pattern": r"\bgroup\b"},
        {"pattern": r"\s+xing\b", "replace": "xing"},
        {"pattern": r"\s+lumin\b", "replace": "lumin"},
        {"pattern": r"\bkg\b"},
        {"pattern": r"\bengi\b"},
        {"pattern": r"\ban\b"},
        {"pattern": r"\bshang\s+yi\b", "replace": "shangyi"},
        {"pattern": r"\bgmbh\b"},
        {"pattern": r"\bindustrical\b", "replace": "industrial"},
        {"pattern": r"\bcompany\b"},
        {"pattern": r"\beconomic\b", "replace": "economy"},
        {"pattern": r"\binstrum?e?n?t?s?a?l?\b", "replace": "instrum"},
        {"pattern": r"\btrading\b"},
        {"pattern": r"\btrade?(ing)?\b"},
        {"pattern": r"\bno\b"},
        {"pattern": r"\s+"},
    ]
    trade_search = name.lower()
    for r in regexes:
        log.debug("applying pattern: {}".format(r["pattern"]))
        trade_search = re.sub(r["pattern"], r.get("replace", " "), trade_search)
    return trade_search.strip()


def get_param(key):
    return key.split("/")[-1].split(".")[0]
