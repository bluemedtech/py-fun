import time
import numpy as np

def calculate_performance_score():
    # Function to calculate CPU score
    def calculate_cpu_score():
        start_time = time.time()
        # Perform a computationally intensive task (e.g., finding prime numbers)
        primes = []
        for num in range(2, 100000):
            is_prime = True
            for i in range(2, int(np.sqrt(num)) + 1):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(num)
        end_time = time.time()
        cpu_time = end_time - start_time
        # Score is inversely proportional to time taken
        cpu_score = 1000 / cpu_time  # Adjust scaling factor as needed
        return cpu_score, cpu_time

    # Function to calculate memory score
    def calculate_memory_score():
        start_time = time.time()
        # Perform a memory-intensive task (e.g., creating and manipulating a large array)
        array_size = 10**7  # 10 million elements
        large_array = np.random.rand(array_size)
        large_array *= 2  # Perform some operation
        end_time = time.time()
        memory_time = end_time - start_time
        # Score is inversely proportional to time taken
        memory_score = 1000 / memory_time  # Adjust scaling factor as needed
        return memory_score, memory_time

    # Function to calculate disk score
    def calculate_disk_score():
        start_time = time.time()
        # Perform a disk-intensive task (e.g., writing and reading a large file)
        file_size = 10**7  # 10 million bytes (~10 MB)
        test_data = np.random.bytes(file_size)
        with open("test_file.bin", "wb") as f:
            f.write(test_data)
        with open("test_file.bin", "rb") as f:
            _ = f.read()
        end_time = time.time()
        disk_time = end_time - start_time
        # Score is inversely proportional to time taken
        disk_score = 1000 / disk_time  # Adjust scaling factor as needed
        return disk_score, disk_time

    # Calculate scores
    cpu_score, cpu_time = calculate_cpu_score()
    memory_score, memory_time = calculate_memory_score()
    disk_score, disk_time = calculate_disk_score()

    # Overall performance score (average of the three scores)
    overall_score = (cpu_score + memory_score + disk_score) / 3

    # Print results
    print(f"CPU Score: {cpu_score:.2f} (Time: {cpu_time:.2f} seconds)")
    print(f"Memory Score: {memory_score:.2f} (Time: {memory_time:.2f} seconds)")
    print(f"Disk Score: {disk_score:.2f} (Time: {disk_time:.2f} seconds)")
    print(f"Overall Performance Score: {overall_score:.2f}")

# Run the function
calculate_performance_score()