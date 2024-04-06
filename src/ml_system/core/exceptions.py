class MLSystemError(Exception):
    """Base exception for all system errors."""
    def __init__(self, message: str, code: int = 500):
        super().__init__(message)
        self.code = code

class ConfigurationError(MLSystemError):
    """Raised when configuration is missing or invalid."""
    pass

class DataValidationError(MLSystemError):
    """Raised when data schema validation fails."""
    pass

class ResourceNotFoundError(MLSystemError):
    """Raised when a requested model, feature, or artifact is missing."""
    pass

class ComponentNotReadyError(MLSystemError):
    """Raised when execute() is called on an uninitialized component."""
    pass

class ConnectionError(MLSystemError):
    """Raised when external service (DB, API) is unreachable."""
    pass
