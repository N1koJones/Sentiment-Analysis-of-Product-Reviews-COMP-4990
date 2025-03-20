from transformers import BertForSequenceClassification

# Function to merge models
def merge_models(model_paths, output_path):
    models = [BertForSequenceClassification.from_pretrained(path) for path in model_paths]
    merged_model = models[0]
    for key in merged_model.state_dict().keys():
        merged_model.state_dict()[key] = sum([model.state_dict()[key] for model in models]) / len(models)
    merged_model.save_pretrained(output_path)

# Example usage of merging models
if __name__ == "__main__":
    model_paths = ['./model1', './model2', './model3', './model4']
    merge_models(model_paths, './merged_model')