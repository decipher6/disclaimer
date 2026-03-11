# ComplianceAI

Simple web interface to run CrewAI compliance reviews on marketing materials.

## Local Setup

```bash
pip install uv
uv sync
```

Create `.env` file in the project root:
```env
GOOGLE_API_KEY=your-google-api-key-here
# or
GEMINI_API_KEY=your-google-api-key-here
```

## Run Locally

```bash
python app.py
```

Open http://localhost:8000

## Usage

1. Upload PDF
2. Select jurisdictions (UAE, KSA, Kuwait, DIFC, Qatar, Oman)
3. Click "Submit for Review"
4. View results with real-time agent updates

## Deployment

See [DEPLOYMENT.md](./DEPLOYMENT.md) for detailed deployment instructions to:
- GitHub
- Vercel (with limitations)
- Railway.app (recommended)
- Render.com
- Fly.io
