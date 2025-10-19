import timeit
import time

def load_homepage():
    time.sleep(0.2)  
    return "Homepage Loaded"

def search_product():
    time.sleep(0.35)  
    return "Search Completed"

def checkout_process():
    time.sleep(0.5)  
    return "Checkout Completed"

if __name__ == "__main__":
    print("Performance Profiling with timeit\n")

    # Measure execution time for 10 runs
    homepage_time = timeit.timeit(load_homepage, number=10)
    search_time = timeit.timeit(search_product, number=10)
    checkout_time = timeit.timeit(checkout_process, number=10)

    # Print average time per run
    print(f"Homepage Load (avg over 10 runs): {homepage_time/10:.4f} sec")
    print(f"Product Search (avg over 10 runs): {search_time/10:.4f} sec")
    print(f"Checkout Process (avg over 10 runs): {checkout_time/10:.4f} sec")
