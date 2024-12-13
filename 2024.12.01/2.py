import urllib.request
import re
import json
import os

def html_to_json(Url, Pattern, Decode = "UTF-8", json_file='extracted_data.json'):
    try:
        with urllib.request.urlopen(Url) as response:
            data = response.read()
            content = data.decode(Decode)
                
        matches = re.findall(Pattern, content)
        
        with open(json_file, "w", encoding="UTF-8") as f:
            json.dump(matches, f, ensure_ascii=False, indent=4)
        
        return os.path.abspath(json_file)
    except Exception as e:
        print(f"Ошибка при получении данных: {e}")
        return None

# >>> url = 'https://docs.python.org/3/py-modindex.html'
# >>> pattern = r'<tr>\s*<td>\s*</td>\s*<td>\s*<a href="[^"]*"><code class="xref">([^<]+)</code></a>\s*</td>\s*<td>\s*<em\>(.*?)</em>\s*</td>\s*</tr>'
# >>> file_path = html_to_json(url, pattern)
# >>> with open(file_path, 'r', encoding='utf-8') as f:
# ...     data = json.load(f)
# ...
# >>> for item in data[:5]:
# ...     print(item)
# ...
# ['__future__', 'Future statement definitions']
# ['_thread', 'Low-level threading API.']
# ['_tkinter', 'A binary module that contains the low-level interface to Tcl/Tk.']
# ['abc', 'Abstract base classes according to :pep:`3119`.']
# ['argparse', 'Command-line option and argument parsing library.']