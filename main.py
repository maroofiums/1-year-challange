import os

def dirs(nums):
    for i in range(99, nums):
        os.makedirs(f"Day{i}", exist_ok=True)

dirs(365)
