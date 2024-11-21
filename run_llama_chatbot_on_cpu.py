# -*- coding: utf-8 -*-
"""Run Llama ChatBot on CPU.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1VWOIo47ZxagzttR08o1JNbJmYi3kcniK
"""

!pip install transformers accelerate bitsandbytes

!pip install -U bitsandbytes

from transformers import AutoModelForCausalLM, AutoTokenizer
model_name = "meta-llama/Llama-2-7b-chat-hf"
prompt = "Tell me about Artificial general Intelligence"
access_token = "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"



model = AutoModelForCausalLM.from_pretrained(model_name, device_map="auto", use_auth_token=access_token)
tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast=True, use_auth_token=access_token)
model_inputs = tokenizer(prompt, return_tensors="pt").to("cuda:0")

output = model.generate(**model_inputs)

print(tokenizer.decode(output[0], skip_special_tokens=True))