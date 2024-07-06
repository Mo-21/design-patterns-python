from tool import Tool

"""
Equals the Context class in the book
"""


class Canvas:
    def __init__(self, tool: Tool) -> None:
        self._current_tool = tool

    def mouse_up(self):
        self._current_tool.mouse_up()

    def mouse_down(self):
        self._current_tool.mouse_down()

    def get_current_tool(self):
        return self._current_tool

    def set_current_tool(self, value):
        self._current_tool = value
