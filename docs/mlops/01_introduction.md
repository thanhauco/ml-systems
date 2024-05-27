# Introduction to MLOps

## What is MLOps?
Machine Learning Operations (MLOps) is the set of practices that aims to deploy and maintain machine learning models in production reliably and efficiently.
It combines **Machine Learning**, **DevOps**, and **Data Engineering**.

## DevOps vs MLOps
| Feature | DevOps | MLOps |
| :--- | :--- | :--- |
| **Artifact** | Code | Code + Data + Model |
| **Versioning** | Git (Code) | Git (Code) + DVC (Data) + Registry (Model) |
| **Testing** | Unit/Integration | + Data validation, Model quality checks |
| **Monitoring** | CPU, Memory, Latency | + Data Drift, Concept Drift, Model Decay |
| **Retraining** | N/A | Essential loop |

## The Core Loop
1.  **Design**: Business Understanding.
2.  **Develop**: Experimentation, Training.
3.  **Operations**: Deployment, Monitoring, Governance.
