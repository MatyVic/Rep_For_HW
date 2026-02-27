# ДЗ 12.1. Очистити текст від html-тегів
import re


def delete_html_tags(html_file, result_file='cleaned.txt'):
      with open(html_file, 'r') as file:
          html = file.read()
          text = ''
          for line in html.splitlines():
               start = line.find(">") + 1
               end = line.find("</")
               if start > 0 and end > start:
                    text += line[start:end].strip() + '\n'

          result_file = open(result_file, 'w').write(text)

delete_html_tags('html_file.html')