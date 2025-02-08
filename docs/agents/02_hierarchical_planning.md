# Hierarchical Planning

## Manager-Worker Topology
To handle long-horizon tasks (e.g., "Write a full codebase"), flat swarms struggle with coherence. Hierarchical planning introduces layers:
1.  **CEO/Planner**: Decomposes the ephemeral goal into milestones.
2.  **Manager**: Takes a milestone and breaks it into tasks.
3.  **Worker**: Executes a specific atomic task (Search, Code, Test).

## Dynamic Team Construction
Advanced swarms in 2025 construct teams *dynamically*. A Planner might decide: "For this query, I need 2 Researchers and 1 Writer," instantiating them on the fly.
