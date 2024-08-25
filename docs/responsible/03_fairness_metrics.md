# Fairness Metrics

## 1. Demographic Parity (Independence)
$$P(\hat{Y}=1 | A=0) = P(\hat{Y}=1 | A=1)$$
The acceptance rate should be the same for Group A and Group B.
*Critique*: Allows accepting qualified A's and unqualified B's.

## 2. Equal Opportunity (Separation)
$$P(\hat{Y}=1 | Y=1, A=0) = P(\hat{Y}=1 | Y=1, A=1)$$
True Positive Rates (TPR) should be equal across groups.
*Ideally*: Qualified people from both groups have equal chance of being selected.

## 3. Calibration
$$P(Y=1 | \hat{Y}=s, A=0) = P(Y=1 | \hat{Y}=s, A=1)$$
If the model says "70% risk", it should be 70% risk for everyone.
