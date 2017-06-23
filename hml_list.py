def html_list(list_items):     
	"""
	Escreva a função html_list. A função pega um
	argumento, uma lista de strings, e retorna uma única string que é uma lista
	HTML. Por exemplo, a função deve produzir a seguinte string quando fornecida com
	a lista ['first string', 'second string'].
	"""
	
    HTML_string = "<ul>\n"
    for item in list_items:
        HTML_string += "<li>{}</li>\n".format(item)
    HTML_string += "</ul>"
    return HTML_string

list = ['first string', 'second string']
print(html_list(list))