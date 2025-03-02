import pkg_resources

# List of packages you want to check
packages = [
    "deepgram-sdk",
    "python-dotenv",
    "pyaudio",
    "sounddevice",
    "numpy",
    # Tkinter is bundled with Python,
]

# Function to get version of installed packages
def check_installed_versions(packages):
    for package in packages:
        try:
            # Get the installed version of the package
            version = pkg_resources.get_distribution(package).version
            print(f"{package}: {version}")
        except pkg_resources.DistributionNotFound:
            print(f"{package}: Not installed")

# Run the function to check versions
if __name__ == "__main__":
    check_installed_versions(packages)
