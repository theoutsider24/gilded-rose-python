from gilded_rose import GildedRose, Item

ITEMS: tuple[tuple[Item, int, int], ...] = (
    (Item(name="+5 Dexterity Vest", sell_in=10, quality=20), 0, -20),
    (Item(name="Aged Brie", sell_in=2, quality=0), 50, -28),
    (Item(name="Elixir of the Mongoose", sell_in=5, quality=7), 0, -25),
    (Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80), 80, 0),
    (Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80), 80, -1),
    (
        Item(name="Backstage passes to a TAFKAL80ETC concert",
             sell_in=15, quality=20),
        0,
        -15,
    ),
    (
        Item(name="Backstage passes to a TAFKAL80ETC concert",
             sell_in=10, quality=49),
        0,
        -20,
    ),
    (
        Item(name="Backstage passes to a TAFKAL80ETC concert",
             sell_in=5, quality=49),
        0,
        -25,
    ),
    (Item(name="Conjured Mana Cake", sell_in=3, quality=6), 0, -27),
)


def test_gilded_rose_quality_updates():
    for _ in range(30):
        GildedRose([i for i, _, _ in ITEMS]).update_quality()

    for item, expected_quality, expected_sellin in ITEMS:
        assert item.quality == expected_quality
        assert item.sell_in == expected_sellin
