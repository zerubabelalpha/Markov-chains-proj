import os
from src.data_loader import load_dataset
from src.graph_builder import build_graph
from src.pagerank import compute_pagerank_networkx, simulate_pagerank_random_walk, compare_distributions
from src.visualization import plot_pagerank_distribution, plot_top_subgraph

def main():
    
    print("PageRank Algorithm Simulation")
    
    # 1. load data
    print("--- Data Loading ---")
    data_file = load_dataset()
    
    # 2. Build Graph
    print("\n--- Building Graph ---")
    G = build_graph(data_file)
    
    # 3. Compute Exact PageRank
    print("\n--- Exact PageRank (Stationary Distribution) ---")
    # NetworkX computes the principal eigenvector via power iteration
    pr_exact = compute_pagerank_networkx(G, alpha=0.85)
    
    # 4. Simulate PageRank (Random Walk)
    print("\n--- Simulated PageRank (Random Sampling) ---")
    # 5 million steps is enough to show correlation, though more might be needed for absolute convergence on 875k nodes.
    steps = 5_000_000 
    pr_simulated = simulate_pagerank_random_walk(G, alpha=0.85, steps=steps)
    
    # 5. Compare
    print("\n--- Comparison ---")
    compare_distributions(pr_exact, pr_simulated, top_k=15)
    
    # 6. Visualization
    print("\n--- Visualization ---")
    if not os.path.exists("outputs"):
        os.makedirs("outputs")
        
    plot_pagerank_distribution(pr_exact, title="Exact PageRank Distribution", filename="outputs/pagerank_exact_dist.png")
    plot_pagerank_distribution(pr_simulated, title="Simulated PageRank Distribution (Random Walk)", filename="outputs/pagerank_simulated_dist.png")
    plot_top_subgraph(G, pr_exact, top_k=50, filename="outputs/top_50_subgraph.png")
    
    print("\nProcess completed successfully...")

if __name__ == "__main__":
    main()
