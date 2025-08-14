import matplotlib.pyplot as plt
import matplotlib.patches as patches  # noqa: F401 (保留可选背景色用)


def read_grid_from_file(filepath: str) -> list[str]:
    """读取 Map.txt，提取中间的60字符列，返回60行，每行60字符。"""
    rows: list[str] = []
    with open(filepath, encoding="utf-8") as f:
        for line in f:
            parts = line.rstrip("\n").split(",")
            if len(parts) >= 2:
                row = parts[1].strip()
                # 规范化为长度60
                row = (row + " " * 60)[:60]
                rows.append(row)
                if len(rows) == 60:
                    break

    # 不足60行则补齐
    while len(rows) < 60:
        rows.append(" " * 60)

    return rows[:60]


def render_grid(rows: list[str]) -> None:
    fig, ax = plt.subplots(figsize=(12, 12))
    ax.set_xlim(0, 60)
    ax.set_ylim(0, 60)
    ax.set_xticks(range(61))
    ax.set_yticks(range(61))
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.grid(True, which="major", linewidth=0.5)

    for y in range(60):
        for x in range(60):
            ch = rows[y][x]
            ax.text(
                x + 0.5,
                59 - y + 0.5,
                ch,
                va="center",
                ha="center",
                fontsize=8,
                color="black",
            )

    ax.set_aspect("equal")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    grid_rows = read_grid_from_file("./Map-Generate/Map.txt")
    render_grid(grid_rows)


