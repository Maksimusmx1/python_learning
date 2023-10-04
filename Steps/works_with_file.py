

def open_file(file):
    # Открываем файл на чтение
    fp = open(file, 'rb')
    files = {'file': fp}
    return files

def close_file(file):
    # Закроем файл на чтение
    file['file'].close
