# Fix for Render Deployment Error

## Problem
Render is trying to run `uv sync` but `uv` is not installed on Render's servers.

## Solution

### Option 1: Use render.yaml (Recommended)
The `render.yaml` file in the repo should automatically configure Render to use `pip` instead of `uv`.

1. Make sure `render.yaml` is committed to your repo
2. When creating the service in Render, it should auto-detect the config
3. If it doesn't, manually set:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python app.py`

### Option 2: Manual Fix in Render Dashboard

1. Go to your Render dashboard
2. Click on your service
3. Go to **Settings** tab
4. Scroll to **Build & Deploy**
5. Change **Build Command** from `uv sync` to:
   ```
   pip install -r requirements.txt
   ```
6. Make sure **Start Command** is:
   ```
   python app.py
   ```
7. Set **Python Version** to `3.13` or `3.12`
8. Click **Save Changes**
9. Trigger a new deploy

### Option 3: Delete and Recreate Service

If the above doesn't work:

1. Delete the current service in Render
2. Create a new Web Service
3. Connect your GitHub repo
4. **IMPORTANT**: In the build settings, make sure:
   - Build Command: `pip install -r requirements.txt` (NOT `uv sync`)
   - Start Command: `python app.py`
   - Python Version: `3.13`
5. Add environment variables
6. Deploy

## Why This Happens

- Your project uses `uv` locally (which is fine)
- Render doesn't have `uv` installed by default
- The `requirements.txt` file provides pip-compatible dependencies
- Render should use `pip install -r requirements.txt` instead

## Verify

After fixing, the build logs should show:
```
==> Running build command 'pip install -r requirements.txt'...
==> Installing dependencies...
```

Instead of:
```
==> Running build command 'uv sync'...
==> uv: command not found
```
