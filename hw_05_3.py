import sys
from typing import List, Dict

def parse_log_line(line: str) -> dict:
    try:
        parts = line.strip().split(" ", 3)
        return {
            "date": parts[0],
            "time": parts[1],
            "level": parts[2],
            "message": parts[3] if len(parts) > 3 else ""
        }
    except IndexError:
        return {}

def load_logs(file_path: str) -> List[dict]:
    logs = []
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            logs = [parse_log_line(line) for line in file if line.strip()]
    except FileNotFoundError:
        print(f"Помилка: Файл '{file_path}' не знайдено.")
        sys.exit(1)
    except Exception as e:
        print(f"Помилка читання файлу: {e}")
        sys.exit(1)
    return logs

def filter_logs_by_level(logs: List[dict], level: str) -> List[dict]:
    return list(filter(lambda log: log.get("level", "").lower() == level.lower(), logs))

def count_logs_by_level(logs: List[dict]) -> Dict[str, int]:
    counts = {}
    for log in logs:
        level = log.get("level")
        if level:
            counts[level] = counts.get(level, 0) + 1
    return counts

def display_log_counts(counts: Dict[str, int]):
    print("\nРівень логування | Кількість")
    print("-----------------|----------")
    for level in sorted(counts):
        print(f"{level:<17}| {counts[level]}")

def display_logs(logs: List[dict]):
    for log in logs:
        print(f"{log['date']} {log['time']} - {log['message']}")

def main():
    if len(sys.argv) < 2:
        print("Використання: python main.py path/to/logfile.log [log_level]")
        sys.exit(1)

    file_path = sys.argv[1]
    level_filter = sys.argv[2] if len(sys.argv) > 2 else None

    logs = load_logs(file_path)
    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    if level_filter:
        filtered_logs = filter_logs_by_level(logs, level_filter)
        print(f"\nДеталі логів для рівня '{level_filter.upper()}':")
        display_logs(filtered_logs)

if __name__ == "__main__":
    main()
