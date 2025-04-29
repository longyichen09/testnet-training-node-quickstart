phi3_template = {
    "system_format": "<|system|>\n{content}<|end|>\n",
    "user_format": "<|user|>\n{content}<|end|>\n<|assistant|>\n",
    "assistant_format": "{content}<|end|>\n",
    "tool_format": "{content}",
    "function_format": "{content}",
    "observation_format": "<|tool|>\n{content}<|end|>\n<|assistant|>\n",
    "system": "You are a helpful AI assistant.",
}

model2template = {
    "microsoft/phi-3-mini-4k-instruct": phi3_template,
}

model2size = {
    "microsoft/phi-3-mini-4k-instruct": 3_800_000_000,  # 3.8B 参数
}

model2base_model = {
    "microsoft/phi-3-mini-4k-instruct": "phi-3",
}
