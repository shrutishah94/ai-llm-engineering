import gradio as gr
from app.models.gpt_client import call_gpt
from app.models.ollama_client import call_ollama
from configs.config import gpt_client, gpt_prompt, ollama_client, ollama_prompt


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
        self.ollama_messages.append(gpt_reply)

        ollama_reply = call_ollama(
            self.ollama_client,
            self.ollama_messages,
            self.ollama_system
        )
        self.gpt_messages.append(ollama_reply)

        return gpt_reply, ollama_reply

    def run_conversation(self, turns=5):
        conversation = []

        for _ in range(turns):
            gpt_reply, ollama_reply = self.run_turn()
            conversation.append(("GPT", gpt_reply))
            conversation.append(("Ollama", ollama_reply))

        return conversation

orchestrator = ConversationOrchestrator(
    gpt_client,
    ollama_client,
    gpt_prompt,
    ollama_prompt
)
    
# def gradio_wrapper(text, turns):
#     orchestrator.gpt_messages = [text or "Hi there"]
#     orchestrator.ollama_messages = [text or "Hi"]
#     conversation = orchestrator.run_conversation(turns=int(turns))
#     return "\n".join([f"{role}: {msg}" for role, msg in conversation])

# gr.Interface(
#     fn=gradio_wrapper,
#     inputs=[
#         gr.Textbox(label="Start message", value="Hi"),
#         gr.Slider(minimum=1, maximum=5, step=1, value=3, label="Turns"),
#     ],
#     outputs="textbox",
#     flagging_mode="never",
# ).launch()

def chat(message, history, turns):
   
    orchestrator.gpt_messages.append(message)
    orchestrator.ollama_messages.append(message)

    conversation = orchestrator.run_conversation(turns=int(turns))
    formatted_conversation = []

    gpt_reply, ollama_reply = orchestrator.run_turn()

    for role, reply in conversation:
        formatted_conversation.append(
            f"{role}:\n{reply}"
        )

    return "\n\n-------------------\n\n".join(
        formatted_conversation
    )


demo = gr.ChatInterface(
    fn=chat,
    additional_inputs=[
        gr.Slider(
            minimum=1,
            maximum=5,
            step=1,
            value=3,
            label="Turns",
        )
    ],
    title="GPT vs Ollama Conversation",
    chatbot=gr.Chatbot(height=500),
).launch()