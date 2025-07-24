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

*Automate the boring stuff* 🚀
