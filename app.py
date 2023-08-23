# list=[1,2,3]
# # print(list[4:0])

# def tw(x):
#     return x+x


# print(map(tw,list))
def list_to_string(list1):
  """
  This function takes a list as input and returns a string
  where the elements of the list are separated by '#'.

  Args:
    list1: A list of strings or numbers.

  Returns:
    A string where the elements of the list are separated by '#'.
  """

  string = ""
  for element in list1:
    if isinstance(element, str):
      string += element + "#"
    elif isinstance(element, int):
      string += str(element) + "#"
    else:
      raise TypeError("The elements of the list must be strings or numbers.")

  return string[:-1]


def count_numbers(list1):

  count = 0
  for element in list1:
    if isinstance(element, int):
      count += element

  return count

list1 = ["hello", 4, "i", 3]
string = list_to_string(list1)
count = count_numbers(list1)
print(f"The string is {string}")
print(f"The number of numbers in the list is {count}")