def count_substring(string, substring):
    cnt = 0
    index = 0
    for item in range(len(string)):
        if string[item] == substring[0]:
            if (string[item : item + len(substring)] == substring):
                cnt += 1
    return cnt
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)