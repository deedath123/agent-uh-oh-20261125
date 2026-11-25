import os

WORD = "hallucinating"


def validate_entry(word):
    if not isinstance(word, str):
        raise ValueError("entry must be a string")
    if not word or not word.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if len(word) < 1 or len(word) > 99:
        raise ValueError("entry must be 1-99 characters")
    if len(word.split()) != 1:
        raise ValueError("entry must be exactly one word")


def main():
    validate_entry(WORD)
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
