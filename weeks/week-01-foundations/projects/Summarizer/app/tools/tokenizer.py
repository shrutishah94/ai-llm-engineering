import tiktoken
from configs.settings import MAX_INPUT_TOKENS


def count_tokens(text, model="gpt-4o-mini"):
    encoding = tiktoken.encoding_for_model(model)
    tokens = encoding.encode(text)
    return len(tokens)

def truncate_text(text, max_tokens=MAX_INPUT_TOKENS, model="gpt-4o-mini"):
    encoding = tiktoken.encoding_for_model(model)
    tokens = encoding.encode(text)

    truncated = tokens[:max_tokens]
    return encoding.decode(truncated)

def prepare_input(text):
    if count_tokens(text) > MAX_INPUT_TOKENS:
        return truncate_text(text, MAX_INPUT_TOKENS)
    return text
