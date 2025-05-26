def comma_code(items):
    if not items:
        return ''
    elif len(items) == 1:
        return str(items[0])
    else:
        # Join all but last item with commas, then add 'and' + last item
        return ', '.join(map(str, items[:-1])) + ' and ' + str(items[-1])

# Example usage:
my_list = ['apples', 'bananas', 'tofu', 'cats']
print(comma_code(my_list))
