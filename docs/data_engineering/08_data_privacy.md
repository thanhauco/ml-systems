# Data Privacy and Security in ML

## PII (Personally Identifiable Information)
Names, Emails, IPs, Device IDs.
**Rule #1**: never train on raw PII unless absolutely necessary.

## Techniques for Anonymization
1.  **Masking**: `jordan@gmail.com` -> `******@gmail.com`.
2.  **Hashing**: `SHA256(email)`. (Warning: Vulnerable to rainbow tables if not salted).
3.  **Tokenization**: Swap PII for a random UUID in a secure vault.
4.  **Differential Privacy**: Add noise to the dataset so that no single individual's data can be reverse-engineered.
    -   *Concept*: The output of `Query(Database)` should be roughly the same whether `User X` is in the DB or not.

## GDPR and "Right to be Forgotten"
If a user requests deletion:
1.  Delete from Raw Database.
2.  Delete from Data Warehouse.
3.  **The Hard Part**: Delete from the *Trained Model*?
    -   *Machine Unlearning*: An active research field.
    -   *Practical Approach*: Retrain the model on the fresh dataset (without the user).

## Federated Learning
Train the model *on the user's device*. Only send weight updates (gradients) to the server. The raw data never leaves the phone.
