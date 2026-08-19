import requests

url = input('Введи url наподобие "https://bsuir.by": ')
print(url)
if not url.startswith(("http://", "https://")):
    print("Ошибка: URL должен начинаться с http:// или https://")
    exit(1)
try:

    response = requests.head(url, timeout=5, allow_redirects=False)
    status = response.status_code
    print(f"Получен статус: {status}")
    message = {
        200: "ресурс доступен и все хорошо",
        301: "ресурс навсегда перемещен в другое место",
        302: "ресурс временно перемещен в другое место",
        401: "нужна авторизация",
        403: "недостаток прав",
        404: "страница заброшена",
        500: "ошибка на строне сервера"
    }
    if status in message:
        print(message[status])
except requests.exceptions.Timeout:
    print(f"[-] {url} Превышен статус ожидания")

except requests.exceptions.ConnectionError:
    print(f"[-] {url} Не удалось подключиться (нет DNS либо сервер лежит)")
except requests.exceptions.RequestException as e:
    print(f"[-] {url} Ошибка запроса: {e}")
