from http.server import BaseHTTPRequestHandler, HTTPServer

# Для начала определим настройки запуска
hostName = "localhost"  # Адрес для доступа по сети
serverPort = 8080  # Порт для доступа по сети


class MyServer(BaseHTTPRequestHandler):
    def get_page_content(self):
        with open('index.html', 'r', encoding='utf-8') as file:
            return file.read()

    def do_GET(self):
        if self.path == '/':
            page_content = self.get_page_content()  # Вызов метода get_page_content()
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')  # Set the response encoding to utf-8
            self.end_headers()
            self.wfile.write(page_content.encode('utf-8'))  # Encode the response content in utf-8
        else:
            self.send_error(404, 'Страница не найдена')


if __name__ == "__main__":
    # Инициализация веб-сервера, который будет по заданным параметрам в сети.
    # Принимать запросы и отправлять их на обработку специальному классу, который был описан выше
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        # Старт веб-сервера в бесконечном цикле прослушивания входящих запросов
        webServer.serve_forever()
    except KeyboardInterrupt:
        # Корректный способ остановить сервер в консоли через сочетание клавиш Ctrl + C
        pass

    # Корректная остановка веб-сервера, чтобы он освободил адрес и порт в сети, которые занимал
    webServer.server_close()
    print("Server stopped.")