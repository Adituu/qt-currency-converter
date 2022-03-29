import csv


def write_currencies(*args):
    if len(args) > 2:
        return None

    try:
        with open('./currencies.csv', 'a') as currencies_file:
            writer = csv.writer(currencies_file, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            writer.writerow([*args])
    except Exception as e:
        print(e)
        return None
    else:
        return True


if __name__ == '__main__':
    write_currencies('USD', 'USD')
