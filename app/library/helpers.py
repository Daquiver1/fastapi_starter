import os.path
import markdown

def openfile(filename):
	"""
	A function that takes markdown files in app/pages,
	converts to html and returns them
	"""
	filepath = os.path.join("app/pages/", filename)
	with open(filepath, "r", encoiding="utf-8") as input_file:
		text = input_file.read()

	html = markdown.markdown(text)
	data = {
			"text": html
	}
	return data