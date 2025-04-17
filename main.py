r=-1;f=-1
CAHCE_SIZE=5

class LRU:
    def __init__(self,size):
        self.hit=0
        self.miss=0
        self.order=[]
        self.size=size
    
    def access(self,page):
        if page in self.order:
            self.hit+=1
            self.order.remove(page)
            self.order.append(page)
        else:
            self.miss+=1;
            if len(self.order)>=self.size:
                self.order.pop(0)
            self.order.append(page)
    
    def stats(self):
        sum=self.hit+self.miss
        if sum>0:
            return "Hits:",self.hit,"\n","Hit Rate:",self.hit/sum,"\n","Misses:",self.miss,"\n","Miss Rate:",self.miss/sum
        else:
            return 0

#testing
chinNIG=LRU(5)
list=[1,1]

for i in list:
    chinNIG.access(i)
    
def simulate_lru(cache_size, total_pages, pages_requested):

    lru_cache = LRU(cache_size)
    all_pages = [x for x in range(1,total_pages+1)]
    requested_sequence = [random.choice(all_pages) for _ in range(pages_requested)]

    print(f"\nSimulating LRU Cache with Size: {cache_size}, Total Pages: {total_pages}, Requests: {pages_requested}")
    for page in requested_sequence:
        lru_cache.access(page)
        print(f"Accessing page: {page}, Current Cache: {lru_cache.order}")

    return lru_cache.stats()

if __name__ == "__main__":
    import random

    cache_size = int(input("Enter Cache Size : "))
    total_available_pages = int(input("Enter Total Available Pages : "))
    number_of_requests = int(input("Enter Number Of Requests : "))

    simulation_results = simulate_lru(cache_size, total_available_pages, number_of_requests)

    print("\nSimulation Results:")
    print(f"Cache Size: {cache_size}")
    print(f"Total Requests: {number_of_requests}")
    print(f"Hits: {simulation_results['Hits']}")
    print(f"Hit Rate: {simulation_results['Hit Rate']:.4f}")
    print(f"Misses: {simulation_results['Misses']}")
    print(f"Miss Rate: {simulation_results['Miss Rate']:.4f}")

    analyze_different_sizes = False
    if analyze_different_sizes:
        cache_sizes_to_test = [5, 10, 15, 20]
        analysis_results = {}
        num_simulations = 5  # Run multiple times for each size to get an average

        print("\n--- Analyzing Hit/Miss Rates for Different Cache Sizes ---")
        for size in cache_sizes_to_test:
            total_hits = 0
            total_misses = 0
            for _ in range(num_simulations):
                results = simulate_lru(size, total_available_pages, number_of_requests)
                total_hits += results['Hits']
                total_misses += results['Misses']

            avg_hits = total_hits / num_simulations
            avg_misses = total_misses / num_simulations
            total_requests = avg_hits + avg_misses
            avg_hit_rate = avg_hits / total_requests if total_requests > 0 else 0
            avg_miss_rate = avg_misses / total_requests if total_requests > 0 else 0

            analysis_results[size] = {
                "avg_hits": avg_hits,
                "avg_hit_rate": avg_hit_rate,
                "avg_misses": avg_misses,
                "avg_miss_rate": avg_miss_rate
            }
            print(f"\nCache Size: {size} (Average over {num_simulations} simulations)")
            print(f"  Average Hits: {avg_hits:.2f}")
            print(f"  Average Hit Rate: {avg_hit_rate:.4f}")
            print(f"  Average Misses: {avg_misses:.2f}")
            print(f"  Average Miss Rate: {avg_miss_rate:.4f}")