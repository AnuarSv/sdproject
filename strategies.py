class ResponseStrategy:
    def get_response(self, message_text: str) -> str:
        raise NotImplementedError

class StandardResponseStrategy(ResponseStrategy):
    def get_response(self, message_text: str) -> str:
        return f"Ответ на ваш запрос: {message_text}"

class ResponseStrategyContext:
    def __init__(self, strategy: ResponseStrategy):
        self.strategy = strategy

    def get_response(self, message_text: str) -> str:
        return self.strategy.get_response(message_text)
