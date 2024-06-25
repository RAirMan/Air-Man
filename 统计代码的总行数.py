from pathlib import Path

# 将所有的py文件筛选出来
def get_files(p, files):
    for each in p.iterdir():
        # 当前的源代码不统计在总行数中
        if str(each) == __file__:
            continue
        if each.is_file() and each.suffix == '.py':
            files.append(each)
        # 递归搜索目前下的其他文件夹
        if each.is_dir():
            p = each    # 该代码的作用就是将文件指向each这个文件夹！
            get_files(p, files)

    return files

# 统计py文件中的代码行数
def count_lines(files):
    lines = 0
    for each in files:
        with open(each, "r", errors="ignore") as f:
            t = f.readlines()
            # 空行不计入总行数
            lines = lines + len(t) - t.count('\n')  # 空行不能算，所以要减去空行数量

    return lines

# 获取当前文件目录
p = Path.cwd()
# 存放py文件
files = []
# 获取所有的py文件
files = get_files(p, files)
# 统计行数
result = count_lines(files)

print(f"一个有 {result} 行代码~")