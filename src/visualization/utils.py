

def save_txt(file_path: str, text: str) -> None:
    with open(
        file=file_path,
        mode='w',
        encoding='utf-8'
    ) as file:
        file.write(text)
