#  Copyright 2020-2024 Capypara and the SkyTemple Contributors
#
#  This file is part of SkyTemple.
#
#  SkyTemple is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  SkyTemple is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with SkyTemple.  If not, see <https://www.gnu.org/licenses/>.

# fmt: off
DEFAULTMONSTERPOOL = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 399, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 424, 425, 426, 427, 428, 429, 430, 431, 432, 433, 434, 435, 436, 437, 438, 439, 440, 441, 442, 443, 444, 445, 446, 447, 448, 449, 450, 451, 452, 453, 454, 455, 456, 457, 458, 459, 460, 461, 462, 463, 464, 465, 466, 467, 468, 469, 470, 471, 472, 473, 474, 475, 476, 477, 478, 479, 480, 481, 482, 483, 484, 485, 486, 487, 488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530, 531, 532, 533, 534, 535, 536]
DEFAULTMOVEPOOL = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 360, 394, 430, 431, 432, 433, 434, 435, 436, 437, 438, 439, 440, 441, 442, 443, 444, 445, 446, 447, 448, 449, 450, 451, 452, 453, 454, 455, 456, 457, 458, 459, 460, 461, 462, 463, 464, 465, 466, 468, 469, 470, 471, 472, 473, 474, 475, 476, 477, 478, 479, 480, 481, 482, 483, 484, 485, 486, 487, 488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530, 531, 532, 533, 534, 535, 536, 537, 538, 539, 540, 541]
DEFAULTABILITYPOOL = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 107, 108, 109, 110, 111, 112, 113, 114, 115, 117, 118, 119, 120, 121, 122, 123]
# fmt: on

