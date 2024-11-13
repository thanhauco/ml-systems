# Data Mesh in ML Contexts

## The Problem: The Monolithic Data Lake
-   Central Data Engineering team is a bottleneck.
-   Producers (Product teams) dump "garbage" into the lake.
-   Consumers (ML teams) struggle to understand the garbage.

## The Principle: Decentralization
Data Mesh treats data as a **Product**, not a byproduct.

### 1. Domain-Oriented Architecture
-   **Checkout Team** owns `checkout_events` data product.
-   **Inventory Team** owns `stock_levels` data product.
-   **ML Team** consumes these well-defined products.

### 2. Data as a Product
The data product must be:
-   **Discoverable**: Registered in a catalog.
-   **Addressable**: Unique global URI.
-   **Trustworthy**: SLOs on quality (e.g., "99.9% complete", "Freshness < 1 hour").
-   **Self-describing**: Schema and documentation included.

### 3. Self-Serve Data Infrastructure
The central platform team provides the *tools* (Infrastructure), not the *labor*.
-   "Here is a template to spin up a Spark Cluster."
-   "Here is a template to register a Data Product."

### 4. Federated Governance
Global standards (security, PII encoding), local application.

## Applying Mesh to ML: The "Model Mesh"
Can we treat Models as Products?
-   **Team A** builds "User Embedding Model". Exposes embeddings as a product.
-   **Team B** builds "Recommendation Model". Consumes user embeddings from Team A.
-   Decouples the teams. Team A can improve the embedding internally, as long as the API contract holds.
