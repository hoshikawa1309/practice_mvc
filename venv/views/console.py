def get_template(template_path):
    with open(template_path ,'r', encoding = 'utf-8') as template_file:
        return template_file.read()