version_info = (0, 2, 2, None)
version = (
    ".".join(map(str, version_info[:3])) +
    (f"-{version_info[3]}" if version_info[3] else "")
)
