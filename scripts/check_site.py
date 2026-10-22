"""Check static portfolio links and metadata without third party packages."""

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
PUBLIC = "https://dannyridz.github.io/daniel.mohamad/"


class PortfolioParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = []
        self.links = []
        self.images = []
        self.metadata = {}
        self.canonical = None
        self.h1_count = 0

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            self.ids.append(attrs["id"])
        if tag in ("a", "link"):
            self.links.append(attrs.get("href", ""))
        if tag == "img":
            self.images.append(attrs)
        if tag == "meta":
            self.metadata[attrs.get("name", attrs.get("property"))] = attrs.get("content", "")
        if tag == "link" and attrs.get("rel") == "canonical":
            self.canonical = attrs.get("href")
        if tag == "h1":
            self.h1_count += 1


def main():
    page = PortfolioParser()
    page.feed((ROOT / "index.html").read_text())
    errors = []
    if len(page.ids) != len(set(page.ids)):
        errors.append("Duplicate HTML IDs")
    if page.h1_count != 1:
        errors.append("Expected exactly one h1")
    if page.canonical != PUBLIC:
        errors.append("Canonical URL changed")

    for link in page.links:
        url = urlsplit(link)
        if not link:
            errors.append("Empty link")
        elif link.startswith("#"):
            if unquote(url.fragment) not in page.ids:
                errors.append(f"Missing anchor: {link}")
        elif not url.scheme and not url.netloc:
            if url.path.startswith("/"):
                errors.append(f"Asset breaks GitHub Pages subpath: {link}")
            elif not (ROOT / unquote(url.path)).is_file():
                errors.append(f"Missing local link target: {link}")
        elif url.scheme not in ("https", "mailto"):
            errors.append(f"Unexpected link scheme: {link}")

    for image in page.images:
        if not (ROOT / image.get("src", "")).is_file():
            errors.append(f"Missing image: {image.get('src')}")
        if not image.get("alt"):
            errors.append("Project image is missing descriptive alternative text")
        if not all(image.get(key, "").isdigit() for key in ("width", "height")):
            errors.append("Image is missing numeric dimensions")

    for key in ("description", "viewport", "og:title", "og:description", "og:image", "og:url", "twitter:card", "twitter:image"):
        if not page.metadata.get(key):
            errors.append(f"Missing metadata: {key}")
    for key in ("og:image", "twitter:image"):
        value = page.metadata.get(key, "")
        if not value.startswith(PUBLIC) or not (ROOT / value.removeprefix(PUBLIC)).is_file():
            errors.append(f"Social image is not available at the expected path: {key}")

    if errors:
        raise SystemExit("\n".join(errors))
    print(f"PASS: {len(page.links)} links, {len(page.ids)} unique anchors, {len(page.images)} project images, metadata and Pages asset paths")


if __name__ == "__main__":
    main()
