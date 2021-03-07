import re

BOLD_RE = re.compile(r"__(.*?)__")
ITALICS_RE = re.compile(r"_(.*?)_")
HEADER_RE = re.compile(r"(#+) (.*)")
LIST_RE = re.compile(r"\* (.*)")

def parse(markdown):
    
    result = []
    for line in markdown.split('\n'):
        line = BOLD_RE.sub(r'<strong>\1</strong>', line)
        line = ITALICS_RE.sub(r'<em>\1</em>', line)
        
        is_header = HEADER_RE.match(line)
        is_list = LIST_RE.match(line)
        
        if is_header:
            result.append('<h{0}>{1}</h{0}>'.format(len(is_header.group(1)), is_header.group(2)))

        elif is_list:
            #we may be appending
            if result and result[-1] == '</ul>':
                result.pop()
            #or starting a new one
            else:
                result.append("<ul>")
            result.extend(["<li>" + is_list.group(1) + "</li>", "</ul>"])
        # everything else is a paragraph
        else:
            result.append("<p>" + line + "</p>")
    return "".join(result)
            

"""def parse(markdown):
    lines = markdown.split('\n')
    res = ''
    in_list = False
    in_list_append = False
    
    
    for i in lines:        if re.match('###### (.*)', i):
            i = '<h6>' + i[7:] + '</h6>'
            
        elif re.match('## (.*)', i):
            i = '<h2>' + i[3:] + '</h2>'
            
        elif re.match('# (.*)', i):
            i = '<h1>' + i[2:] + '</h1>'
            
        if re.match(r'\* (.*)', i):
            
            m = re.match(r'\* (.*)', i)
            curr = m.group(1)
            m1 = re.match('(.*)__(.*)__(.*)', curr)
            
            if m1:
                curr = m1.group(1) + '<strong>' + m1.group(2) + '</strong>' + m1.group(3)
            
            m1 = re.match('(.*)_(.*)_(.*)', curr)
            
            if m1:
                curr = m1.group(1) + '<em>' + m1.group(2) + '</em>' + m1.group(3)
            
            if not in_list:
                in_list = True
                i = '<ul><li>' + curr + '</li>'
                
            else:                    
                i = '<li>' + curr + '</li>'
                
        else:
            if in_list:
                in_list_append = True
                in_list = False

        m = re.match('<h|<ul|<p|<li', i)
        if not m:
            #If no <> match was found, it's a paragraph!
            i = '<p>' + i + '</p>'
        m = re.match('(.*)__(.*)__(.*)', i)
        if m:
            i = m.group(1) + '<strong>' + m.group(2) + '</strong>' + m.group(3)
        m = re.match('(.*)_(.*)_(.*)', i)
        if m:
            i = m.group(1) + '<em>' + m.group(2) + '</em>' + m.group(3)
        if in_list_append:
            i = '</ul>' + i
            in_list_append = False
        res += i
    if in_list:
        res += '</ul>'
    return res"""