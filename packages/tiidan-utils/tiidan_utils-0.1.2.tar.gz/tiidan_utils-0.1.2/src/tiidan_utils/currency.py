import re


def parse_chinese_number(number_string: str):
    TENS_OF_CHARS = {
        # https: // en.wikipedia.org / wiki / Chinese_numerals
        "一": 1,  # Normal
        "壹": 1,  # Financial / Tradination
        "十": 10,
        "拾": 10,
        "百": 100,
        "佰": 100,
        "千": 1000,
        "仟": 1000,
        "万": 10000,
        "萬": 10000,
        "亿": 100000000,
        "億": 100000000,
    }
    tens_of = 1
    for char, value in TENS_OF_CHARS.items():
        if char in number_string:
            number_string = number_string.replace(char, "")
            tens_of = tens_of * value
    number_string = re.search(r"\d+(\.\d*)?", number_string).group()
    return float(number_string) * tens_of


def get_currency(currency_str):
    currency_symbols = {"JPY": "日元", "USD": "美元", "CNY": "人民币", "EUR": "欧", "HKD": "港"}
    for k, v in currency_symbols.items():
        if v in currency_str:
            return k
    return "CNY"


def convert(from_, to):
    CACHED = {"JPY_USD": 0.0091, "EUR_USD": 1.11, "CNY_USD": 0.14, "HKD_USD": 0.13}
    return CACHED[from_ + "_" + to]
