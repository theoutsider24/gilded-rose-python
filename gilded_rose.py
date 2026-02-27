from enum import StrEnum


class ITEMTYPE(StrEnum):
    AGED_BRIE = "Aged Brie"
    BACKSTAGE_PASS = "Backstage passes to a TAFKAL80ETC concert"
    SULFURAS = "Sulfuras, Hand of Ragnaros"


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return f"{self.name}, {self.sell_in}, {self.quality}"


class GildedRose:
    items: list[Item]

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name == ITEMTYPE.SULFURAS:
                continue

            if item.sell_in > 0:
                if item.name not in [ITEMTYPE.AGED_BRIE, ITEMTYPE.BACKSTAGE_PASS]:
                    GildedRose._alter_quality(item, -1)
                elif item.name == ITEMTYPE.AGED_BRIE:
                    GildedRose._alter_quality(item, 1)
                elif item.name == ITEMTYPE.BACKSTAGE_PASS:
                    if item.sell_in <= 5:
                        GildedRose._alter_quality(item, 2)
                    elif item.sell_in <= 10:
                        GildedRose._alter_quality(item, 3)
            else:
                if item.name not in [ITEMTYPE.AGED_BRIE, ITEMTYPE.BACKSTAGE_PASS]:
                    GildedRose._alter_quality(item, -2)
                elif item.name == ITEMTYPE.AGED_BRIE:
                    GildedRose._alter_quality(item, 2)
                elif item.name == ITEMTYPE.BACKSTAGE_PASS:
                    GildedRose._alter_quality(item, -item.quality)

            GildedRose._update_sell_in(item)

    @classmethod
    def _update_sell_in(cls, item: Item):
        if item.name != ITEMTYPE.SULFURAS:
            item.sell_in = item.sell_in - 1

    @classmethod
    def _alter_quality(cls, item: Item, val: int = 1):
        if cls.is_conjured(item):
            val = val * 2
        item.quality = max(0, min(50, item.quality + val))

    @classmethod
    def is_conjured(cls, item: Item):
        return "conjured" in [word.lower() for word in item.name.split(" ")]
