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

## Vercel Deployment

### Important Notes:
⚠️ **Vercel has limitations for long-running processes:**
- Function timeout: 10 seconds (Hobby) / 60 seconds (Pro)
- CrewAI reviews can take 2-5+ minutes
- You may need Vercel Pro plan or consider alternatives

### Option 1: Vercel (with Pro plan for longer timeouts)

1. **Install Vercel CLI:**
   ```bash
   npm i -g vercel
   ```

2. **Login to Vercel:**
   ```bash
   vercel login
   ```

3. **Deploy:**
   ```bash
   vercel
   ```
   Follow the prompts to link your GitHub repo.

4. **Set Environment Variables:**
   - Go to Vercel Dashboard → Your Project → Settings → Environment Variables
   - Add: `GOOGLE_API_KEY` = your API key
   - Add: `CONTEXTUAL_AI_API_KEY` = your ContextualAI key (if needed)

5. **Upgrade to Pro (if needed):**
   - Vercel Pro allows 60-second timeouts
   - For longer processes, consider alternatives below

### Option 2: Alternative Deployments (Recommended for CrewAI)

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
2. New → Web Service
3. Connect GitHub repo
4. Settings:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `python app.py`
5. Add environment variables

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

- **Timeout errors**: Upgrade to Pro plan or use Railway/Render
- **Import errors**: Check that all dependencies are in requirements.txt
- **API key errors**: Verify environment variables are set correctly
- **File upload issues**: Check uploads directory permissions
