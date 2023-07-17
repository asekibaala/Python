import difflib
import sys
def compare_files(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        lines1 = f1.readlines()
        lines2 = f2.readlines()
    diff = difflib.unified_diff(lines1, lines2)
     # Print differences on the screen
    for line in diff:
        print(line)
     # Save differences to a text file
    with open('differences.txt', 'w') as diff_file:
        diff_file.writelines(diff)
if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python compare_java_files.py <file1> <file2>")
        sys.exit(1)
    file1 = sys.argv[1]
    file2 = sys.argv[2]
    compare_files(file1, file2)