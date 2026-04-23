from app.models.gpt_client import call_gpt
from app.models.ollama_client import call_ollama


class ConversationOrchestrator:
    def __init__(self, gpt_client, ollama_client, gpt_prompt, ollama_prompt):
        self.gpt_client = gpt_client
        self.ollama_client = ollama_client

        self.gpt_system = gpt_prompt
        self.ollama_system = ollama_prompt

        self.gpt_messages = ["Hi there"]
        self.ollama_messages = ["Hi"]

    def run_turn(self):
        gpt_reply = call_gpt(
            self.gpt_client,
            self.gpt_messages,
            self.gpt_system
        )
        self.gpt_messages.append(gpt_reply)

        ollama_reply = call_ollama(
            self.ollama_client,
            self.gpt_messages,
            self.ollama_system
        )
        self.ollama_messages.append(ollama_reply)

        return gpt_reply, ollama_reply

    def run_conversation(self, turns=5):
        conversation = []

        for _ in range(turns):
            gpt_reply, ollama_reply = self.run_turn()
            conversation.append(("GPT", gpt_reply))
            conversation.append(("Ollama", ollama_reply))

        return conversation