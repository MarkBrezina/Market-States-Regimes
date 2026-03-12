
def realized_volatility(returns, window=20):

    return returns.rolling(window).std() * np.sqrt(252)
