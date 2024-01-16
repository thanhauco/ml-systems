class PipelineStage:
    """
    Manages a subset of layers and point-to-point recv/send.
    """
    
    def __init__(self, stage_id, num_stages, model_chunk):
        self.stage_id = stage_id
        self.is_first = (stage_id == 0)
        self.is_last = (stage_id == num_stages - 1)
        self.model = model_chunk

    def step(self, batch=None):
        if not self.is_first:
            # batch = recv_from(self.stage_id - 1)
            print("Recv activations from prev stage")
            pass
            
        output = self.model(batch) if batch else "Forward"
        
        if not self.is_last:
            # send_to(self.stage_id + 1, output)
            print("Send activations to next stage")
            
        return output
