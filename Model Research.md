# 🤖 AI-Driven Code Reviewer

An intelligent automated system that analyzes Python programs and generates structured, educational feedback using AST-based static analysis and AI-powered semantic evaluation.

---

## 📌 Abstract

Manual evaluation of programming assignments is time-consuming and inconsistent in academic environments. This project proposes an AI-driven code reviewer that automates code analysis and feedback generation.

The system combines:
- **Abstract Syntax Tree (AST) parsing** for structural analysis
- **Static analysis techniques** for error detection
- **AI-based semantic evaluation** for meaningful explanations and optimization suggestions

The goal is to enhance student learning while reducing instructor workload.

---

## 🎯 Problem Statement

Manual code review:
- Takes significant time
- Lacks consistency
- Is difficult to scale in large classrooms

Existing static tools only provide rule-based checks and do not offer educational explanations.

This project addresses the need for an intelligent system that:
- Detects syntax and logical errors
- Evaluates coding style (PEP8)
- Suggests optimizations
- Generates structured feedback

---

## 🏗️ System Architecture

The system consists of the following modules:

### 1️⃣ Code Parsing & Preprocessing
- Uses Python’s `AST` module
- Understands program structure (functions, loops, conditions)

### 2️⃣ Error Detection
- Syntax errors
- Undefined variables
- Unused imports
- Logical inconsistencies

### 3️⃣ Coding Style Analysis
- PEP8 compliance
- Indentation checking
- Naming conventions
- Line length validation

### 4️⃣ AI-Based Semantic Review
- Code readability improvements
- Optimization suggestions
- Best practice recommendations
- Human-like explanations

### 5️⃣ Feedback Interface
- Categorized structured output
- Web-based display for students

---

## ⚙️ Methodology

The system is implemented using Python due to its strong AST support and AI integration capabilities.

### 🔹 Static Analysis Layer
Performs rule-based validation using AST traversal.

### 🔹 AI Semantic Layer
Uses GPT-based API models to analyze deeper logical structure and provide educational explanations.

Combining these two layers ensures both technical accuracy and conceptual clarity.

---

## 📊 Results

Initial prototype testing shows:

- Accurate detection of syntax and logical errors  
- Effective identification of style violations  
- Meaningful AI-generated optimization suggestions  
- Reduced manual review effort  

The system delivers more comprehensive feedback compared to traditional static analysis tools.

---

## 🚀 Future Enhancements

- Multi-language support (Java, C++)
- Plagiarism detection
- Performance benchmarking
- LMS integration
- Personalized learning analytics

---

## 🛠️ Tech Stack

- Python (AST Module)
- Node.js / Flask (Backend)
- React.js (Frontend)
- MongoDB / SQL (Database)
- GPT API (AI Integration)

---

## 📚 References

1. Python Software Foundation – PEP 8 Style Guide  
2. A. V. Aho et al., *Compilers: Principles, Techniques, and Tools*  
3. T. Parr, *The Definitive ANTLR 4 Reference*  



