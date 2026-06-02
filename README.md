# 🚀 Doomscroller

> An AI-powered attention monitoring system that detects distraction in real time and instantly interrupts doomscrolling with visual and audio feedback.




\

---

## Overview

Doomscroller is a real-time computer vision application designed to reduce digital distraction.

Using webcam-based face tracking, eye tracking, and head pose estimation, the system continuously evaluates whether the user is focused on the screen.

When attention is lost, Doomscroller immediately:

* Displays a distraction-interrupting dog video
* Plays an audio alert
* Continues monitoring until attention returns

Once focus is regained, the alert automatically disappears.

---

## Problem Statement

Modern users spend significant time scrolling social media feeds and switching attention away from productive tasks.

Traditional productivity tools rely on timers, notifications, or manual intervention.

Doomscroller introduces a real-time AI-based attention monitoring system that reacts instantly to user behavior.

---

## Features

| Feature                       | Status |
| ----------------------------- | ------ |
| Real-Time Face Detection      | ✅      |
| Eye Tracking                  | ✅      |
| Head Direction Tracking       | ✅      |
| Focus Detection               | ✅      |
| Distraction Detection         | ✅      |
| Dog Video Alert               | ✅      |
| Audio Alert System            | ✅      |
| Split-Screen Interface        | ✅      |
| Cross-Platform Python Support | ✅      |

---

## 🏗 Architecture

```text
┌─────────────────────────┐
│       Webcam Feed       │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│     MediaPipe Face      │
│       Detection         │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│ Eye + Head Analysis     │
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│ Focus Classification    │
└──────┬─────────┬────────┘
       │         │
 Focused     Distracted
       │         │
       ▼         ▼
   Continue   Dog Video
   Tracking   + Audio
```

---

## Detection Pipeline

| Signal         | Purpose                    |
| -------------- | -------------------------- |
| Face Mesh      | Face landmark extraction   |
| Iris Tracking  | Eye movement detection     |
| Head Direction | Attention estimation       |
| Focus Logic    | Focused / Distracted state |
| Alert Engine   | Trigger response system    |

---

## System Workflow

```text
User Looking At Screen
          │
          ▼
      Focused
          │
          ▼
   No Alert Triggered

────────────────────────

User Looks Away
          │
          ▼
     Distracted
          │
          ▼
  Video + Audio Alert
          │
          ▼
User Returns Focus
          │
          ▼
 Alert Automatically Stops
```

---

## Overview

Problem Statement

Features

Architecture

Detection Pipeline

Workflow

---

## Technology Stack

| Category             | Technology |
| -------------------- | ---------- |
| Language             | Python     |
| Computer Vision      | OpenCV     |
| Face Tracking        | MediaPipe  |
| Numerical Processing | NumPy      |
| Audio System         | Pygame     |
| UI Rendering         | OpenCV     |

---

## Project Structure

```text
Doomscroller/
│
├── assets/
│   ├── dog.mp4
│   ├── dog_sound.mp3
│   └── logo.png
│
├── docs/
│   ├── architecture.png
│   ├── demo.gif
│   └── screenshots/
│
├── src/
│   ├── main.py
│   ├── face_tracker.py
│   ├── video_panel.py
│   ├── audio_controller.py
│   ├── config.py
│   └── utils.py
│
├── requirements.txt
├── README.md
└── LICENSE
```

---

## Installation

```bash
git clone <repository-url>

cd Doomscroller

pip install -r requirements.txt

python src/main.py
```

---

## Future Roadmap

* [ ] Advanced gaze estimation
* [ ] Attention scoring system
* [ ] Productivity analytics
* [ ] Custom alert media
* [ ] Desktop application build
* [ ] Multi-monitor support
* [ ] Session statistics dashboard

---

## License

This project is licensed under the MIT License.

---

## Author

Aayush Patil
