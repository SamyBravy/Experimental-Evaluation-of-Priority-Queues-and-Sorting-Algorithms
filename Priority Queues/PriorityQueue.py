import time
import random
import matplotlib.pyplot as plt

class MaxHeap:
	def __init__(self):
		self.heap = []
		self.size = 0

	def _parent(self, index):
		return (index - 1) // 2

	def _left(self, index):
		return 2 * index + 1
	
	def _right(self, index):
		return 2 * index + 2

	def _heapify(self, index):
		l = self._left(index)
		r = self._right(index)
		largest = index
		if l < self.size and self.heap[l] > self.heap[largest]:
			largest = l
		if r < self.size and self.heap[r] > self.heap[largest]:
			largest = r
		if largest != index:
			self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
			self._heapify(largest)

	# O(log n)
	def insert(self, key):
		self.heap.append(float('-inf'))
		self.size += 1
		self.increment_key(self.size - 1, key)

	# O(1)
	def maximum(self):
		if self.size == 0:
			raise Exception("Heap is empty")
		return self.heap[0]
	
	# O(log n)
	def extract_max(self):
		if self.size == 0:
			raise Exception("Heap is empty")
		max_value = self.heap[0]
		self.heap[0] = self.heap[self.size - 1]
		self.heap.pop()
		self.size -= 1
		if self.size > 0:
			self._heapify(0)
		return max_value
	
	# O(log n)
	def increment_key(self, index, key):
		if index < 0 or index >= self.size:
			raise Exception("Index out of bounds")
		if key < self.heap[index]:
			raise Exception("New key is smaller than current key")
		self.heap[index] = key
		while index > 0 and self.heap[self._parent(index)] < self.heap[index]:
			self.heap[index], self.heap[self._parent(index)] = self.heap[self._parent(index)], self.heap[index]
			index = self._parent(index)

	def get_value(self, index):
		if index < 0 or index >= self.size:
			raise Exception("Index out of bounds")
		return self.heap[index]

class Node:
	def __init__(self, value):
		self.value = value
		self.next = None

class UnsortedLinkedList:
	def __init__(self):
		self.head = None
		self.size = 0
	
	# O(1)
	def insert(self, value):
		new_node = Node(value)
		new_node.next = self.head
		self.head = new_node
		self.size += 1

	# O(n)
	def maximum(self):
		if self.head is None:
			raise Exception("List is empty")
		max_value = self.head.value
		current = self.head.next
		while current is not None:
			if current.value > max_value:
				max_value = current.value
			current = current.next
		return max_value

	# O(n)
	def extract_max(self):
		if self.head is None:
			raise Exception("List is empty")
		max_node = self.head
		prev_max = None
		current = self.head
		prev = None
		while current is not None:
			if current.value > max_node.value:
				max_node = current
				prev_max = prev
			prev = current
			current = current.next
		max_value = max_node.value
		if prev_max is None:
			self.head = max_node.next
		else:
			prev_max.next = max_node.next
		self.size -= 1
		return max_value

	def _get_node_at(self, index):
		if index < 0 or index >= self.size:
			raise Exception("Index out of bounds")
		current = self.head
		for _ in range(index):
			current = current.next
		return current
	
	# O(n)
	def increment_key(self, index, key):
		node_to_update = self._get_node_at(index)
		if key < node_to_update.value:
			raise Exception("New key is smaller than current key")
		node_to_update.value = key

	def get_value(self, index):
		return self._get_node_at(index).value

class SortedLinkedList:
	def __init__(self):
		self.head = None
		self.size = 0

	# O(n)
	def insert(self, value):
		new_node = Node(value)
		self.size += 1
		if self.head is None or self.head.value < value:
			new_node.next = self.head
			self.head = new_node
		else:
			current = self.head
			while current.next is not None and current.next.value >= value:
				current = current.next
			new_node.next = current.next
			current.next = new_node

	# O(1)
	def maximum(self):
		if self.head is None:
			raise Exception("List is empty")
		return self.head.value

	# O(1)
	def extract_max(self):
		if self.head is None:
			raise Exception("List is empty")
		max_value = self.head.value
		self.head = self.head.next
		self.size -= 1
		return max_value
	
	# O(n)
	def increment_key(self, index, key):
		if index < 0 or index >= self.size:
			raise Exception("Index out of bounds")
		current = self.head
		prev = None
		for _ in range(index):
			prev = current
			current = current.next
		if key < current.value:
			raise Exception("New key is smaller than current key")
		if prev is None:
			self.head = current.next
		else:
			prev.next = current.next
		self.size -= 1
		self.insert(key)
	
	def get_value(self, index):
		if index < 0 or index >= self.size:
			raise Exception("Index out of bounds")
		current = self.head
		for _ in range(index):
			current = current.next
		return current.value

