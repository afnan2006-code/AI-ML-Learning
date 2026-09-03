# Day 14 — Sentiment Analysis with DistilBERT

## 📌 Project Overview

Day 14 focused on building a **Sentiment Analysis model using DistilBERT and PyTorch**.

The project uses customer review text to classify reviews into two sentiment categories:

* **0 → Negative**
* **1 → Positive**

Sentiment labels were generated from the review ratings:

* Rating ≥ 4 → Positive
* Rating ≤ 3 → Negative

## 📊 Dataset

* Total reviews: **1,000**
* Training samples: **800**
* Testing samples: **200**
* Features available: 6
* Text feature used: `Cleaned_Review`
* Target: `Sentiment`

### Class Distribution

* Negative: **655 (65.5%)**
* Positive: **345 (34.5%)**

## 🤖 Model

The project uses:

* **DistilBERT**
* PyTorch
* Hugging Face Transformers
* AdamW optimizer
* CrossEntropyLoss
* CPU training

The pretrained `distilbert-base-uncased` model was fine-tuned for binary sentiment classification.

## ⚙️ Training

* Epochs: **3**
* Batch size: **16**
* Learning rate: **2e-5**
* Maximum sequence length: **128**

### Training Loss

| Epoch | Training Loss |
| ----- | ------------: |
| 1     |        0.3136 |
| 2     |        0.0121 |
| 3     |        0.0046 |

## 📈 Evaluation

The fine-tuned model achieved:

**Test Accuracy: 100%**

Classification results:

| Class    | Precision | Recall | F1-Score |
| -------- | --------: | -----: | -------: |
| Negative |      1.00 |   1.00 |     1.00 |
| Positive |      1.00 |   1.00 |     1.00 |

The test set contained **200 reviews**.

## 🔍 Inference

The trained model was tested on new reviews.

Example positive review:

> The product is excellent and I am very happy with it.

**Prediction: Positive**

Example negative review:

> The product stopped working after only a few days and I am very disappointed.

**Prediction: Negative**

## 💾 Saved Model

The fine-tuned model and tokenizer were saved to:

`day14_sentiment_model`

## 🛠️ Technologies

* Python
* PyTorch
* Hugging Face Transformers
* DistilBERT
* scikit-learn
* Pandas
* Matplotlib
* Jupyter Notebook

## 📁 Project Structure

```text
Day 14/
├── sentiment_analysis.ipynb
├── day14_sentiment_model/
└── README.md
```

## 🎯 Key Learning Outcomes

* Working with pretrained Transformer models
* Tokenizing text with a Hugging Face tokenizer
* Creating PyTorch datasets and DataLoaders
* Fine-tuning DistilBERT for classification
* Evaluating NLP classification models
* Performing sentiment inference on new text
* Saving and reusing a fine-tuned Transformer model

## ⚠️ Note

The reported 100% test accuracy should be interpreted carefully because sentiment labels were derived directly from review ratings. This dataset-specific labeling approach can make the classification task easier than sentiment classification on independently labeled real-world data.
