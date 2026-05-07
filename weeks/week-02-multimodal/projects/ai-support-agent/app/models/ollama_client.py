from configs.config import ollama_model


def call_ollama(client, messages, system_prompt, model=ollama_model, timeout=60):
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            *[{"role": "user", "content": m} for m in messages],
        ],
        timeout=timeout,
    )
    return response.choices[0].message.content