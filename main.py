import os

def dirs(nums):
    for i in range(60, nums):
        os.makedirs(f"Day{i}", exist_ok=True)

dirs(365)
