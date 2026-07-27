# DecodeLabs Project 1: Rule-Based AI Chatbot

## Overview
This repository contains a **System 2 (Deterministic / Rule-Based) AI Chatbot** developed as part of the DecodeLabs AI Engineering training track. The system uses predefined conditional rules to respond to user inputs cleanly and reliably.

## Key Features
- **String Normalization:** Uses `.lower()` and `.strip()` to handle uppercase, lowercase, and spacing inconsistencies.
- **Continuous CLI Loop:** Runs interactively via a `while` loop until explicit exit commands (`exit`, `quit`, `bye`) are given.
- **Edge Case & Fallback Handling:** Manages empty queries and unknown inputs gracefully.
- **Modular Code Architecture:** Decouples execution loop logic from core response processing.

## Project Structure
```text
rule-based-chatbot/
├── chatbot.py
└── README.md