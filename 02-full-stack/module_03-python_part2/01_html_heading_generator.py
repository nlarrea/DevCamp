""" ENUNCIADO
sintaxis:
heading_generator(title, heading_type)

ejemplos:
heading_generator('Greeting', '1')
<h1>Greeting</h1>

heading_generator('Greeting', '3')
<h3>Greeting</h3>
"""

def heading_generator(title, h_type):
    return f"<h{h_type}>{title}</h{h_type}>"

print(heading_generator("Greeting", "1"))
print(heading_generator("Greeting", "3"))