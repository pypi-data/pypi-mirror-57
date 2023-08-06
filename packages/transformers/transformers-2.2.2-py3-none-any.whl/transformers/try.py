from transformers import squad_convert_examples_to_features, SquadV2Processor
from transformers import BertTokenizer

tokenizer = BertTokenizer.from_pretrained("bert-base-cased")
processor = SquadV2Processor()
examples = processor.get_dev_examples("../examples/tests_samples/SQUAD")

yes = squad_convert_examples_to_features(
    examples,
    tokenizer,
    384,
    50,
    128,
    False,
    return_dataset="tf"
)

print("nice")