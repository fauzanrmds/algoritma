def count_query(input_array, query_array):
  result = []
  for query_word in query_array:
    count = input_array.count(query_word)
    result.append(count)
  return result

INPUT = ['xc', 'dz', 'bbb', 'dz']
QUERY = ['bbb', 'ac', 'dz']

occurrences = count_query(INPUT, QUERY)
print(f"Kemunculan kata: {occurrences}") 
