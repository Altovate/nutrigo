"""
To get better results when matching ingredients to products in database we need to
change the naming convention for products. This module is used to rename products in database.

ALL WORDS SHOULD BE SINGULAR

Usage:
    >>> manage.py collectnames
"""

# Legend:
# ID: [name, description, common_name]
# Description and common name may be null.
names = {
    # Butter
    1145: ["Butter"],
    1001: ["Butter", "salted"],
    1002: ["Butter", "whipped"],
    1323: ["Clarified butter", "", "Ghee"],
    4617: ["Margarine"],
    # Cheese
    1004: ["Blue cheese"],
    1005: ["Brick cheese"],
    1006: ["Brie cheese"],
    1007: ["Camembert cheese"],
    1008: ["Caraway cheese"],
    1009: ["Cheddar cheese"],
    1010: ["Cheshire cheese"],
    1014: ["Cottage cheese"],
    1012: ["Colby cheese"],
    1017: ["Cream cheese"],
    1018: ["Edam cheese"],
    1019: ["Feta cheese"],
    1020: ["Fontina cheese"],
    1021: ["Gjetost cheese"],
    1022: [
        "Gouda cheese",
        "",
        "Cheese",
    ],  # I (MakuZo) have chosen gouda as a default cheese; fite me if u disagree
    1023: ["Gruyere cheese"],
    1024: ["Limburger cheese"],
    1025: ["Monterey cheese"],
    1026: ["Mozarella cheese"],
    1030: ["Muenster cheese"],
    1031: ["Neufchatel cheese"],
    1032: ["Parmesan cheese", "grated"],
    1033: ["Parmesan cheese"],
    1034: ["Port Salut cheese"],
    1035: ["Provolone cheese"],
    1036: ["Ricotta cheese"],
    1038: ["Romano cheese"],
    1039: ["Roquefort cheese"],
    1040: ["Swiss cheese"],
    1041: ["Tilsit cheese"],
    1156: ["Goat cheese"],
    # Cream
    1049: ["Fluid cream"],
    1054: ["Whipped cream", "", "Cream topping"],
    1056: ["Sour cream"],
    # Milk
    1211: ["Milk", "3.25% fat", "Milk"],  # Default for now - debatable though
    1175: ["Milk", "1% fat"],
    1174: ["Milk", "2% fat"],
    1212: ["Dry milk"],
    16120: ["Soymilk"],  # Might move it to other category
    # Yogurt
    1116: ["Yogurt"],
    1117: ["Yogurt", "low fat"],
    1293: ["Greek yogurt"],
    1287: ["Greek yogurt", "low fat"],
    1119: ["Vanilla yogurt", "low fat"],
    # Whey
    1112: ["Whey", "acid fluid"],
    1113: ["Whey", "acid dried"],
    1114: ["Whey", "sweet fluid"],
    1115: ["Whey", "sweet dried"],
    # Egg
    1123: ["Egg", "", "Egg"],
    1124: [
        "Egg white",
        "",
        "White",
    ],  # Might affect results with adjective e.g white chocolate - to be checked
    1125: ["Egg yolk", "", "Yolk"],
    # Kefir
    1289: ["Kefir"],
    1290: ["Strawberry kefir"],
    # Ice cream
    19095: ["Vanilla ice cream"],
    19270: ["Chocolate ice cream"],
    # Spices and vinegars
    2001: ["Allspice", "ground"],
    2002: ["Anise seed"],
    2003: ["Basil", "dried"],
    2004: ["Bay leaf"],
    2005: ["Caraway seed"],
    2006: ["Cardamom"],
    2007: ["Celery seed"],
    2008: ["Chervil", "dried"],
    2009: ["Chili powder"],
    2010: ["Cinnamon", "ground"],
    2011: ["Cloves", "ground"],
    2012: ["Coriander leaf", "dried"],
    2013: ["Coriander seed"],
    2014: ["Cumin seed"],
    2015: ["Curry powder"],
    2016: ["Dill seed"],
    2017: ["Dill weed", "dried"],
    2018: ["Fennel seed"],
    2019: ["Fenugreek seed"],
    2020: ["Garlic powder"],
    2021: ["Ginger", "ground"],
    2022: ["Mace", "ground"],
    2023: ["Marjoram", "dried"],
    2024: ["Mustard seed", "ground"],
    2025: ["Nutmeg", "ground"],
    2026: ["Onion powder"],
    2027: ["Oregano", "dried"],
    2028: ["Paprika", "dried"],
    2029: ["Parsley", "dried"],
    2030: ["Black pepper"],
    2031: ["Cayenne pepper"],
    2032: ["White pepper"],
    2033: ["Poppy seed"],
    2034: ["Poultry seasoning"],
    2035: ["Pumpkin pie spice"],
    2036: ["Rosemary", "dried"],
    2037: ["Saffron"],
    2038: ["Sage", "ground"],
    2039: ["Savory", "ground"],
    2041: ["Tarragon", "dried"],
    2042: ["Thyme", "dried"],
    2043: ["Turmeric", "ground"],
    2044: ["Basil", "fresh"],
    2045: ["Dill weed", "fresh"],
    2046: ["Mustard"],
    2047: ["Salt"],
    2048: ["Cider vinegar"],
    2049: ["Thyme", "fresh"],
    2050: ["Vanilla extract"],
    2054: ["Capers"],
    2055: ["Horseradish"],
    2063: ["Rosemary", "fresh"],
    2064: ["Peppermint", "fresh"],
    2065: ["Spearmint", "fresh"],
    2066: ["Spearmint", "dried"],
    2068: ["Red wine vinegar"],
    2069: ["Balsamic vinegar"],
    # Animal Fats
    4001: ["Beef tallow"],
    4002: ["Lard"],
    4575: ["Turkey fat"],
    4576: ["Goose fat"],
    # Oils
    4044: ["Soybean oil"],
    4037: ["Rice bran oil"],
    4038: ["Wheat germ oil"],
    4042: ["Peanut oil"],
    4047: ["Coconut oil"],
    4053: ["Olive oil"],
    4055: ["Palm oil"],
    4058: ["Sesame oil"],
    4060: ["Sunflower oil", "", "Vegetable oil"],  # Probably most used vegetable oil?
    4528: ["Walnut oil"],
    4581: ["Avocado oil"],
    # Mayonnaise
    4708: ["Mayonnaise"],
    # Chicken
    5006: ["Chicken", "whole"],
    5332: ["Chicken", "ground"],
    5011: ["Chicken", "skinless"],
    5015: ["Chicken skin"],
    5020: ["Chicken giblet"],
    5025: ["Chicken heart"],
    5027: ["Chicken liver"],
    5048: ["Chicken back"],
    5053: ["Chicken back", "skinless"],
    5057: ["Chicken breast"],
    5062: ["Chicken breast", "skinless"],
    5066: ["Chicken drumstick"],
    5075: ["Chicken leg"],
    5080: ["Chicken leg", "skinless"],
    5084: ["Chicken neck"],
    5088: ["Chicken neck", "skinless"],
    5091: ["Chicken thigh"],
    5096: ["Chicken thigh", "skinless"],
    5100: ["Chicken wing"],
    5105: ["Chicken wing", "skinless"],
    # Duck
    5139: ["Duck", "whole"],
    5141: ["Duck", "skinless"],
    5143: ["Duck liver"],
    5145: ["Duck breast"],
    # Goose
    5146: ["Goose", "whole"],
    5148: ["Goose", "skinless"],
    5150: ["Goose liver"],
    # Guinea hen
    5151: ["Guinea hen", "whole"],
    5152: ["Guinea hen", "skinless"],
    # Pheasant
    5153: ["Pheasant", "whole"],
    5154: ["Pheasant", "skinless"],
    # Quail
    5157: ["Quail", "whole"],
    5158: ["Quail", "skinless"],
    5159: ["Quail breast"],
    # Squab
    5160: ["Squab", "whole", "Pigeon"],
    5161: ["Squab", "skinless", "Pigeon"],
    # Turkey
    5165: ["Turkey", "whole"],
    5167: ["Turkey", "skinless"],
    5169: ["Turkey skin"],
    5171: ["Turkey giblets"],
    5175: ["Turkey heart"],
    5177: ["Turkey liver"],
    5179: ["Turkey neck"],
    5191: ["Turkey breast"],
    5193: ["Turkey leg"],
    5195: ["Turkey wing"],
    5215: ["Turkey back"],
    5738: ["Turkey drumstick"],
    7254: ["Turkey bacon"],
    # Emu
    5621: ["Emu", "ground"],
    5623: ["Emu fan fillet"],
    5625: ["Emu flat fillet"],
    5626: ["Emu full rump"],
    5628: ["Emu inside drum"],
    5630: ["Emu outside drum"],
    5631: ["Emu oyster"],
    # Ostrich
    5641: ["Ostrich", "ground"],
    5643: ["Ostrich fan"],
    5644: ["Ostrich inside leg"],
    5646: ["Ostrich inside strip"],
    5648: ["Ostrich outside leg"],
    5651: ["Ostrich oyster"],
    5653: ["Ostrich round"],
    5654: ["Ostrich tenderloin"],
    5657: ["Ostrich top loin"],
    # Soups
    6008: ["Beef broth"],
    6076: ["Beef broth cube"],
    6194: ["Chicken broth"],
    6081: ["Chicken broth cube"],
    6700: ["Vegetable broth"],
    6963: ["Fish broth"],
    # Gravies
    6116: ["Beef gravy"],
    6118: ["Brown gravy"],
    6119: ["Chicken gravy"],
    6120: ["Chicken gravy", "dry"],
    # Sauces
    6150: ["Barbecue sauce", "", "BBQ Sauce"],
    6151: ["Plum sauce"],
    6152: ["Pizza sauce"],
    6164: ["Salsa sauce"],
    6169: ["Tabasco sauce"],
    6175: ["Hoisin sauce"],
    6176: ["Oyster sauce"],
    6179: ["Fish sauce"],
    6189: ["Teriyaki sauce"],
    6285: ["Sweet and sour sauce"],
    6626: ["Pesto sauce"],
    6631: ["Sriracha sauce"],
    6930: ["Cheese sauce"],
    6931: ["Spaghetti sauce"],
    6971: ["Worcestershire sauce"],
    6972: ["Tomato chili sauce"],
    9081: ["Cranberry sauce"],
    9143: ["Guava sauce"],
    # Sausages and similair
    7001: ["Barbecue pork loaf"],
    7002: ["Beerwurst sausage", "", "Beer salami"],
    7004: ["Berliner sausage"],
    7005: ["Blood sausage"],
    7006: ["Bockwurst sausage"],
    7007: ["Bologna sausage", "beef"],
    7008: ["Bologna sausage", "beef pork"],
    7010: ["Bologna sausage", "pork"],
    7011: ["Bologna sausage", "turkey"],
    7013: ["Bratwurst sausage"],
    7019: ["Chorizo sausage"],
    7022: ["Frankfurter sausage", "beef"],
    7024: ["Frankfurter sausage", "chicken"],
    7025: ["Frankfurter sausage", "turkey"],
    7036: ["Italian sausage"],
    7038: ["Knackwurst sausage"],
    7041: ["Liver sausage", "pork", "Liverwurst"],
    7057: ["Pepperoni"],
    7059: ["Polish sausage"],  # Polan can into db!
    7060: ["Luxury loaf"],
    7063: ["Pork sausage"],
    7075: ["Smoked link sausage"],
    7090: ["Luncheon sausage"],
    7934: ["Kielbasa"], # !!!
    # Ham
    7027: ["Ham"],
    7029: ["Ham", "sliced"],
    7030: ["Ham", "minced"],
    7026: ["Ham", "chopped canned"],
    7050: ["Mortadella", "beef pork"],
    # Pates
    7053: ["Chicken liver pate"],
    7054: ["Goose liver pate"],
    7055: ["Liver pate"],
    # Salami
    7926: ["Salami"],
    7068: ["Salami", "cooked beef"],
    7069: ["Salami", "cooked pork"],
    7070: ["Salami", "turkey"],
    7071: ["Salami", "dry hard"],
    # Cereals
    8037: ["Granola cereal"],
    8506: ["Corn flakes cereal"],
    8046: ["Honeycomb cereal"],
    8120: ["Oat cereal"],
    8084: ["Wheat germ cereal"],
    # Fruits
    9001: ["Acerola", "", "West indian cherry"],
    9002: ["Acerola juice"],
    9003: ["Apple"],
    9500: ["Apple", "red delicious"],
    9501: ["Apple", "golden delicious"],
    9502: ["Apple", "granny smith"],
    9503: ["Apple", "gala"],
    9504: ["Apple", "fuji"],
    9004: ["Apple peeled"],
    9016: ["Apple juice"],
    9020: ["Applesauce"],
    9021: ["Apricot"],
    9035: ["Apricot", "frozen"],
    9022: ["Canned apricot"],
    9023: ["Canned apricot", "peeled"],
    9037: ["Avocado"],
    9040: ["Banana"],
    9042: ["Blackberry"],
    9048: ["Blackberry", "frozen"],
    9043: ["Blackberry juice"],
    9050: ["Blueberry"],
    9054: ["Blueberry", "frozen"],
    9163: ["Blueberry", "dried sweetened"],
    9057: ["Boysenberries", "frozen"],
    9059: ["Breadfruit"],
    9060: ["Carambola", "", "starfruit"],
    9061: ["Carissa", "", "natal-plum"],
    9062: ["Cherimoya"],
    9063: ["Cherry", "sour red"],
    9064: ["Cherry", "sour red canned"],
    9068: ["Cherry", "sour red frozen"],
    9070: ["Cherry", "sweet"],
    9071: ["Cherry", "sweet canned"],
    9077: ["Crabapple"],
    9078: ["Cranberry"],
    9079: ["Cranberry", "dried sweetened"],
    9083: ["Currant", "european black"],
    9084: ["Currant", "red white"],
    9085: ["Currant", "zante dried"],
    9086: ["Custard-apple", "", "Bullock's-heart"],
    9087: ["Date", "", "Deglet noor"],
    9088: ["Elderberry"],
    9089: ["Fig"],
    9090: ["Fig", "canned"],
    9094: ["Fig", "dried"],
    9107: ["Gooseberry"],
    9109: ["Gooseberry", "canned"],
    9110: ["Goji berry", "dried"],
    9111: ["Grapefruit", "pink red white"],
    9128: ["Grapefruit juice", "white"],
    9127: ["Grapefruit juice", "red pink"],
    9124: ["Grapefruit juice", "white canned sweetened"],
    9123: ["Grapefruit juice", "white canned bottled unsweetened"],
    9129: ["Grape", "muscadine"],
    9131: ["Grape", "american"],
    9135: ["Grape juice", "canned bottled unsweetened"],
    9138: ["Groundcherry", "", "Poha"],
    9139: ["Guavas", "common"],
    9140: ["Guabas", "strawberry"],
    9144: ["Jackfruit"],
    9145: ["Java-plum", "", "Jambolan"],
    9146: ["Jujube"],
    9148: ["Kiwifruit", "green"],
    9149: ["Kumquat"],
    9150: ["Lemon"],
    9152: ["Lemon juice"],
    9156: ["Lemon peel"],
    9159: ["Lime"],
    9160: ["Lime juice"],
    9164: ["Lychee", "", "Litchi"],
    9165: ["Lychee", "dried", "Litchi"],
    9167: ["Loganberry", "frozen"],
    9172: ["Longan"],
    9173: ["Longan", "dried"],
    9174: ["Loquat"],
    9175: ["Mammy-apple", "", "Mamey"],
    9176: ["Mango"],
    9177: ["Mangosteen", "canned"],
    9178: ["Mango", "dried sweetend"],
    9181: ["Melon", "cantaloupe"],
    9183: ["Melon", "casaba"],
    9184: ["Melon", "honeydew"],
    9185: ["Melon ball", "frozen"],
    9190: ["Mulberry"],
    9191: ["Nectarine"],
    9192: ["Oheloberry"],
    9193: ["Ripe olive", "canned small-extra large"],
    9194: ["Ripe olive", "canned jumbo-super colossal"],
    9195: ["Olive", "pickled canned bottled green"],
    9200: ["Orange"],
    9206: ["Orange juice"],
    9207: ["Orange juice", "canned unsweetened"],
    9216: ["Orange peel"],
    9218: ["Tangerine", "", "Mandarin orange"],
    9218: ["Tangerine", "cabbed juice", "Mandarin orange"],
    9218: ["Tangerine", "light syrup pack", "Mandarin orange"],
    9221: ["Tangerine juice"],
    9226: ["Papaya"],
    9228: ["Papaya", "canned heavy syrup drained"],
    9229: ["Papaya nectar", "canned"],
    9231: ["Passion-fruit", "purple", "Granadilla"],
    9232: ["Passion-fruit juice", "purple"],
    9232: ["Passion-fruit juice", "yellow"],
    9236: ["Peach", "yellow"],
    9237: ["Peach", "canned water pack"],
    9239: ["Peach", "canned extra light syrup"],
    9246: ["Peach", "dried sulfured uncooked"],
    9250: ["Peach", "frozen"],
    9252: ["Pear"],
    9253: ["Pear", "canned water pack"],
    9254: ["Pear", "canned juice pack"],
    9255: ["Pear", "extra light syrup pack"],
    9259: ["Pear", "dried sulfured uncooked"],
    9262: ["Pear nectar", "canned"],
    9263: ["Persimmons", "japanese"],
    9264: ["Persimmons", "japanese dried"],
    9265: ["Persimmons", "native"],
    9266: ["Pineapple"],
    9267: ["Pineapple", "canned water pack"],
    9272: ["Pineapple", "frozen chunk sweetened"],
    9273: ["Pineapple juice", "canned bottled unsweetened"],
    9276: ["Pitanga", "", "Surinam-cherry"],
    9277: ["Plantain", "yellow"],
    9278: ["Plantain", "yellow baked"],
    9279: ["Plum"],
    9281: ["Plum", "canned water pack"],
    9282: ["Plum", "canned juice pack"],
    9268: ["Pomegranate"],
    9288: ["Prune", "canned heavy syrup pack"],
    9289: ["Prune", "dehydrated uncooked low-moisture"],
    9291: ["Plum", "dried uncooked"],
    9294: ["Prune juice", "canned"],
    9295: ["Pummelo"],
    9296: ["Quince"],
    9297: ["Raisin", "golden seedless"],
    9298: ["Raisin", "dark seedless"],
    9299: ["Raisin", "seeded"],
    9301: ["Rambutan", "canned syrup pack"],
    9302: ["Raspberry"],
    9518: ["Raspberry", "frozen unsweetened"],
    9304: ["Raspberry", "canned syrup"],
    9306: ["Raspberry", "frozen sweetened"],
    9307: ["Rhubarb"],
    9309: ["Rhubarb", "frozen uncooked"],
    9310: ["Rhubarb", "frozen cooked with sugar"],
    9311: ["Roselle", "", "Gravola"],
    9312: ["Rose-apples"],
    9313: ["Sapodilla"],
    9314: ["Sapote", "", "Mamey"],
    9315: ["Soursop"],
    9316: ["Strawberry"],
    9317: ["Strawberry", "canned heavy syrup"],
    9318: ["Strawberry", "frozen unsweetened"],
    9320: ["Strawberry", "frozen sweetened"],
    9321: ["Sugar-apple", "", "Sweetsop"],
    9322: ["Tamarind"],
    9326: ["Watermelon"],
    9328: ["Maraschino cherry", "canned drained"],
    9334: ["Feijoa"],
    9340: ["Pear", "asian"],
    9404: ["Grapefruit juice", "ping"],
    9409: ["Pineapple juice", "canned bottled unsweetened enriched"],
    9416: ["Grapefruit juice", "white bottled unsweetened"],
    9421: ["Medjool date"],
    9422: ["Durian", "raw frozen"],
    9423: ["Prune puree"],
    9426: ["Candied fruit"],
    9427: ["Abiyuch"],
    9428: ["Rowal"],
    9429: ["Pineapple"],
    9433: ["Clementine"],
    9434: ["Guanabana nectar", "canned"],
    9435: ["Guava nectar", "canned"],
    9436: ["Mango nectar", "canned"],
    9437: ["Tamarind nectar", "canned"],
    9442: ["Pomegranate juice", "bottled"],
    9542: ["Plantain", "green raw"],
    9543: ["Plantain", "green boiled"],
    9446: ["Plantain", "green fried"],
    9447: ["Plantain", "yellow fried"],
    9450: ["Naranjilla pulp", "frozen unsweetened"],
    9451: ["Horned melon", "", "Kiwano"],
    9544: ["Baobab powder"],
    # Pork
    10219: ["Pork", "ground"],
    10001: ["Pork carcass"],
    10004: ["Pork backfat"],
    10005: ["Pork belly"],
    10008: ["Pork leg", "", "Pork ham"],
    10020: ["Pork loin", "whole"],
    10028: ["Pork loin", "blade bone-in"],
    10989: ["Pork loin", "blade boneless"],
    10036: ["Pork loin", "center chop bone-in"],
    10044: ["Pork loin", "center rib bone-in"],
    10052: ["Pork loin", "sirloin bone-in"],
    10218: ["Pork loin", "tenderloin"],
    10062: ["Pork loin", "top chop boneless"],
    10070: ["Pork shoulder", "whole"],
    10074: ["Pork shoulder", "arm picnic"],
    10080: ["Pork shoulder", "blade steak", "Boston butt"],
    10088: ["Pork sparerib"],
    10094: ["Pork loin", "center chop boneless"],
    10096: ["Pork brain"],
    10098: ["Pork chitterling"],
    10100: ["Pork ear", "frozen"],
    10102: ["Pork foot"],
    10103: ["Pork heart"],
    10105: ["Pork jowl"],
    10106: ["Pork kidney"],
    10109: ["Pork leaf fat"],
    10110: ["Pork liver"],
    10112: ["Pork lung"],
    10115: ["Pork pancreas"],
    10117: ["Pork spleen"],
    10119: ["Pork stomach"],
    10121: ["Pork tongue"],
    10123: ["Pork bacon", "cured", "Bacon"],
    10130: ["Canadian bacon"],
    10192: ["Pork backrib"],
    10194: ["Pork loin", "center rib boneless"],
    10204: ["Pork loin", "country-style rib"],
    10210: ["Pork loin", "sirloin boneless"],
    10958: ["Pork shoulder breast", "boneless"],
    10961: ["Pork shoulder petite tender"],
    # Vegetables
    11001: ["Alfalfa seed", "sprouted"],
    11003: ["Amaranth leaf"],
    11005: ["Arrowhead"],
    11007: ["Artichoke"],
    11011: ["Asparagus"],
    11022: ["Balsam-pear", "leafy tip", "Bitter gourd"],
    11024: ["Balsam-pear", "pod", "Bitter gourd"],
    11026: ["Bamboo shoot"],
    11029: ["Kidney bean", "mature seed"],
    11031: ["Lima bean", "immature seed"],
    11043: ["Mung bean", "sprouted"],
    11046: ["Navy bean", "sprouted"],
    11052: ["Snap bean", "green"],
    11080: ["Beet"],
    11086: ["Beet green"],
    11088: ["Broadbean", "immature seed"],
    11090: ["Broccoli"],
    11092: ["Broccoli", "frozen chopped unprepared"],
    11096: ["Broccoli raab"],
    11098: ["Brussels sprout"],
    11100: ["Brussels sprout", "frozen"],
    11104: ["Burdock root"],
    11106: ["Butterbur", "", "Fuki"],
    11109: ["Cabbage"],
    11112: ["Red cabbage"],
    11114: ["Savoy cabbage"],
    11116: ["Chinese cabbage", "", "Pak-choi"],
    11118: ["Kimchi cabbage"],
    11119: ["Chinese cabbage", "", "Pe-tsai"],
    11122: ["Cardoon"],
    11124: ["Carrot"],
    11130: ["Carrot", "frozen unprepared"],
    11134: ["Cassava"],
    11135: ["Cauliflower"],
    11137: ["Cauliflower", "frozen unprepared"],
    11141: ["Celeriac"],
    11143: ["Celery"],
    11145: ["Celtuce"],
    11147: ["Chard", "swiss"],
    11149: ["Chayote", "fruit"],
    11151: ["Chicory", "witloof"],
    11152: ["Chicory green"],
    11154: ["Chicory root"],
    11156: ["Chive"],
    11157: ["Chrysanthemum", "garland"],
    11161: ["Collard"],
    11165: ["Coriander leaf"],
    11167: ["Corn", "sweet yellow"],
    11190: ["Cornsalad"],
    11191: ["Cowpea", "immature seed", "Blackeye"],
    11197: ["Cowpea", "young pod seed"],
    11199: ["Yardlong bean"],
    11201: ["Cowpea", "leafy tip"],
    11203: ["Cress", "garden"],
    11205: ["Cucumber"],
    11206: ["Cucumber", "peeled"],
    11207: ["Dandelion green"],
    11209: ["Eggplant"],
    11211: ["Edamame", "frozen unprepared"],
    11212: ["Edamame", "frozen prepared"],
    11213: ["Endive"],
    11215: ["Garlic"],
    11216: ["Ginger root"],
    11218: ["Gourd", "white-flowered", "Calabash"],
    11220: ["Gourd", "dishcloth", "Towelgourd"],
    11222: ["Drumstick leaf"],
    11224: ["Hyacinth bean", "", "Lablab"],
    11226: ["Jerusalem artichoke"],
    11228: ["Jew ear", "", "Pepeao"],
    11230: ["Pepeao", "dried", "Pepeao"],
    11231: ["Jute", "potherb"],
    11233: ["Kale"],
    11238: ["Shiitake mushroom"],
    11239: ["Chanterelle mushroom"],
    11240: ["Morel mushroom"],
    11241: ["Kohlrabi"],
    11244: ["Lambsquarter"],
    11246: ["Leek"],
    11248: ["Lentil", "sprouted"],
    11250: ["Lettuce", "butterhead"],
    11251: ["Lettuce", "cos romaine"],
    11252: ["Lettuce", "iceberg"],
    11253: ["Lettuce", "green leaf"],
    11254: ["Lotus root"],
    11257: ["Lettuce red"],
    11258: ["Mountain yam", "hawaii"],
    11260: ["Mushroom", "white"],
    11265: ["Mushroom", "portabella"],
    11266: ["Mushroom", "brown italian crimini"],
    11270: ["Mustard green"],
    11274: ["Mustard spinach"],
    11276: ["Spinach", "New Zealand"],
    11278: ["Okra"],
    11282: ["Onion"],
    11286: ["Onion", "yellow sauteed"],
    11282: ["Onion", "young green"],
    11293: ["Welsh onion"],
    11294: ["Sweet onion"],
    11297: ["Parsley"],
    11298: ["Parsnip"],
    11300: ["Pea"],
    11304: ["Pea", "green"],
    11333: ["Green pepper", "sweet"],
    11344: ["Pigeon pea"],
    11349: ["Poi"],
    11350: ["Pokeberry shoot", "", "Poke"],
    11352: ["Potato"],
    11353: ["Potato", "russet"],
    11354: ["Potato", "white"],
    11355: ["Potato", "red"],
    11416: ["Pumpkin flower"],
    11418: ["Pumpkin leaf"],
    11422: ["Pumpkin"],
    11427: ["Purslane"],
    11429: ["Radish"],
    11430: ["Radish", "oriental"],
    11435: ["Rutabaga"],
    11437: ["Salsify", "", "Vegetable oyster"],
    11442: ["Seaweed", "agar"],
    11444: ["Seaweed", "irishmoss"],
    11445: ["Seaweed", "kelp"],
    11446: ["Seaweed", "laver"],
    11447: ["Sesbania flower"],
    11450: ["Soybean", "green"],
    11457: ["Spinach"],
    11463: ["Spinach", "frozen"],
    11467: ["Squash", "summer crookneck straightneck"],
    11475: ["Squash", "summer scallop"],
    11477: ["Squash", "summer zucchini"],
    11482: ["Squash", "winter acorn"],
    11485: ["Squash", "winter butternut"],
    11489: ["Squash", "winter hubbard"],
    11492: ["Squash", "winter spaghetti"],
    11495: ["Succotash"],
    11503: ["Water convolvulus"],
    11507: ["Sweet potato"],
    11505: ["Sweet potato leaf"],
    11518: ["Taro"],
    11520: ["Taro leaf"],
    11522: ["Taro shoot"],
    11525: ["Taro tahitian"],
    11527: ["Tomato", "green"],
    11529: ["Tomato", "red ripe"],
    11564: ["Turnip"],
    11568: ["Turnip green"],
    11587: ["Vinespinach", "", "Basella"],
    11591: ["Watercress"],
    11593: ["Waxgourd"],
    11595: ["Winged bean"],
    11597: ["Winged bean leaf"],
    11599: ["Winged bean tuber"],
    11601: ["Yam"],
    11603: ["Yambean"],
    11613: ["Borage"],
    11616: ["Dock"],
    11620: ["Drumstick pod"],
    11637: ["Radish", "white icicle"],
    11641: ["Squash", "summer"],
    11643: ["Squash", "winter"],
    11666: ["Seaweed", "spirulina", "Spirulina"],
    11669: ["Seaweed", "wakame", "Wakame"],
    11670: ["Hot chili pepper"],
    11677: ["Shallot"],
    11695: ["Tomato", "orange"],
    11696: ["Tomato", "yellow"],
    11697: ["Arrowroot"],
    11698: ["Chrysanthemum leaf"],
    11722: ["Yellow bean", "snap"],
    11739: ["Broccoli leaf"],
    11741: ["Broccoli stalk"],
    11749: ["Cabbage", "", "Cabbage"],
    11819: ["Red hot chili pepper", "", "californication.mp3"],
    11821: ["Red pepper", "sweet"],
    11900: ["Sweet corn", "white"],    
    11950: ["Enoki mushroom"],
    11951: ["Yellow pepper", "sweet"],
    11952: ["Radicchio"],
    11954: ["Tomatillo"],
    11957: ["Fennel", "bulb"],
    11959: ["Arugula"],
    11960: ["Baby carrot"],
    11963: ["Nopales"],
    11965: ["Cauliflower", "green"],
    11972: ["Lemon grass", "", "Citronella"],
    11973: ["Fava bean"],
    11974: ["Grape leaf"],
    11976: ["Banana pepper"],
    11977: ["Serrano pepper"],
    11979: ["Jalapeno pepper"],
    11981: ["Hungarian pepper"],
    11984: ["Epazote"],
    11985: ["Fireweed"],
    11987: ["Oyster mushroom"],
    11990: ["Wasabi", "root"],
    11991: ["Yautia", "", "Tannier"],
    11993: ["Maitake mushroom"],
    11994: ["Broccoli", "chinese"],
    11995: ["Fiddlehead fern"],
    # Seeds'n'nuts
    12001: ["Breadfruit seed"],
    12004: ["Breadnut tree seed"],
    12058: ["Acorn nut"],
    12087: ["Cashew nut"],
    12093: ["Chestnut", "chinese"],
    12097: ["Chestnut", "european"],
    12104: ["Coconut meat"],
    12117: ["Coconut milk"],
    12127: ["Ginkgo nut"],
    12131: ["Macadamia nut"],
    12151: ["Pistachio nut"],
    12202: ["Chestnut", "japanese"],
    12205: ["Lotus seed"],
    # Beef
    13000: ["Beef strip steak"],
    13001: ["Beef carcass"],
    13047: ["Beef", "ground boneless"],
    13065: ["Beef flank steak"],
    13147: ["Beef shortrib"],
    13231: ["Beef porterhouse steak"],
    13235: ["Beef t-bone steak"],
    13284: ["Beef rib eye"],
    13318: ["Beef brain"],
    13321: ["Beef heart"],
    13323: ["Beef kidney"],
    13325: ["Beef liver"],
    13328: ["Beef lung"],
    13331: ["Beef pancreas"],
    13333: ["Beef spleen"],
    13335: ["Beef suet"],
    13337: ["Beef thymus"],
    13339: ["Beef tongue"],
    13341: ["Beef tripe"],
    13344: ["Beef cured"],
    13349: ["Beef chuck", "boneless"],
    13486: ["Beef tip round"],
    13498: ["Beef", "ground boneless 70% 30%"],
    13519: ["Beef shoulder top blade steak"],
    13595: ["Beef brisket", "boneless"],
    13647: ["Beef shoulder pot roast"],
    13786: ["Beef chuck eye roast"],
    13803: ["Beef brisket", "whole"],
    13809: ["Beef arm pot roast"],
    13815: ["Beef blade roast"],
    13824: ["Beef rib", "whole 6-12"],
    13838: ["Beef rib", "large end 6-9"],
    13850: ["Beef rib", "small end 10-12"],
    13863: ["Beef shoulder top blade steak", "boneless"],
    13864: ["Beef round", "full cut"],
    13868: ["Beef round", "bottom"],
    13883: ["Beef round", "tip"],
    13891: ["Beef round", "top"],
    13904: ["Beef brisket", "flat half"],
    13905: ["Beef short loin", "porterhouse steak"],
    13907: ["Beef short loin", "t-bone steak"],
    13909: ["Beef short loin", "top"],
    13917: ["Beef tenderloin", "steak", "Beef steak"],
    13929: ["Beef top sirloin", "steak"],
    13954: ["Beef bottom sirloin", "tri-tip roast"],
    13970: ["Beef flank", "steak"],
    13972: ["Beef chuck eye roast", "boneless"],
    # Beverages
    14555: ["Water", "", "Water"],
    # Fish
    15001: ["Anchovy fish"],
    15003: ["Bass fish"],
    15005: ["Bluefish fish"],
    15006: ["Burbot fish"],
    15007: ["Butterfish fish"],
    15008: ["Carp fish"],
    15010: ["Catfish fish", "wild channel"],
    15013: ["Cisco fish"],
    15015: ["Cod fish"],
    15020: ["Croaker fish"],
    15022: ["Cusk fish"],
    15023: ["Mahimahi fish"],
    15024: ["Drum fish"],
    15025: ["Eel fish"],
    15028: ["Flatfish fish"],
    15031: ["Grouper fish"],
    15033: ["Haddock fish"],
    15036: ["Halibut fish"],
    15039: ["Herring fish"],
    15044: ["Ling fish"],
    15045: ["Lingcod fish"],
    15046: ["Mackerel fish"],
    15053: ["Milkfish fish"],
    15054: ["Monkfish fish"],
    15055: ["Mullet fish"],
    15057: ["Ocean perch fish"],
    15059: ["Pout fish"],
    15060: ["Perch fish"],
    15062: ["Pike fish"],
    15065: ["Pollock fish"],
    15068: ["Pompano fish"],
    15070: ["Rockfish fish"],
    15072: ["Roe fish"],
    15073: ["Roughy fish"],
    15074: ["Sablefish fish"],
    15076: ["Salmon fish"],
    15090: ["Scup fish"],
    15091: ["Sea bass fish"],
    15093: ["Seatrout fish"],
    15094: ["Shad fish"],
    15095: ["Shark fish"],
    15097: ["Sheepshead fish"],
    15099: ["Smelt fish", "rainbow"],
    15101: ["Snapper fish"],
    15103: ["Spot fish"],
    15104: ["Sturgeon fish"],
    15107: ["Sucker fish", "white"],
    15108: ["Sunfish fish"],
    15110: ["Swordfish fish"],
    15112: ["Tilefish fish"],
    15114: ["Trout fish"],
    15117: ["Tuna fish"],
    15129: ["Turbot fish"],
    15130: ["Whitefish fish"],
    15132: ["Whiting fish"],
    15134: ["Wolffish fish"],
    15135: ["Yellowtail fish"],
}
