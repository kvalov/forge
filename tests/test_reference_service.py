from pathlib import Path

from forge.python.reference_service import ReferenceService


def test_reference_service(tmp_path: Path) -> None:

    source = tmp_path / "example.py"

    source.write_text(
        """
from pathlib import Path

path = Path(".")

print(path)
""",
        encoding="utf-8",
    )

    service = ReferenceService()

    references = service.references(
        (source,),
        "Path",
    )

    assert len(references) == 1