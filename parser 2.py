from tika import parser
import collections
import glob

def read_pdf(file_path):
    file_data = parser.from_file(file_path)
    text = file_data["content"]
    return text

def counter(text,top_num = None):
    splite_text = text.split()
    count_text = collections.Counter(splite_text).most_common(top_num)
    return count_text

def save_data(save_data,filename):
    if type(save_data) is not str:
        save_data = str(save_data)
        print("convert string")
    with open(filename + ".txt","w") as f:
        f.write(save_data)

# カウント
# file_path = "/Users/yukihirakawa/Desktop/django/pdftext/english_table.pdf"
# splite_text = readpdf(file_path)
# count_text = counter(splite_text)
# save_data(count_text)

#生テキスト
# file_path = "/Users/yukihirakawa/Desktop/django/pdftext/jp_sample.pdf"
# text = read_pdf(file_path)
# save_data(text)

file_path = "/Users/yukihirakawa/Desktop/django/pdftext/jp_sample.pdf"
text = read_pdf(file_path)
count_text = counter(text)
save_data(count_text)