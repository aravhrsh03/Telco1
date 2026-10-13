class RateLimitException(Exception):
    def __init__(self, attempts):
        self.attempts = attempts
        super().__init__(f"Failed after {attempts} Attempts")

def retry(func):
    def wrapper(*args, **kwargs):
        attempts = 0

        while attempts < 5:
            try:
                attempts += 1

                result = func(*args, **kwargs)

                if result:
                    print("Connected")
                    return result

            except Exception:
                pass

        raise RateLimitException(attempts)

    return wrapper

class Server:
    def __init__(self, url):
        self.url = url
        self.standard_url = "https://server.com:65000"

    @retry
    def connect(self):
        if self.url == self.standard_url:
            return True

        raise Exception("Connection failed")

try:
    url = "https://server.com:65001"
    cursor = Server(url=url)

    cursor.connect()

except RateLimitException as e:
    print(e)