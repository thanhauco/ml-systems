# ML Systems: Theory & Code
> *From Principles to Production: A Comprehensive Engineering Resource*

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![PyTorch](https://img.shields.io/badge/pytorch-2.0%2B-orange)
![Status](https://img.shields.io/badge/status-complete-green)

This repository serves as a **production-grade implementation guide** for modern Machine Learning Systems. Unlike traditional academic resources that focus solely on algorithms, this emphasizes the **system engineering**, **infrastructure**, and **operational rigor** required to build scalable AI platforms.

It bridges the gap between research notebooks and high-scale production services.

## 📊 Project Overview

- **Scale**: ~350+ source files across 10 distinct engineering disciplines.
- **Goal**: To provide copy-pasteable patterns and deep theoretical context for Principal Engineers and Architects.

## 📚 Curriculum Structure

The project is organized into 10 modular topics. Each topic contains a dedicated `docs/` folder for theory and diverse `src/` modules for implementation.

| Topic | Theory Docs | Implementation | Engineering Concepts |
|-------|-------------|----------------|----------------------|
| **1. System Design** | `docs/system_design/` | `src/ml_system/` | Reliability patterns, Data Mesh, Batch vs Stream pipelines. |
| **2. Data Engineering** | `docs/data_engineering/` | `src/data_engineering/` | Lakehouse architecture, ETL, Delta Lake, Vector Databases. |
| **3. Model Deployment** | `docs/deployment/` | `src/deployment/` | Kubernetes, Docker, Triton, gRPC, Canary deployments. |
| **4. MLOps Lifecycle** | `docs/mlops/` | `src/mlops/` | CI/CD on Jenkins/Actions, Model Registry, Drift Detection. |
| **5. Edge AI** | `docs/edge/` | `src/edge/` | TinyML, TFLite/TensorRT optimization, Pruning & Quantization. |
| **6. Responsible AI** | `docs/responsible/` | `src/responsible/` | Fairness metrics, SHAP/LIME Explainability, Differential Privacy. |
| **7. Fine-Tuning & LLMs** | `docs/llm/` | `src/llm/` | PEFT/LoRA, RAG Pipelines, Agentic workflows, RLHF. |
| **8. Scaling ML** | `docs/scaling/` | `src/scaling/` | Infrastructure as Code (Terraform), Slurm, Ray Clusters. |
| **9. Distributed Training** | `docs/distributed/` | `src/distributed/` | DDP, FSDP, 3D Parallelism (Data/Tensor/Pipeline). |
| **10. Multimodal** | `docs/multimodal/` | `src/multimodal/` | Diffusion Models, Vision Transformers (ViT), CLIP alignment. |
| **11. Reasoning Models** | `docs/reasoning/` | `src/reasoning/` | System 2, Tree-of-Thoughts (ToT), Chain-of-Thought (CoT). |
| **12. Autonomous Swarms** | `docs/agents/` | `src/agents/` | Multi-Agent Orchestration, Hierarchical Planning, Actor Model. |
| **13. High-Performance Serving** | `docs/serving_optimization/` | `src/serving_optimization/` | vLLM, PagedAttention, Continuous Batching. |
| **14. Distributed Orchestration** | `docs/distributed_ray/` | `src/distributed_ray/` | Ray Clusters, Global Control Store, Parameter Server. |

## 🛠️ Getting Started

### Prerequisites
*   Python 3.10+
*   Docker & Kubernetes (Minikube/Kind recommended for local testing)
*   NVIDIA GPU (Optional, for Distributed/Scaling modules)

### Installation
```bash
git clone https://github.com/google-deepmind/ml-systems-textbook.git
cd ml-systems-textbook
pip install -r requirements.txt
```

### Running Key Examples

**1. Distributed Training (Topic 9)**
Simulate a Distributed Data Parallel (DDP) training loop:
```bash
python src/distributed/examples/train_dist.py
```

**2. RAG Pipeline for LLMs (Topic 7)**
Run a local Retrieval Augmented Generation pipeline:
```bash
python src/llm/rag/generator.py
```

**3. Edge Inference Loop (Topic 5)**
Run a mocked infinite inference loop for embedded devices:
```bash
python src/edge/runtime/edge_inference_loop.py
```

**4. Multimodal Generation (Topic 10)**
Execute a Text-to-Image pipeline mockup:
```bash
python src/multimodal/pipelines/txt2img.py
```

**5. Autonomous Swarm Mission (Topic 12)**
Initialize a multi-agent swarm to solve a hierarchical task:
```bash
python src/agents/swarm_orchestrator.py
```

python src/agents/swarm_orchestrator.py
```

**6. vLLM Engine Simulation (Topic 13)**
Run a continuous batching scheduler loop:
```bash
python src/serving_optimization/vllm_lite.py
```

**7. Distributed Ray Job (Topic 14)**
Launch a simulated cluster and run a parameter server training job:
```bash
python src/distributed_ray/distributed_trainer.py
```

## 📓 Notebooks (Capstone Projects)
Three "Big Projects" are provided in the `notebooks/` directory to demonstrate end-to-end workflows:

| Notebook | Focus | Key Integrations |
|----------|-------|------------------|
| **01 The Brain** | Enterprise RAG | `src/data_engineering` + `src/reasoning` |
| **02 The Forge** | Distributed Factory | `src/distributed_ray` + `src/serving_optimization` |
| **03 The Studio** | Creative Agency | `src/multimodal` + `src/agents` |

## 📝 License
MIT License.
