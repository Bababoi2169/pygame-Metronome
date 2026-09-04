```markdown
# Pygame Metronome

A simple metronome application built with Python, Pygame, and `pygame-widgets`.

The application allows you to enter a BPM value and play a repeating beep at that tempo.

## Features

- Enter a tempo in beats per minute
- Start the metronome by pressing Enter
- Generate a beep sound automatically
- Reset the BPM input
- Quit the application with a keyboard shortcut
- Basic Pygame button interface
- Adjustable controls planned for future versions

## Requirements

You need the following installed:

- Python 3.9 or newer
- Pygame
- pygame-widgets
- `aplay` on Linux systems

The current version uses the Linux `aplay` command to play the generated WAV file. Therefore, audio playback currently works best on Linux.

## Project Structure

```text
pygame-metronome/
├── metronome.py
├── requirements.txt
└── README.md
```

The beep file is generated automatically at:

```text
/tmp/metronome_beep.wav
```

It does not need to be added to the repository.

## Installation

### 1. Clone the repository

Open a terminal or command prompt and run:

```bash
git clone https://github.com/YOUR_USERNAME/pygame-metronome.git
```

Replace `YOUR_USERNAME` with your GitHub username.

Move into the project directory:

```bash
cd pygame-metronome
```

### 2. Create a virtual environment

A virtual environment keeps this project's packages separate from your other Python projects.

#### Linux and macOS

```bash
python3 -m venv .venv
```

Activate it:

```bash
source .venv/bin/activate
```

#### Windows Command Prompt

```cmd
python -m venv .venv
```

Activate it:

```cmd
.venv\Scripts\activate
```

#### Windows PowerShell

```powershell
python -m venv .venv
```

Activate it:

```powershell
.venv\Scripts\Activate.ps1
```

If PowerShell prevents the activation script from running, open PowerShell as a user and run:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Then try activating the environment again:

```powershell
.venv\Scripts\Activate.ps1
```

When the virtual environment is active, you should see `(.venv)` at the beginning of your terminal prompt.

### 3. Install Python dependencies

Install the packages listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

If your system uses `pip3`, run:

```bash
pip3 install -r requirements.txt
```

The `requirements.txt` file should contain:

```text
pygame
pygame-widgets
```

### 4. Install Linux audio support

The current application uses `aplay` to play the metronome sound.

On Debian, Ubuntu, Linux Mint, and similar systems:

```bash
sudo apt update
sudo apt install alsa-utils
```

Check whether `aplay` is installed:

```bash
which aplay
```

You should see a path similar to:

```text
/usr/bin/aplay
```

On Fedora:

```bash
sudo dnf install alsa-utils
```

On Arch Linux:

```bash
sudo pacman -S alsa-utils
```

## Running the Application

Make sure your virtual environment is active, then run:

```bash
python metronome.py
```

On some Linux systems, use:

```bash
python3 metronome.py
```

To stop the application, press `Q` or close the application window.

## Controls

| Key | Action |
|---|---|
| Number keys | Enter a BPM value |
| Backspace | Delete the last BPM digit |
| Enter | Start the metronome |
| R | Reset the BPM input |
| Q | Quit the application |

The metronome accepts BPM values between 20 and 300.

## How BPM Works

BPM means beats per minute.

For example:

- `60 BPM` plays one beat every second
- `120 BPM` plays two beats every second
- `180 BPM` plays three beats every second

The interval between beats is calculated using:

```text
interval = 60 / BPM
```

For example, at 120 BPM:

```text
60 / 120 = 0.5 seconds per beat
```

## Troubleshooting

### `ModuleNotFoundError: No module named 'pygame'`

Install the dependencies:

```bash
pip install -r requirements.txt
```

Make sure your virtual environment is active.

### `ModuleNotFoundError: No module named 'pygame_widgets'`

Install `pygame-widgets`:

```bash
pip install pygame-widgets
```

### `FileNotFoundError: aplay`

Install ALSA utilities on Linux:

```bash
sudo apt install alsa-utils
```

The current version depends on `aplay` and may not work on Windows or macOS without modification.

### The application window freezes while playing

The current implementation uses a blocking metronome loop and `time.sleep()`. While the metronome is running, Pygame may not process window events normally.

A future version should use one of these approaches:

- `pygame.time.Clock()`
- Pygame timers
- A separate audio thread
- `pygame.mixer.Sound`

### No sound is playing

Check the following:

1. Make sure your system volume is turned up.
2. Test whether your sound system works:

   ```bash
   speaker-test
   ```

3. Check that `aplay` exists:

   ```bash
   which aplay
   ```

4. Confirm that the generated file exists:

   ```bash
   ls /tmp/metronome_beep.wav
   ```

5. Try playing the file manually:

   ```bash
   aplay /tmp/metronome_beep.wav
   ```

## Development

After making changes, run the application again:

```bash
python metronome.py
```

Check which files have changed:

```bash
git status
```

Add your changes:

```bash
git add .
```

Create a commit:

```bash
git commit -m "Describe your changes"
```

Upload the changes to GitHub:

```bash
git push
```

Example:

```bash
git add .
git commit -m "Add BPM input validation"
git push
```

## Updating the Project

To download the latest version from GitHub:

```bash
git pull
```

If new dependencies are added, install them again:

```bash
pip install -r requirements.txt
```

## Deactivating the Virtual Environment

When you finish working on the project, deactivate the virtual environment:

```bash
deactivate
```

You can activate it again later using the commands in the installation section.

## Future Improvements

Planned improvements include:

- Replace `aplay` with Pygame audio for Windows and macOS compatibility
- Add Start and Stop buttons
- Add a BPM slider
- Add accented beats
- Add different sound choices
- Add volume control
- Add time signatures
- Add visual beat indicators
- Prevent the application from freezing during playback
- Add keyboard shortcuts for increasing and decreasing BPM
- Add automated tests
- Package the application as an executable

## Contributing

Contributions are welcome.

To contribute:

1. Fork the repository.
2. Create a new branch:

   ```bash
   git checkout -b add-new-feature
   ```

3. Make your changes.
4. Test the application.
5. Commit your changes:

   ```bash
   git add .
   git commit -m "Add new feature"
   ```

6. Push your branch:

   ```bash
   git push origin add-new-feature
   ```

7. Open a pull request on GitHub.

## License

This project is available under the MIT License.

You may use, modify, and distribute the code with attribution.

To use the MIT License, create a file named `LICENSE` in the project folder and add the standard MIT License text.

## Author

Created by [Bababoi2169](https://github.com/Bababoi2169).

GitHub repository:

[https://github.com/Bababoi2169/pygame-Metronome.git](https://github.com/Bababoi2169/pygame-Metronome.git)
```
