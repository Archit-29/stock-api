from fastapi import FastAPI
from .services import get_stock_price, analyze_stock
import google.generativeai as genai
from app.config import Config

genai.configure(api_key=Config.GOOGLE_API_KEY)

app = FastAPI(title="Stock Market AI Agent", version="1.0")

@app.get("/")
def home():
    return {"message": "Stock Market AI API is Running"}

@app.get("/stock/{ticker}")
def stock_price(ticker: str):
    return get_stock_price(ticker)

@app.get("/analyze/{ticker}")
def stock_analysis(ticker: str):
    return analyze_stock(ticker)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
