# Chat Widget Test Automation

Проект автоматизации тестирования чат-виджета AutoFAQ (https://autofaq.ai). 
Включает API и E2E тесты с использованием Pytest и Playwright.

## Особенности проекта
- Асинхронные тесты (asyncio)
- Page Object паттерн для E2E тестов
- API тесты для бэкенд функционала
- Allure отчеты с видео и скриншотами падений
- Контейнеризация с использованием Docker

## Структура проекта
```
.
├── api_tests/                  # API тесты
│   ├── core/                  # Базовые классы и утилиты
│   └── tests/                 # Тестовые сценарии
├── e2e_tests/                 # E2E тесты
│   ├── pages/                # Page Objects
│   └── tests/                # Тестовые сценарии
├── docker-compose.yml         # Docker конфигурация
├── api.Dockerfile            # Dockerfile для API тестов
└── e2e.Dockerfile           # Dockerfile для E2E тестов
```

## Запуск тестов

### 1. Требования
- Docker
- Docker Compose

### 2. Установка и запуск

1. Клонируйте репозиторий:
```bash
git clone git@github.com:telez371/chat-widget-qa-task.git
cd chat-widget-qa-task
```

2. Соберите Docker образы:
```bash
docker-compose build
```

3. Запустите тесты:
```bash
docker-compose up
```

4. После завершения тестов просмотрите Allure отчет:
```bash
docker run --rm -v $(pwd):/app -p 8080:8080 chat-widget-qa-task:api allure serve -h 0.0.0.0 -p 8080 /app/allure-results
```

Отчет будет доступен по адресу: http://localhost:8080

## Описание тестов

### API Тесты
- Отправка текстовых сообщений
- Валидация формата сообщений
- Проверка обработки ошибок
- Тестирование граничных значений

### E2E Тесты
- Открытие чат-виджета
- Отправка сообщений через интерфейс
- Загрузка файлов
- Проверка уведомлений

## Allure отчет
В отчете доступны:
- Общая статистика прохождения тестов
- Видео и скриншоты упавших тестов
- Временные метрики выполнения
- Логи выполнения тестов

## Решение проблем

При необходимости пересборки с нуля:
```bash
# Очистка
docker-compose down
docker rmi chat-widget-qa-task:api chat-widget-qa-task:e2e

# Пересборка
docker-compose build --no-cache
```

## Замечания
- API тесты запускаются первыми
- E2E тесты запускаются после завершения API тестов
- Некоторые тесты намеренно настроены на падение для демонстрации отчетности
- Для остановки Allure отчета используйте Ctrl+C