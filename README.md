# EchoForm

A tkinter-based GUI application for displaying music data with typewriter-style text animation.
A further implementation will bring together text and visual art

## Project Structure

```
EchoForm/
├── main.py                 # Entry point
├── README.md              # Project documentation
├── song_viewer.py         # Song display logic (deprecated - moved to core/)
├── database/
│   └── ListeningSession.csv  # Music data
└── core/
    ├── __init__.py        # Package initialization
    ├── song_viewer.py     # Main GUI and typewriter implementation
    └── requirements.txt   # Python dependencies
```

## Installation

1. Clone or download this repository
2. Install dependencies:

```bash
pip install -r core/requirements.txt
```

## Requirements

- Python 3.8+
- pandas >= 2.3.0

## Usage

```bash
python main.py
```
