class History:
    def __init__(self):
        self.__states = []

    def push(self, state):
        self.__states.append(state)

    def pop(self):
        return self.__states.pop()
