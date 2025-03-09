import networkx as nx
import matplotlib.pyplot as plt
import json

# 读取 JSON 数据
file_path = "data.json"  # 确保 data.json 文件在同一目录
with open(file_path, "r", encoding="utf-8") as f:
    data = json.load(f)

# 提取所有节点
nodes = data["all_nodes"]

# 创建有向图
G = nx.DiGraph()

# 添加节点和边
for node in nodes:
    node_id = node["id"]
    parent_id = node["parent"]
    reward = node["reward"]

    # 添加节点，显示 ID 和奖励值
    G.add_node(node_id, label=f"ID: {node_id}\nReward: {reward:.2f}")

    # 连接父子节点（根节点 parent=-1 不添加边）
    if parent_id != -1:
        G.add_edge(parent_id, node_id)

# 绘制树状图
plt.figure(figsize=(12, 8))
pos = nx.drawing.nx_agraph.graphviz_layout(G, prog="dot")  # 层次布局
labels = nx.get_node_attributes(G, "label")

nx.draw(G, pos, with_labels=True, labels=labels, node_size=2000, node_color="lightblue",
        font_size=8, font_weight="bold", edge_color="gray")

plt.title("MCTS 树状结构")
plt.show()
