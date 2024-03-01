from abc import ABC, abstractmethod

class Logger(ABC):
    @abstractmethod
    def log(self, message):
        raise NotImplementedError("Implement function!")
    
class LoguruLogger(Logger):
    def log(self, message):
        print(f"Logged for Loguru: {message}")

class Google_authLogger(Logger):
    def log(self, message):
        print(f"Logged for Google_auth: {message}")

class LoggerProcessor:
    def __init__(self, log_method: Logger):
        self.log_method = log_method

    def log_message(self, message):
        self.log_method.log(message)

def main():
    GoogleLog = LoggerProcessor(Google_authLogger())
    LoguruLog = LoggerProcessor(LoguruLogger())

    GoogleLog.log_message("Google Log")
    LoguruLog.log_message("Loguru Log")

if __name__ == "__main__":
    main()