@echo off
set ZIP_NAME=ai-video-studio-export.zip
if exist "%ZIP_NAME%" del "%ZIP_NAME%"
powershell -NoProfile -Command "Compress-Archive -Path '.\*' -DestinationPath '.\%ZIP_NAME%' -Force -CompressionLevel Optimal -Exclude '.git','.venv','backend\models'"
echo Created %ZIP_NAME%
pause
