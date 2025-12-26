def greet(name: str = "World") -> str:
    """Return a greeting for name (default: World)."""
    return f"Hello, {name}!"

__all__ = ["greet"]
