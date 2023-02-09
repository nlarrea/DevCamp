# POLYMORPHISM
"""
tenemos la clase Html, que tiene un método llamado 'render', pero no para que
sea usado desde esta clase (lanzaría un error), sino para que sus child classes
puedan tener ese método y, usando el polimorfismo, aunque cada instancia use el
mismo método, para cada instancia el método será diferente
"""

class Html:
    def __init__(self, content):
        self.content = content

    def render(self):
        raise NotImplementedError("Subclass must implement render method")


class Heading(Html):
    def render(self):
        return f"<h1>{self.content}</h1>"


class Div(Html):
    def render(self):
        return f"<div>{self.content}</div>"


tags = [
    Div("Some content"),
    Heading("Some big heading"),
    Div("Another div")
]

for tag in tags:
    print(tag.render())
    
    """ se imprime lo siguiente:
    <div>Some content</div>
    <h1>Some big heading</h1>
    <div>Another div</div>
    """



# OTRA FORMA DE HACER LO MISMO CON FUNCIONES DE POLIMORFISMO
class Heading2:
    def __init__(self, content):
        self.content = content
    
    def render(self):
        return f"<h1>{self.content}</h1>"
    

class Div2:
    def __init__(self, content):
        self.content = content
    
    def render(self):
        return f"<div>{self.content}</div>"


div_one = Div("Some content")
heading = Heading("Some big heading")
div_two = Div("Another div")

def html_render(tag_object):
    print(tag_object.render())

html_render(div_one)        # <div>Some content</div>
html_render(heading)        # <h1>Some big heading</h1>
html_render(div_two)        # <div>Another div</div>



""" CUÁNDO USAR UNA FORMA U OTRA?
si solo tienes una parent class con un método compartido, es mejor usar la
segunda forma de hacerlo, pero si tus child classes comparten más datos con la
parent class, es mejor usar la primera forma
"""