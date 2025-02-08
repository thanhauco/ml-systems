# Swarm Intelligence & Multi-Agent Systems

## Beyond the Monolith
By early 2025, the limitations of single, monolithic agents became clear. "Swarm" architectures emerged, where many specialized, lightweight agents collaborate to solve complex tasks.

## Key Patterns
1.  **Handoffs**: Agent A explicitly transfers control to Agent B (e.g., Triage Agent -> Billing Agent).
2.  **Broadcasting**: Agents publish messages to a shared bus; verified subscribers react.
3.  **Synthesizers**: A "Manager" agent aggregates partial results from "Worker" agents.

## The "Actor" Model
Swarms naturally map to the Actor Model of concurrency:
- Agents are isolated state units.
- They communicate *only* via asynchronous messages.
- No shared memory locks (though shared *state* usually exists in a DB).
