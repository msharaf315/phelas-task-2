FROM python:3.11

RUN pip install requests

COPY extract_market_prices.py .

CMD ["python", "extract_market_prices.py"]