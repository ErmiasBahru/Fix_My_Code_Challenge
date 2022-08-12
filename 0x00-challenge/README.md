# 0x00-challenge

[0-fizzbuzz](./0-fizzbuzz.py)

```python

# only update this

if (i % 3) == 0:
    tmp_result.append("Fizz")
elif (i % 3) == 0 and (i % 5) == 0:
    tmp_result.append("FizzBuzz")

```

```python

# to this

if (i % 3) == 0 and (i % 5) == 0:
    tmp_result.append("FizzBuzz")
elif (i % 3) == 0:
    tmp_result.append("Fizz")

```

[1-print_square](./1-print_square.js)

```js
// update this

size = parseInt(process.argv[2], 16)

// to

size = parseInt(process.argv[2], 10)

```

[2-sort](./2-sort.rb)

```ruby
# update this

result.insert(i - 1, i_arg)

# to

result.insert(i, i_arg)
```

that's it!
