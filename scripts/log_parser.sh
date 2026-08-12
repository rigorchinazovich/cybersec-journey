#!/bin/bash
LOG_FILE="$1"
if [ -z "$LOG_FILE" ]; then
    echo "Ошибка: укажи путь к логу"
    exit 1
fi
if [ ! -f "$LOG_FILE" ]; then
    echo "Ошибка: файл $LOG_FILE не найден"
    exit 1
fi
grep "Failed password" "$LOG_FILE" 2>/dev/null | awk '{print $(NF-3)}' | sort | uniq -c | sort -nr | head -5
