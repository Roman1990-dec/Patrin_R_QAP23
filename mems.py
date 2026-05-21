class MemeCollection:
    def __init__(self):
        self.memes = []

    def add_meme(self, title, category, likes):
        self.memes.append({"title": title, "category": category, "likes": likes})

    def get_by_category(self, category):
        return [meme for meme in self.memes if meme["category"] == category]

    def get_most_popular(self):
        if not self.memes:
            return None

        return max(self.memes, key=lambda meme: meme["likes"])

    def clear(self):
        self.memes = []


# 1 Создать фикстуру которая будет создавать и возвращать пустую коллекцию
# 2 Создать фикстуру которая будет подготавливать данные и создавать коллекцию мемов
# 3 Создать тесты:
#               1 проверить что коллекция пустая
#               2 проверить что коллекция заполнена
#               3 добавить колецию посмотреть что есть новая запись
