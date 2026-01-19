def load_text(file_path: str) -> str:
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()

    # Basic cleanup
    text = text.replace("\n", " ").strip()
    return text
