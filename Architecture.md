## 🏗️ System Architecture

The AI-Driven Code Reviewer follows a layered modular architecture. 
The system separates frontend, backend, static analysis, AI semantic analysis, and database components to ensure scalability and maintainability.
## 🏗️ System Architecture

```mermaid
flowchart TD

    A[Student User] --> B[Frontend React Application]

    B --> C[Backend API Server]

    C --> D[Static Analysis Engine]
    C --> E[AI Semantic Analysis Engine]
    C --> F[(Database)]

    D --> D1[AST Parser]
    D --> D2[PEP8 Style Checker]
    D --> D3[Syntax and Logic Error Detection]

    E --> E1[GPT API Integration]
    E --> E2[Code Optimization Suggestions]
    E --> E3[Human Readable Feedback Generator]

    D --> G[Feedback Aggregator]
    E --> G

    G --> F
    F --> H[Structured Feedback Response]

    H --> B
```

<img width="1840" height="704" alt="image" src="https://github.com/user-attachments/assets/fff55fd8-8449-47ce-9104-4b2e95a68cff" />

### 🔍 Architecture Description

- **Frontend Layer**: Accepts student code and displays structured feedback.
- **Backend Layer**: Handles API requests and coordinates analysis modules.
- **Static Analysis Engine**: Performs AST parsing, syntax validation, and style checking.
- **AI Semantic Engine**: Uses GPT API to generate optimization suggestions and human-readable explanations.
- **Database Layer**: Stores code submissions and feedback history.

This layered design ensures modularity, scalability, and clear separation of concerns.
