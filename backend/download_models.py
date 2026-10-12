from pathlib import Path

BASE = Path(__file__).resolve().parent
MODELS = BASE / "models"
MODELS.mkdir(exist_ok=True)

print("Local AI model helper")
print("This project is a local starter generator.")
print("No API key is required for the starter package.")
print("")
print(f"Model directory: {MODELS}")
print("Add local diffusion model folders here for real generation.")
print("Examples:")
print("  backend/models/stable-diffusion-v1-5")
print("  backend/models/sd-turbo")
print("")
print("If no model is found, the app still runs in placeholder mode so you can test the UI.")
