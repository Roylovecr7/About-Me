import re
from pathlib import Path


README = Path(__file__).resolve().parents[1] / "README.md"


def test_readme_has_required_sections() -> None:
    text = README.read_text(encoding="utf-8")
    for heading in [
        "## 🔬 Research Focus",
        "## 🧰 Skills & Tools",
        "## 📌 Featured Projects",
        "## 📫 Contact",
    ]:
        assert heading in text


def test_contact_block_has_valid_email_and_homepage_link() -> None:
    text = README.read_text(encoding="utf-8")

    email_match = re.search(r"- Email: ([^\s]+)", text)
    assert email_match, "Missing email line in contact section"
    assert re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", email_match.group(1))

    homepage_match = re.search(r"- Homepage: \[(https?://[^\]]+)\]\((https?://[^)]+)\)", text)
    assert homepage_match, "Homepage must use explicit markdown link format"
    assert homepage_match.group(1) == homepage_match.group(2)


def test_featured_project_wording_is_consistent() -> None:
    text = README.read_text(encoding="utf-8")
    assert "Speech-rate optimization" not in text
    assert "Speech rate optimization" in text
