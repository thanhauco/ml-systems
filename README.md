# ML Systems (Theory & Code)

A comprehensive, modular resource for mastering modern Machine Learning Systems. This repository bridges the gap between theoretical textbooks and production-grade engineering.

## 📚 Project Structure

The project is divided into 10 core topics, each containing focused Data Structures, Algorithms, and System Architectures.

| Topic | Theory (`docs/`) | Code (`src/`) | Key Concepts |
|-------|------------------|---------------|--------------|
| **1. System Design** | `docs/system_design/` | `src/ml_system/` | Reliability, Scalability, Modularity, Data Mesh. |
| **2. Data Engineering** | `docs/data_engineering/` | `src/data_engineering/` | Ingestion, ETL, Delta Lake, Vector DBs. |
| **3. Model Deployment** | `docs/deployment/` | `src/deployment/` | Kubernetes, Docker, Triton, gRPC, Monitoring. |
| **4. MLOps Lifecycle** | `docs/mlops/` | `src/mlops/` | CI/CD, Experiment Tracking, Model Registry, Drift detection. |
| **5. Edge AI** | `docs/edge/` | `src/edge/` | TFLite, TensorRT, Pruning, Quantization, TinyML. |
| **6. Responsible AI** | `docs/responsible/` | `src/responsible/` | Fairness, Explainability (SHAP), Privacy (DP), Green AI. |
| **7. Fine-Tuning & LLMs** | `docs/llm/` | `src/llm/` | LoRA, PEFT, RAG, Agents, RLHF. |
| **8. Scaling ML** | `docs/scaling/` | `src/scaling/` | Ray, Slurm, K8s, Autoscaling, Cost Optimization. |
| **9. Distributed Training** | `docs/distributed/` | `src/distributed/` | DDP, FSDP, 3D Parallelism, Optimizers (LARS/Lamb). |
| **10. Multimodal** | `docs/multimodal/` | `src/multimodal/` | Diffusion, ViT, CLIP, Audio, Video Generation. |

## 🛠️ Getting Started

### Prerequisites
- Python 3.10+
- PyTorch 2.0+
- Docker & Kubernetes (Local: Minikube/Kind)

### Installation
```bash
git clone https://github.com/google-deepmind/ml-systems-textbook.git
cd ml-systems-textbook
pip install -r requirements.txt
```

### Running Examples

**Distributed Training (Topic 9)**
```bash
python src/distributed/examples/train_dist.py
```

**RAG Pipeline (Topic 7)**
```bash
python src/llm/rag/generator.py
```

**Edge Inference (Topic 5)**
```bash
python src/edge/runtime/edge_inference_loop.py
```

## 📈 Stats
- **Total Files**: ~350+
- **Languages**: Python, C++, SQL, Bash, YAML, Dockerfile
- **Coverage**: End-to-End ML Lifecycle

## 📝 License
MIT License.
