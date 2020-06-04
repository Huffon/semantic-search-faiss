import torch
from transformers import ElectraModel, ElectraTokenizer


class Encoder:
    """KoELELCTRA Encoder class"""

    def __init__(self, model_size: str, dimension: int):
        self.model = ElectraModel.from_pretrained(
            f"monologg/koelectra-{model_size}-discriminator")
        self.tokenizer = ElectraTokenizer.from_pretrained(
            f"monologg/koelectra-{model_size}-discriminator")
        self.dimension = dimension

    def encode(self, sent: str):
        tokens = self.tokenizer.tokenize(f"[CLS] {sent} [SEP]")
        n_tokens = len(tokens)
        indices = torch.tensor(self.tokenizer.convert_tokens_to_ids(
            tokens)).unsqueeze(0)  # batchify
        attn_masks = torch.tensor(
            [1 for _ in range(n_tokens)]).unsqueeze(0)  # batchify
        last_states = self.model(indices, attn_masks)[0][:, 0, :]  # extract [CLS] token
        return last_states.detach().numpy()  # [1, 256]
