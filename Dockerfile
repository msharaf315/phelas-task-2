FROM python:3.11

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY extract_market_prices.py .

COPY market_price_repository.py .

COPY market_prices_analysis.py .

CMD ["python", "extract_market_prices.py"]