import google.generativeai as genai
from config import GEMINI_API
from texts import bot_instr

async def gpt(promt: str, history: str, context: str, purpose: str=bot_instr) -> str:
    try:
        genai.configure(api_key=GEMINI_API)

        # Set up the model
        generation_config = {
            "temperature": 0,
            "top_p": 0,
            "top_k": 1,
        }

        model = genai.GenerativeModel(model_name="gemini-1.5-flash",
                                      generation_config=generation_config,
                                      system_instruction=purpose,)

        response = await model.generate_content_async([f'Data: {context}, User History: {history}\n\nQuestion: {promt}'])
        return response.text

    except Exception as e:
        return 'ERROR' + '\n' + str(e)
