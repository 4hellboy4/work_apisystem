def init_logs() -> None:
    with open('data/logs.txt', 'w', encoding='utf-8') as f:
        f.write('START\n')