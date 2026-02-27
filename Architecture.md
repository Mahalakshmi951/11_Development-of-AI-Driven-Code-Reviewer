# Development of an AI-Driven Code Reviewer

## Abstract

Manual evaluation of programming assignments is a repetitive and time-consuming task in academic environments. Instructors must assess not only code correctness but also coding style, logical structure, and efficiency. This paper presents a compact research model for an AI-driven code reviewer designed to automate code analysis and feedback generation. The proposed system integrates Abstract Syntax Tree (AST) parsing with AI-based language models to detect syntax and logical errors, analyze coding style compliance, and suggest optimizations. The solution aims to enhance learning outcomes by providing instant, structured, and student-friendly feedback while reducing the evaluation workload for instructors.

## Keywords

AI-based code review, AST parsing, automated feedback, GPT API, programming education

## 1. Introduction

Code review is an essential component of software development and programming education. In academic settings, students submit a large number of coding assignments that must be evaluated for correctness, readability, and adherence to coding standards. Manual review is often inconsistent and time-intensive, particularly in large classrooms.

With advances in artificial intelligence and natural language processing, automated systems can now assist in code understanding and analysis. AI-driven tools offer the ability to identify errors, recommend best practices, and provide explanations in a human-like manner. This research proposes an AI-driven code reviewer that combines deterministic program analysis using AST with AI-based semantic evaluation to deliver comprehensive feedback to students.

## 2. Problem Statement

Manual code review for large volumes of student submissions is inefficient and prone to inconsistency. Existing static analysis tools focus mainly on rule-based checks and lack personalized feedback. There is a need for an intelligent system that can automatically analyze student code, identify errors, evaluate coding style, and suggest meaningful improvements in an educational context.

## 3. Proposed System

The proposed system is an automated code review platform primarily designed for Python programs. It accepts student code as input and processes it through multiple analysis layers to generate structured feedback.

### 3.1 System Architecture

The system consists of the following modules:

* **Code Parsing and Preprocessing:** Parses input code using Python’s AST module to understand program structure and normalize formatting.
* **Error and Bug Detection:** Identifies syntax errors, undefined variables, unused imports, and unreachable code through static analysis.
* **Coding Style Analysis:** Evaluates adherence to PEP8 guidelines, checking naming conventions, indentation, and line length.
* **Optimization Suggestions:** Uses the GPT API to analyze code efficiency and readability, recommending best practices and alternative approaches.
* **Feedback Delivery Interface:** Presents categorized feedback through a web-based user interface.

## 4. Methodology

The implementation uses Python for backend processing due to its strong support for AST manipulation and AI integration. Static analysis techniques are applied for error and style detection, while AI models generate semantic feedback and optimization suggestions. The system produces clear explanations along with code improvement recommendations, making it suitable for learning environments.

## 5. Results and Discussion

Initial testing shows that the AI-driven reviewer successfully detects common syntax and logical errors in student code. Style violations are accurately identified, and AI-generated suggestions improve code readability and structure. The automated feedback reduces manual review effort and helps students understand their mistakes more effectively.

## 6. Conclusion and Future Work

This research model demonstrates the potential of AI-driven code review systems in academic environments. By combining AST-based static analysis with AI-powered feedback, the system delivers comprehensive and educational code evaluations. Future enhancements include multi-language support, integration with learning management systems, and advanced analytics for personalized learning.

## References

1. Python Software Foundation, “PEP 8 – Style Guide for Python Code.”
2. A. V. Aho et al., *Compilers: Principles, Techniques, and Tools*.

