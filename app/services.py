import yfinance as yf
from langchain.schema import HumanMessage
from .models import llm

def get_stock_price(ticker: str):
    stock = yf.Ticker(ticker)
    try:
        history = stock.history(period="1d")

        if history.empty:
            return {"error": "Invalid ticker symbol or no data available."}

        price = history["Close"].iloc[-1]
        return {"ticker": ticker, "price": round(price, 2)}

    except Exception as e:
        return {"error": f"Failed to retrieve stock data"}

def analyze_stock(ticker):
    stock = yf.Ticker(ticker)
    price_data = stock.history(period="1d")

    if price_data.empty:
        return {"ticker": ticker, "price": None, "AI_Analysis": "No data available. Stock may be delisted or invalid."}

    price = price_data["Close"].iloc[-1]

    prompt = f"Analyze the stock price trends, valuation, and key financial indicators for {ticker} with a current price of ${price:.2f}. Based on this, provide buy, sell, or hold only state wether to buy,hold or sell statement only"
    response = llm.generate_content(prompt)

    if response and response.candidates:
        ai_analysis = response.candidates[0].content.parts[0].text.strip().replace("\n", " ").replace("**", "")
    else:
        ai_analysis = "No response from AI"

    return {"ticker": ticker, "price": round(price, 2), "AI_Analysis": ai_analysis}

