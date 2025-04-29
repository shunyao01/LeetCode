# Machine Learning Engineer (MLE) - System Design Q&A

This document provides common system design interview questions for junior Machine Learning Engineers, along with concise answers and reasoning.

---

## 1. How would you deploy a trained model to production?

**Answer:**
> Export the trained model (e.g., as a pickle, ONNX, or joblib file), wrap it in an API using Flask or FastAPI, containerize it with Docker, and deploy to a cloud service (e.g., AWS ECS, Cloud Run). For real-time applications, the API serves predictions. For batch jobs, use scheduled workflows to process data and store outputs.

---

## 2. How would you update a model when new data arrives?

**Answer:**
> Periodically retrain the model with new labeled data, validate it, and if it performs better, deploy the new version. This can be manual (e.g., weekly) or automated with pipelines (e.g., Airflow, CI/CD). Ensure rollback is possible.

---

## 3. How would you monitor a model in production for degradation?

**Answer:**
> Monitor both input data and model predictions. For data, check feature distribution shifts (e.g., data drift). For predictions, track performance metrics like accuracy, confidence scores, and prediction distribution. Set up alerts for anomalies.

---

## 4. Would you use batch or real-time inference for [some use case]?

**Example: Fraud detection during checkout**

**Answer:**
> Use real-time inference due to the need for instant decisions. Batch is better for non-time-sensitive tasks like offline analytics or periodic reporting.

---

## 5. Describe the end-to-end ML pipeline.

**Answer:**
> 1. Data ingestion (from logs, DBs)
> 2. Data preprocessing/feature engineering
> 3. Model training and validation
> 4. Deployment (real-time or batch)
> 5. Monitoring and feedback loops
> 6. Periodic retraining

---

## 6. What trade-offs do you consider when designing ML systems?

**Answer:**
> - **Latency vs accuracy**: Smaller models are faster, but may lose precision
> - **Batch vs real-time**: Real-time is responsive but complex; batch is simpler
> - **Interpretability vs complexity**: Simple models are easier to debug
> - **Retraining frequency vs stability**: Too frequent = overfitting; too little = staleness
> - **Cost vs performance**: GPUs are fast but expensive

---

## Tips for Interviews
- Be ready to explain your reasoning
- Ask clarifying questions ("Is latency critical?", "Does this need to scale?")
- Focus on practical design and real-world impact

