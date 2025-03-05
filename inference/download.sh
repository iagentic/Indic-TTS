#!/bin/bash

# Define the destination directory for downloads and extraction.
DEST_DIR="models"

# Create the directory if it doesn't exist.
mkdir -p "$DEST_DIR"

# List of zip files to download.
FILES=(
    "gs://indic_tts_models/as.zip"
    "gs://indic_tts_models/bn.zip"
    "gs://indic_tts_models/brx.zip"
    "gs://indic_tts_models/en+hi.zip"
    "gs://indic_tts_models/en.zip"
    "gs://indic_tts_models/gu.zip"
    "gs://indic_tts_models/hi.zip"
    "gs://indic_tts_models/kn.zip"
    "gs://indic_tts_models/ml.zip"
    "gs://indic_tts_models/mni.zip"
    "gs://indic_tts_models/mr.zip"
    "gs://indic_tts_models/or.zip"
    "gs://indic_tts_models/pa.zip"
    "gs://indic_tts_models/raj.zip"
    "gs://indic_tts_models/ta.zip"
    "gs://indic_tts_models/te.zip"
    "gs://indic_tts_models/en.zip"
    "gs://indic_tts_models/en+hi.zip"
)

# Loop through each file.
for file in "${FILES[@]}"; do
    # Extract the filename from the URL.
    filename=$(basename "$file")
    
    echo "Downloading $file..."
    gsutil cp "$file" "$DEST_DIR/$filename"
    
    # Check if download succeeded before unzipping.
    if [ $? -eq 0 ]; then
        echo "Unzipping $filename..."
        unzip -o "$DEST_DIR/$filename" -d "$DEST_DIR"
    else
        echo "Error downloading $filename. Skipping unzip."
    fi
    
    echo "----------------------------------"
done

echo "Download and extraction completed."
