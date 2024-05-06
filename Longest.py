def longest(sentence):
  words = sentence.split()
  longest = max(words, key=len)
  return longest

sentence = "Saya sangat senang mengerjakan soal algoritma"
longest = longest(sentence)
print(f"Kata terpanjang: {longest} {len(longest)} character")
