# mse1h2024-coderunner

Данный проект нацелен на реализацию приложения для передачи сообщений (задач) между платформой moodle (с подключённым к нему плагином CodeRunner) и сервером JOBE. Приложение абстрагирует moodle и JOBE друг от друга и вперспективе будет обеспечивать запуск N серверов JOBE на разных машинах без использования доменных имен. 

Функциональность: moodle с помощью плагина CodeRunner отдаёт задачу в приложение, где задачи распределяются в очереди Celery, затем развёрнутый в docker-контейнере JOBE берёт задачи из нужной очереди, выполняет и возвращает ответ в очередь, откуда его забирает moodle.
