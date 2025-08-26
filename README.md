# Workflow Automators

Python scripts to automate common development tasks.

## Scripts

### 1. [Folder Creator](folder_creator.py)
Creates numbered subfolders with intelligent naming.

**Usage:**
```bash
# In "module05" directory, creates: chapter5.1, chapter5.2, chapter5.3
python folder_creator.py chapter 3

# Custom path
python folder_creator.py section 4 --path /path/to/directory
```

**Features:**
- Auto-detects module numbers from directory names
- Handles existing folders gracefully
- Cross-platform compatible

---

### 2. [Python Module Checker](check_if_installed.py)
A simple utility function to programmatically check if a specific Python module is installed in the current environment. This avoids crashing a script with an ImportError and allows for graceful handling or user prompts.

**Usage:**
```python
import sys
import os

# Assuming 'check_if_installed.py' is in a 'utils' directory
# Adjust the path as needed for your project structure
utils_path = os.path.abspath(os.path.join(os.getcwd(), 'path', 'to', 'utils'))

if utils_path not in sys.path:
    sys.path.append(utils_path)

from check_if_installed import check_if_installed

# Check for a few different modules
check_if_installed('numpy')
check_if_installed('pandas')
check_if_installed('non_existent_module')
```

**Example Output:**
```bash
✅ Module 'numpy' is installed.
✅ Module 'pandas' is installed.
❌ Module 'non_existent_module' is NOT installed.
```

**Features:**
- Avoids Errors: Safely checks for modules without causing an ImportError.
- Zero Dependencies: Works out-of-the-box using built-in pip functions.
- Clear Feedback: Provides a simple, direct "installed" or "not installed" status.
- Environment Aware: Accurately checks the currently active Python environment.

---

### 3\. [Screenshot Renamer](rename_screenshot.py)

Automatically renames screenshot files based on their content using OCR and AI, adding a sequential three-digit prefix to keep them organized.

#### Setup

1.  **Install Tesseract-OCR**:

      * **Windows**: Download the installer from [tesseract-ocr's GitHub](https://github.com/tesseract-ocr/tesseract/releases).
      * **macOS**: `brew install tesseract`
      * **Linux**: `sudo apt install tesseract-ocr`

2.  **Install Python Libraries**:

    ```bash
    pip install google-generativeai pillow pytesseract
    ```

3.  **Set Gemini API Key**:

      * Get your API key from [Google AI Studio](https://aistudio.google.com/app/apikey).
      * Set it as an environment variable named `GEMINI_API_KEY`.

#### Usage

Run the script from your terminal, pointing it to the folder containing your screenshots.

```bash
python rename_screenshots.py "C:\path\to\your\screenshot_notes"
```

The script will automatically find the last used index (e.g., `047_...`) and start naming new files from the next number (`048_...`).

#### Features

  - **AI-Powered Naming**: Uses Gemini to generate relevant, descriptive filenames from image content.
  - **Automatic Indexing**: Scans the directory to find the last number and continues the sequence, keeping notes in order.
  - **Smart Processing**: Intelligently skips files that are already correctly named, only processing new screenshots.
  - **Text Recognition**: Employs Tesseract OCR to accurately extract text from any screenshot.

---

### 4. [Sequential Image Renamer](rename_images_sequentially.py)
A simple script to batch rename all image files in a folder to a sequential format using a specified keyword.

**Usage:**
```bash
# Renames all images in the 'vacation_pics' folder
python rename_images_sequentially.py beach_day --path ./vacation_pics
```

**Example Output:**
```bash
✓ Renamed 'IMG_2024.jpg' to 'beach_day_01.jpg'
✓ Renamed 'Screenshot (1).png' to 'beach_day_02.png'
✓ Renamed 'photo_001.jpeg' to 'beach_day_03.jpeg'
```

**Features:**
- **Simple & Fast**: Quickly renames all supported image types in a directory.
- **Custom Keywords**: Use any keyword as the base for your new filenames.
- **Consistent Naming**: Creates a clean, numbered sequence (e.g., `keyword_01`, `keyword_02`).
- **Safe**: Checks for a valid directory and handles potential errors gracefully.

---


*Automate the boring stuff* 🚀
