import yfinance as yf

def get_asia_tech_risk(tickers):
    data = yf.download(tickers, period="2d")['Close']
    if data.empty:
        return {}
    percent_changes = data.pct_change().iloc[-1] * 100
    return percent_changes.to_dict()
