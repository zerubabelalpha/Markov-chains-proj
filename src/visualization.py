import matplotlib.pyplot as plt
import seaborn as sns
import networkx as nx

def plot_pagerank_distribution(pagerank_scores, title="PageRank Distribution", filename="pagerank_dist.png"):
    
    print(f"Plotting PageRank distribution to {filename}...")
    scores = list(pagerank_scores.values())
    
    plt.figure(figsize=(10, 6))
    sns.histplot(scores, bins=50, log_scale=(False, True), color='royalblue', alpha=0.7)
    plt.title(title, fontsize=15)
    plt.xlabel("PageRank Score", fontsize=12)
    plt.ylabel("Frequency (Log Scale)", fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(filename, dpi=200)
    plt.close()

def plot_top_subgraph(G, pagerank_scores, top_k=50, filename="top_subgraph.png"):
   
    print(f"Plotting subgraph of top {top_k} nodes to {filename}...")
    # Get top K nodes
    sorted_nodes = sorted(pagerank_scores.items(), key=lambda x: x[1], reverse=True)
    top_nodes = [node for node, score in sorted_nodes[:top_k]]
    
    # Create subgraph
    subgraph = G.subgraph(top_nodes)
    
    plt.figure(figsize=(14, 14))
    
    # Calculate node sizes based on relative score in the top_k
    max_score = max([pagerank_scores[n] for n in top_nodes]) if top_nodes else 1
    node_sizes = [max(150, (pagerank_scores[n] / max_score) * 2000) for n in subgraph.nodes()]
    
    pos = nx.spring_layout(subgraph, k=0.4, seed=42)
    
    nx.draw_networkx_nodes(subgraph, pos, node_size=node_sizes, node_color='lightgreen', alpha=0.9, edgecolors='black')
    nx.draw_networkx_edges(subgraph, pos, alpha=0.4, arrows=True, arrowsize=15, arrowstyle='->', connectionstyle='arc3,rad=0.1')
    
    labels = {n: str(n) for n in subgraph.nodes()}
    nx.draw_networkx_labels(subgraph, pos, labels=labels, font_size=9, font_family='sans-serif', font_weight='bold')
    
    plt.title(f"Subgraph of Top {top_k} PageRank Nodes", fontsize=18)
    plt.axis('off')
    plt.tight_layout()
    plt.savefig(filename, dpi=300)
    plt.close()
