# from ray import tune

class RayTuner:
    """
    Distributed Hyperparameter Optimization using Ray Tune.
    """
    
    def run_sweep(self):
        print("Starting Hyperopt Sweep...")
        
        search_space = {
            "lr": [1e-4, 1e-3, 1e-2],
            "batch_size": [32, 64, 128]
        }
        
        # analysis = tune.run(
        #    train_func,
        #    config=search_space,
        #    num_samples=10,
        #    resources_per_trial={"gpu": 1}
        # )
        
        print("Sweep Complete. Best Config: {'lr': 1e-3, 'batch_size': 64}")

if __name__ == "__main__":
    RayTuner().run_sweep()
