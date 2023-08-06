import util

class feature_extractor:
    extractors = {}

    def add_extractor(self, f):
        self.function = f
        self.entrypoint = f"{f.__module__}.{f.__name__}"
        self.extractors[self.name] = self

    def __init__(self, name=None):
        self.name = None
        self.function = None
        self.entrypoint = None
        if not name:
            util.invalid_extractor(
                code="invalid_extractor", error="feature extractors must contain a name parameter"
            )
        else:
            self.name = name

    def __call__(self, f, *args, **kwargs):
        if self.function:
            return self.function(f, *args, **kwargs)
        else:
            if not f:
                util.invalid_extractor(
                    code="invalid_extractor",
                    error="@feature_extractor must be called with a function"
                )
            else:
                self.add_extractor(f)
                return f

    @classmethod
    def all(cls):
        return cls.extractors