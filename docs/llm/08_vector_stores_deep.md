# Vector Stores & Retrieval

## ANN (Approximate Nearest Neighbors)
Exact Search ($O(N)$) is too slow for 1B vectors. ANN trades accuracy for speed.

## Algorithms
1.  **HNSW (Hierarchical Navigable Small World)**:
    -   Graph-based.
    -   Fastest query time, higher memory usage.
    -   Standard in Weaviate, Chroma, Qdrant.
2.  **IVF (Inverted File Index)**:
    -   Clustering (K-Means).
    -   Search only the nearest cluster.
    -   FAISS implementation.

## Distance Metrics
-   **Cosine Similarity**: Angle between vectors. (Normalized).
-   **Euclidean (L2)**: Straight line distance.
-   **Dot Product**: Magnitude aware.

## Filtering
"Find vectors near 'Apple' WHERE year > 2020".
-   **Pre-filtering**: Filter then search (can yield empty results if K is small).
-   **Post-filtering**: Search then filter (wasteful).
-   **Native filtering**: HNSW with bitmaps.
