model_configs = {
    "Llama-3.2-Instruct": {
        "base_config": {
            "st_model_id": "c01zaut/Llama-3.2-3B-Instruct-rk3588-1.1.1",
            "max_context_len": 32768,
            "max_new_tokens": 4196,
            "top_k": 20,
            "top_p": 0.9,
            "temperature": 0.6,
            "repeat_penalty": 1.1,
            "frequency_penalty": 0.3,
            "system_prompt": "You are Llama 3.2, an artificial intelligence model trained by Meta. You are a helpful assistant."
            },
        "models": {
            "Llama-3.2-Instruct-3B": {"filename": "Llama-3.2-3B-Instruct-rk3588-w8a8-opt-1-hybrid-ratio-0.0.rkllm", "parameter_size": "3B"}
        }
    },
    "Phi-3.5-Mini-Instruct": {
        "base_config": {
            "st_model_id": "microsoft/Phi-3.5-mini-instruct",
            "max_context_len": 8192,
            "max_new_tokens": 2048,
            "top_k": 1,
            "top_p": 0.9,
            "temperature": 0.7,
            "repeat_penalty": 1.1,
            "frequency_penalty": 1.0,
            "system_prompt": "You are Phi 3.5 Mini, an artificial intelligence model trained by Microsoft. You are a helpful AI assistant."
        },
        "models": {
            "Phi-3.5B-Mini-Instruct": {"filename": "Phi-3.5-mini-instruct-rk3588-w8a8-opt-0-hybrid-ratio-0.0.rkllm", "parameter_size": "3.5B"}
        }
    },
    "Qwen-2.5-Coder-7B-Instruct": {
        "base_config": {
            "st_model_id": "Qwen/Qwen2.5-7B-Instruct",
            "max_context_len": 8192,
            "max_new_tokens": 4196,
            "top_k": 5,
            "top_p": 0.8,
            "temperature": 0.2,
            "repeat_penalty": 1.00,
            "frequency_penalty": 0.2,
            "system_prompt": "You are Qwen, created by Alibaba Cloud. You are a helpful assistant."
        },
        "models": {
            "Qwen2.5-Coder-7B-Instruct": {"filename": "Qwen2.5-Coder-7B-Instruct-rk3588-w8a8-opt-0-hybrid-ratio-0.0.rkllm", "parameter_size": "7B"}
        },
    },
    "Gemma-2-IT-Google": {
        "base_config": {
            "st_model_id": "c01zaut/gemma-2-9b-it-rk3588-1.1.2",
            "max_context_len": 8192,
            "max_new_tokens": 2048,
            "top_k": 15,
            "top_p": 0.95,
            "temperature": 0.7,
            "repeat_penalty": 1.05,
            "frequency_penalty": 0.5,
            "system_prompt": ""
        },
        "models": {
            "gemma-2-2b-it-opt": {"filename": "gemma-2-2b-it-rk3588-w8a8-opt-1-hybrid-ratio-0.0.rkllm", "parameter_size": "2B"},
            "gemma-2-9b-it-opt": {"filename": "gemma-2-9b-it-rk3588-w8a8-opt-1-hybrid-ratio-0.0.rkllm", "parameter_size": "9B"}
        }
    },
    "DeepSeek-R1-Distill-Qwen-1.5B": {
        "base_config": {
            "st_model_id": "deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B",
            "max_context_len": 8192,
            "max_new_tokens": 2048,
            "top_k": 15,
            "top_p": 0.8,
            "temperature": 0.7,
            "repeat_penalty": 1.00,
            "frequency_penalty": 0.5,
            "system_prompt": "You are DeepSeek. You are a helpful AI assistant."
        },
        "models": {
            "DeepSeek-R1-Distill-Qwen": {"filename": "DeepSeek-R1-Distill-Qwen-1.5B_W8A8_RK3588.rkllm", "parameter_size": "1.5B"},
        }
    },
    "DeepSeek-R1-Distill-Llama-8B": {
        "base_config": {
            "st_model_id": "deepseek-ai/DeepSeek-R1-Distill-Llama-8B",
            "max_context_len": 8192,
            "max_new_tokens": 2048,
            "top_k": 15,
            "top_p": 0.8,
            "temperature": 0.7,
            "repeat_penalty": 1.00,
            "frequency_penalty": 0.5,
            "system_prompt": "You are DeepSeek. You are a helpful AI assistant."
        },
        "models": {
            "DeepSeek-R1-Distill-Llama-8B": {"filename": "DeepSeek-R1-Distill-Llama-8B-rk3588-w8a8-opt-1-hybrid-ratio-0.0.rkllm", "parameter_size": "8B"},
        }
    },
    "Meta-Llama-2-Chat-13b-hf": {
        "base_config": {
            "st_model_id": "meta-llama/Llama-2-13b-chat-hf",
            "max_context_len": 32768,
            "max_new_tokens": 4196,
            "top_k": 15,
            "top_p": 0.8,
            "temperature": 0.7,
            "repeat_penalty": 1.00,
            "frequency_penalty": 0.5,
            "system_prompt": "You are DeepSeek. You are a helpful AI assistant."
        },
        "models": {
            "Meta-Llama-2-Chat-13b-hf": {"filename": "meta-llama2-chat-13b-hf-rk3588.rkllm", "parameter_size": "13B"},
        }
    },           
}
