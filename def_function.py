def is_positive(number):
  if number > 0:    # concept of branching
    return True
  else:
    return None


def is_even(number):
    if number % 2 == 0:
        return True     # 若这一行为真，下一行就不会被执行了
    return False      # 这一行只有在上一行不能执行的时候被执行

def number_group(number):
  if number > 0:
    return "Positive"
  elif number == 0:  # elif只有在if为否的时候被执行
    return "Zero"
  else:
    return "Negative"

def greeting(name):
  if name == "Taylor":
    return "Welcome back Taylor!"
  else:
    return "Hello there, " + name

print(greeting("Taylor"))
print(greeting("John"))


def calculate_storage(filesize):
    block_size = 4096
    full_blocks = filesize // block_size
    partial_block_remainder = filesize % block_size
    if full_blocks == 0 and partial_block_remainder > 0:
      return block_size
    elif partial_block_remainder == 0:
      return full_blocks * block_size
    elif full_blocks >= 1:
      return full_blocks * block_size + block_size


print(calculate_storage(1))    # Should be 4096
print(calculate_storage(4096)) # Should be 4096
print(calculate_storage(4097)) # Should be 8192
print(calculate_storage(6000)) # Should be 8192


def calculate_storage(filesize):
    block_size = 4096
    full_blocks = filesize // block_size
    partial_block_remainder = filesize % block_size
    if partial_block_remainder == 0:
        return filesize
    else:
        return (full_blocks + 1) * block_size

def format_name(first_name, last_name):
  if last_name != "" and first_name != "": # 先考虑的情况先执行，逻辑是有在先，没有在后
    return "Name: " + last_name + ", " + first_name
  elif last_name != "" or first_name != "":
    return "Name: " + last_name + first_name
  else:
    return ""

print(format_name("Ernest", "Hemingway"))
# Should return the string "Name: Hemingway, Ernest"

print(format_name("", "Madonna"))
# Should return the string "Name: Madonna"

print(format_name("Voltaire", ""))
# Should return the string "Name: Voltaire"

print(format_name("", ""))
# Should return an empty string

def fractional_part(numerator, denominator):
    if denominator == 0 or numerator == 0 or numerator == denominator:
      return 0  #把例外的情况先列出来
    elif denominator != 0:
      x = float(numerator / denominator) - int(numerator / denominator)
      return x

print(fractional_part(5, 5)) # Should be 0
print(fractional_part(5, 4)) # Should be 0.25
print(fractional_part(5, 3)) # Should be 0.66...
print(fractional_part(5, 2)) # Should be 0.5
print(fractional_part(5, 0)) # Should be 0
print(fractional_part(0, 5)) # Should be 0
