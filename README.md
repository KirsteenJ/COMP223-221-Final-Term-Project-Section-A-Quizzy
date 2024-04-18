# Quiz App Project: Quizzy

## Graphical Abstract
### Flow:
![Cute Flow](https://i.imgur.com/nFfABcg.jpeg "A cute Flow")

```mermaid
flowchart LR
    A[HomePageView] --> B(Create Account)
    A --> C[Login]
    C --> D[HomePageView]
    D --> E{"Attempt Quiz"}
    E --> F[Get Result]
    E --> G[Delete Quiz]
    G --> H{"Delete Question"}
    H --> I[Delete Option]
    D --> J{"Create Quiz"}
    J --> K[test question]
    K --> L[Delete Question]
    D --> M{"Create Question"}
    M --> N[test question]
    N --> O[Assign Options]
    O --> P[Delete Option]
```

### Data Structure:
![Cute DB](https://i.imgur.com/2MpdU5S.png "A cute DB")

```mermaid
erDiagram
    USERS ||--o{ QUIZZES : owns
    USERS ||--o{ USER_ANSWERS : answers
    QUIZZES ||--o{ QUESTIONS : contains
    QUESTIONS ||--o{ OPTIONS : includes
    QUESTIONS ||--o{ USER_ANSWERS : answered
    OPTIONS ||--o{ USER_ANSWERS : selected

    USERS {
        integer id PK "primary key"
        varchar username
        varchar email
        varchar password
        boolean is_staff
        boolean is_active
        timestamp date_joined
    }

    QUIZZES {
        integer id PK "primary key"
        varchar title
        text description
        timestamp created_at
        integer owner_id FK "foreign key to USERS"
    }

    QUESTIONS {
        integer id PK "primary key"
        integer quiz_id FK "foreign key to QUIZZES"
        varchar text
        timestamp created_at
    }

    OPTIONS {
        integer id PK "primary key"
        integer question_id FK "foreign key to QUESTIONS"
        varchar text
        boolean is_correct
    }

    USER_ANSWERS {
        integer id PK "primary key"
        integer user_id FK "foreign key to USERS"
        integer question_id FK "foreign key to QUESTIONS"
        integer selected_option_id FK "foreign key to OPTIONS"
        boolean is_correct
    }
```

## Demo
#TODO

[Demo Web APP](http://getbackwork.pythonanywhere.com/quiz)

## Purpose of the Software
Quizzy is designed as a personal practice tool for users preparing for various tests. The objective is to provide a simple yet efficient way to create, practice, and evaluate quizzes to enhance learning and test preparation.

### Software Development Process Applied
- **Waterfall Model**: We chose the Waterfall model for its straightforwardness and structured approach, which is conducive to the small scale and well-defined scope of our project.

### Why This Type?
- The Waterfall model allows our team to focus on a thorough requirement analysis and extensive planning at the early stages, ensuring a solid foundation for the rest of the project. Given that our app has a clear set of requirements with a predictable outcome, the sequential design of the Waterfall model suits our needs perfectly.

### Possible Usage
- **Target Market**: Our primary users are students and professionals looking for an effective way to prepare for exams or test their knowledge in specific subjects. Quizzy can be used for self-assessment or in a study group as a collaborative learning tool.

## Software Development Plan

### Development Process
The project is divided into distinct phases in line with the Waterfall model: Requirements, Design, Implementation, Verification, and Maintenance. 

### Members
- **Kenny Kou (P2204712)**: Configuring views and urls and models for the app.
- **Alex Leong (P2204876)**: Configuring templates,graphical abstract,ideas for future plan section
- **Matthew NG (P2204935)**: Responsible for demo video editing,providing help on configuring templates and future plan.

### Schedule
- **Day 1**: System design and architecture planning.
- **Day 2~3**: Implementation of core functionalities.
- **Day 4**: Testing and debugging.
- **Day 5**: Final review and project wrap-up.

### Algorithm
The core algorithm handles quiz creation, option selection, and scoring. It ensures that quizzes are created efficiently, answers are recorded accurately, and scores are calculated correctly.

### Current Status
The backend for quiz and question creation is complete. Frontend design and the import functionality for quizzes are testing.

### Future Plan
Moving forward, we plan to introduce an audio test feature and we will support the uploading of MP3 files. We are also adding a scoreboard feature for public online ranking, which includes the name, usage time, date, and ranking. For individual users, we will add a test record feature to help users identify their mistakes. In the user creation feature, we will add user levels, such as teacher, student, etc. In addition, we will add a database to create a public question bank, where each user can upload 1-5 question files. Finally, we will add a feature to randomize the order of the questions and the number of questions to be answered in the question settings.
