from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import joblib
from numpy import round

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

model = joblib.load("model.pkl")

options = [
    "Did not Survive",
    "Survived"
]


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "request": request,
            "prediction": None
        }
    )
@app.post("/predict", response_class=HTMLResponse)
def predict(
    request: Request,
    Age: float = Form(...),
    Fare: float = Form(...),
    Pclass: float = Form(...),
    Sex: float = Form(...),
    SibSp: float = Form(...),
    Parch: float = Form(...)
):

    # Input data
    input_data = [[
        Age,
        Fare,
        Pclass,
        Sex,
        SibSp,
        Parch
    ]]

    # Prediction
    prediction = model.predict(input_data)[0]

    # Prediction probabilities
    predict_probability = model.predict_proba(input_data)

    # Predicted class (0 or 1)
    predicted_class = int(prediction)

    # Survived / Did not Survive
    predicted_option = options[predicted_class]

    # Confidence of predicted class
    probability = round(
        float(predict_probability[0][predicted_class]) * 100,
        2
    )

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "request": request,
            "prediction": predicted_option,
            "probability": probability
        }
    )
