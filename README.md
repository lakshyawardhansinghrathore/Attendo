<p align="center">
  <img src="https://i.ibb.co/ccX6XTND/LOGO.jpg" alt="Attendo Logo" width="120"/>
</p>

<h1 align="center">Attendo</h1>

<p align="center">
  <strong>AI-Powered Attendance System using Face Recognition & Voice Identification</strong>
</p>

<p align="center">
  🚀 <strong>Live Demo: <a href="https://tinyurl.com/Attendo-App">https://tinyurl.com/Attendo-App</a></strong>
</p>

<p align="center">
  <a href="#-overview">Overview</a> •
  <a href="#-features">Features</a> •
  <a href="#%EF%B8%8F-tech-stack">Tech Stack</a> •
  <a href="#%EF%B8%8F-architecture">Architecture</a> •
  <a href="#-getting-started">Getting Started</a> •
  <a href="#-usage">Usage</a> •
  <a href="#%EF%B8%8F-database-schema">Database Schema</a> •
  <a href="#-contributing">Contributing</a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit"/>
  <img src="https://img.shields.io/badge/Supabase-3FCF8E?style=for-the-badge&logo=supabase&logoColor=white" alt="Supabase"/>
  <img src="https://img.shields.io/badge/dlib-008000?style=for-the-badge&logo=opencv&logoColor=white" alt="dlib"/>
  <img src="https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white" alt="scikit-learn"/>
</p>

---

## 🎯 Overview

**Attendo** is an intelligent classroom attendance system that eliminates manual roll calls using two AI-powered recognition methods:

1. **📸 Face Recognition** — Teachers upload or capture classroom photos, and the system automatically identifies enrolled students using facial embeddings and an SVM classifier.
2. **🎙️ Voice Identification** — Students speak a short phrase (e.g., *"I am present"*), and the system matches their voice print against stored embeddings using cosine similarity.

The platform features two dedicated portals — **Teacher** and **Student** — each with role-specific authentication and dashboards.

---

## ✨ Features

### 🧑‍🏫 Teacher Portal

| Feature | Description |
|---|---|
| **Register & Login** | Secure password-based authentication with bcrypt hashing |
| **Create Subjects** | Add subjects with code, name, and section |
| **Take Photo Attendance** | Upload or capture multiple classroom photos, then run AI face analysis |
| **Take Voice Attendance** | Record classroom audio and identify students by voice |
| **Review & Confirm** | Preview attendance results (✅ Present / ❌ Absent) before saving |
| **Attendance Records** | View historical attendance logs grouped by session, with present/total stats |
| **Analytics Dashboard** | Visualize attendance trends over time and identify students with low attendance |
| **Export to CSV** | Download full attendance records as a CSV file for offline use |
| **Share via QR Code** | Generate QR codes and shareable links for students to join subjects |

### 🧑‍🎓 Student Portal

| Feature | Description |
|---|---|
| **FaceID Login** | Students authenticate by showing their face to the camera — no passwords |
| **New Student Registration** | First-time students register with a face photo and optional voice sample |
| **Enroll in Subjects** | Join classes using a subject code or scan a QR link |
| **Quick Enrollment** | Auto-enrollment via shareable URL with `?join-code=` query parameter |
| **View Enrolled Subjects** | See all enrolled courses with attendance statistics |
| **Unenroll** | Leave a subject at any time |

### 🤖 AI Capabilities

