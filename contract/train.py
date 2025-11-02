#train
from transformers import AutoTokenizer, AutoModelForSequenceClassification, Trainer, TrainingArguments
from datasets import Dataset

# 1. Prepare your labeled dataset
texts = [
    "Landlord hereby agrees to rent ...",
    "Employee shall work for the company ...",
    "This agreement is between vendor and client ..."
]
labels = [0, 1, 2]  # 0=Rental, 1=Employment, 2=Vendor

dataset = Dataset.from_dict({"text": texts, "label": labels})

# 2. Load tokenizer + base model
tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")
model = AutoModelForSequenceClassification.from_pretrained("distilbert-base-uncased", num_labels=3)

# 3. Tokenize
def tokenize(batch):
    return tokenizer(batch["text"], padding=True, truncation=True)
dataset = dataset.map(tokenize, batched=True)

# 4. Training args
training_args = TrainingArguments(
    output_dir="./contract_classifier",
    learning_rate=2e-5,
    per_device_train_batch_size=4,
    num_train_epochs=3,
    logging_steps=10
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=dataset
)

# 5. Train
trainer.train()

# 6. Save model for later use
model.save_pretrained("./contract_classifier")
tokenizer.save_pretrained("./contract_classifier")