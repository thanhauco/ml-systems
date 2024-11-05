class Autoscaler:
    """
    Scales replicas based on Queries Per Second (QPS).
    """
    
    def __init__(self, target_qps_per_replica=100):
        self.target = target_qps_per_replica
        self.replicas = 1

    def update(self, current_total_qps):
        needed = max(1, int(current_total_qps / self.target))
        if needed != self.replicas:
            print(f"Rescaling: QPS={current_total_qps}. Replicas {self.replicas} -> {needed}")
            self.replicas = needed
            # k8s_api.scale_deployment("my-model", replicas)
        else:
            print(f"Stable: QPS={current_total_qps}. Replicas {self.replicas}")
        return self.replicas


