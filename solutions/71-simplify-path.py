def simplifyPath(path):
    stack = []

    for seg in path.split("/")[1:]:
        if seg in ['', '.']:
            continue
        elif seg == '..':
            if stack:
                stack = stack[:-1]
        else:
            stack.append(seg)

    return "/"+"/".join(stack)
