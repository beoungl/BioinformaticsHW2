from hmmlearn import hmm
import numpy as np
import math

model = hmm.MultinomialHMM(n_components = 2)
model.startprob_ = np.array([0.6666666,0.333333])
model.transmat_ = np.array([[0.8,0.2],[0.6,0.4]])
model.emissionprob_ = np.array([[0.8,0.2],[0.4,0.6]])
print(math.exp(model.score(np.array([[0,1]]))))
print(math.exp(model.score(np.array([[1,0]]))))
print(math.exp(model.score(np.array([[1,1]]))))
print(math.exp(model.score(np.array([[0,0]]))))

logprob1, seq1 = model.decode(np.array([[0,1,0]]).transpose())
print(seq1)
print(np.exp(logprob1))
logprob2,seq2 = model.decode(np.array([[0,1]]).transpose())
print(seq2, np.exp(logprob2))
logprob3, seq3 = model.decode(np.array([[0,1,0,1,0,1,0]]).transpose())
print(seq3,np.exp(logprob3))
logprob4, seq4 = model.decode(np.array([[0,0,1,1,1,0]]).transpose())
print(seq4,np.exp(logprob4))
