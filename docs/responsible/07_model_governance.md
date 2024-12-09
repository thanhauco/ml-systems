# Model Governance and Auditing

## Trust but Verify
Organizations need a "Control Plane" for AI.

## Key Components
1.  **Model Cards**: Documentation. "Usage", "Limitations", "Training Data".
2.  **Human-in-the-loop (HITL)**: High-stakes decisions (e.g., denying bail) must be reviewed by a human.
3.  **Audit Trails**: Immutable logs. "Model V3 predicted X at time T".
4.  **Role Based Access Control (RBAC)**: Only Lead Data Scientist can deploy to Prod.

## The Audit Checklist
-   [ ] Is the data representative?
-   [ ] Have we tested for bias on protected groups?
-   [ ] Is the model robust to adversarial attacks?
-   [ ] Is there a fallback mechanism?
