from tool import Tool


class BrushTool(Tool):
    def mouse_up(self):
        print("Brush Icon")

    def mouse_down(self):
        print("Draw a line")
