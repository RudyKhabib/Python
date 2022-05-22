class MyDict(dict):
    def get(self, key):
        if super().get(key) is None:
            return 0
        else:
            return super().get(key)