- **Face Detection** — dlib's HOG-based frontal face detector
- **Face Embeddings** — 128-dimensional face descriptors via dlib's ResNet model
- **Face Classification** — SVM classifier with linear kernel and balanced class weights
- **Resemblance Threshold** — Euclidean distance threshold of `0.6` to reject false positives
- **Voice Embeddings** — Speaker embedding via [Resemblyzer](https://github.com/resemble-ai/Resemblyzer) encoder
- **Voice Identification** — Cosine similarity matching with a `0.65` threshold
- **Bulk Audio Processing** — Automatic voice activity detection (VAD) to segment multi-speaker audio and identify each speaker independently

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **Frontend** | [Streamlit](https://streamlit.io/) with custom CSS (Plus Jakarta Sans font) |
| **Backend** | Python 3.10+ |
| **Database** | [Supabase](https://supabase.com/) (PostgreSQL) |
| **Face Recognition** | dlib, face_recognition_models, scikit-learn (SVM) |
| **Voice Recognition** | Resemblyzer, librosa |
| **Auth** | bcrypt (teacher), FaceID (student) |
| **QR Generation** | segno |
| **Image Processing** | Pillow, NumPy |
| **Data Handling** | Pandas |

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────┐
│                    Streamlit App                     │
│  ┌──────────────┐  ┌──────────┐  ┌───────────────┐  │
│  │  Home Screen  │  │ Teacher  │  │   Student     │  │
│  │  (Portal      │  │ Portal   │  │   Portal      │  │
│  │   Selection)  │  │          │  │               │  │
│  └──────────────┘  └────┬─────┘  └───────┬───────┘  │
│                         │                │           │
│  ┌──────────────────────┴────────────────┴────────┐  │
│  │              UI Components Layer               │  │
│  │  Dialogs │ Headers │ Footers │ Subject Cards   │  │
│  └──────────────────────┬─────────────────────────┘  │
│                         │                            │
│  ┌──────────────────────┴─────────────────────────┐  │
│  │              AI Pipelines Layer                 │  │
│  │  ┌─────────────────┐  ┌──────────────────────┐ │  │
│  │  │ Face Pipeline   │  │  Voice Pipeline      │ │  │
│  │  │ (dlib + SVM)    │  │  (Resemblyzer)       │ │  │
│  │  └─────────────────┘  └──────────────────────┘ │  │
│  └──────────────────────┬─────────────────────────┘  │
│                         │                            │
│  ┌──────────────────────┴─────────────────────────┐  │
│  │              Database Layer (Supabase)          │  │
│  │  teachers │ students │ subjects │ attendance    │  │
│  └────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────┘
```

---

## 📂 Project Structure

```
AI Attendence/
├── app.py                          # Entry point — routing & page config
├── requirements.txt                # Python dependencies
├── .streamlit/
│   └── secrets.toml                # Supabase credentials (not committed)
│
└── src/
    ├── screens/
    │   ├── home_screen.py          # Portal selection (Student / Teacher)
    │   ├── teacher_screen.py       # Teacher login, register, dashboard & tabs
    │   └── student_screen.py       # Student FaceID login, registration & dashboard
    │
    ├── pipelines/
    │   ├── face_pipeline.py        # Face detection, embedding, SVM training & prediction
    │   └── voice_pipeline.py       # Voice embedding, speaker identification & bulk processing
    │
    ├── components/
    │   ├── header.py               # App header (home & dashboard variants)
    │   ├── footer.py               # App footer with branding
    │   ├── subject_card.py         # Reusable subject card with stats
    │   ├── dialog_add_photo.py     # Camera capture / file upload dialog
    │   ├── dialog_attendance_results.py  # Review & confirm attendance results
    │   ├── dialog_voice_attendance.py    # Voice-based attendance dialog
    │   ├── dialog_create_subject.py      # Create new subject form
    │   ├── dialog_enroll.py              # Manual subject enrollment
    │   ├── dialog_auto_enroll.py         # Auto-enrollment via QR/link
    │   └── dialog_share_subject.py       # QR code & link generation
    │
    ├── database/
    │   ├── config.py               # Supabase client initialization
    │   └── db.py                   # All CRUD operations (teachers, students, subjects, attendance)
    │
    └── ui/
        └── base_layout.py          # Global CSS theming & custom fonts
```

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.10+**
- **CMake** (required for dlib compilation)
- A **Supabase** project with the required tables (see [Database Schema](#database-schema))

### 1. Clone the Repository

```bash
git clone https://github.com/LakshyawardhanSingh/Attendo.git
cd Attendo
```

### 2. Create a Virtual Environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

> **Note:** `dlib` requires CMake and a C++ compiler. On Windows, install [Visual Studio Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/). On Ubuntu: `sudo apt install cmake build-essential`.

### 4. Configure Supabase Secrets

Create `.streamlit/secrets.toml` with your Supabase credentials:

```toml
SUPABASE_URL = "https://your-project.supabase.co"
SUPABASE_KEY = "your-anon-or-service-role-key"
```

### 5. Run the Application

```bash
streamlit run app.py
```

The app will open at `http://localhost:8501`.

---

## 📖 Usage

### Teacher Workflow

```
Register/Login  →  Create Subject  →  Share QR Code with Students
                                    →  Take Attendance (Photo or Voice)
                                    →  Review & Confirm Results
                                    →  View Historical Records
```

1. **Register** a teacher account with username & password.
2. **Create a subject** (e.g., `CS101 — Intro to CS — Section A`).
3. **Share** the subject code or QR link with students.
4. **Take attendance** by uploading/capturing classroom photos or recording audio.
5. **Review** the AI-generated results and confirm to save.

### Student Workflow

```
Face Scan  →  Register (if new)  →  Enroll in Subjects  →  Attend Classes
```

1. **Scan your face** with the camera to log in instantly.
2. **New students** register with their name, a face photo, and an optional voice sample.
3. **Enroll** in subjects using a code or QR link shared by the teacher.
4. **Attend** classes — the teacher's AI analysis will automatically detect your presence.

---

## 🗄️ Database Schema

The app uses **Supabase (PostgreSQL)** with the following tables:

```sql
-- Teachers table
CREATE TABLE teachers (
    teacher_id  BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    username    TEXT UNIQUE NOT NULL,
    password    TEXT NOT NULL,          -- bcrypt hashed
    name        TEXT NOT NULL
);

-- Students table
CREATE TABLE students (
    student_id      BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    name            TEXT NOT NULL,
    face_embedding  FLOAT8[],          -- 128-dim face descriptor
    voice_embedding FLOAT8[]           -- 256-dim voice embedding
);

-- Subjects table
CREATE TABLE subjects (
    subject_id    BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    subject_code  TEXT UNIQUE NOT NULL,
    name          TEXT NOT NULL,
    section       TEXT,
    teacher_id    BIGINT REFERENCES teachers(teacher_id)
);

-- Student-Subject enrollment (many-to-many)
CREATE TABLE subject_students (
    id          BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    student_id  BIGINT REFERENCES students(student_id),
    subject_id  BIGINT REFERENCES subjects(subject_id)
);

-- Attendance logs
CREATE TABLE attendance_logs (
    id          BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    student_id  BIGINT REFERENCES students(student_id),
    subject_id  BIGINT REFERENCES subjects(subject_id),
    timestamp   TIMESTAMPTZ NOT NULL,
    is_present  BOOLEAN DEFAULT FALSE
);
```

---

## 🔬 How the AI Works

### Face Recognition Pipeline

```
Classroom Photo
       │
       ▼
┌─────────────────┐
│  dlib HOG Face   │ ──→ Detect all faces in the image
│  Detector        │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  dlib Shape      │ ──→ Locate 68 facial landmarks
│  Predictor       │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  dlib ResNet     │ ──→ Generate 128-dim face embedding
│  Face Encoder    │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  SVM Classifier  │ ──→ Predict student ID
│  (Linear Kernel) │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Euclidean       │ ──→ Verify match (threshold ≤ 0.6)
│  Distance Check  │
└─────────────────┘
```

### Voice Recognition Pipeline

```
Classroom Audio
       │
       ▼
┌─────────────────┐
│  librosa VAD     │ ──→ Split audio into speech segments
│  (top_db=30)     │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Resemblyzer     │ ──→ Generate speaker embedding per segment
│  VoiceEncoder    │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Cosine          │ ──→ Match against enrolled voice profiles
│  Similarity      │     (threshold ≥ 0.65)
└─────────────────┘
```

---

## ⚙️ Configuration

| Parameter | Location | Default | Description |
|---|---|---|---|
| `resemblance_threshold` | `face_pipeline.py` | `0.6` | Max Euclidean distance for a valid face match |
| `threshold` | `voice_pipeline.py` | `0.65` | Min cosine similarity for a valid voice match |
| `top_db` | `voice_pipeline.py` | `30` | Silence threshold for audio segmentation |
| `sr` | `voice_pipeline.py` | `16000` | Audio sample rate (Hz) |
| `app_domain` | `dialog_share_subject.py` | `attendo.streamlit.app` | Domain used in shareable QR links |

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 🙏 Acknowledgements

- [dlib](http://dlib.net/) — Face detection & recognition models
- [Resemblyzer](https://github.com/resemble-ai/Resemblyzer) — Voice encoder for speaker verification
- [Streamlit](https://streamlit.io/) — Rapid web app framework for Python
- [Supabase](https://supabase.com/) — Open-source Firebase alternative (PostgreSQL backend)
- [scikit-learn](https://scikit-learn.org/) — SVM classifier for face identification
- [librosa](https://librosa.org/) — Audio analysis and voice activity detection

---

<p align="center">
  © 2026 Attendo AI. All rights reserved.
</p>