def benchmark_structure(structure_class, size):
	data = random.sample(range(size * 10), size)
	structure = structure_class()
	for x in data:
		structure.insert(x)

	new_value = random.randint(0, size * 10)
	t0 = time.perf_counter()
	structure.insert(new_value)
	insert_time = time.perf_counter() - t0
	structure.extract_max()

	t1 = time.perf_counter()
	_ = structure.maximum()
	max_time = time.perf_counter() - t1

	t2 = time.perf_counter()
	extracted = structure.extract_max()
	extract_time = time.perf_counter() - t2
	structure.insert(extracted)

	idx_to_inc = random.randint(0, size - 1)
	old_value = structure.get_value(idx_to_inc)
	new_key = old_value + random.randint(1, 100)
	t3 = time.perf_counter()
	structure.increment_key(idx_to_inc, new_key)
	increment_time = time.perf_counter() - t3

	return insert_time, max_time, extract_time, increment_time

def run_benchmarks(sizes, trials):
	structures = {
		"Max Heap": MaxHeap,
		"Unsorted List": UnsortedLinkedList,
		"Sorted List": SortedLinkedList
	}
	
	# results[operation][structure] = [list of average times]
	results = {
		"insert": {name: [] for name in structures},
		"maximum": {name: [] for name in structures},
		"extract": {name: [] for name in structures},
		"increment": {name: [] for name in structures},
	}

	for size in sizes:
		print(f"\n--- Benchmarking for size: {size} (trials: {trials}) ---")
		
		# avg_times[structure] = [insert_avg, max_avg, ...]
		avg_times = {name: [0.0] * 4 for name in structures}

		for name, struct_class in structures.items():
			print(f"Testing {name}...")
			total_times = [0.0] * 4
			for i in range(trials):
				times = benchmark_structure(struct_class, size)
				for j in range(4):
					total_times[j] += times[j]
			
			avg_times[name] = [t / trials for t in total_times]

		for name in structures:
			results["insert"][name].append(avg_times[name][0])
			results["maximum"][name].append(avg_times[name][1])
			results["extract"][name].append(avg_times[name][2])
			results["increment"][name].append(avg_times[name][3])
	
	return results

def plot_results(results, sizes):
	operations = {
		"insert": "Insert",
		"maximum": "Maximum",
		"extract": "Extract Max",
		"increment": "Increment Key"
	}
	
	print("\nGenerating plots...")
	
	for op_key, op_title in operations.items():
		plt.figure(figsize=(10, 6))
		for struct_name, times in results[op_key].items():
			plt.plot(sizes, times, marker='o', linestyle='-', label=struct_name)
		
		plt.xlabel("Structure size (N)")
		plt.ylabel("Average time (seconds)")
		plt.title(f"Performance: {op_title}")
		plt.legend()
		plt.grid(True)
		plt.yscale('log')
		plt.xscale('log')
		plt.savefig(f"benchmark_{op_key}.png")
		
	plt.show()

def print_latex_tables(results, sizes):
	operations = {
		"insert": "Insert",
		"maximum": "Maximum",
		"extract": "Extract Max",
		"increment": "Increment Key"
	}
	struct_names = list(results["insert"].keys())

	print("\n\n--- LATEX TABLES ---")
	for op_key, op_title in operations.items():
		print(f"\n% Table for: {op_title}")
		print("\\begin{table}[H]")
		print("    \\centering")
		print("    \\sisetup{scientific-notation=true, round-mode=places, round-precision=2}")
		print(f"    \\caption{{Average times (s) for the \\texttt{{{op_key}}} operation.}}")
		print(f"    \\label{{tab:{op_key}}}")
		print("    \\begin{tabular}{r" + "S" * len(struct_names) + "}")
		print("        \\toprule")
		header = "        \\textbf{Size (N)}"
		for name in struct_names:
			header += f" & {{\\textbf{{{name}}}}}"
		print(header + " \\\\")
		print("        \\midrule")

		for i, size in enumerate(sizes):
			row = f"        {size}"
			for name in struct_names:
				row += f" & {results[op_key][name][i]:.2e}" 
			print(row + " \\\\")
		
		print("        \\bottomrule")
		print("    \\end{tabular}")
		print("\\end{table}")

if __name__ == "__main__":
	sizes = [10, 50, 100, 500, 1000, 2500, 5000, 10000]
	trials = 30

	results = run_benchmarks(sizes, trials)
	
	# print_latex_tables(results, sizes)
	
	plot_results(results, sizes)
