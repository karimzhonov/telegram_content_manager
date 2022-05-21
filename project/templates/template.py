def template(header=None, body=None, footer=None):
    header = '\r' if header is None else f"<b>{header}</b>"
    body = '\r' if body is None else f"<code>{body}</code>"
    footer = '\n' if footer is None else footer
    return '\n'.join([header, body, footer])
