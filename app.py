from pathlib import Path

import joblib
import pandas as pd
from flask import Flask, render_template, request

app = Flask(__name__)

# Cargar el modelo una vez, al iniciar la aplicación
carpeta = Path(__file__).resolve().parent
modelo = joblib.load(carpeta / "studybot_model.joblib")

# Conservar los nombres y el orden utilizados al entrenar
columnas = list(modelo.feature_names_in_)


def predecir_lugar(valores):
    entrada = pd.DataFrame([valores], columns=columnas)
    prediccion = modelo.predict(entrada)[0]

    return "APTO" if prediccion == 1 else "NO APTO"


@app.route("/", methods=["GET", "POST"])
def inicio():
    resultado = None
    error = None
    seleccion = {}

    if request.method == "POST":
        seleccion = request.form.to_dict()

        try:
            valores = []

            for columna in columnas:
                valor = float(request.form.get(columna, ""))

                if valor not in (0, 1):
                    raise ValueError

                valores.append(int(valor))

            resultado = predecir_lugar(valores)

        except (ValueError, TypeError):
            error = "Completa todos los campos con valores de 0 o 1."

    return render_template(
        "index.html",
        columnas=columnas,
        resultado=resultado,
        error=error,
        seleccion=seleccion
    )


if __name__ == "__main__":
    app.run(port=5001)