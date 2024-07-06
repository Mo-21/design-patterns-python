from tool import Tool


class SelectionTool(Tool):
    def mouse_up(self):
        print("Selection Icon")

    def mouse_down(self):
        print("Draw a dashed line")
