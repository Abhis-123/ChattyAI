from transformers.utils import logging
logging.set_verbosity_error()


from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

class ChatBot:
    def __init__(self,name ="cookie", model_name = "microsoft/DialoGPT-small"):
        self.name = name
        self.prev_chat = []
        self.model_name = model_name
        self.tokenizer = AutoTokenizer.from_pretrained(model_name, padding_side='left')
        self.model = AutoModelForCausalLM.from_pretrained(model_name)
    def process(self, message=""):
        input_ids = self.tokenizer.encode(message + " " + self.tokenizer.eos_token,
                                          return_tensors="pt")
        bot_input_ids = torch.cat([self.prev_chat, input_ids], dim=-1) if self.prev_chat.__len__() > 0 else input_ids
            # generate a bot response
        self.prev_chat = self.model.generate(
            bot_input_ids,
            max_length=1000,
            do_sample=True,
            top_k=100,
            temperature=0.75,
            pad_token_id=self.tokenizer.eos_token_id

        )
        output = self.tokenizer.decode(self.prev_chat[:, bot_input_ids.shape[-1]:][0], 
                                       skip_special_tokens=True)

        return output


if __name__ == '__main__':
    chatbot = ChatBot(model_name = "microsoft/DialoGPT-large")
    current_text = ""
    while True:
        current_text = input(">>You: ")
        if current_text == "exit" or current_text=="bye":
            print(">>Bot: I love You")
            break
        out_text = chatbot.process(current_text)
        print(">>Bot: "+ out_text)

