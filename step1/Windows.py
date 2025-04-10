import subprocess

def get_windows_updates():
    #Uses PowerShell to list installed updates
    command = 'powershell "Get-HotFix | Select-Object -Property Description, HotFixID, InstalledOn"'
    result = subprocess.run(command, capture_output=True, text=True, shell=True)
    return result.stdout

def check_auto_updates():
    command = 'powershell "(Get-ItemProperty \\"HKLM:\\\\Software\\\\Policies\\\\Microsoft\\\\Windows\\\\WindowsUpdate\\\\AU\\").NoAutoUpdate"'
    result = subprocess.run(command, capture_output=True, text=True, shell=True)
    return "Disabled" if "1" in result.stdout else "Enabled"

print("Installed Updates:")
print(get_windows_updates())
print("\nAutomatic Updates:")
print(check_auto_updates())
