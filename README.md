# Market State Regimes

This repository explores **market regime detection** and how financial markets transition between different structural states such as:

- Trending markets
- Mean-reverting markets
- High volatility regimes
- Low volatility regimes
- Structural transitions

Understanding market regimes is essential for systematic trading because strategies behave differently depending on the underlying state of the market.

Examples:

| Strategy | Good Regime | Bad Regime |
|--------|--------|--------|
| Trend Following | Trending markets | Choppy markets |
| Mean Reversion | Range-bound markets | Strong trends |
| Volatility Strategies | High volatility | Quiet markets |

The goal of this project is to explore:

1. How regimes can be detected from market data
2. How volatility structures relate to regime shifts
3. How strategies behave under different regimes
4. Whether regime transitions can be predicted

---

# Methods Explored

The project explores several approaches to detecting market states:

- Hidden Markov Models
- Volatility clustering
- ARIMA residual structure
- Flow and momentum signals
- State convergence indicators

---

# Example Results

Some results explored in the notebooks:

- Volatility clustering indicating regime shifts
- Hidden Markov Models identifying bull/bear phases
- Convergence/divergence of signals before transitions

---

# Repository Structure
