# CoolocOCR
OCR Service for Cooloc application.

Used to analyze receipts and extract information such as the articles, total amount and date using OpenAI API.

This is using IA, do not trust the results blindly. Always second check the results.

## Developer guide
### Project requirements

- Python 3.12 [Check UV's doc first to install Python](https://docs.astral.sh/uv/guides/install-python/)
- [UV](https://docs.astral.sh/uv/)
- OpenAI API key

### Installation

```bash
git clone https://github.com/ComePicard/CoolocOCR.git
cd CoolocOCR
uv pip install -e .
```

Make a copy of the `.env.example` file and rename it to `.env`. Then fill in the OpenAI API key in the `.env` file.

```bash
cp .env.example .env
```