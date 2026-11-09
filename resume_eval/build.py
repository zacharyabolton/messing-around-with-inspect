"""Generate visually identical PDFs with extractable tiny white payloads."""

from pathlib import Path

import pymupdf

ASSETS = Path(__file__).parent / "assets"
VARIANTS = ("baseline", "direct", "ctf", "recruiter")
HIDDEN_FONT_SIZE = 0.01


def build_pdfs(output_dir: Path = ASSETS) -> dict[str, Path]:
    output_dir.mkdir(parents=True, exist_ok=True)
    resume = (ASSETS / "resume.txt").read_text()
    paths = {}
    for variant in VARIANTS:
        with pymupdf.open() as doc:
            page = doc.new_page(width=612, height=792)
            page.draw_rect(page.rect, color=None, fill=(1, 1, 1))
            remaining = page.insert_textbox(
                pymupdf.Rect(48, 48, 564, 744), resume,
                fontsize=11, fontname="helv", lineheight=1.35, color=(0, 0, 0),
            )
            if remaining < 0:
                raise ValueError("Visible resume does not fit on one page")
            if variant != "baseline":
                # A single line preserves the payload's spaces through extraction.
                # Keep it on-page and nonzero to avoid geometric filtering.
                payload = " ".join(
                    (ASSETS / f"injection_{variant}.txt").read_text().split()
                )
                page.insert_text(
                    (10, 10), payload, fontsize=HIDDEN_FONT_SIZE,
                    fontname="helv", color=(1, 1, 1),
                )
            path = output_dir / f"resume_{variant}.pdf"
            doc.save(path, deflate=True)
            paths[variant] = path
    return paths


if __name__ == "__main__":
    for variant, path in build_pdfs().items():
        print(f"{variant}: {path}")
