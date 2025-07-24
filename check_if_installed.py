try:
    from pip._internal.operations import freeze
except ImportError:
    from pip.operations import freeze

def check_if_installed(module_name):
    # (your function code here)
    installed_packages = [p.split('==')[0] for p in freeze.freeze()]
    if module_name in installed_packages:
        print(f"✅ Module '{module_name}' is installed.")
    else:
        print(f"❌ Module '{module_name}' is NOT installed.")