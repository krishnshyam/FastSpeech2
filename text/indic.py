cons = [
    "p",
    "t̪",
    "ʈ",
    "k",
    "tʃ",
    "m",
    "n",
    "ɳ",
    "ɾ",
    "ʋ",
    "l",
    "ɻ",
    "ɭ",
    "j",
]
vow = [
    "i",
    "u",
    "e",
    "o",
    "a",
    "aɪ",
    "aʊ"
]

long_vow = [s + "ː" for s in vow]

valid_symbols = cons + vow + long_vow