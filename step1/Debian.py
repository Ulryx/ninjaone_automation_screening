import subprocess

def get_linux_updates():
    command = ['dpkg-query', '-W', '-f=${Package} ${Version}\n']
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout

print("Installed Packages (Linux):")
print(get_linux_updates())
