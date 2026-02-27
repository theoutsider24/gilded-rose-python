from enum import StrEnum


class ITEMTYPE(StrEnum):
    AGED_BRIE = "Aged Brie"
    BACKSTAGE_PASS = "Backstage passes to a TAFKAL80ETC concert"
    SULFURAS = "Sulfuras, Hand of Ragnaros"


class GildedRose:
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name == ITEMTYPE.SULFURAS:
                continue

            if item.sell_in > 0:
                if item.name not in [ITEMTYPE.AGED_BRIE, ITEMTYPE.BACKSTAGE_PASS]:
                    GildedRose.reduce_quality(item)
                elif item.name == ITEMTYPE.AGED_BRIE:
                    GildedRose.increase_quality(item)
                elif item.name == ITEMTYPE.BACKSTAGE_PASS:
                    if item.sell_in <= 5:
                        GildedRose.increase_quality(item, 2)
                    elif item.sell_in <= 10:
                        GildedRose.increase_quality(item, 3)
            else:
                if item.name not in [ITEMTYPE.AGED_BRIE, ITEMTYPE.BACKSTAGE_PASS]:
                    GildedRose.reduce_quality(item, 2)
                elif item.name == ITEMTYPE.AGED_BRIE:
                    GildedRose.increase_quality(item, 2)
                elif item.name == ITEMTYPE.BACKSTAGE_PASS:
                    item.quality = 0

            GildedRose.update_sell_in(item)

    @classmethod
    def update_sell_in(cls, item):
        if item.name != ITEMTYPE.SULFURAS:
            item.sell_in = item.sell_in - 1

    @classmethod
    def reduce_quality(cls, item, val: int = 1):
        item.quality = max(0, item.quality - val)

    @classmethod
    def increase_quality(cls, item, val: int = 1):
        item.quality = min(50, item.quality + val)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
