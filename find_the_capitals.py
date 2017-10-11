def capitals(word):
    result = [i for i in len(word) if word[i].upper() == word[i]]
    return result


if __name__ == '__main__':
    print(capitals('WasdAvcAgfdD'))