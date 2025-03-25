# Stock Price & Analysis API

A FastAPI-based stock price and AI-powered stock analysis API using Yahoo Finance and Gemini AI.

## Features
- Fetch real-time stock prices using Yahoo Finance.
- AI-based stock analysis (Hold or Sell) using Google Gemini AI.

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/stock-api.git
   cd stock-api
   ```

2. Create and activate a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## API Endpoints

### Get Stock Price
- **URL:** `GET /stock/{stock_name}`
- **Description:** Fetches the latest stock price.
- **Example:**
  ```sh
  curl http://127.0.0.1:8000/stock/AAPL
  ```
- **Response:**
  ```json
  {
    "ticker": "AAPL",
    "price": 179.32
  }
  ```

### AI-based Stock Analysis
- **URL:** `GET /analyze/{stock_name}`
- **Description:** Uses AI to analyze stock performance and provide a recommendation (Hold or Sell).
- **Example:**
  ```sh
  curl http://127.0.0.1:8000/analyze/AAPL
  ```
- **Response:**
  ```json
  {
    "ticker": "AAPL",
    "price": 179.32
    "recommendation": "Hold"
  }
  ```

## Running the API
Start the FastAPI server:
```sh
uvicorn main:app --reload
```

## Environment Variables
- `GOOGLE_API_KEY` - Required for Gemini AI integration.

## License
This project is licensed under the MIT License.
