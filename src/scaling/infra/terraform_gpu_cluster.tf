resource "aws_instance" "gpu_node" {
  count         = 4
  ami           = "ami-0123456789" # Deep Learning AMI
  instance_type = "p4d.24xlarge" # 8x A100

  placement_group = aws_placement_group.cluster.id
  
  tags = {
    Name = "GPU-Worker-${count.index}"
    Project = "ScalingML"
  }
}

resource "aws_placement_group" "cluster" {
  name     = "gpu-cluster-placement"
  strategy = "cluster" # Pack nodes close together for low latency
}

resource "aws_efs_file_system" "dataset_store" {
  creation_token = "ml-datasets"
}
