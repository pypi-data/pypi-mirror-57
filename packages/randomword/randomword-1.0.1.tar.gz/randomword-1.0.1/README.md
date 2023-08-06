## RandomWord Description
`randomword` is a simple python library that chooses a random word from [dwyl's list of English words](https://github.com/dwyl/english-words).
Unlike other libraries, there is no API. This library can be used without internet access.

## Usage
```python
from randomword import randomword

random_word = randomword.get_random_word()
# importing randomword and then doing randomword.randomword.get_random_word() is also applicable.
print(f"My favorite word in the dictionary is {random_word}.")

multiple_random_words = randomword.get_random_word(2)
print(f"If I had to choose, I would say my top two favorite words are {multiple_random_words[0]} and {multiple_random_words[1]}.")
```
## Output
```python
My favorite word in the dictionary is unutilized.
If I had to choose, I would say my top two favorite words are barhopped and passionful.
```