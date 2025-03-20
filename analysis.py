import torch
from transformers import BertTokenizer, BertForSequenceClassification, Trainer, TrainingArguments
from datasets import load_dataset, Dataset

# Check if GPU is available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Load the dataset from CSV
dataset = Dataset.from_csv('top50.csv')

# Select a portion of the dataset (e.g., lines 1-5000)
# Change the range here to select different lines
selected_dataset = dataset.select(range(5000))

# Initialize the tokenizer and model
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertForSequenceClassification.from_pretrained('bert-base-uncased', num_labels=5)  # Assuming 5 possible scores
model.to(device)  # Move the model to the GPU

# Tokenize the dataset
def tokenize_function(examples):
    return tokenizer(examples['Text'], padding='max_length', truncation=True)

tokenized_datasets = selected_dataset.map(tokenize_function, batched=True)

# Rename the 'Score' column to 'labels' as expected by the Trainer
tokenized_datasets = tokenized_datasets.rename_column('Score', 'labels')

# Function to check and correct labels
def correct_labels(dataset, num_labels=5):
    def correct_label(example):
        if example['labels'] >= num_labels:
            example['labels'] = num_labels - 1
        return example
    return dataset.map(correct_label)

# Correct the labels in the tokenized datasets
tokenized_datasets = correct_labels(tokenized_datasets, num_labels=5)

# Split the dataset into train and test sets
train_test_split = tokenized_datasets.train_test_split(test_size=0.2)
train_dataset = train_test_split['train']
test_dataset = train_test_split['test']

# Define the training arguments
training_args = TrainingArguments(
    output_dir='./results',
    eval_strategy='epoch',  # Updated to use eval_strategy
    learning_rate=2e-5,
    per_device_train_batch_size=16,
    per_device_eval_batch_size=16,
    num_train_epochs=3,
    weight_decay=0.01,
)

# Initialize the Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=test_dataset,
)

# Train the model
trainer.train()

# Save the model
model.save_pretrained('./bert-summarization-model')
tokenizer.save_pretrained('./bert-summarization-model')

# Function to generate summary
def generate_summary(reviews, max_length=555):
    inputs = tokenizer(reviews, return_tensors='pt', padding=True, truncation=True).to(device)  # Move inputs to GPU
    outputs = model(**inputs)
    summary = tokenizer.decode(outputs.logits.argmax(dim=-1), skip_special_tokens=True)
    return summary[:max_length]

# Example usage
reviews = ["This product is great!", "I had a terrible experience with this product."]
summary = generate_summary(reviews)
print("Summary:", summary)