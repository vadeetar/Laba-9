# Лабораторная работа №9: Мультиязычное программирование

**Студент:** Тарасов Вадим Романович  
**Группа:** 221131  
**Вариант:** 8

## Описание
Реализована интеграция трех языков программирования:
- **Go** — HTTP микросервис и консольный калькулятор
- **Rust** — высокопроизводительная библиотека (AES-128 шифрование + обработка изображений)
- **Python** — оркестратор на FastAPI

## Структура проекта
├── docker/
├── go_calculator/
├── go_service/
├── python_app/
├── rust_lib/
├── tests/
├── .gitignore
├── PROMPT_LOG.md
├── docker-compose.yml
├── requirements.txt
└── README.md

## Запуск тестов
```bash
# Python тесты
pytest tests/ -v

# Go тесты
cd go_service && go test -v
cd ../go_calculator && go test -v

# Rust тесты
cd rust_lib && cargo test
Запуск через Docker
bash
docker-compose up --build
После запуска:

Go сервис: http://localhost:8080

FastAPI Swagger: http://localhost:8000/docs
