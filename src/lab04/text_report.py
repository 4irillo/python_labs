from pathlib import Path
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import io_text_csv
import libs.text

# added this comment through neovim
path = Path('/home/kirill/Desktop/451DegreeUkranian.txt')

txt = io_text_csv.read_text(path=path)
print(libs.text.summarize(txt))
# print(libs.text.count_freq(libs.text.tokenize(libs.text.normalize(txt))).items())
io_text_csv.write_csv(
    libs.text.count_freq(libs.text.tokenize(libs.text.normalize(txt))).items(),
    path='/home/kirill/Documents/vscode/python_labs/data/lab04/output.csv',
    header=[['Words', 'Amount']],
)
