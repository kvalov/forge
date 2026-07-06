from pathlib import Path

from forge.python.parser import PythonParser


def test_parser(tmp_path: Path):

    file = tmp_path / "example.py"

    file.write_text(
        """
import pathlib

class Demo:
    pass

def hello():
    pass
""",
        encoding="utf-8",
    )

    module = PythonParser().parse(file)

    assert len(module.classes) == 1
    assert len(module.functions) == 1
    assert len(module.imports) == 1

    assert module.classes[0].name == "Demo"
    assert module.functions[0].name == "hello"