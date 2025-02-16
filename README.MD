


# Автотесты API микросервиса объявлений

Добро пожаловать в репозиторий с автотестами для API микросервиса, который позволяет создавать, получать и анализировать объявления. В этом проекте реализована параметризация тестов с использованием JSON-файлов, чистая архитектура тестов и возможность запуска тестов как локально, так и в контейнере Docker.

---

## Содержание

- [Описание](#описание)
- [Пример JSON-конфигурации](#Пример JSON-конфигурации)
- [Подробное описание структуры JSON](#Подробное описание структуры JSON)
- [Структура проекта](#структура-проекта)
- [Установка зависимостей](#установка-зависимостей)
- [Запуск тестов](#запуск-тестов)
  - [Локальный запуск](#локальный-запуск)
  - [Запуск через Docker](#запуск-чрез-docker)
- [Контакты](#контакты)

---

## Описание

В данном проекте реализованы автотесты для следующих API ручек:
- **GET /api/1/item/:id** — получение объявления по его идентификатору;
- **POST /api/1/item** — создание нового объявления;
- **GET /api/1/:sellerID/item** — получение всех объявлений по идентификатору продавца;
- **GET /api/1/statistic/:id** — получение статистики по объявлению.

Тесты используют параметризацию через внешний JSON-файл для хранения тестовых данных, что позволяет легко расширять и поддерживать набор тестовых сценариев.

---


## Пример JSON-конфигурации

Файл `tests/data/item_test_data.json` содержит объект с несколькими ключами, каждый из которых соответствует определённой группе тестовых сценариев:

```json
{
  "test_get_item_by_id": [
    {
      "item_id": "0cd4183f-a699-4486-83f8-b513dfde477a",
      "expected_status": 200,
      "description": "Valid existing item id"
    },
    {
      "item_id": "non-existent-uuid",
      "expected_status": 400,
      "description": "Non-existent id"
    },
    {
      "item_id": "abc",
      "expected_status": 400,
      "description": "Invalid id format"
    },
    {
      "item_id": "",
      "expected_status": 404,
      "description": "Empty id value"
    }
  ],
  "test_create_item": [
    {
      "payload": {
        "sellerID": 123456,
        "name": "Item Name",
        "price": 100,
        "statistics": {
          "contacts": 5,
          "likes": 10,
          "viewCount": 20
        }
      },
      "expected_status": 200,
      "description": "Valid item creation"
    },
    {
      "payload": {
        "sellerID": 123456,
        "name": "",
        "price": 100,
        "statistics": {
          "contacts": 5,
          "likes": 10,
          "viewCount": 20
        }
      },
      "expected_status": 400,
      "description": "Empty item name"
    },
    {
      "payload": {
        "sellerID": 123456,
        "name": "Item Name",
        "price": -50,
        "statistics": {
          "contacts": 5,
          "likes": 10,
          "viewCount": 20
        }
      },
      "expected_status": 400,
      "description": "Negative price"
    }
  ],
  "test_get_items_by_seller": [
    {
      "seller_id": "123456",
      "expected_status": 200,
      "description": "Valid seller id with items"
    },
    {
      "seller_id": "non-numeric",
      "expected_status": 400,
      "description": "Invalid seller id format"
    }
  ],
  "test_get_item_statistic": [
    {
      "item_id": "0cd4183f-a699-4486-83f8-b513dfde477a",
      "expected_status": 200,
      "description": "Valid item id for statistic"
    },
    {
      "item_id": "non-existent-uuid",
      "expected_status": 400,
      "description": "Non-existent item id for statistic"
    },
    {
      "item_id": "abc",
      "expected_status": 400,
      "description": "Invalid id format for statistic"
    }
  ]
}
```

---

## Подробное описание структуры JSON

### 1. **test_get_item_by_id**
Этот раздел содержит массив объектов для тестирования ручки **GET /api/1/item/:id**.

- **item_id**  
  Значение, которое подставляется в URL запроса. Может быть корректным идентификатором, несуществующим, пустым или не соответствующим ожидаемому формату.

- **expected_status**  
  Ожидаемый HTTP-статус ответа от API (например, 200 для корректного запроса, 400 или 404 для ошибочных кейсов).  
  **Важно:** Значения могут отличаться в зависимости от логики API.

- **description**  
  Краткое описание тестового сценария, которое помогает быстро понять суть теста при выводе результатов.

### 2. **test_create_item**
В этом разделе находятся тестовые кейсы для ручки **POST /api/1/item**, которая отвечает за создание объявления.

- **payload**  
  Объект, который отправляется в теле запроса в формате JSON. Содержит необходимые поля для создания объявления (например, `sellerID`, `name`, `price` и объект `statistics` с подполями `contacts`, `likes`, `viewCount`).

- **expected_status**  
  Ожидаемый статус ответа. Например, для корректного создания — 200, для ошибочных данных (например, пустое имя или отрицательная цена) — 400.

- **description**  
  Описание кейса, поясняющее, что именно тестируется (валидные данные, пустое имя, отрицательная цена и т.д.).

### 3. **test_get_items_by_seller**
Здесь описаны сценарии для ручки **GET /api/1/:sellerID/item**, которая возвращает все объявления определённого продавца.

- **seller_id**  
  Идентификатор продавца, который передаётся в URL.

- **expected_status**  
  Ожидаемый статус ответа API.

- **description**  
  Описание тестового кейса (например, корректный идентификатор продавца или невалидный формат).

### 4. **test_get_item_statistic**
Раздел для тестирования ручки **GET /api/1/statistic/:id**.

- **item_id**  
  Идентификатор объявления, по которому запрашивается статистика.

- **expected_status**  
  Ожидаемый статус ответа (например, 200, если объявление существует, или 400, если id некорректен/не существует).

- **description**  
  Текстовое описание сценария.

---














## Структура проекта


```
project_root/
├── tests/
│   ├── __init__.py
│   ├── conftest.py              # Определение глобальных фикстур (например, api_client)
│   ├── api/
│   │   ├── __init__.py
│   │   ├── client.py            # Клиент для отправки HTTP-запросов
│   │   └── item.py              # Класс ItemAPI с методами для работы с API
│   ├── data/
│   │   └── item_test_data.json  # Тестовые данные для параметризации
│   ├── helpers/
│   │   ├── __init__.py
│   │   └── data_provider.py     # Загрузчик тестовых данных из JSON
│   └── test_item_api.py         # Параметризованные тесты API
├── Dockerfile                   # Dockerfile для контейнеризации автотестов
├── docker-compose.yml           # Docker Compose для запуска тестов в контейнере
└── requirements.txt             # Зависимости проекта
```

---

## Установка зависимостей

1. **Клонируйте репозиторий:**

   ```bash
   git clone https://github.com/your-username/your-repo.git
   ```
   
   Или скачайте zip-архив с репозиторием и распакуйте его.

2. **Убедитесь, что у вас установлен Python 3.11 или выше.**  
   Для проверки выполните:

   ```bash
   python --version
   ```

3. **Установите зависимости:**

   Перейдите в корневую директорию проекта и выполните команду:

   ```bash
   pip install -r requirements.txt
   ```

---

## Запуск тестов

### Локальный запуск

Чтобы запустить автотесты локально, выполните в корневой директории проекта команду:

```bash
pytest -v
```

Тесты находятся в папке `tests/` и будут выполнены с использованием параметризованных данных из `tests/data/item_test_data.json`.

### Запуск через Docker

Проект содержит Dockerfile и docker-compose.yml для удобного запуска тестов в контейнере.

1. **Перейдем в папку второго задания:**
```bash
cd Task2.1/ 
```


2. **Соберите образ Docker:**

   ```bash
   docker compose build
   ```

3. **Запустите тесты:**

   ```bash
   docker compose up --abort-on-container-exit
   ```

После завершения выполнения контейнер автоматически остановится, а результаты тестов будут выведены в консоль.





