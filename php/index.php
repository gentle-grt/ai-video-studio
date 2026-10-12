<?php
$api_base = "http://127.0.0.1:5000";
?>
<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <title>Local AI Studio</title>
  <style>
    body { font-family: Arial, sans-serif; max-width: 980px; margin: 24px auto; padding: 0 16px; }
    h2 { margin-top: 30px; }
    label { display:block; margin:12px 0 6px 0; font-weight: bold; }
    input, textarea { width: 100%; box-sizing: border-box; padding: 8px; }
    button { padding: 10px 16px; cursor: pointer; margin-top: 10px; }
    .box { border: 1px solid #ddd; padding: 16px; border-radius: 8px; margin-top: 16px; }
    img, video { max-width: 100%; border: 1px solid #ddd; margin-top: 12px; }
    .small { color: #666; font-size: 12px; }
  </style>
</head>
<body>
  <h1>Local AI Studio</h1>
  <p class="small">Runs locally on your computer with no API key. XAMPP serves this file at localhost:8080.</p>

  <div class="box">
    <h2>Text → Image</h2>
    <form id="txt2imgForm">
      <label>Prompt</label>
      <textarea id="txt2imgPrompt" rows="4">A cinematic valley at sunset, highly detailed</textarea>
      <button type="submit">Generate Image</button>
    </form>
    <div id="txt2imgResult"></div>
  </div>

  <div class="box">
    <h2>Image → Image</h2>
    <form id="img2imgForm" enctype="multipart/form-data">
      <label>Upload image</label>
      <input type="file" id="img2imgFile" accept="image/*">
      <label>Prompt</label>
      <input type="text" id="img2imgPrompt" value="Convert this into a stylized fantasy scene">
      <button type="submit">Generate Image</button>
    </form>
    <div id="img2imgResult"></div>
  </div>

  <div class="box">
    <h2>Text → Video</h2>
    <form id="txt2videoForm">
      <label>Prompt</label>
      <input type="text" id="txt2videoPrompt" value="A futuristic city skyline flying through the night">
      <label>Frames</label>
      <input type="number" id="txt2videoFrames" value="8" min="4" max="20">
      <button type="submit">Generate Video</button>
    </form>
    <div id="txt2videoResult"></div>
  </div>

  <div class="box">
    <h2>Image → Video</h2>
    <form id="img2videoForm" enctype="multipart/form-data">
      <label>Upload image</label>
      <input type="file" id="img2videoFile" accept="image/*">
      <label>Frames</label>
      <input type="number" id="img2videoFrames" value="8" min="4" max="20">
      <button type="submit">Generate Video</button>
    </form>
    <div id="img2videoResult"></div>
  </div>

  <script>
    async function sendForm(url, formData) {
      const response = await fetch(url, { method: 'POST', body: formData });
      if (!response.ok) {
        const text = await response.text();
        throw new Error(text);
      }
      return await response.blob();
    }

    document.getElementById('txt2imgForm').addEventListener('submit', async function (event) {
      event.preventDefault();
      const form = new FormData();
      form.append('prompt', document.getElementById('txt2imgPrompt').value);
      document.getElementById('txt2imgResult').innerHTML = 'Generating...';
      try {
        const blob = await sendForm('<?php echo $api_base; ?>/txt2img', form);
        const url = URL.createObjectURL(blob);
        document.getElementById('txt2imgResult').innerHTML = '<img src="' + url + '" />';
      } catch (err) {
        document.getElementById('txt2imgResult').innerHTML = 'Error: ' + err.message;
      }
    });

    document.getElementById('img2imgForm').addEventListener('submit', async function (event) {
      event.preventDefault();
      const file = document.getElementById('img2imgFile').files[0];
      if (!file) {
        alert('Choose an image');
        return;
      }
      const form = new FormData();
      form.append('file', file);
      form.append('prompt', document.getElementById('img2imgPrompt').value);
      document.getElementById('img2imgResult').innerHTML = 'Generating...';
      try {
        const blob = await sendForm('<?php echo $api_base; ?>/img2img', form);
        const url = URL.createObjectURL(blob);
        document.getElementById('img2imgResult').innerHTML = '<img src="' + url + '" />';
      } catch (err) {
        document.getElementById('img2imgResult').innerHTML = 'Error: ' + err.message;
      }
    });

    document.getElementById('txt2videoForm').addEventListener('submit', async function (event) {
      event.preventDefault();
      const form = new FormData();
      form.append('prompt', document.getElementById('txt2videoPrompt').value);
      form.append('frames', document.getElementById('txt2videoFrames').value);
      document.getElementById('txt2videoResult').innerHTML = 'Generating...';
      try {
        const blob = await sendForm('<?php echo $api_base; ?>/txt2video', form);
        const url = URL.createObjectURL(blob);
        document.getElementById('txt2videoResult').innerHTML = '<video controls src="' + url + '"></video>';
      } catch (err) {
        document.getElementById('txt2videoResult').innerHTML = 'Error: ' + err.message;
      }
    });

    document.getElementById('img2videoForm').addEventListener('submit', async function (event) {
      event.preventDefault();
      const file = document.getElementById('img2videoFile').files[0];
      if (!file) {
        alert('Choose an image');
        return;
      }
      const form = new FormData();
      form.append('file', file);
      form.append('frames', document.getElementById('img2videoFrames').value);
      document.getElementById('img2videoResult').innerHTML = 'Generating...';
      try {
        const blob = await sendForm('<?php echo $api_base; ?>/img2video', form);
        const url = URL.createObjectURL(blob);
        document.getElementById('img2videoResult').innerHTML = '<video controls src="' + url + '"></video>';
      } catch (err) {
        document.getElementById('img2videoResult').innerHTML = 'Error: ' + err.message;
      }
    });
  </script>
</body>
</html>
