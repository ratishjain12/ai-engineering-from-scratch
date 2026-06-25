def stream_file(path, strip_newline=True, skip_empty_lines=False, encoding = "utf-8", with_line_numbers=False):
    with open(path, 'r', encoding=encoding) as file:
        for line_number, line in enumerate(file, start=1):
            if strip_newline:
                line = line.rstrip('\n')
            if skip_empty_lines and not line:
                continue
            if with_line_numbers:
                yield line_number, line
            else:
                yield line

def batch_stream(iterable, batch_size):
    batch = []

    for item in iterable:
        batch.append(item)
        if len(batch) == batch_size:
            yield batch
            batch = []
    
    if batch:
        yield batch


if __name__ == "__main__":
    file_path = "logs.txt"  # Replace with your file path

    for line in stream_file(file_path):
        print(line)
    
    lines = stream_file(file_path, strip_newline=True, skip_empty_lines=True, with_line_numbers=True)
    for batch in batch_stream(lines, batch_size=5):
        print(batch)