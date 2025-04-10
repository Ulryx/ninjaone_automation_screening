import subprocess

def get_mac_updates():
    command = ['softwareupdate', '--history']
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout

print("Installed Updates (macOS):")
print(get_mac_updates())