MONSTERS = {
    0: "??????????",
    1: "Bulbasaur",
    2: "Ivysaur",
    3: "Venusaur",
    4: "Charmander",
    5: "Charmeleon",
    6: "Charizard",
    7: "Squirtle",
    8: "Wartortle",
    9: "Blastoise",
    10: "Caterpie",
    11: "Metapod",
    12: "Butterfree",
    13: "Weedle",
    14: "Kakuna",
    15: "Beedrill",
    16: "Pidgey",
    17: "Pidgeotto",
    18: "Pidgeot",
    19: "Rattata",
    20: "Raticate",
    21: "Spearow",
    22: "Fearow",
    23: "Ekans",
    24: "Arbok",
    25: "Pikachu",
    26: "Raichu",
    27: "Sandshrew",
    28: "Sandslash",
    29: "Nidoran♀",
    30: "Nidorina",
    31: "Nidoqueen",
    32: "Nidoran♂",
    33: "Nidorino",
    34: "Nidoking",
    35: "Clefairy",
    36: "Clefable",
    37: "Vulpix",
    38: "Ninetales",
    39: "Jigglypuff",
    40: "Wigglytuff",
    41: "Zubat",
    42: "Golbat",
    43: "Oddish",
    44: "Gloom",
    45: "Vileplume",
    46: "Paras",
    47: "Parasect",
    48: "Venonat",
    49: "Venomoth",
    50: "Diglett",
    51: "Dugtrio",
    52: "Meowth",
    53: "Persian",
    54: "Psyduck",
    55: "Golduck",
    56: "Mankey",
    57: "Primeape",
    58: "Growlithe",
    59: "Arcanine",
    60: "Poliwag",
    61: "Poliwhirl",
    62: "Poliwrath",
    63: "Abra",
    64: "Kadabra",
    65: "Alakazam",
    66: "Machop",
    67: "Machoke",
    68: "Machamp",
    69: "Bellsprout",
    70: "Weepinbell",
    71: "Victreebel",
    72: "Tentacool",
    73: "Tentacruel",
    74: "Geodude",
    75: "Graveler",
    76: "Golem",
    77: "Ponyta",
    78: "Rapidash",
    79: "Slowpoke",
    80: "Slowbro",
    81: "Magnemite",
    82: "Magneton",
    83: "Farfetch'd",
    84: "Doduo",
    85: "Dodrio",
    86: "Seel",
    87: "Dewgong",
    88: "Grimer",
    89: "Muk",
    90: "Shellder",
    91: "Cloyster",
    92: "Gastly",
    93: "Haunter",
    94: "Gengar",
    95: "Onix",
    96: "Drowzee",
    97: "Hypno",
    98: "Krabby",
    99: "Kingler",
    100: "Voltorb",
    101: "Electrode",
    102: "Exeggcute",
    103: "Exeggutor",
    104: "Cubone",
    105: "Marowak",
    106: "Hitmonlee",
    107: "Hitmonchan",
    108: "Lickitung",
    109: "Koffing",
    110: "Weezing",
    111: "Rhyhorn",
    112: "Rhydon",
    113: "Chansey",
    114: "Tangela",
    115: "Kangaskhan",
    116: "Horsea",
    117: "Seadra",
    118: "Goldeen",
    119: "Seaking",
    120: "Staryu",
    121: "Starmie",
    122: "Mr. Mime",
    123: "Scyther",
    124: "Jynx",
    125: "Electabuzz",
    126: "Magmar",
    127: "Pinsir",
    128: "Tauros",
    129: "Magikarp",
    130: "Gyarados",
    131: "Lapras",
    132: "Ditto",
    133: "Eevee",
    134: "Vaporeon",
    135: "Jolteon",
    136: "Flareon",
    137: "Porygon",
    138: "Omanyte",
    139: "Omastar",
    140: "Kabuto",
    141: "Kabutops",
    142: "Aerodactyl",
    143: "Snorlax",
    144: "Articuno",
    145: "Zapdos",
    146: "Moltres",
    147: "Dratini",
    148: "Dragonair",
    149: "Dragonite",
    150: "Mewtwo",
    151: "Mew",
    152: "Chikorita",
    153: "Bayleef",
    154: "Meganium",
    155: "Cyndaquil",
    156: "Quilava",
    157: "Typhlosion",
    158: "Totodile",
    159: "Croconaw",
    160: "Feraligatr",
    161: "Sentret",
    162: "Furret",
    163: "Hoothoot",
    164: "Noctowl",
    165: "Ledyba",
    166: "Ledian",
    167: "Spinarak",
    168: "Ariados",
    169: "Crobat",
    170: "Chinchou",
    171: "Lanturn",
    172: "Pichu",
    173: "Cleffa",
    174: "Igglybuff",
    175: "Togepi",
    176: "Togetic",
    177: "Natu",
    178: "Xatu",
    179: "Mareep",
    180: "Flaaffy",
    181: "Ampharos",
    182: "Bellossom",
    183: "Marill",
    184: "Azumarill",
    185: "Sudowoodo",
    186: "Politoed",
    187: "Hoppip",
    188: "Skiploom",
    189: "Jumpluff",
    190: "Aipom",
    191: "Sunkern",
    192: "Sunflora",
    193: "Yanma",
    194: "Wooper",
    195: "Quagsire",
    196: "Espeon",
    197: "Umbreon",
    198: "Murkrow",
    199: "Slowking",
    200: "Misdreavus",
    201: "Unown",
    202: "Unown",
    203: "Unown",
    204: "Unown",
    205: "Unown",
    206: "Unown",
    207: "Unown",
    208: "Unown",
    209: "Unown",
    210: "Unown",
    211: "Unown",
    212: "Unown",
    213: "Unown",
    214: "Unown",
    215: "Unown",
    216: "Unown",
    217: "Unown",
    218: "Unown",
    219: "Unown",
    220: "Unown",
    221: "Unown",
    222: "Unown",
    223: "Unown",
    224: "Unown",
    225: "Unown",
    226: "Unown",
    227: "Unown",
    228: "Unown",
    229: "Wobbuffet",
    230: "Girafarig",
    231: "Pineco",
    232: "Forretress",
    233: "Dunsparce",
    234: "Gligar",
    235: "Steelix",
    236: "Snubbull",
    237: "Granbull",
    238: "Qwilfish",
    239: "Scizor",
    240: "Shuckle",
    241: "Heracross",
    242: "Sneasel",
    243: "Teddiursa",
    244: "Ursaring",
    245: "Slugma",
    246: "Magcargo",
    247: "Swinub",
    248: "Piloswine",
    249: "Corsola",
    250: "Remoraid",
    251: "Octillery",
    252: "Delibird",
    253: "Mantine",
    254: "Skarmory",
    255: "Houndour",
    256: "Houndoom",
    257: "Kingdra",
    258: "Phanpy",
    259: "Donphan",
    260: "Porygon2",
    261: "Stantler",
    262: "Smeargle",
    263: "Tyrogue",
    264: "Hitmontop",
    265: "Smoochum",
    266: "Elekid",
    267: "Magby",
    268: "Miltank",
    269: "Blissey",
    270: "Raikou",
    271: "Entei",
    272: "Suicune",
    273: "Larvitar",
    274: "Pupitar",
    275: "Tyranitar",
    276: "Lugia",
    277: "Ho-Oh",
    278: "Celebi",
    279: "Celebi",
    280: "Treecko",
    281: "Grovyle",
    282: "Sceptile",
    283: "Torchic",
    284: "Combusken",
    285: "Blaziken",
    286: "Mudkip",
    287: "Marshtomp",
    288: "Swampert",
    289: "Poochyena",
    290: "Mightyena",
    291: "Zigzagoon",
    292: "Linoone",
    293: "Wurmple",
    294: "Silcoon",
    295: "Beautifly",
    296: "Cascoon",
    297: "Dustox",
    298: "Lotad",
    299: "Lombre",
    300: "Ludicolo",
    301: "Seedot",
    302: "Nuzleaf",
    303: "Shiftry",
    304: "Taillow",
    305: "Swellow",
    306: "Wingull",
    307: "Pelipper",
    308: "Ralts",
    309: "Kirlia",
    310: "Gardevoir",
    311: "Surskit",
    312: "Masquerain",
    313: "Shroomish",
    314: "Breloom",
    315: "Slakoth",
    316: "Vigoroth",
    317: "Slaking",
    318: "Nincada",
    319: "Ninjask",
    320: "Shedinja",
    321: "Whismur",
    322: "Loudred",
    323: "Exploud",
    324: "Makuhita",
    325: "Hariyama",
    326: "Azurill",
    327: "Nosepass",
    328: "Skitty",
    329: "Delcatty",
    330: "Sableye",
    331: "Mawile",
    332: "Aron",
    333: "Lairon",
    334: "Aggron",
    335: "Meditite",
    336: "Medicham",
    337: "Electrike",
    338: "Manectric",
    339: "Plusle",
    340: "Minun",
    341: "Volbeat",
    342: "Illumise",
    343: "Roselia",
    344: "Gulpin",
    345: "Swalot",
    346: "Carvanha",
    347: "Sharpedo",
    348: "Wailmer",
    349: "Wailord",
    350: "Numel",
    351: "Camerupt",
    352: "Torkoal",
    353: "Spoink",
    354: "Grumpig",
    355: "Spinda",
    356: "Trapinch",
    357: "Vibrava",
    358: "Flygon",
    359: "Cacnea",
    360: "Cacturne",
    361: "Swablu",
    362: "Altaria",
    363: "Zangoose",
    364: "Seviper",
    365: "Lunatone",
    366: "Solrock",
    367: "Barboach",
    368: "Whiscash",
    369: "Corphish",
    370: "Crawdaunt",
    371: "Baltoy",
    372: "Claydol",
    373: "Lileep",
    374: "Cradily",
    375: "Anorith",
    376: "Armaldo",
    377: "Feebas",
    378: "Milotic",
    379: "Castform",
    380: "Castform",
    381: "Castform",
    382: "Castform",
    383: "Kecleon",
    384: "Kecleon",
    385: "Shuppet",
    386: "Banette",
    387: "Duskull",
    388: "Dusclops",
    389: "Tropius",
    390: "Chimecho",
    391: "Absol",
    392: "Wynaut",
    393: "Snorunt",
    394: "Glalie",
    395: "Spheal",
    396: "Sealeo",
    397: "Walrein",
    398: "Clamperl",
    399: "Huntail",
    400: "Gorebyss",
    401: "Relicanth",
    402: "Luvdisc",
    403: "Bagon",
    404: "Shelgon",
    405: "Salamence",
    406: "Beldum",
    407: "Metang",
    408: "Metagross",
    409: "Regirock",
    410: "Regice",
    411: "Registeel",
    412: "Latias",
    413: "Latios",
    414: "Kyogre",
    415: "Groudon",
    416: "Rayquaza",
    417: "Jirachi",
    418: "Deoxys",
    419: "Deoxys",
    420: "Deoxys",
    421: "Deoxys",
    422: "Turtwig",
    423: "Grotle",
    424: "Torterra",
    425: "Chimchar",
    426: "Monferno",
    427: "Infernape",
    428: "Piplup",
    429: "Prinplup",
    430: "Empoleon",
    431: "Starly",
    432: "Staravia",
    433: "Staraptor",
    434: "Bidoof",
    435: "Bibarel",
    436: "Kricketot",
    437: "Kricketune",
    438: "Shinx",
    439: "Luxio",
    440: "Luxray",
    441: "Budew",
    442: "Roserade",
    443: "Cranidos",
    444: "Rampardos",
    445: "Shieldon",
    446: "Bastiodon",
    447: "Burmy",
    448: "Burmy",
    449: "Burmy",
    450: "Wormadam",
    451: "Wormadam",
    452: "Wormadam",
    453: "Mothim",
    454: "Combee",
    455: "Vespiquen",
    456: "Pachirisu",
    457: "Buizel",
    458: "Floatzel",
    459: "Cherubi",
    460: "Cherrim",
    461: "Cherrim",
    462: "Shellos",
    463: "Shellos",
    464: "Gastrodon",
    465: "Gastrodon",
    466: "Ambipom",
    467: "Drifloon",
    468: "Drifblim",
    469: "Buneary",
    470: "Lopunny",
    471: "Mismagius",
    472: "Honchkrow",
    473: "Glameow",
    474: "Purugly",
    475: "Chingling",
    476: "Stunky",
    477: "Skuntank",
    478: "Bronzor",
    479: "Bronzong",
    480: "Bonsly",
    481: "Mime Jr.",
    482: "Happiny",
    483: "Chatot",
    484: "Spiritomb",
    485: "Gible",
    486: "Gabite",
    487: "Garchomp",
    488: "Munchlax",
    489: "Riolu",
    490: "Lucario",
    491: "Hippopotas",
    492: "Hippowdon",
    493: "Skorupi",
    494: "Drapion",
    495: "Croagunk",
    496: "Toxicroak",
    497: "Carnivine",
    498: "Finneon",
    499: "Lumineon",
    500: "Mantyke",
    501: "Snover",
    502: "Abomasnow",
    503: "Weavile",
    504: "Magnezone",
    505: "Lickilicky",
    506: "Rhyperior",
    507: "Tangrowth",
    508: "Electivire",
    509: "Magmortar",
    510: "Togekiss",
    511: "Yanmega",
    512: "Leafeon",
    513: "Glaceon",
    514: "Gliscor",
    515: "Mamoswine",
    516: "Porygon-Z",
    517: "Gallade",
    518: "Probopass",
    519: "Dusknoir",
    520: "Froslass",
    521: "Rotom",
    522: "Uxie",
    523: "Mesprit",
    524: "Azelf",
    525: "Dialga",
    526: "Palkia",
    527: "Heatran",
    528: "Regigigas",
    529: "Giratina",
    530: "Cresselia",
    531: "Phione",
    532: "Manaphy",
    533: "Darkrai",
    534: "Shaymin",
    535: "Shaymin",
    536: "Giratina",
    537: "??????????",
    538: "??????????",
    539: "??????????",
    540: "??????????",
    541: "??????????",
    542: "??????????",
    543: "??????????",
    544: "??????????",
    545: "??????????",
    546: "??????????",
    547: "??????????",
    548: "??????????",
    549: "??????????",
    550: "??????????",
    551: "??????????",
    552: "Dialga",
    553: "Decoy",
    554: "Statue",
    555: "Wigglytuff",
    556: "Regigigas",
    557: "Bronzong",
    558: "Hitmonlee",
    559: "Chimecho",
    560: "Wigglytuff",
    561: "Uxie",
    562: "Azelf",
    563: "Mesprit",
    564: "Sunflora",
    565: "Diglett",
    566: "Dugtrio",
    567: "Corphish",
    568: "Loudred",
    569: "Bidoof",
    570: "Chatot",
    571: "Grovyle",
    572: "Dusknoir",
    573: "Sableye",
    574: "Darkrai",
    575: "Mama",
    576: "Grovyle",
    577: "Dusknoir",
    578: "Dusknoir",
    579: "Sentret",
    580: "Bellossom",
    581: "reserve_27",
    582: "reserve_28",
    583: "reserve_29",
    584: "reserve_30",
    585: "reserve_31",
    586: "reserve_32",
    587: "reserve_33",
    588: "reserve_34",
    589: "reserve_35",
    590: "reserve_36",
    591: "reserve_37",
    592: "reserve_38",
    593: "reserve_39",
    594: "reserve_40",
    595: "reserve_41",
    596: "reserve_42",
    597: "reserve_43",
    598: "reserve_44",
    599: "reserve_45",
}

