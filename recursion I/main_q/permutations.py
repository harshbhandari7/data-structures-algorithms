arr = [1, 0]
permutations = []
freq = {}

def get_permutations(seq, arr, freq):
    if len(seq) == len(arr):
        temp = seq.copy()
        permutations.append(temp)
        return

    for i in range(len(arr)):
        if not(i in freq and freq[i]):
            freq[i] = True
            seq.append(arr[i])
            get_permutations(seq, arr, freq)
            seq.remove(seq[len(seq) - 1])
            freq[i] = False

get_permutations([], arr, freq)
print(permutations)