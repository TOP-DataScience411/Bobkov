import os

def important_message(msg):
    terminal_w = os.get_terminal_size().columns
    frame_w = terminal_w - 4
    frame_wc = terminal_w -6
    
    words = msg.split()
    lines = []
    line = ""
    
    for word in words:
        if len(line) + len(word) + 2 <= terminal_w:
            line += (word + " ")
        else:
            lines.append(line.strip())
            line = word + " "
    
    if line:
        lines.append(line)
        
    border = "#" + ("-" * frame_w) + "#\n"
    
    
    message = border
    message += f"# {" " * frame_wc} #\n"
    for line in lines:
        message += f"# {line.center(terminal_w - 6)} #\n"
    message += f"# {" " * frame_wc} #\n"
    message += f"{border}"
    
    return message