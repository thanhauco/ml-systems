# The Actor Pattern at Scale

## Stateless Tasks vs Stateful Actors
- **Tasks (`@ray.remote`)**: Pure functions. Great for data processing (map/reduce).
- **Actors (`@ray.remote` class)**: Stateful processes. Great for model holding, environment simulation, or DB connections.

## Actor Lifecycle
1.  **Creation**: `actor = MyActor.remote()`
2.  **Invocation**: `actor.method.remote()` returns an `ObjectRef`.
3.  **Death**: When ref count drops to zero, or manual kill.

## Scaling Patterns
- **Pool of Actors**: Maintain a fixed pool (e.g., 100 Simulators) and dispatch tasks to them via a queue.
- **Actor Handle Passing**: Pass the handle of Actor A to Actor B so they can communicate directly (p2p).
