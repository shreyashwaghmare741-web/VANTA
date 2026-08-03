# CHANGELOG

All notable changes to **VANTA (Virtual Autonomous Neural Task Assistant)** are documented in this file.

---

# Version 0.0.7
**Date:** 01 August 2026

## Desktop Automation

### Added
- Smart Application Launcher
- Open installed applications
- Open websites
- Open common Windows folders
- Application database for launch targets
- Desktop automation framework

### Supported Commands
- open chrome
- open vscode
- open github
- open downloads

### Rebranding
- Renamed project from **EON** to **VANTA**
- Official expansion:
  **Virtual Autonomous Neural Task Assistant**
- Renamed AI function:
  - `ask_eon()` → `ask_vanta()`
- Updated welcome message
- Updated goodbye message
- Updated README
- Updated documentation
- Updated project branding
- Removed remaining EON references

### Project Philosophy
**Think. Understand. Act.**

### Improved
- Faster application launching
- Cleaner project branding
- Better maintainability

---

# Version 0.0.6
**Date:** 01 August 2026

## System Monitoring Module

### Added
- Battery monitoring
- CPU usage monitoring
- RAM usage monitoring
- Disk usage monitoring
- System information retrieval
- `psutil` integration
- `platform` integration

### Intent Router
Added support for:
- battery
- charge
- charging
- cpu
- processor
- ram
- memory
- disk
- storage
- drive
- system
- computer
- pc

### Improved
- Local system commands execute instantly
- No AI required for hardware monitoring
- Reduced response time
- Lower LLM workload
- More intelligent routing decisions

---

# Version 0.0.5
**Date:** 31 July 2026

## Project Refactoring

### Added
- Modular folder structure
- `run.py` launcher
- Git version tracking
- CHANGELOG documentation
- Project cleanup

### New Directories
- ai/
- automation/
- core/
- docs/
- memory/
- plugins/
- projects/
- router/
- security/
- skills/
- tests/
- ui/
- utils/
- vision/
- voice/

### Improved
- Cleaner project organization
- Easier future expansion
- Better maintainability

---

# Version 0.0.4
**Date:** 31 July 2026

## Skill Architecture

### Added
- Intent Router
- Calculator Skill
- Skill-based architecture
- Automatic routing between AI and local tools

### Improved
- Mathematical calculations no longer require AI
- Faster responses for arithmetic operations
- Reduced unnecessary LLM usage

---

# Version 0.0.3
**Date:** 30 July 2026

## Session Memory System

### Added
- SessionMemory class
- Chat history storage
- Automatic conversation context
- Message management using TypedDict

### Improved
- AI now remembers previous messages during the session
- More natural multi-turn conversations

---

# Version 0.0.2
**Date:** 30 July 2026

## User Experience Improvements

### Added
- Thinking spinner while AI generates responses
- Cleaner terminal interface
- Welcome message on startup

### Improved
- Better user feedback during long AI responses
- More professional console output

---

# Version 0.0.1
**Date:** 29 July 2026

## Initial Release

### Added
- Created the initial VANTA project structure
- Integrated Ollama with Qwen3:8B
- Built the first command-line chat interface
- Added AI communication module (`ai/llm.py`)
- Created the main application entry point
- Added configuration management
- Added project README
- Initialized Git repository

---

# Current Project Status

## AI
- ✅ Local Qwen3:8B
- ✅ Ollama Integration
- ✅ Conversation Memory
- ✅ Context Awareness

## Core
- ✅ Config System
- ✅ Main Launcher
- ✅ Intent Router
- ✅ Session Memory

## Skills
- ✅ Calculator
- ✅ System Monitoring
- ✅ Desktop Automation

## User Interface
- ✅ Terminal Interface
- ✅ Thinking Spinner
- ✅ Welcome Screen
- ✅ Goodbye Screen

## Development
- ✅ Git Repository
- ✅ Version Tracking
- ✅ Modular Architecture
- ✅ Documentation

---

# Roadmap

## Version 0.0.8
### Skill Manager
- Centralized skill registry
- Automatic skill loading
- Cleaner architecture
- Easier feature expansion

---

## Version 0.0.9
### File Management
- Search files
- Create folders
- Move files
- Rename files
- Delete files
- Smart file organization

---

## Version 0.1.0
### Voice Assistant
- Speech recognition
- Text-to-speech
- Wake word ("Hey VANTA")
- Hands-free interaction

---

## Long-Term Vision

### Version 0.2.x
- Vision Module

### Version 0.3.x
- Persistent Memory

### Version 0.4.x
- Autonomous Agent

### Version 0.5.x
- Project Workspace Manager

### Version 0.6.x
- Multi-Agent Architecture

### Version 1.0.0
**First Stable Public Release**