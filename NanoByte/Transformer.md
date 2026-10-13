# Transformer Architecture Notes

## 📌 Keywords Covered
- Transformer
- Artificial Intelligence (AI)
- Machine Learning (ML)
- Deep Learning
- Neural Networks
- RNN
- Transformer Architecture
- Encoder
- Decoder
- Tokenization
- Token Embeddings
- Word Embeddings
- Positional Encoding
- Self-Attention
- Multi-Head Attention
- Feed Forward Network (FFN)
- Context Vectors
- Cross-Attention
- Masked Attention
- KV Cache
- Softmax
- Query (Q)
- Key (K)
- Value (V)
- GPT-1
- GPT-3
- GPT-4
- ChatGPT
- BERT
- Mixture of Experts (MoE)
- AI Agents
- Model Training
- Inference
- Parameters
- Hyperparameters
- Gradient Descent
- Loss Function
- Overfitting
- Underfitting
- Regularization

---

## 🏷️ Tags & Keywords Used in Notes
- `=>` (Sub-point)
- `->` (Flow / Relationship)
- AI
- ML
- RNN
- GPT
- BERT
- MoE
- FFN
- KV Cache

---

# Transformer

## Definition

A **Transformer** is a deep learning architecture introduced in **2017** that processes sequences using the **attention mechanism** instead of recurrence. Unlike RNNs, Transformers process tokens in parallel during training, making them significantly faster and more effective for capturing long-range dependencies.

---

# Key AI/ML Terminology

## Model

- A mathematical function that learns patterns from data to perform predictions or generate outputs.

---

## Parameters

- Internal values learned during training (e.g., weights and biases).

---

## Hyperparameters

- Configuration values set before training begins.
- Examples:
  - Learning Rate
  - Batch Size
  - Number of Epochs
  - Number of Layers

---

## Training

- The process of teaching the model using training data by updating its parameters.

---

## Inference

- Using a trained model to make predictions or generate outputs.

---

## Epoch

- One complete pass through the entire training dataset.

---

## Batch Size

- Number of training samples processed before updating the model parameters.

---

## Loss Function

- Measures how far the model's predictions are from the expected outputs.

---

## Gradient Descent

- Optimization algorithm used to minimize the loss function by updating model parameters.

---

## Overfitting

- Model learns the training data too well, including noise, resulting in poor generalization on new data.

---

## Underfitting

- Model fails to learn important patterns from the training data.

---

## Regularization

- Techniques used to reduce overfitting and improve model generalization.

---

# RNN (Recurrent Neural Network) Architecture

## Sequential Processing

### 1. Input Sequence

- Takes a sequence of inputs.
- Processes one input at a time in order.

---

### 2. Hidden State

- At every step, the model updates an internal memory called the **hidden state**.
- The hidden state is computed using:
  - Current input
  - Previous hidden state
- This enables RNNs to remember previous context.

---

### 3. Recurrent Connection

- The hidden state from the previous time step is passed to the next time step.
- This recurrent connection enables sequential memory across the input sequence.

---

# Limitations of RNNs

## Sequential Processing

- Words are processed one after another.
- **No parallelization**, leading to slower training.

---

## Vanishing / Exploding Gradients

- During backpropagation, gradients may:
  - Become extremely small (**vanishing gradients**)
  - Become extremely large (**exploding gradients**)
- Makes learning long-term dependencies difficult.

---

## Limited Long-Range Memory

- Hidden state has a fixed size.
- Creates an **information bottleneck**, making it difficult to retain information from distant tokens.

---

# Overcoming These Limitations

| Year | Milestone |
|------|-----------|
| **2017** | Transformer introduced |
| **2018** | GPT-1 / BERT |
| **2020** | GPT-3 |
| **2022** | ChatGPT |
| **2023** | GPT-4 |
| **2025–2026** | MoE (Mixture of Experts) / AI Agents |

---

# How Does a Transformer Work?

```text
Input
   │
   ▼
Attention
   │
   ▼
Output
```

---

# Transformer Architecture — Overview

```text
Input Text
      │
      ▼
Token Embedding
      │
      ▼
Encoder
      │
      ▼
Context Vectors
      │
      ▼
Decoder
      │
      ▼
Output
```

---

# Step 1 — Tokenization & Embeddings

## Tokenization

- Splits input text into smaller units called **tokens**.

---

## Word Embeddings

- Every token is mapped to a dense vector of numbers.
- These vectors are learned during training.

---

## Positional Encoding

- Since Transformers process tokens in parallel, positional information must be added.
- Uses **sine** and **cosine** functions to encode token positions.
- Allows the model to distinguish between positions such as **position 0** and **position 4**.

---

# Step 2 — Self-Attention (Core Mechanism)

Self-attention enables every token to determine how much attention it should give to every other token in the sequence.

## Query (Q)

- Represents what the current token is looking for.

---

## Key (K)

- Represents what each token offers.

---

## Value (V)

- Represents the information carried by each token.

---

# Step 3 — Multi-Head Attention

Instead of performing one attention operation, the Transformer performs multiple attention operations in parallel.

Different heads can learn different relationships.

### Head 1

- Syntax
- Grammar

### Head 2

- Semantics
- Meaning of words

### Head 3

- Long-range dependencies
- Relationships between distant tokens

---

# Step 4 — Feed Forward Network (FFN)

Each token independently passes through the same neural network.

```text
Input Vector
      │
      ▼
Linear Layer 1
      │
      ▼
ReLU Activation
      │
      ▼
Linear Layer 2
```

---

# Step 5 — Stacked Encoder Layers

- Multiple encoder layers are stacked together.
- Each successive layer builds a richer and more abstract representation of the input.

---

# Step 6 — Decoder — Generating Output Tokens

The decoder generates **one token at a time**.

### Generation Flow

```text
KV Cache
     +
Previous Token
      │
      ▼
Masked Attention
      │
      ▼
Cross-Attention
      │
      ▼
Feed Forward Network (FFN)
      │
      ▼
Softmax
      │
      ▼
Sample Next Token
```

---

## Masked Attention

- Decoder can only attend to tokens that have already been generated.
- Future tokens are hidden (masked).

**Purpose**

- Prevents the model from "cheating."
- Forces genuine **left-to-right generation**.

---

## Cross-Attention

- Reads the encoder's context vectors at every decoding step.
- Acts as the bridge between:
  - Source sentence
  - Target sentence / Generated output

---

## KV Cache (Key-Value Cache)

- Stores previously computed **Key** and **Value** vectors during inference.
- Prevents recomputation for earlier tokens.
- Significantly speeds up autoregressive text generation.

---

## Softmax

- Converts output scores (logits) into a probability distribution.
- The next token is sampled or selected based on these probabilities.

---

# Summary

## RNN Workflow

```text
Input
   │
   ▼
Hidden State
   │
   ▼
Next Hidden State
   │
   ▼
Output
```

---

## Transformer Workflow

```text
Input Text
      │
      ▼
Tokenization
      │
      ▼
Embeddings + Positional Encoding
      │
      ▼
Self-Attention
      │
      ▼
Multi-Head Attention
      │
      ▼
Feed Forward Network (FFN)
      │
      ▼
Stacked Encoder Layers
      │
      ▼
Context Vectors
      │
      ▼
Decoder
      │
      ▼
Masked Attention
      │
      ▼
Cross-Attention
      │
      ▼
Softmax
      │
      ▼
Generated Output Token