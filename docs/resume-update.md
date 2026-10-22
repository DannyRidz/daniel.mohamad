# Resume update

Updated 22 October 2026 at the owner's request, with page three excluded from edits.

## Content changes

* Replaced the job application specific heading and footer with the portfolio's full stack and AI application positioning.
* Added Cartograph, the public RidzTalk technical showcase and Crop Health Assistant as the main project evidence.
* Distinguished RidzTalk's published Android app from its iOS native project. The production source remains private.
* Updated The Odin Project to completed, using the owner's explicit statement in the portfolio brief.
* Kept the existing portrait, contact details, employment dates, other qualifications, languages and existing employment figures. Updated the Industrial Engineering & Management degree to completed December 2025, as explicitly confirmed by the owner. No new numerical outcomes were added.
* Kept Blog API and Messaging App as concise additional backend work.
* Added clickable portfolio and project links. Resume links on the site use a query version to avoid reusing an older cached PDF.

## Page three preservation

The original recommendation letter was copied directly from the previous PDF. It was not regenerated, OCR processed, cropped or compressed. Checks confirmed identical decoded page content, page dimensions and rendered pixels at 1.5x scale.

## Validation

* Exactly three pages.
* Visually reviewed the final first and second page renders for spacing, line wrapping, alignment, portrait quality and legibility.
* No extracted text blocks outside the first two page boundaries.
* Eleven clickable PDF links.
* Confirmed the primary projects, curriculum completion, and the existing 15% and 98% employment figures remain in the extracted text.
* Original PDF retained locally in ignored `output/pdf/original-resume.pdf`.
* Final deliverable in `assets/documents/daniel-mohamad-cv.pdf`, with a review copy and page renders in ignored `output/pdf/`.

Poppler was unavailable, so rendering and pixel comparisons used PyMuPDF. Generation used ReportLab and page preservation used pypdf, installed in a temporary virtual environment. No dependencies were added to the website runtime. The PDF is searchable; no claim of PDF/UA conformance or ATS certification is made.

The revised file is about 343KB, down from about 3.1MB. Only the portrait on the newly authored first page was resized; the recommendation letter's rendered content remains identical.

## Future edits

`scripts/build_resume.py` contains the first two pages' content and layout. It requires ReportLab, pypdf and Pillow. The default font paths use macOS Arial; `--font-dir` can point to another folder containing `Arial.ttf` and `Arial Bold.ttf`.

```sh
python scripts/build_resume.py --reference assets/documents/daniel-mohamad-cv.pdf
```

The output goes to `output/pdf/daniel-mohamad-cv.pdf`. Review its renders and verify page three before replacing the public asset. The owner authorized publication after confirming the degree completion date. The portfolio link was subsequently updated to `https://dannyridz.github.io/daniel.mohamad/` at the owner's request.
