def selection_sort(v):

	len_v = len(v)

	for i in range(len_v):
		menor = i
		for j in range(i + 1, len_v):
			if v[j] < v[menor]:
				menor = j
		v[menor], v[i] = v[i], v[menor]
