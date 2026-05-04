import networkx as nx
import random

def compute_pagerank_networkx(G, alpha=0.85):
    
    print("Computing PageRank using NetworkX (Power Iteration)...")
    return nx.pagerank(G, alpha=alpha)

def simulate_pagerank_random_walk(G, alpha=0.85, steps=5000000):
    
    print(f"Simulating Random Walk with {steps} steps (alpha={alpha})...")
    nodes = list(G.nodes())
    if not nodes:
        return {}
        
    visits = {n: 0 for n in nodes}
    current_node = random.choice(nodes)
    
    for i in range(steps):
        if i % 1000000 == 0 and i > 0:
            print(f"  ... completed {i} steps")
            
        visits[current_node] += 1
        
        # Damping factor: follow link or teleport
        if random.random() < alpha:
            # G._succ[node] is faster than G.successors(node)
            neighbors = list(G._succ[current_node].keys())
            if neighbors:
                # Follow a random outgoing link
                current_node = random.choice(neighbors)
            else:
                # Dangling node (no out-edges): teleport to a random node
                current_node = random.choice(nodes)
        else:
            # Teleport to a random node
            current_node = random.choice(nodes)
            
    total_visits = steps
    pagerank_dist = {node: count / total_visits for node, count in visits.items()}
    
    return pagerank_dist

def compare_distributions(pr_exact, pr_simulated, top_k=10):
   
    print(f"\nTop {top_k} nodes by Exact PageRank:")
    sorted_exact = sorted(pr_exact.items(), key=lambda x: x[1], reverse=True)
    for i, (node, score) in enumerate(sorted_exact[:top_k]):
        print(f"{i+1}. Node {node}: {score:.6f}")
        
    print(f"\nTop {top_k} nodes by Simulated PageRank (Random Walk):")
    sorted_sim = sorted(pr_simulated.items(), key=lambda x: x[1], reverse=True)
    for i, (node, score) in enumerate(sorted_sim[:top_k]):
        print(f"{i+1}. Node {node}: {score:.6f}")
