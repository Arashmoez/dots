with open('batman.txt', 'r') as f:
    lines = [line.rstrip() for line in f.readlines()]

# Find the minimum indentation (non-zero)
min_indent = float('inf')
for line in lines:
    if line.strip():  # Only consider non-empty lines
        indent = len(line) - len(line.lstrip())
        if indent < min_indent:
            min_indent = indent

# Remove the common left padding
trimmed_lines = []
for line in lines:
    if line.strip():  # Non-empty line
        trimmed_lines.append(line[min_indent:].rstrip())
    else:  # Empty line
        trimmed_lines.append('')

# Remove empty lines from start and end
while trimmed_lines and not trimmed_lines[0].strip():
    trimmed_lines.pop(0)
while trimmed_lines and not trimmed_lines[-1].strip():
    trimmed_lines.pop(-1)

with open('batman_trimmed.txt', 'w') as f:
    f.write('\n'.join(trimmed_lines))