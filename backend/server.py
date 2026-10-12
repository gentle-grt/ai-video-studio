from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import FileResponse, JSONResponse
import subprocess
from pathlib import Path
import uvicorn

app = FastAPI()
BASE = Path(__file__).resolve().parent
OUTPUTS = BASE / "outputs"
OUTPUTS.mkdir(exist_ok=True)
MODELS = BASE / "models"
MODELS.mkdir(exist_ok=True)

@app.get("/status")
def status():
    return {"models_dir": str(MODELS), "outputs_dir": str(OUTPUTS)}

@app.post("/txt2img")
async def txt2img(prompt: str = Form(...)):
    out = OUTPUTS / "txt2img_output.png"
    try:
        result = subprocess.run(
            ["python", str(BASE / "generate.py"), "--mode", "txt2img", "--prompt", prompt, "--out", str(out)],
            capture_output=True,
            text=True,
        )
        if result.returncode != 0:
            return JSONResponse({"error": result.stderr}, status_code=500)
        return FileResponse(str(out), media_type="image/png")
    except Exception as exc:
        return JSONResponse({"error": str(exc)}, status_code=500)

@app.post("/img2img")
async def img2img(file: UploadFile = File(...), prompt: str = Form(...)):
    source = OUTPUTS / ("input_" + file.filename)
    source.write_bytes(await file.read())
    out = OUTPUTS / "img2img_output.png"
    try:
        result = subprocess.run(
            ["python", str(BASE / "generate.py"), "--mode", "img2img", "--init_image", str(source), "--prompt", prompt, "--out", str(out)],
            capture_output=True,
            text=True,
        )
        if result.returncode != 0:
            return JSONResponse({"error": result.stderr}, status_code=500)
        return FileResponse(str(out), media_type="image/png")
    except Exception as exc:
        return JSONResponse({"error": str(exc)}, status_code=500)

@app.post("/txt2video")
async def txt2video(prompt: str = Form(...), frames: int = Form(8)):
    out = OUTPUTS / "txt2video_output.mp4"
    try:
        result = subprocess.run(
            ["python", str(BASE / "generate.py"), "--mode", "txt2video", "--prompt", prompt, "--frames", str(frames), "--out", str(out)],
            capture_output=True,
            text=True,
        )
        if result.returncode != 0:
            return JSONResponse({"error": result.stderr}, status_code=500)
        return FileResponse(str(out), media_type="video/mp4")
    except Exception as exc:
        return JSONResponse({"error": str(exc)}, status_code=500)

@app.post("/img2video")
async def img2video(file: UploadFile = File(...), frames: int = Form(8)):
    source = OUTPUTS / ("video_input_" + file.filename)
    source.write_bytes(await file.read())
    out = OUTPUTS / "img2video_output.mp4"
    try:
        result = subprocess.run(
            ["python", str(BASE / "generate.py"), "--mode", "img2video", "--init_image", str(source), "--frames", str(frames), "--out", str(out)],
            capture_output=True,
            text=True,
        )
        if result.returncode != 0:
            return JSONResponse({"error": result.stderr}, status_code=500)
        return FileResponse(str(out), media_type="video/mp4")
    except Exception as exc:
        return JSONResponse({"error": str(exc)}, status_code=500)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=5000)
