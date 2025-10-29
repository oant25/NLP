from openai import OpenAI
import time

class Translator:
    def __init__(self, input_text: str, CHUNK_SIZE: int):
        self.input_text = input_text
        self.CHUNK_SIZE = CHUNK_SIZE
        self.chunks = []
        self.translatedChunks = []
        self.output = ""
        
        self._split_into_chunks()
                
    def _split_into_chunks(self):
        text_length = len(self.input_text)
        count_of_chunks = (text_length + self.CHUNK_SIZE - 1) // self.CHUNK_SIZE
        
        for i in range(count_of_chunks):
            start_index = i * self.CHUNK_SIZE
            end_index = min((i + 1) * self.CHUNK_SIZE, text_length)
            chunk = self.input_text[start_index:end_index]
            self.chunks.append(chunk)

    def get_chunks(self):
        return self.chunks

    def request_to_LLM(self, prompt: str) -> str:
        client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key="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",
        )

        completion = client.chat.completions.create(
            extra_headers={
                "HTTP-Referer": "http://localhost:3000",
                "X-Title": "Translation App",
            },
            extra_body={},
            model="google/gemma-2-9b-it:free",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            max_tokens=1000
        )
        
        response = completion.choices[0].message.content
        print(f"\nОтвет от LLM: {response[:200]}...\n")
        return response

    def translate_to(self, LANGUAGE: str) -> str:
        for i, chunk in enumerate(self.chunks):
            print(f"Перевод чанка {i+1}/{len(self.chunks)}...")
            
            TranslatePrompt = f"""STRICT TRANSLATION TO {LANGUAGE} FROM RUSSIAN ONLY. NO COMMENTS.

RUSSIAN: {chunk}

{LANGUAGE}:
"""
            
            translated_chunk = self.request_to_LLM(TranslatePrompt)
            self.translatedChunks.append(translated_chunk)
            
            time.sleep(2)
        print("Сборка переведенного текста...")
        
        self.output = " ".join(self.translatedChunks)
        
        return self.output