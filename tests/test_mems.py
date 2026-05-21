import pytest

from mems import MemeCollection


@pytest.fixture
def empty_collection():
    collection = MemeCollection()
    return collection


@pytest.fixture
def filled_collection():
    collection = MemeCollection()
    collection.add_meme("Wat", "странные", 1000)
    collection.add_meme("Дверь мне запили", "странные", 550)
    collection.add_meme("Surprise, mother faka", "сериальные", 20000)
    return collection


# ============= ТЕСТЫ =============
def test_collection_is_empty(empty_collection):
    assert len(empty_collection.memes) == 0
    assert empty_collection.get_most_popular() is None


def test_collection_is_filled(filled_collection):
    assert len(filled_collection.memes) > 0
    assert filled_collection.get_most_popular() is not None
