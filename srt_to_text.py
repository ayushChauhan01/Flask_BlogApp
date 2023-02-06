def remove_timestamps(text):
    import re

    # Remove timestamps using regex
    result = re.sub(r'\d{1,2}:\d{2}', '\n', text)

    return result


new_text = remove_timestamps(text)

print(new_text)
