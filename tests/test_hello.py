import subprocess
import sys
from hello import greet


class TestHello:
    def test_greet_default(self):
        assert greet() == "Hello, World!"

    def test_greet_name(self):
        assert greet("Alice") == "Hello, Alice!"

    def test_cli_no_args(self):
        result = subprocess.run(
            [sys.executable, "-c", "from hello import greet; print(greet())"],
            capture_output=True,
            text=True,
            check=True,
        )
        assert result.stdout.strip() == "Hello, World!"

    def test_cli_with_arg(self):
        result = subprocess.run(
            [sys.executable, "-c", "from hello import greet; print(greet('Bob'))"],
            capture_output=True,
            text=True,
            check=True,
        )
        assert result.stdout.strip() == "Hello, Bob!"
