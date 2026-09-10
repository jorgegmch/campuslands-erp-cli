# Campuslands ERP CLI

![License: MIT](https://img.shields.io/badge/license-MIT-green)

A command-line ERP for academic management — student and trainer records, academic-risk tracking, scheduling, and reporting — built in pure Python with **file-based JSON persistence** and no external database or third-party dependencies.

## Why JSON, not a database

This project is a deliberate technical exercise in building a working persistence layer from first principles: designing a data schema, writing CRUD operations, and managing referential consistency (students ↔ trainers ↔ schedules ↔ evaluations) entirely with the standard library. It complements a separate Python project built against a relational database (SQLite) — together they demonstrate both approaches: building persistence by hand, and building it on top of a database engine.

## Features

- Student (camper) and trainer registration and management
- Academic and behavioral risk-status tracking
- Grade and academic-module tracking
- Trainer, classroom, and schedule assignment
- Academic route creation for trainers
- Session-based login flow
- Interactive, menu-driven CLI
- Activity and academic-status reporting

## Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.10+ |
| Persistence | Local JSON files |
| Dependencies | None — standard library only (`os`, `json`) |
| Interface | Command-line (interactive menus) |

## Project Structure

```
campuslands-erp-cli/
├── modules/
│   ├── crud.py          # Core CRUD operations
│   ├── menus.py         # Role-based menu loops (coordinator, trainer, camper)
│   └── messages.py      # CLI messages and prompts
├── utils/
│   └── utils.py         # Shared helper functions
├── data/
│   ├── areas.json
│   ├── evaluaciones.json
│   ├── matriculas.json
│   └── usuarios.json
├── main.py               # Application entry point
├── .gitignore
├── LICENSE
└── README.md
```

## Installation & Usage

```bash
# Clone the repository
git clone https://github.com/jorgegmch/campuslands-erp-cli.git
cd campuslands-erp-cli

# Requires Python 3.10+, no external packages needed
python main.py
```

Once running, you'll be prompted to log in, then routed through interactive menus to manage campers, trainers, schedules, and reports.

## Design Notes

- **Modular separation**: CRUD logic, messaging, and menu orchestration live in separate modules rather than a single script.
- **Data model**: entities (users, enrollments, evaluations, areas) are normalized across separate JSON files rather than a single flat store, mirroring how you'd think about tables in a relational design.
- **Known limitation**: JSON files are not safe for concurrent multi-user access — this is a single-session, local-use system by design.

## License

MIT — see [LICENSE](LICENSE) for details.

---

Built by [Jorge Gomez](https://github.com/jorgegmch).
