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
    prediction = model.predict([[
        Age,
        Fare,
        Pclass,
        Sex,
        SibSp,
        Parch
    ]])
    predict_probability = model.predict_proba([[
        Age,
        Fare,
        Pclass,
        Sex,
        SibSp,
        Parch
    ]])
    predicted_class = int(prediction[0])
    predicted_option = options[predicted_class]
    probability = round(predict_probability[0],2)

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "request": request,
            "prediction": predicted_option,
            "probability": probability
        }
    )
