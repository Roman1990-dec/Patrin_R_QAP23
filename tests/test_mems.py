import pytest

from mems import MemeCollection


# ========== 1. Фикстуры ==========
@pytest.fixture
def empty_collection():
    coll = MemeCollection()
    return coll


@pytest.fixture
def filled_collection():
    coll = MemeCollection()
    coll.add_meme("Дверь мне запили", "чудики", "120")
    coll.add_meme("Wat", "чудики", "4440")
    coll.add_meme("Surprise mothf**r", "сериалы", "50000")
    coll.add_meme("Reptile", "животные", "200")
    return coll


@pytest.fixture
def cleanup_collection():
    coll = MemeCollection()
    yield coll
    coll.clear()


# ========== 2. Базовое поведение ==========
def test_new_collection_is_empty(empty_collection):
    """Новая коллекция мемов пустая"""
    assert len(empty_collection.memes) == 0
    assert empty_collection.get_most_popular() is None


def test_filled_collection_contains_memes(filled_collection):
    """ "подготовленная через фикстуру коллекция содержит мемы"""
    assert len(filled_collection.memes) > 0
    assert filled_collection.memes[0]["title"] is not None


def test_add_meme_success(empty_collection):
    """ "
    - новый мем успешно добавляется в коллекцию
    - после добавления количество мемов увеличивается на 1
    - данные добавленного мема сохраняются корректно: title, category, likes
    """
    old_len = len(empty_collection.memes)
    result = empty_collection.add_meme("Бобер ААААА", "животные", "9999999")
    assert result == "Success"
    assert len(empty_collection.memes) == old_len + 1
    added = empty_collection.memes[-1]
    assert added["title"] == "Бобер ААААА"
    assert added["category"] == "животные"
    assert added["likes"] == "9999999"


# ========== 3. ПОИСК ПО КАТЕГОРИИ ==========
def test_get_by_category_exists(filled_collection):
    """Категория существует — метод возвращает список мемов этой категории"""
    result = filled_collection.get_by_category("чудики")
    assert len(result) == 2
    for meme in result:
        # из-за ошибки в get_by_category (сравнивается title, а не category) тест упадёт
        assert meme["category"] == "чудики"


def test_get_by_category_not_exist(filled_collection):
    """ "Категория не существует — метод возвращает пустой список"""
    result = filled_collection.get_by_category("спортики")
    assert result == []


# ========== 4. САМЫЙ ПОПУЛЯРНЫЙ МЕМ ==========
def test_most_popular_empty(empty_collection):
    """в коллекции нет мемов — метод возвращает None"""
    assert empty_collection.get_most_popular() is None


def test_most_popular(filled_collection):
    """в коллекции несколько мемов с разным количеством лайков
    — метод возвращает мем с максимальным количеством лайков
    """
    # ожидается мем с максимальным лайком 50000 - "Surprise mothf**r"
    popular = filled_collection.get_most_popular()
    # из-за ошибки (min вместо max) тест упадёт
    assert popular["title"] == "Surprise mothf**r"
    assert int(popular["likes"]) == 50000


def test_most_popular_tie_likes():
    """в коллекции несколько мемов с одинаковым количеством лайков
    — метод возвращает один из мемов с этим значением.
    """
    coll = MemeCollection()
    coll.add_meme("Мем1", "спорт", "100")
    coll.add_meme("Мем2", "авто", "100")
    popular = coll.get_most_popular()
    assert int(popular["likes"]) == 100
    assert popular["title"] in ["Мем1", "Мем2"]


# ========== 5. ОЧИСТКА КОЛЛЕКЦИИ ==========
def test_clear_collection(filled_collection):
    """ "
    - берёт заполненную коллекцию;
    - вызывает метод clear;
    - проверяет, что после очистки список мемов пустой.
    """
    assert len(filled_collection.memes) > 0
    filled_collection.clear()
    # из-за ошибки (pop вместо полной очистки) останутся элементы, тест упадёт
    assert len(filled_collection.memes) == 0


# ========== 6. ВАЛИДАЦИЯ ВХОДНЫХ ДАННЫХ ==========
@pytest.mark.parametrize(
    "title, category, likes",
    [
        ("Название", "категория", 100),
        ("  с пробелами  ", "  котики  ", 0),
        ("Мем", "фото", 999999),
    ],
)
def test_add_meme_valid_data(empty_collection, title, category, likes):
    result = empty_collection.add_meme(title, category, likes)
    #из-за ошибки (ждёт строку для likes) упадёт
    assert result == "Success"
    assert len(empty_collection.memes) == 1


@pytest.mark.parametrize(
    "title, category, likes, expected_error_substring",
    [
        ("", "норм", "10", "title не должен быть пустым"),
        ("  ", "норм", "10", "title не должен быть пустым"),
        ("норм", "", "10", "category не должен быть пустым"),
        ("норм", "  ", "10", "category не должен быть пустым"),
        ("норм", "норм", "", "likes не должен быть пустым"),
        ("норм", "норм", "  ", "likes не должен быть пустым"),
        ("норм", "норм", "abc", "likes должен быть строкой с числом"),
        ("норм", "норм", "-5", "likes должен быть строкой с числом"),
        (123, "норм", "10", "title должен быть строкой"),
        ("норм", 456, "10", "category должен быть строкой"),
        ("норм", "норм", 3.14, "likes должен быть строкой"),
    ],
)
def test_add_meme_invalid_data(
    empty_collection, title, category, likes, expected_error_substring
):
    result = empty_collection.add_meme(title, category, likes)
    assert result != "Success"
    if result is not True and isinstance(result, str):
        assert expected_error_substring in result
    else:
        assert result != "Success"
