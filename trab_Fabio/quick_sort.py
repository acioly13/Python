def particiona(v, ini, fim):

	pivo = ini

	for i in range(ini + 1, fim + 1):
		if v[i] <= v[ini]:
			pivo += 1
			v[i], v[pivo] = v[pivo], v[i]

	v[pivo], v[ini] = v[ini], v[pivo]

	return pivo


def quick_sort(v, ini, fim):

	if fim > ini:

		pivo = particiona(v, ini, fim)
		quick_sort(v, ini, pivo - 1)
		quick_sort(v, pivo + 1, fim)
