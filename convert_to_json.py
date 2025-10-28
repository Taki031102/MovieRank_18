import json
import re

input_file = "part-00000"
output_file = "top20.json"

results = []

with open(input_file, "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line.startswith("(") or not line.endswith(")"):
            continue
        # 去除左右括号
        content = line[1:-1]

        # 从右往左找最后一个逗号，避免标题中带逗号被误分割
        try:
            last_comma = content.rfind(",")
            title = content[:last_comma].strip().strip('"')
            score = float(content[last_comma + 1:])
            results.append({"title": title, "score": round(score, 2)})
        except Exception as e:
            print(f"跳过错误行：{line}，原因：{e}")

# 写入 JSON 文件
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print(f"✅ 转换完成，共导出 {len(results)} 条记录到 {output_file}")
