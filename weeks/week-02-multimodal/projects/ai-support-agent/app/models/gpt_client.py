def call_gpt(client, messages, system_prompt, model="gpt-4.1-mini", timeout=30):
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            *[{"role": "user", "content": m} for m in messages]
        ],
        timeout=timeout,
    )
    return response.choices[0].message.content