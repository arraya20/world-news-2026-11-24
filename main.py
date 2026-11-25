"""Write the original 24 November 2026 news image for make.fun."""

from pathlib import Path
import os


def main() -> None:
    image = Path(__file__).with_name("entry.png").read_bytes()
    if not image.startswith(b"\x89PNG\r\n\x1a\n") or len(image) > 1_048_576:
        raise ValueError("The news image must be a PNG smaller than 1 MiB")
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.png").write_bytes(image)


if __name__ == "__main__":
    main()
