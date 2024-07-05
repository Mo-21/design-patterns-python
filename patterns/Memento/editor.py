from editor_state import EditorState


class Editor:

    def __init__(self):
        self.__content = None

    def get_content(self):
        return self.__content

    def set_content(self, value):
        self.__content = value

    def create_state(self):
        return EditorState(self.__content)

    def restore(self, state: EditorState):
        self.__content = state.get_state()
