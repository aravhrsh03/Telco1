class Logger:
    instance = None

    def __new__(self):
        if Logger.instance is None:
            Logger.instance = super().__new__(self)
            return Logger.instance
        else:
            return Logger.instance

log = Logger()
log1 = Logger()

print(log is log1)
print(id(log))
print(id(log1))