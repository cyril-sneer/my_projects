class Book:
    def __init__(self, title, author, publisher):
        self.__title = title
        self.__author = author
        self.__publisher = publisher

    def set_title(self, title):
        self.__title = title
    def get_title(self):
        return self.__title

    def set_author(self, author):
        self.__author = author
    def get_author(self):
        return self.__author

    def set_putlisher(self, publisher):
        self.__publisher = publisher
    def get_publisher(self):
        return self.__publisher

    def __str__(self):
        state_string = f"Название: {self.__title} \n" \
                       f"Автор: {self.__author} \n" \
                       f"Издатель: {self.__publisher}"
        return state_string