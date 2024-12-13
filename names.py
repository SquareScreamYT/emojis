food = {
  "amphora.png": "1f3fa",
  "apple.png": "1f34e",
  "avocado.png": "1f951",
  "baby_bottle.png": "1f37c",
  "bacon.png": "1f953",
  "bagel.png": "1f96f",
  "baguette.png": "1f956",
  "banana.png": "1f34c",
  "beans.png": "1fad8",
  "beer.png": "1f37a",
  "beers.png": "1f37b",
  "bell_pepper.png": "1fad1",
  "bento_box.png": "1f371",
  "blueberries.png": "1fad0",
  "bowl_spoon.png": "1f963",
  "bread.png": "1f35e",
  "broccoli.png": "1f966",
  "brown_mushroom.png": "1f344-200d-1f7eb",
  "bubble_tea.png": "1f9cb",
  "burrito.png": "1f32f",
  "butter.png": "1f9c8",
  "cake.png": "1f370",
  "candy.png": "1f36c",
  "canned_food.png": "1f96b",
  "carrot.png": "1f955",
  "champagne.png": "1f37e",
  "cheese.png": "1f9c0",
  "cherry.png": "1f352",
  "chestnut.png": "1f330",
  "chili.png": "1f336",
  "chocolate.png": "1f36b",
  "chopsticks.png": "1f962",
  "clinking_glass.png": "1f942",
  "cocktail.png": "1f378",
  "coconut.png": "1f965",
  "coffee.png": "2615",
  "cookie.png": "1f36a",
  "corn.png": "1f33d",
  "croissant.png": "1f950",
  "cucumber.png": "1f952",
  "cupcake.png": "1f9c1",
  "curry_rice.png": "1f35b",
  "dango.png": "1f361",
  "donut.png": "1f369",
  "dumpling.png": "1f95f",
  "egg.png": "1f95a",
  "eggplant.png": "1f346",
  "falafel.png": "1f9c6",
  "fish_cake.png": "1f365",
  "flatbread.png": "1fad3",
  "fondue.png": "1fad5",
  "fork_knife.png": "1f374",
  "fork_knife_plate.png": "1f37d",
  "fortune_cookie.png": "1f960",
  "fried_egg.png": "1f373",
  "fries.png": "1f35f",
  "garlic.png": "1f9c4",
  "ginger.png": "1fada",
  "grape.png": "1f347",
  "green_apple.png": "1f34f",
  "hamburger.png": "1f354",
  "honey.png": "1f36f",
  "hot_dog.png": "1f32d",
  "ice.png": "1f9ca",
  "ice_cream.png": "1f368",
  "jar.png": "1fad9",
  "juice_box.png": "1f9c3",
  "kiwi.png": "1f95d",
  "knife.png": "1f52a",
  "leafy_greens.png": "1f96c",
  "lemon.png": "1f34b",
  "lime.png": "1f34b-200b-1f7e9",
  "lollipop.png": "1f36d",
  "mango.png": "1f96d",
  "mate.png": "1f9c9",
  "meat_bone.png": "1f356",
  "meat_cut.png": "1f969",
  "meat_drumstick.png": "1f357",
  "melon.png": "1f348",
  "milk_cup.png": "1f95b",
  "mooncake.png": "1f96e",
  "noodles.png": "1f35c",
  "oden.png": "1f362",
  "olive.png": "1fad2",
  "onigiri.png": "1f359",
  "onion.png": "1f9c5",
  "orange.png": "1f34a",
  "pancakes.png": "1f95e",
  "passion_fruit.png": "none",
  "peach.png": "1f351",
  "peanut.png": "1f95c",
  "pear.png": "1f350",
  "peas.png": "1fadb",
  "pie.png": "1f967",
  "pineapple.png": "1f34d",
  "pizza.png": "1f355",
  "popcorn.png": "1f37f",
  "potato.png": "1f954",
  "pouring_glass.png": "1f943",
  "pretzel.png": "1f968",
  "pudding.png": "1f36e",
  "pumpkin.png": "1f383",
  "rice.png": "1f35a",
  "rice_cracker.png": "1f358",
  "sake.png": "1f376",
  "salad.png": "1f957",
  "salt.png": "1f9c2",
  "sandwich.png": "1f96a",
  "shaved_ice.png": "1f367",
  "shortcake.png": "1f370",
  "soft_serve.png": "1f366",
  "soup.png": "1f958",
  "soup_side.png": "1f372",
  "spaghetti.png": "1f35d",
  "spoon.png": "1f944",
  "straw_cup.png": "1f964",
  "strawberry.png": "1f353",
  "stuffed_flatbread.png": "1f959",
  "sushi.png": "1f363",
  "sweet_potato.png": "1f360",
  "taco.png": "1f32e",
  "takeout_box.png": "1f961",
  "tamale.png": "1fad4",
  "teacup.png": "1f375",
  "teapot.png": "1fad6",
  "tempura.png": "1f364",
  "tomato.png": "1f345",
  "tropical_drink.png": "1f379",
  "tumbler.png": "1f943",
  "waffle.png": "1f9c7",
  "watermelon.png": "1f349",
  "wine.png": "1f377"
}

for filename, unicode in food.items():
  if unicode == "none":
    continue
  chars = [chr(int(code, 16)) for code in unicode.split('-')]
  emoji = ''.join(chars)
  print(f"{emoji}: {filename}")

from fontTools.ttLib import TTFont, newTable
from fontTools.ttLib.tables import _n_a_m_e
from fontTools.ttLib.tables._c_m_a_p import CmapSubtable
import os

def create_color_emoji_font(food_dict, output_path="color_emoji.ttf"):
    font = TTFont()
    
    # Add required tables with initialized values
    head = newTable('head')
    head.magicNumber = 0x5F0F3CF5
    head.flags = 0x000B
    head.unitsPerEm = 1000
    head.created = 3406620153
    head.modified = 3406620153
    font['head'] = head

    hhea = newTable('hhea')
    hhea.ascent = 900
    hhea.descent = -100
    hhea.lineGap = 0
    font['hhea'] = hhea

    maxp = newTable('maxp')
    maxp.numGlyphs = len(food_dict)
    font['maxp'] = maxp

    os2 = newTable('OS/2')
    os2.version = 4
    os2.usWeightClass = 400
    os2.usWidthClass = 5
    font['OS/2'] = os2

    name = newTable('name')
    name.names = []
    namerecord = _n_a_m_e.NameRecord()
    namerecord.nameID = 1
    namerecord.string = "Color Emoji Font"
    name.names.append(namerecord)
    font['name'] = name

    # Setup CMAP table
    cmap = newTable('cmap')
    subtable = CmapSubtable.newSubtable(3, 1)
    subtable.cmap = {}
    cmap.tables = [subtable]
    font['cmap'] = cmap

    # Setup color tables
    colr = newTable('COLR')
    cpal = newTable('CPAL')
    font['COLR'] = colr
    font['CPAL'] = cpal

    # Add emoji mappings
    for filename, unicode_value in food_dict.items():
        if unicode_value == "none":
            continue
        
        codes = [int(code, 16) for code in unicode_value.split('-')]
        for code in codes:
            subtable.cmap[code] = filename.replace('.png', '')

    font.save(output_path)

# Use the existing food dictionary
create_color_emoji_font(food)
