# importing os
import os

# Importing the class Flask
from flask import Flask, render_template
# render template es poara render un archivo html

# Creating an instance of this class
#  El argumento __name__ es una variable predefinida de Python que representa el nombre del módulo actual.
app = Flask(__name__)

# route decorator


@app.route("/")
def index():
    return render_template('index.html')


if __name__ == "__main__":  # garantiza que el servidor web se ejecute solo si el script es ejecutado directamente,
    app.run(  # se utiliza para ejecutar la aplicación Flask.
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True  # nunca en production application o cuando lo mandamos a evaluar
    )
