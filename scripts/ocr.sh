#!/bin/bash

# Select area with slurp and capture with grim
grimblast --freeze save area - | \
tesseract -l eng - - | wl-copy && \

notify-send -a "Ax-Shell" -i "${full_path}" "OCR Sucess" "Text Copied to Clipboard"
