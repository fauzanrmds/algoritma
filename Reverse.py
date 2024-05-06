def reverse(alphabet):
  result = ""
  for char in alphabet:
    if char.isalpha():
      result = char + result
    else:
      result += char
  return result

alphabet = "NEGIE1"
reverse_alphabet = reverse(alphabet)
print(reverse_alphabet)
