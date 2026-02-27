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
            if (
                item.name not in [ITEMTYPE.AGED_BRIE, ITEMTYPE.BACKSTAGE_PASS]
            ):
                if item.quality > 0:
                    if item.name != ITEMTYPE.SULFURAS:
                        item.reduce_quality()
            else:
                if item.quality < 50:
                    item.increase_quality()
                    if item.name == ITEMTYPE.BACKSTAGE_PASS:
                        if item.sell_in < 11:
                            if item.quality < 50:
                                item.increase_quality()
                        if item.sell_in < 6:
                            if item.quality < 50:
                                item.increase_quality()
            if item.sell_in < 0:
                if item.name != ITEMTYPE.AGED_BRIE:
                    if item.name != ITEMTYPE.BACKSTAGE_PASS:
                        if item.quality > 0:
                            if item.name != ITEMTYPE.SULFURAS:
                                item.reduce_quality()
                    else:
                        item.quality = item.quality - item.quality
                else:
                    if item.quality < 50:
                        item.increase_quality()

            item.update_sellin()


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

    def update_sellin(self):
        if self.name != ITEMTYPE.SULFURAS:
            self.sell_in = self.sell_in - 1

    def reduce_quality(self, val: int = 1):
        self.quality = max(0, self.quality - val)

    def increase_quality(self, val: int = 1):
        self.quality = min(50, self.quality + val)
