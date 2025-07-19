# Workflow Automators

Python scripts to automate common development tasks.

## Scripts

### 1. [Folder Creator](folder_creator.py)
Creates numbered subfolders with intelligent naming.

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

*Automate the boring stuff* 🚀
