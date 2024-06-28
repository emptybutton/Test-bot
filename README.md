# Результат тестового задания
Реализованны:
1. телеграм-бот для конечных пользователей, написанный на `aiogram`
2. полу-рак, полу-микросервис на `FastAPI`

Можно запустить при помощи команд:
```bash
git clone https://github.com/emptybutton/Test-bot.git
docker compose --project-directory ./Test-bot run telegrambot alembic upgrade head
docker compose --project-directory ./Test-bot up
```

## Телеграм-бот
Запрашивает у пользователя два числа и отправляет их в FastAPI-приложение для "вычисления":

<img src="https://github.com/emptybutton/Test-bot/blob/main/assets/dialog.png?raw=true"/>

## API приложения
Имеет два эндпоинта для сложения и умножения двух чисел:

<img src="https://github.com/emptybutton/Test-bot/blob/main/assets/api.png?raw=true"/>

## Взаимодействия
Оба приложения общаются друг с другом, используя как синхронный, так и асинхронный вид взаимодействия.

Синхронное взаимодействие используется при вычислении суммы чисел, переданных конечным пользователем боту. </br>
Бот, вместо самостоятельного вычисления, отправляет HTTP запрос веб-приложению, которое отправляет вычисленную сумму в ответ.

Асинхронное взаимодействие используется, когда веб-приложение получает запрос на умножение всех чисел. </br>
Перед отправкой ответа, веб-приложение генерирует событие о факте запроса, содержащее два переданных числа и их произведение.

Далее бот получает это событие и отправляет сообщение всем своим пользователям, сообщая о том, что оно произошло:

<img src="https://github.com/emptybutton/Test-bot/blob/main/assets/interaction-result.png?raw=true"/>

> [!NOTE]
> Перед этим:
> 
> <img src="https://github.com/emptybutton/Test-bot/blob/main/assets/interaction-start.png?raw=true"/>