MOVES = {
    0: "Nothing",
    1: "Iron Tail",
    2: "Ice Ball",
    3: "Yawn",
    4: "Lovely Kiss",
    5: "Nightmare",
    6: "Morning Sun",
    7: "Vital Throw",
    8: "Dig",
    9: "Thrash",
    10: "Sweet Scent",
    11: "Charm",
    12: "Rain Dance",
    13: "Confuse Ray",
    14: "Hail",
    15: "Aromatherapy",
    16: "Bubble",
    17: "Encore",
    18: "Cut",
    19: "Rage",
    20: "Super Fang",
    21: "Pain Split",
    22: "Torment",
    23: "String Shot",
    24: "Swagger",
    25: "Snore",
    26: "Heal Bell",
    27: "Screech",
    28: "Rock Throw",
    29: "Rock Smash",
    30: "Rock Slide",
    31: "Weather Ball",
    32: "Whirlpool",
    33: "Fake Tears",
    34: "Sing",
    35: "Spite",
    36: "Air Cutter",
    37: "SmokeScreen",
    38: "Pursuit",
    39: "DoubleSlap",
    40: "Mirror Move",
    41: "Overheat",
    42: "Aurora Beam",
    43: "Memento",
    44: "Octazooka",
    45: "Flatter",
    46: "Astonish",
    47: "Will-O-Wisp",
    48: "Return",
    49: "Grudge",
    50: "Strength",
    51: "Counter",
    52: "Flame Wheel",
    53: "Flamethrower",
    54: "Odor Sleuth",
    55: "Sharpen",
    56: "Double Team",
    57: "Gust",
    58: "Harden",
    59: "Disable",
    60: "Razor Wind",
    61: "Bide",
    62: "Crunch",
    63: "Bite",
    64: "Thunder",
    65: "ThunderPunch",
    66: "Endeavor",
    67: "Facade",
    68: "Karate Chop",
    69: "Clamp",
    70: "Withdraw",
    71: "Constrict",
    72: "Brick Break",
    73: "Rock Tomb",
    74: "Focus Energy",
    75: "Focus Punch",
    76: "Giga Drain",
    77: "Reversal",
    78: "SmellingSalt",
    79: "Spore",
    80: "Leech Life",
    81: "Slash",
    82: "Silver Wind",
    83: "Metal Sound",
    84: "GrassWhistle",
    85: "Tickle",
    86: "Spider Web",
    87: "Crabhammer",
    88: "Haze",
    89: "Mean Look",
    90: "Cross Chop",
    91: "Outrage",
    92: "Low Kick",
    93: "AncientPower",
    94: "Synthesis",
    95: "Agility",
    96: "Rapid Spin",
    97: "Icy Wind",
    98: "Mind Reader",
    99: "Cosmic Power",
    100: "Sky Attack",
    101: "Powder Snow",
    102: "Follow Me",
    103: "Meteor Mash",
    104: "Endure",
    105: "Rollout",
    106: "Scary Face",
    107: "Psybeam",
    108: "Psywave",
    109: "Psychic",
    110: "Psycho Boost",
    111: "Hypnosis",
    112: "Uproar",
    113: "Water Spout",
    114: "Signal Beam",
    115: "Psych Up",
    116: "Submission",
    117: "Recover",
    118: "Earthquake",
    119: "Nature Power",
    120: "Lick",
    121: "Flail",
    122: "Tail Whip",
    123: "Selfdestruct",
    124: "Stun Spore",
    125: "Bind",
    126: "Shadow Punch",
    127: "Shadow Ball",
    128: "Charge",
    129: "Thunderbolt",
    130: "Mist",
    131: "Fissure",
    132: "ExtremeSpeed",
    133: "Extrasensory",
    134: "Safeguard",
    135: "Absorb",
    136: "Sky Uppercut",
    137: "Skill Swap",
    138: "Sketch",
    139: "Headbutt",
    140: "Double-Edge",
    141: "Sandstorm",
    142: "Sand-Attack",
    143: "Sand Tomb",
    144: "Spark",
    145: "Swift",
    146: "Kinesis",
    147: "Smog",
    148: "Growth",
    149: "Sacred Fire",
    150: "Sheer Cold",
    151: "SolarBeam",
    152: "SonicBoom",
    153: "Fly",
    154: "Tackle",
    155: "Explosion",
    156: "Dive",
    157: "Fire Blast",
    158: "Waterfall",
    159: "Muddy Water",
    160: "Stockpile",
    161: "Slam",
    162: "Twister",
    163: "Bullet Seed",
    164: "Twineedle",
    165: "Softboiled",
    166: "Egg Bomb",
    167: "Faint Attack",
    168: "Barrage",
    169: "Minimize",
    170: "Seismic Toss",
    171: "Supersonic",
    172: "Taunt",
    173: "Moonlight",
    174: "Peck",
    175: "Arm Thrust",
    176: "Horn Attack",
    177: "Horn Drill",
    178: "Wing Attack",
    179: "Aerial Ace",
    180: "Icicle Spear",
    181: "Swords Dance",
    182: "Vine Whip",
    183: "Conversion",
    184: "Conversion 2",
    185: "Helping Hand",
    186: "Iron Defense",
    187: "Teleport",
    188: "ThunderShock",
    189: "Shock Wave",
    190: "Quick Attack",
    191: "Sweet Kiss",
    192: "Thunder Wave",
    193: "Zap Cannon",
    194: "Block",
    195: "Howl",
    196: "Poison Gas",
    197: "Toxic",
    198: "Poison Fang",
    199: "PoisonPowder",
    200: "Poison Sting",
    201: "Spike Cannon",
    202: "Acid Armor",
    203: "Take Down",
    204: "Jump Kick",
    205: "Bounce",
    206: "Hi Jump Kick",
    207: "Tri Attack",
    208: "Dragon Claw",
    209: "Trick",
    210: "Triple Kick",
    211: "Drill Peck",
    212: "Mud Sport",
    213: "Mud-Slap",
    214: "Thief",
    215: "Amnesia",
    216: "Night Shade",
    217: "Growl",
    218: "Slack Off",
    219: "Surf",
    220: "Role Play",
    221: "Needle Arm",
    222: "Double Kick",
    223: "Sunny Day",
    224: "Leer",
    225: "Wish",
    226: "Fake Out",
    227: "Sleep Talk",
    228: "Pay Day",
    229: "Assist",
    230: "Heat Wave",
    231: "Sleep Powder",
    232: "Rest",
    233: "Ingrain",
    234: "Confusion",
    235: "Body Slam",
    236: "Swallow",
    237: "Curse",
    238: "Frenzy Plant",
    239: "Hydro Cannon",
    240: "Hydro Pump",
    241: "Hyper Voice",
    242: "Hyper Beam",
    243: "Superpower",
    244: "Steel Wing",
    245: "Spit Up",
    246: "DynamicPunch",
    247: "Guillotine",
    248: "ViceGrip",
    249: "Knock Off",
    250: "Pound",
    251: "Razor Leaf",
    252: "Baton Pass",
    253: "Petal Dance",
    254: "Splash",
    255: "BubbleBeam",
    256: "Doom Desire",
    257: "Belly Drum",
    258: "Barrier",
    259: "Light Screen",
    260: "Scratch",
    261: "Hyper Fang",
    262: "Ember",
    263: "Secret Power",
    264: "Dizzy Punch",
    265: "Bulk Up",
    266: "Imprison",
    267: "FeatherDance",
    268: "Whirlwind",
    269: "Beat Up",
    270: "Blizzard",
    271: "Stomp",
    272: "Blast Burn",
    273: "Flash",
    274: "Teeter Dance",
    275: "Crush Claw",
    276: "Blaze Kick",
    277: "Present",
    278: "Eruption",
    279: "Sludge",
    280: "Sludge Bomb",
    281: "Glare",
    282: "Transform",
    283: "Poison Tail",
    284: "Roar",
    285: "Bone Rush",
    286: "Camouflage",
    287: "Covet",
    288: "Tail Glow",
    289: "Bone Club",
    290: "Bonemerang",
    291: "Fire Spin",
    292: "Fire Punch",
    293: "Perish Song",
    294: "Wrap",
    295: "Spikes",
    296: "Magnitude",
    297: "Magical Leaf",
    298: "Magic Coat",
    299: "Mud Shot",
    300: "Mach Punch",
    301: "Protect",
    302: "Defense Curl",
    303: "Rolling Kick",
    304: "Substitute",
    305: "Detect",
    306: "Pin Missile",
    307: "Water Sport",
    308: "Water Gun",
    309: "Mist Ball",
    310: "Water Pulse",
    311: "Fury Attack",
    312: "Fury Swipes",
    313: "Destiny Bond",
    314: "False Swipe",
    315: "Foresight",
    316: "Mirror Coat",
    317: "Future Sight",
    318: "Milk Drink",
    319: "Calm Mind",
    320: "Mega Drain",
    321: "Mega Kick",
    322: "Mega Punch",
    323: "Megahorn",
    324: "Hidden Power",
    325: "Metal Claw",
    326: "Attract",
    327: "Mimic",
    328: "Frustration",
    329: "Leech Seed",
    330: "Metronome",
    331: "Dream Eater",
    332: "Acid",
    333: "Meditate",
    334: "Snatch",
    335: "Luster Purge",
    336: "Leaf Blade",
    337: "Recycle",
    338: "Reflect",
    339: "Refresh",
    340: "Revenge",
    341: "Dragon Rage",
    342: "DragonBreath",
    343: "Dragon Dance",
    344: "Ice Punch",
    345: "Ice Beam",
    346: "Fury Cutter",
    347: "Comet Punch",
    348: "Skull Bash",
    349: "Lock-On",
    350: "Rock Blast",
    351: "Cotton Spore",
    352: "Struggle",
    353: "Aeroblast",
    354: "Volt Tackle",
    355: "regular attack",
    356: "is watching",
    357: "Bide",
    358: "Revenge",
    359: "Avalanche",
    360: "Wide Slash",
    361: "$$$",
    362: "$$$",
    363: "See-Trap",
    364: "Takeaway",
    365: "Rebound",
    366: "Bloop Slash",
    367: "Switcher",
    368: "Blowback",
    369: "Warp",
    370: "Transfer",
    371: "Slow Down",
    372: "Speed Boost",
    373: "Searchlight",
    374: "Petrify",
    375: "Stay Away",
    376: "Pounce",
    377: "Trawl",
    378: "Cleanse",
    379: "Observer",
    380: "Decoy Maker",
    381: "Siesta",
    382: "Totter",
    383: "Two-Edge",
    384: "No-Move",
    385: "Escape",
    386: "Scan",
    387: "Power-Ears",
    388: "Drought",
    389: "Trap Buster",
    390: "Wild Call",
    391: "Invisify",
    392: "One-Shot",
    393: "HP Gauge",
    394: "Vacuum-Cut",
    395: "Reviver",
    396: "Shocker",
    397: "Echo",
    398: "Famish",
    399: "One-Room",
    400: "Fill-In",
    401: "Trapper",
    402: "Possess",
    403: "Itemize",
    404: "[M:D1]",
    405: "projectile",
    406: "Hurl",
    407: "Mobile",
    408: "Item-Toss",
    409: "See Stairs",
    410: "Long Toss",
    411: "[M:D1]",
    412: "Pierce",
    413: "[M:D1]",
    414: "[M:D1]",
    415: "[M:D1]",
    416: "[M:D1]",
    417: "[M:D1]",
    418: "[M:D1]",
    419: "[M:D1]",
    420: "[M:D1]",
    421: "[M:D1]",
    422: "[M:D1]",
    423: "[M:D1]",
    424: "[M:D1]",
    425: "[M:D1]",
    426: "[M:D1]",
    427: "[M:D1]",
    428: "[M:D1]",
    429: "[M:D1]",
    430: "Hammer Arm",
    431: "Iron Head",
    432: "Aqua Jet",
    433: "Aqua Tail",
    434: "Aqua Ring",
    435: "Spacial Rend",
    436: "Dark Pulse",
    437: "Ominous Wind",
    438: "Gastro Acid",
    439: "Healing Wish",
    440: "Close Combat",
    441: "Wood Hammer",
    442: "Air Slash",
    443: "Energy Ball",
    444: "Tailwind",
    445: "Punishment",
    446: "Chatter",
    447: "Lucky Chant",
    448: "Guard Swap",
    449: "Heal Order",
    450: "Heal Block",
    451: "Shadow Sneak",
    452: "Thunder Fang",
    453: "Rock Wrecker",
    454: "Focus Blast",
    455: "Giga Impact",
    456: "Defog",
    457: "Trump Card",
    458: "Grass Knot",
    459: "Cross Poison",
    460: "Attack Order",
    461: "Ice Fang",
    462: "Ice Shard",
    463: "Psycho Cut",
    464: "Psycho Shift",
    465: "Me First",
    466: "Embargo",
    467: "$$$",
    468: "Seed Flare",
    469: "Brine",
    470: "X-Scissor",
    471: "Natural Gift",
    472: "Payback",
    473: "Zen Headbutt",
    474: "Wring Out",
    475: "Gyro Ball",
    476: "Shadow Claw",
    477: "Shadow Force",
    478: "Gravity",
    479: "Vacuum Wave",
    480: "Stealth Rock",
    481: "Stone Edge",
    482: "Switcheroo",
    483: "Dark Void",
    484: "Earth Power",
    485: "Gunk Shot",
    486: "Seed Bomb",
    487: "Double Hit",
    488: "Assurance",
    489: "Charge Beam",
    490: "Pluck",
    491: "Night Slash",
    492: "Acupressure",
    493: "Magnet Rise",
    494: "Roar of Time",
    495: "Poison Jab",
    496: "Toxic Spikes",
    497: "Last Resort",
    498: "Dragon Rush",
    499: "Trick Room",
    500: "Drain Punch",
    501: "Mud Bomb",
    502: "U-turn",
    503: "Fling",
    504: "Worry Seed",
    505: "Crush Grip",
    506: "Heart Swap",
    507: "Force Palm",
    508: "Aura Sphere",
    509: "Roost",
    510: "Bullet Punch",
    511: "Power Whip",
    512: "Power Gem",
    513: "Power Swap",
    514: "Power Trick",
    515: "Sucker Punch",
    516: "Feint",
    517: "Flare Blitz",
    518: "Brave Bird",
    519: "Lava Plume",
    520: "Defend Order",
    521: "Discharge",
    522: "Fire Fang",
    523: "Magnet Bomb",
    524: "Magma Storm",
    525: "Copycat",
    526: "Lunar Dance",
    527: "Mirror Shot",
    528: "Miracle Eye",
    529: "Bug Bite",
    530: "Bug Buzz",
    531: "Wake-Up Slap",
    532: "Metal Burst",
    533: "Head Smash",
    534: "Captivate",
    535: "Avalanche",
    536: "Flash Cannon",
    537: "Leaf Storm",
    538: "Draco Meteor",
    539: "Dragon Pulse",
    540: "Rock Polish",
    541: "Rock Climb",
    542: "Nasty Plot",
    543: "[M:D1]",
    544: "[M:D1]",
    545: "[M:D1]",
    546: "[M:D1]",
    547: "[M:D1]",
    548: "[M:D1]",
    549: "[M:D1]",
    550: "[M:D1]",
    551: "[M:D1]",
    552: "[M:D1]",
    553: "[M:D1]",
    554: "[M:D1]",
    555: "[M:D1]",
    556: "[M:D1]",
    557: "[M:D1]",
    558: "[M:D1]",
    559: "[M:D1]",
    560: "[M:D1]",
}

if __name__ == "__main__":
    from ndspy.rom import NintendoDSRom

    from skytemple_files.common.types.file_types import FileType
    from skytemple_files.common.util import get_ppmdu_config_for_rom

    rom = NintendoDSRom.fromFile("/tmp/out.nds")
    config = get_ppmdu_config_for_rom(rom)
    str = FileType.STR.deserialize(rom.getFileByName("MESSAGE/text_e.str"))
    move_name_block = config.string_index_data.string_blocks["Move Names"]
    pokemon_name_block = config.string_index_data.string_blocks["Pokemon Names"]

    print("MONSTERS = {")
    for i, str_i in enumerate(range(pokemon_name_block.begin, pokemon_name_block.end)):
        print(f"    {i}: '{str.strings[str_i]}',")
    print("}")

    print("MOVES = {")
    for i, str_i in enumerate(range(move_name_block.begin, move_name_block.end)):
        print(f"    {i}: '{str.strings[str_i]}',")
    print("}")
