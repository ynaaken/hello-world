import re

emails = []
email_pattern = "\w*@\w*(.)\w*"
input_file = "e-mails.txt"


def main():
    writefile("new.txt", openfile(input_file))
    print(emails)


def openfile(file):
    with open(file, 'r') as f:
        for line in f.readlines():
            try:
                emails.append(re.match(email_pattern, line).group(0)+'\n')
            except AttributeError:
                pass
    return emails


def writefile(file, emails):
    with open(file, 'w') as f:
        for i in range(len(emails)):
            f.write(emails[i])


if __name__ == '__main__':
    main()
