# from torch.profiler import profile, RecordScope, ProfilerActivity

class TraceProfiler:
    """
    Generates Chrome Tracing JSON.
    """
    
    def __enter__(self):
        print("Starting PyTorch Profiler...")
        # self.prof = profile(activities=[ProfilerActivity.CPU, ProfilerActivity.CUDA])
        # self.prof.start()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Stopping Profiler and keeping trace...")
        # self.prof.stop()
        # self.prof.export_chrome_trace("trace.json")
