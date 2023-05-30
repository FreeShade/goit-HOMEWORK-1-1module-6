import re

CYRILLIC_SYMBOLS = "абвгдеєжзиіїйклмнопрстуфхцчшщьюя"
TRANSLATION = (
    "a",
    "b",
    "v",
    "g",
    "d",
    "e",
    "e",
    "j",
    "z",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "r",
    "s",
    "t",
    "u",
    "f",
    "h",
    "ts",
    "ch",
    "sh",
    "sch",
    "",
    "e",
    "",
    "yu",
    "u",
    "ja",
    "je",
    "ji",
    "g",
)

TRANS = {}
# maping
for cyrylic, trans in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[
        ord(cyrylic)
    ] = trans  # cyrylic = , trans = a   |    cyrylic = b, trans = b .....
    TRANS[ord(cyrylic.upper())] = trans.upper()


def normalize(name: str) -> str:
    t_name = name.translate(TRANS)  # perekladaemo
    t_name = re.sub(
        r"\W", "_", t_name
    )  # замінює всі символи, крім літер латинського алфавіту та цифр, на символ '_';
    return t_name
