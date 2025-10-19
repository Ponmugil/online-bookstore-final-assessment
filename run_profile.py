import cProfile
import pstats
from io import StringIO
import time

# Simulate a typical user flow on the website
def simulate_user_flow():
    print("Starting user flow simulation...")
    time.sleep(0.2)  
    time.sleep(0.3)  
    time.sleep(0.4)  
    print("User flow completed.")

if __name__ == "__main__":
    print("Running cProfile for user flow...")

    pr = cProfile.Profile()
    pr.enable()              # start profiling
    simulate_user_flow()
    pr.disable()             # stop profiling

    s = StringIO()
    ps = pstats.Stats(pr, stream=s).sort_stats(pstats.SortKey.TIME)
    ps.print_stats()         # print profiling results
    print(s.getvalue())      # output to console

