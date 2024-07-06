from document_state import DocumentState


class Document:
    def __init__(self):
        self.__content = None
        self.__font_name = None
        self.__font_size = None

    def get_content(self):
        return self.__content

    def set_content(self, value):
        self.__content = value

    def get_font_name(self):
        return self.__font_name

    def set_font_name(self, value):
        self.__font_name = value

    def get_font_size(self):
        return self.__font_size

    def set_font_size(self, value):
        self.__font_size = value

    def create_state(self):
        return DocumentState(self.__content, self.__font_name, self.__font_size)

    def restore(self, state: DocumentState):
        self.__content = state.get_content()
        self.__font_name = state.get_font_name()
        self.__font_size = state.get_font_size()
