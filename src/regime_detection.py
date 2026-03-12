from hmmlearn.hmm import GaussianHMM
import numpy as np

def detect_regimes(returns, n_states=2):

    model = GaussianHMM(
        n_components=n_states,
        covariance_type="full",
        n_iter=1000
    )

    model.fit(returns.reshape(-1,1))
    states = model.predict(returns.reshape(-1,1))

    return states
