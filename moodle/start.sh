#!/bin/bash

if [ ! -d "/bitnami/moodle/question/type/coderunner" ]; then
  while true; do
      if ps aux | grep "[h]ttpd" >/dev/null; then
          echo "Install coderunner plugin..."
          echo "deb http://archive.debian.org/debian stretch main" > /etc/apt/sources.list

          apt update && apt install -y git
          git clone https://github.com/trampgeek/moodle-qtype_coderunner.git /bitnami/moodle/question/type/coderunner && \
              cd /bitnami/moodle/question/type/coderunner && \
              git checkout tags/4.2.3
          git clone https://github.com/trampgeek/moodle-qbehaviour_adaptive_adapted_for_coderunner.git /bitnami/moodle/question/behaviour/adaptive_adapted_for_coderunner

          sudo sed -i 's/\$CFG->directorypermissions = 02775;/\$CFG->directorypermissions = 0777;/g' /bitnami/moodle/config.php

          sudo chmod +x /bitnami/moodle/admin/cli/upgrade.php
          sudo /opt/bitnami/php/bin/php /bitnami/moodle/admin/cli/upgrade.php --non-interactive

          echo "Coderunner plugin installed!"

          sudo mysql -h mariadb -u root mariadb < /create_questions.sql

          echo "Test task created!"

          break
      else
          echo "Configuration moodle, waiting..."
          sleep 5
      fi
done
else
  echo "All dependencies are already installed"
fi


echo "Configuration Done"
tail -f /dev/null
