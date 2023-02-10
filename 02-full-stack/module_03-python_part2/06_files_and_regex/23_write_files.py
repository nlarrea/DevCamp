# CREAR Y ESCRIBIR EN FICHEROS
"""
los ficheros normalmente se usan para loggear datos

open() -> nos permite crear o abrir ficheros. Si el fichero existía, lo abre,
si el fichero no existía, lo crea

w+ -> nos permite escribir en el archivo
"""

# crear o abrir un archivo
file_builder = open("02-full-stack/module_03-python_part2/06_files_and_regex/logger.txt", "w+")

# escribir en el archiv
file_builder.write("Hey, I'm in a file!")

# cerrar el archivo
file_builder.close()



# OTRO EJEMPLO
# se borrará lo que se haya escrito antes en el fichero, porque estamos usando 'w+'
file_builder = open("02-full-stack/module_03-python_part2/06_files_and_regex/logger.txt", "w+")

for i in range(100):
    file_builder.write(f"I'm on line {i + 1}\n")

file_builder.close()