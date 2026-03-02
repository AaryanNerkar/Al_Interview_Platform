# HireByte Project Structure

> [!IMPORTANT]
> **READ-ONLY PROTECTION RULES**
>
> The following areas are strictly **Read-Only**. Modification of logic, functionality, or structure in these directories is prohibited to maintain system integrity:
>
> - **Backend Logic**: All files in `backend/` (FastAPI core, services, models).
> - **API Routes**: All endpoint definitions in `backend/main.py`.
> - **Authentication**: Supabase Auth integration and `AuthContext`.
> - **Database**: Connection logic in `backend/config/database.py`.
> - **Routing**: React Router structure in `frontend/src/App.tsx`.
>
> **ALLOWED MODIFICATIONS**
>
> Modifications are only permitted in the following areas:
>
> - **UI Components**: Visual elements in `frontend/src/components/`.
> - **Styling**: CSS and Tailwind configurations.
> - **Layout Design**: Minor structural changes to page layouts in `frontend/src/pages/` that do not affect functionality.

## 1. Backend Structure (FastAPI)

The backend is a high-performance FastAPI application located in the `backend/` directory. It handles interview logic, AI processing, and data persistence.

### API Endpoints

- **REST API (`/`)**
  - `GET /`: Health check / Root.
  - `GET /health`: Detailed status check.
  - `POST /upload-resume`: Processes PDF resumes and JDs.
  - `POST /start-topic-interview`: Starts a session without a resume.
  - `POST /transcribe`: Whisper-1 audio transcription.
  - `POST /get-hint`: Provides progressive interview hints.
  - `GET /report`: Fetches current session report data.
  - `GET /api/analytics`: Current session analytics.
  - `GET /api/session/download-pdf`: Generates on-the-fly report PDF.
  - `POST /api/session/save`: Persists session to database.
  - `POST /api/roadmap`: Generates AI study roadmaps.
  - `POST /api/audio-brief`: Generates TTS audio briefings.
  - `GET /api/session/weakness-analysis`: Topic-based weakness scoring.
  - `GET /api/session/hint-status`: Tracks hint availability.

- **WebSocket (`/ws`)**
  - `/ws/interview`: Core interview conversation loop (JSON-based).
  - `/ws/video`: Real-time video metric/emotion processing.

### Architecture Layering

- **`main.py`**: Entry point, FastAPI app instance, and global session state.
- **`services/`**: Business logic (LLM abstraction, Video/Audio processing, PDF generation).
- **`config/`**: Database configuration (Supabase) and environment loading.
- **`models/`**: Pydantic schemas for request/response validation.

### Database Connection

- **Supabase**: Used for data persistence (Interviews, Analytics, Reports).
- **Integration**: Configured via `backend/config/database.py` using `SUPABASE_URL` and `SUPABASE_KEY`.

---

## 2. Frontend Structure (React + Vite)

The frontend is a modern React application located in the `frontend/` directory, styled with Tailwind CSS and Framer Motion for animations.

### Pages and Routes

- `/`: **Landing Page** (Intro and start options).
- `/setup`: **Setup Page** (Resume upload, JD input, and topic selection).
- `/interview`: **Interview Page** (Interactive chat with video and real-time AI).
- `/analytics`: **Analytics Page** (Detailed performance reports and radar charts).

### Component Hierarchy

- **Layout**: `Layout.tsx`, `Navbar.tsx`, `Sidebar.tsx`.
- **Interview Components**: `ChatBox.tsx`, `WebcamPreview.tsx`, `AIAssistanceBadge.tsx`.
- **Analytics Components**: `RadarChart.tsx`, `WeaknessReport.tsx`, `CandidateReport.tsx`.
- **Modals**: `WelcomeModal.tsx`, `LoginModal.tsx`, `ConsentModal.tsx`.

### Context Providers

- **`ThemeContext`**: Handles UI appearance (Dark/Light mode).
- **`AuthContext`**: Manages user session state and Supabase Auth integration.

---

## 3. Dependency List

### Backend (Python)

- **Framework**: `FastAPI`, `Uvicorn`.
- **AI Libraries**: `openai` (Whisper, GPT), `cv2` (Video processing), `pydantic`.
- **Database**: `supabase-py`, `pymongo` (legacy/optional).
- **Utilities**: `PyPDF2`, `python-dotenv`, `python-multipart`.

### Frontend (TypeScript/React)

- **Framework**: `React 18`, `Vite`.
- **Styling**: `Tailwind CSS`, `clsx`, `tailwind-merge`.
- **State Management**: React Context API, `react-router-dom`.
- **Visualization**: `recharts`, `framer-motion`.
- **Tools**: `lucide-react`, `react-webcam`, `html2pdf.js`.

---

## 4. Protected Files

The following files and directories are critical for system operation and should not be modified without specific intent:

- **`.env` files**: Contains sensitive API keys (OpenAI, Supabase).
- **`backend/config/`**: Database and core configuration logic.
- **`backend/services/video_service.py`**: Complex computer vision logic.
- **`frontend/src/config/api.ts`**: Centralized API and WebSocket mapping.
- **`requirements.txt` / `package.json`**: Core dependency locking.

---

## 5. Routing Map

| Route | Page Component | Primary API Dependencies |
| :--- | :--- | :--- |
| `/` | `LandingPage` | N/A |
| `/setup` | `SetupPage` | `/upload-resume`, `/start-topic-interview` |
| `/interview` | `InterviewPage` | `/ws/interview`, `/ws/video`, `/get-hint` |
| `/analytics` | `AnalyticsPage` | `/api/analytics`, `/api/session/save` |
