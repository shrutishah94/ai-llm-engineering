from app.orchestration.conversation_prompt import ConversationOrchestrator
from configs.config import gpt_client, gpt_prompt, ollama_client, ollama_prompt

if __name__ == "__main__":
    orchestrator = ConversationOrchestrator(
        gpt_client=gpt_client,
        ollama_client=ollama_client,
        gpt_prompt=gpt_prompt,
        ollama_prompt=ollama_prompt,
    )

    chat = orchestrator.run_conversation(turns=5)
    for speaker, text in chat:
        print(f"{speaker}: {text}\n")