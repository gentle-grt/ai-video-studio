import argparse
from pathlib import Path
from PIL import Image, ImageDraw
import subprocess

BASE = Path(__file__).resolve().parent
OUTPUTS = BASE / "outputs"
OUTPUTS.mkdir(exist_ok=True)


def placeholder_image(prompt: str, out_path: Path, width: int = 512, height: int = 512):
    img = Image.new("RGB", (width, height), color=(25, 72, 101))
    draw = ImageDraw.Draw(img)
    draw.text((20, 20), prompt[:120], fill=(255, 255, 255))
    img.save(out_path)


def make_mp4_from_png(png_path: Path, out_mp4: Path):
    subprocess.run([
        "ffmpeg", "-y",
        "-loop", "1",
        "-i", str(png_path),
        "-t", "1",
        "-vf", "scale=512:512",
        str(out_mp4)
    ], check=True)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", required=True)
    parser.add_argument("--prompt", default="")
    parser.add_argument("--init_image", default="")
    parser.add_argument("--frames", type=int, default=8)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()

    out_path = Path(args.out)

    if args.mode == "txt2img":
        placeholder_image(args.prompt or "Local AI image generation", out_path)

    elif args.mode == "img2img":
        src = Path(args.init_image)
        if src.exists():
            img = Image.open(src).convert("RGB").resize((512, 512))
            draw = ImageDraw.Draw(img)
            draw.text((20, 20), args.prompt or "Image-to-image edit", fill=(255, 255, 255))
            img.save(out_path)
        else:
            placeholder_image(args.prompt or "Image-to-image", out_path)

    elif args.mode == "txt2video":
        temp_png = OUTPUTS / "temp_txt2video.png"
        placeholder_image(args.prompt or "Text to video", temp_png)
        make_mp4_from_png(temp_png, out_path)

    elif args.mode == "img2video":
        temp_png = OUTPUTS / "temp_img2video.png"
        src = Path(args.init_image)
        if src.exists():
            img = Image.open(src).convert("RGB").resize((512, 512))
            draw = ImageDraw.Draw(img)
            draw.text((20, 20), "Image to video", fill=(255, 255, 255))
            img.save(temp_png)
        else:
            placeholder_image("Image-to-video", temp_png)
        make_mp4_from_png(temp_png, out_path)

    print(f"Saved: {out_path}")


if __name__ == "__main__":
    main()
