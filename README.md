# Local AI Studio

This project is built for a local Windows + XAMPP setup using Apache on port 8080.

It includes:
- Text → Image
- Image → Image
- Text → Video
- Image → Video
- No API key required
- Full local processing on your computer
- Open-source model support

Important notes:
- This is a local demo/starter generator. It does not ship huge model weights in the repository because those files are too large for normal GitHub storage and ZIP delivery.
- The project uses a lightweight local fallback when models are missing, so it still runs.
- To get real AI generation output, add a local open-source model into `backend/models` and restart the backend.
- For Windows 10/11, XAMPP is expected to serve the PHP UI on `http://localhost:8080/ai-video-studio/`.
- On 8 GB RAM, keep generation short (small resolutions and short clips). 16–19 second video will require more GPU power and memory.

Folder layout
- `php/index.php` – web UI served by XAMPP
- `backend/server.py` – FastAPI backend exposing local generation endpoints
- `backend/generate.py` – local generation runner
- `backend/download_models.py` – instructions and model-check helper
- `backend/requirements.txt` – Python dependencies
- `setup-windows.bat` – Windows setup runner
- `package_zip.bat` – zips the project for export

Installation
1. Place the project in your XAMPP web folder, for example:
   `C:\xampp\htdocs\ai-video-studio`
2. Open a terminal in the project folder.
3. Run `setup-windows.bat`.
4. Start Apache in XAMPP.
5. Open:
   `http://localhost:8080/ai-video-studio/`

The backend runs locally on port 5000.

How to add a real model
1. Create a folder like:
   `backend/models/stable-diffusion-v1-5`
2. Put a valid local diffusers or checkpoint model there.
3. Restart the backend.

If no model is present, the project still runs in placeholder mode so you can test the UI.

Production note
This project is intentionally designed to be easy to run and easy to modify. It is not a full commercial-grade video generator on 8 GB RAM. For high-quality 16–19 second videos, use a stronger GPU and more storage.

License
MIT
