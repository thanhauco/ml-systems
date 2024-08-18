# Privacy Preserving AI

## The Risks
1.  **Membership Inference Attack**: "Was Uncle Bob in the cancer study dataset?"
2.  **Model Inversion Attack**: Reconstructing the training face from the face recognition model.

## k-Anonymity
A dataset has k-anonymity if every record is indistinguishable from at least k-1 other records.
*Method*: Generalize/Suppress data. Turn "Age: 27" into "Age: 20-30".

## Differential Privacy (DP)
The Gold Standard.
*Definition*: The output of the algorithm should be roughly the same whether any single individual is in the dataset or not.
$$P(M(D) \in S) \le e^\epsilon P(M(D') \in S)$$
*Mechanism*: Add Laplacian or Gaussian noise to the gradients (DP-SGD) or the query result.
*Epsilon ($\epsilon$)*: The privacy budget. Lower is more private but less accurate.
