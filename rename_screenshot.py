# rename_screenshots.py
# Automatically renames screenshots with a sequential three-digit prefix
# based on their content using OCR and AI.

import os
import sys
import argparse
import re
import google.generativeai as genai
from PIL import Image
import pytesseract

# --- CONFIGURATION ---
# If you installed Tesseract-OCR in a custom location on Windows, update this path.
# For example:
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Load the Gemini API key from environment variables
try:
    GEMINI_API_KEY = os.environ["GEMINI_API_KEY"]
    genai.configure(api_key=GEMINI_API_KEY)
except KeyError:
    print("❌ Error: GEMINI_API_KEY environment variable not found.")
    print("   Please get an API key from https://aistudio.google.com/app/apikey and set it.")
    sys.exit(1)

def get_next_index(folder_path):
    """
    Scans a folder to find the highest existing three-digit prefix in filenames
    and returns the next number in sequence.
    """
    max_index = 0
    # Regex to find filenames starting with exactly three digits and an underscore
    pattern = re.compile(r'^(\d{3})_')
    
    for filename in os.listdir(folder_path):
        match = pattern.match(filename)
        if match:
            index = int(match.group(1))
            if index > max_index:
                max_index = index
    
    # The next index is the highest found plus one.
    return max_index + 1

def sanitize_filename(name):
    """
    Cleans a string to be a valid filename.
    """
    name = name.lower()
    name = re.sub(r'[\s-]+', '_', name)
    name = re.sub(r'[^\w_]', '', name)
    return name

def get_text_from_image(image_path):
    """
    Extracts text from an image file using Tesseract-OCR.
    """
    try:
        with Image.open(image_path) as img:
            text = pytesseract.image_to_string(img)
            return text
    except Exception as e:
        print(f"  - Error processing image with Tesseract: {e}")
        return None

def get_ai_generated_name(text_content):
    """
    Uses the Gemini API to generate a descriptive filename from text.
    """
    if not text_content or text_content.strip() == "":
        return "document_scan"

    model = genai.GenerativeModel('gemini-1.5-flash-latest')
    
    prompt = f"""
    Based on the following text from a screenshot, generate a short, 2-6 word filename.
    The name should capture the main topic. Use underscores for spaces. No file extension.

    TEXT:
    ---
    {text_content[:2000]}
    ---

    FILENAME:
    """

    try:
        response = model.generate_content(prompt)
        filename = response.text.strip().replace('\n', '_')
        return filename
    except Exception as e:
        print(f"  - Error calling Gemini API: {e}")
        return "ai_naming_failed"

def process_screenshots(folder_path):
    """
    Main function to find new screenshots, process them, and rename them
    with a three-digit sequential prefix.
    """
    print(f"🔍 Scanning folder: {os.path.abspath(folder_path)}")
    
    # 1. Determine the starting index for new files
    current_index = get_next_index(folder_path)
    print(f"📈 Starting next index from: {current_index:03d}")
    print("-" * 50)

    supported_extensions = ('.png', '.jpg', '.jpeg', '.bmp', '.tiff')
    renamed_count = 0
    
    # Regex to identify files that are already named correctly
    indexed_pattern = re.compile(r'^\d{3}_')
    
    # Create a list of files to process so we don't have issues while renaming
    files_to_process = sorted([f for f in os.listdir(folder_path) if f.lower().endswith(supported_extensions)])

    for filename in files_to_process:
        # 2. Skip any file that already matches our desired naming format
        if indexed_pattern.match(filename):
            continue

        original_file_path = os.path.join(folder_path, filename)
        print(f"Processing: {filename}")

        # 3. Extract text using OCR
        extracted_text = get_text_from_image(original_file_path)
        if not extracted_text:
            print("  - ⚠ Could not extract text. Skipping.")
            continue

        # 4. Get a new name from the AI
        print("  - 🧠 Asking AI for a good name...")
        ai_name = get_ai_generated_name(extracted_text)
        clean_name = sanitize_filename(ai_name)
        
        if not clean_name:
            print("  - ⚠ AI returned an empty name. Skipping.")
            continue

        # 5. Construct the new filename with the three-digit prefix
        file_extension = os.path.splitext(filename)[1]
        # The :03d format pads the number with leading zeros (e.g., 48 -> 048)
        new_filename = f"{current_index:03d}_{clean_name}{file_extension}"
        new_file_path = os.path.join(folder_path, new_filename)

        # Handle potential name collisions, though unlikely with indexing
        counter = 1
        while os.path.exists(new_file_path):
            new_filename = f"{current_index:03d}_{clean_name}_{counter}{file_extension}"
            new_file_path = os.path.join(folder_path, new_filename)
            counter += 1

        try:
            os.rename(original_file_path, new_file_path)
            print(f"  - ✅ Renamed to: {new_filename}")
            renamed_count += 1
            current_index += 1 # IMPORTANT: Increment index for the next file
        except Exception as e:
            print(f"  - ❌ Failed to rename file: {e}")
        
        print("-" * 20)

    print("-" * 50)
    if renamed_count > 0:
        print(f"✨ Process complete! Renamed {renamed_count} new files.")
    else:
        print("✨ No new screenshots found to rename.")

def main():
    parser = argparse.ArgumentParser(
        description="Automatically rename screenshot files in a folder with a sequential index based on their content."
    )
    parser.add_argument("folder", help="The path to the folder containing your screenshots.")
    args = parser.parse_args()

    if not os.path.isdir(args.folder):
        print(f"❌ Error: The specified path is not a valid directory: {args.folder}")
        sys.exit(1)
        
    process_screenshots(args.folder)

if __name__ == "__main__":
    main()
