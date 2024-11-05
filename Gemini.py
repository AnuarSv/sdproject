import google.generativeai as genai
from config import GEMINI_API
from texts import purpose, dataAITU

class GeminiService:
    def __init__(self):
        genai.configure(api_key=GEMINI_API)
        self.generation_config = {"temperature": 0, "top_p": 0, "top_k": 1}

    async def get_response(self, question: str, history: str) -> str:
        model = genai.GenerativeModel(model_name="gemini-1.5-flash", generation_config=self.generation_config,
                                      system_instruction=purpose)
        try:
            #print(history)
            response = await model.generate_content_async([f'GIVE CLEAR SHORT ANSWER. Depennding on USER question answer this language!\n\nData about AITU: {dataAITU}, READ: History of previous user answer: {history}\n\nNOW answer User question: {question}'])
            return response.text
        except Exception as e:
            return 'ERROR: ' + str(e)

