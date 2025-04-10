import platform
import subprocess

def run_command(command, shell=False):
    try:
        result = subprocess.run(command, capture_output=True, text=True, shell=shell)
        return result.stdout.strip()
    except Exception as e:
        return f"Error: {e}"

def detect_os():
    os_name = platform.system()
    print(f"Detected OS: {os_name}")
    return os_name

def get_patches(os_name):
    if os_name == "Windows":
        return run_command('powershell "Get-HotFix | Select Description, HotFixID, InstalledOn"', shell=True)
    elif os_name == "Linux":
        return run_command(['dpkg-query', '-W', '-f=${Package} ${Version}\n'])
    elif os_name == "Darwin":
        return run_command(['softwareupdate', '--history'])
    else:
        return "Unsupported OS."

def check_auto_updates(os_name):
    if os_name == "Windows":
        command = 'powershell "(Get-ItemProperty \\"HKLM:\\\\Software\\\\Policies\\\\Microsoft\\\\Windows\\\\WindowsUpdate\\\\AU\\").NoAutoUpdate"'
        result = run_command(command, shell=True)
        if "1" in result:
            return "Automatic Updates: Disabled"
        else:
            return "Automatic Updates: Enabled"
    elif os_name == "Linux":
        return "Check unattended-upgrades or dnf-automatic (manual for now)."
    elif os_name == "Darwin":
        return "macOS auto-updates managed in System Preferences (manual check)."
    else:
        return "Unsupported OS."

def validate_patch_output(output):
    if not output or "Error" in output:
        return "Validation Failed: No output or error detected."
    if any(keyword in output for keyword in ["KB", "Installed", "Update", "Package"]):
        return "Validation Passed: Looks like patch data is present!"
    return "Validation Inconclusive: Couldn't find expected keywords."

def main():
    print("Starting Patch Checker\n" + "-"*30)
    os_name = detect_os()
    
    print("\nFetching Installed Patches...")
    patch_output = get_patches(os_name)
    print(patch_output[:1000])  # limit output length in preview

    print("\nChecking Automatic Update Status...")
    auto_update_status = check_auto_updates(os_name)
    print(auto_update_status)

    print("\nValidating Output...")
    validation_result = validate_patch_output(patch_output)
    print(validation_result)

    print("\nCompleted")

if __name__ == "__main__":
    main()
