FROM bitnami/moodle:3.8.0

COPY start.sh .
RUN chmod +x start.sh

COPY create_question.sql .

CMD ["/bin/bash", "-c", "/app-entrypoint.sh /run.sh & /start.sh"]