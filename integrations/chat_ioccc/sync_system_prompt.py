#!/usr/bin/env python3
from pathlib import Path

src = Path(__file__).with_name("SYSTEM_INSTRUCTIONS.txt")
dst = Path(__file__).with_name("system_prompt.h")
text = src.read_text(encoding="utf-8")
escaped = (
    text.replace("\\", "\\\\")
        .replace('"', '\\"')
        .replace("\r\n", "\\n")
        .replace("\n", "\\n")
)
dst.write_text('#ifndef RICHARD_SYSTEM_PROMPT_H\n#define RICHARD_SYSTEM_PROMPT_H\n#define S "' + escaped + '"\n#endif\n', encoding="utf-8")
print(dst)
