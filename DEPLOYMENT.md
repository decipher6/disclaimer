# Deployment Guide

## GitHub Setup

1. **Initialize Git (if not already done):**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   ```

2. **Create a new repository on GitHub:**
   - Go to https://github.com/new
   - Create a new repository (e.g., `compliance-ai-reviewer`)
   - Don't initialize with README (you already have one)

3. **Push to GitHub:**
   ```bash
   git remote add origin https://github.com/YOUR_USERNAME/compliance-ai-reviewer.git
   git branch -M main
   git push -u origin main
   ```

## Deployment Options (Recommended for CrewAI)

Long-running CrewAI reviews (2–5+ minutes) need a platform that supports them. Use one of the options below.

#### Railway.app (Recommended)
- Better for long-running Python apps
- Free tier available
- Easy deployment from GitHub

1. Go to https://railway.app
2. New Project → Deploy from GitHub
3. Select your repository
4. Add environment variables:
   - `GOOGLE_API_KEY`
   - `CONTEXTUAL_AI_API_KEY`
5. Railway auto-detects Python and deploys

#### Render.com
- Free tier with 750 hours/month
- Supports long-running processes
- Easy GitHub integration

1. Go to https://render.com
2. Sign up/login with GitHub
3. New → Web Service
4. Connect your GitHub repository
5. Settings:
   - **Name**: compliance-ai-reviewer
   - **Environment**: Python 3
   - **Python Version**: `3.13.12` ⚠️ **IMPORTANT: Must be 3.13, NOT 3.14** (crewai doesn't support 3.14)
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python app.py`
   - **Plan**: Free (or Starter for better performance)
6. Add environment variables:
   - `GOOGLE_API_KEY` = your Gemini API key
   - `GEMINI_API_KEY` = same as above (optional, for compatibility)
7. Click "Create Web Service"

**Note**: Render will auto-detect `render.yaml` if present, or use the settings above.

#### Fly.io
- Good free tier
- Supports Python apps
- Global deployment

1. Install flyctl: `curl -L https://fly.io/install.sh | sh`
2. `fly launch` (follow prompts)
3. Add secrets: `fly secrets set GOOGLE_API_KEY=your_key`

## Environment Variables

Make sure to set these in your deployment platform:

- `GOOGLE_API_KEY` - Your Google/Gemini API key
- `CONTEXTUAL_AI_API_KEY` - Your ContextualAI key (currently hardcoded in crew.py)

## Post-Deployment

1. Test the deployment URL
2. Upload a test PDF
3. Monitor logs for any issues
4. Share the URL with test users

## Troubleshooting

- **Timeout errors**: Use Railway or Render for long-running reviews
- **Import errors**: Check that all dependencies are in requirements.txt
- **API key errors**: Verify environment variables are set correctly
- **File upload issues**: Check uploads directory permissions
