from document import Document
from history import History

doc = Document()
history = History()

doc.set_content("a")
doc.set_font_name("times")
doc.set_font_size("12")
history.push(doc.create_state())

doc.set_content("b")
doc.set_font_name("mono")
history.push(doc.create_state())

doc.set_content("c")
doc.set_font_name("random")
doc.set_font_size("16")
history.push(doc.create_state())

doc.restore(history.pop())
doc.restore(history.pop())

print(doc.get_content(), doc.get_font_name(), doc.get_font_size())
