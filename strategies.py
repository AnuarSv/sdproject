class ResponseStrategy:
    async def generate_response(self, message: Message, history: str):
        pass

class HistoryResponseStrategy(ResponseStrategy):
    async def generate_response(self, message: Message, history: str):
        return history if history else "No history available."

class GPTResponseStrategy(ResponseStrategy):
    async def generate_response(self, message: Message, history: str):
        response = await gpt(message.text, history)
        return response