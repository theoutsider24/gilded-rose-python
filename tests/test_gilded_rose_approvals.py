import pytest
from gilded_rose import GildedRose, Item

ITEMS: tuple[tuple[Item, int, int], ...] = (
    (Item(name="+5 Dexterity Vest", sell_in=10, quality=20), 0, -20),
    (Item(name="Aged Brie", sell_in=2, quality=0), 50, -28),
    (Item(name="Elixir of the Mongoose", sell_in=5, quality=7), 0, -25),
    (Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80), 80, 0),
    (Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80), 80, -1),
    (
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
        0,
        -15,
    ),
    (
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49),
        0,
        -20,
    ),
    (
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49),
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


class TestQualityChange:
    class TestBrie:
        @pytest.mark.parametrize(
            "initial_quality,initial_sell_in,time,expected_quality",
            [
                (10, 1, 1, 11),  # One reverse degredation
                (10, 1, 2, 13),  # One reverse degredation at x1, one at x2
                (10, 0, 2, 14),  # Two reverse degredations at x2
                (10, 0, 30, 50),  # Capped quality at 50
            ],
        )
        def test_quality(
            self, initial_quality, initial_sell_in, time, expected_quality
        ):
            rose = GildedRose(
                [
                    Item(
                        name="Aged Brie",
                        sell_in=initial_sell_in,
                        quality=initial_quality,
                    )
                ]
            )
            for _ in range(time):
                rose.update_quality()
            assert rose.items[0].quality == expected_quality

    class TestConjuredItem:
        @pytest.mark.parametrize(
            "name,is_conjured",
            [
                ("MY conjuRed biscuit", True),
                ("MY conjuRedbiscuit", False),
                ("onjuRed biscuit", False),
                ("conjuRed biscuit", True),
            ],
        )
        def test_is_conjured(self, name, is_conjured):
            item = Item(name=name, sell_in=0, quality=0)
            assert GildedRose.is_conjured(item) == is_conjured

        @pytest.mark.parametrize(
            "initial_quality,initial_sell_in,time,expected_quality",
            [
                (10, 1, 1, 8),  # One degradation at x2
                (10, 1, 2, 4),  # One degradation at x2, one at x4
                (10, 0, 2, 2),  # Two degradations at x4
                (10, 0, 10, 0),  # Capped quality at 0
            ],
        )
        def test_quality(
            self, initial_quality, initial_sell_in, time, expected_quality
        ):
            rose = GildedRose(
                [
                    Item(
                        name="Conjured Mana Cake",
                        sell_in=initial_sell_in,
                        quality=initial_quality,
                    )
                ]
            )
            for _ in range(time):
                rose.update_quality()
            assert rose.items[0].quality == expected_quality
