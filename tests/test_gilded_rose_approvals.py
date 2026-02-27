from gilded_rose import GildedRose, Item

ITEMS = [
    [Item(name="+5 Dexterity Vest", sell_in=10, quality=20), 0],
    [Item(name="Aged Brie", sell_in=2, quality=0), 50],
    [Item(name="Elixir of the Mongoose", sell_in=5, quality=7), 0],
    [Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80), 80],
    [Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80), 80],
    [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20), 0],
    [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49), 0],
    [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49), 0],
    [Item(name="Conjured Mana Cake", sell_in=3, quality=6), 0],
]


def test_gilded_rose_quality_updates():
    for _ in range(30):
        GildedRose([i for i, _ in ITEMS]).update_quality()

    for item, expected_quality in ITEMS:
        assert item.quality == expected_quality
