# Quizzy: Your Ultimate Quiz Preparation Tool 📚✨

## Graphical Abstract 🎨
### Flow:
![Cute Flow](https://media.discordapp.net/attachments/1046753920460017688/1230901790258630686/GraphicalAb.jpg?ex=6635019f&is=66228c9f&hm=9f30e413221fd3165f22a0d1d3e2b13e4ac6b9e575b20a1c46aaab97dde4bfab&=&format=webp&width=1210&height=934
 "A cute Flow")

```mermaid
flowchart LR
    A(HomePageView) -->|Create Account| B(CreateAccount)
    A -->|Login| C(Login)
    C -->|Attempt Quiz| D(AttemptQuiz)
    C -->|Import Quizzes| E(ImportQuizzes)
    E -->|Use CSV| F(UseCSV)
    C -->|Create Quiz| G(CreateQuiz)
    C -->|Delete Quiz| H(DeleteQuiz)
    C -->|Create Question| I(CreateQuestion)
    C -->|Assign Options| J(AssignOptions)
    D -->|Get Result| K(GetResult)
```

### Data Structure:
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

**Feeling puzzled about preparing for your exams? Say goodbye to confusion with Quizzy, the charming practice buddy designed to make your test prep as easy as pie!** 🍰

## 🚀 Quick Demo
Curious to dive in? Take a peek at Quizzy in action. Just hop over to ➔ [Demo Web APP](http://getbackwork.pythonanywhere.com/quiz)

## 🎯 Purpose
**Quizzy** is not just a tool; it's your personal cheerleader- ensuring you're sprint-ready for any test coming your way. Whether it's acing your school exams or smashing that professional certification, Quizzy's got your back!

## 💧 Software Development Process: The Classic Waterfall Model
We embraced the time-honored Waterfall model, valuing its linear, cascading essence which aligns with our crisp and clear project outline.

### Why Waterfall? Here's the splash!
* Structured and Steady: With a robust foundation phase and methodical overhead, we're on track to create Quizzy magic without any hitches.
* A predictable playbook: No room for guesswork or improvisation, we're sticking to the script to craft an outstanding quiz experience for you.

## 🎯 Target Market Snapshot
From bustling students to career-boosting professionals, Quizzy is the perfect prep companion for anyone with an appetite for knowledge and a hunger for success.

## 🛠️ Software Development Saga

### The Creation Odyssey
Following the Waterfall's legacy, we delved through stages from contemplation to realization:
* **Blueprinting Dreams:** Sculpting out Quizzy's DNA from authentication marvels to progress tracking victories.
* **Artful Designing:** Choreographing a symphony of screens and data dances, enriching Django's soul with our very own models and view masterpieces.
* **Crafting the Core:** Breathing life into Quizzy with the real deal - CRUD spells, question conjurations, and CSV enchantments.
* **Testing Triumphs:** Sending Quizzy through trials and tribulations with our rigorous test alchemists ensuring everything is tickety-boo.
* **Global Unveiling:** Setting the stage with servers, database glam, and static showstoppers, we're red-carpet ready for Quizzy's grand entrance.

### The Visioneers
Here's to the dream weavers behind Quizzy:
* **Kenny Kou (P2204767)**: The code whisperer for views, urls, and models.
* **Matthew NG (P2204935)**: The creative crusader for designing templates that aren't just visually pleasing but also intuitively navigable.
* **Alex Leong (P2204876)**: The maestro of demos, graphic and documents, a support hero, and a visionary for now, then and tomorrow's Quizzy.

### The March of Progress
* **Day 1:** Conceiving the grand design.
* **Day 2~3:** Breathing life into the creation.
* **Day 4:** Triumphing over bugs and glitches.
* **Day 5:** The final review; a toast to completion.

### The Code Conundrum
At the heart of Quizzy lies the algorithmic pulse - a rhythmic wizardry that spins the wheels of creation, chronicling answers, and tallying scores with the grace of a seasoned maestro.

### Progress Pulse
Backend brilliance ready! Frontend finery and quiz-importing alchemy in the test crucible.

### 🌟 Future Flashes
Tomorrow's Quizzy shines with features unheard and unseen:
* 🎧 Audio adventures with MP3 trails.
* 🏆 Scoreboard spectacles flaunting online glories.
* 📚 Test records unraveling the mysteries of knowledge.
* 🎭 User avatars ranging from wisdom-imparting teachers to knowledge-seeking students.
* 🏦 The treasure trove of a public question vault.
* 🔀 A merry-go-round of questions; neither knowing start nor end.
* 📱 Device dances, ensuring a sway-friendly Quizzy.
* 🔒 Fortified bastions guarding the sanctity of your Quizzy journey.
