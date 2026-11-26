# StudyBot

Aplicación en Flask que utiliza un modelo Gradient Boosting entrenado para predecir si un lugar es apto para trabajar durante 30 minutos.

## Cómo ejecutarlo

Desde la terminal, dentro de la carpeta del proyecto:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python app.py
```

Abrir http://127.0.0.1:5001 en el navegador.

Seleccionar las condiciones del lugar y presionar **Evaluar lugar**. El archivo `studybot_model.joblib` debe estar en la misma carpeta que `app.py`.

Para detener la aplicación, presionar **Control + C** en la terminal.