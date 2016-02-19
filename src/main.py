import os
from jinja2 import Environment, FileSystemLoader
from .read_file import File
from .generate import GenerateMarkdown
from .read_config import ReadConfig
from .helpers import cp_folders, delete_file_folder, sorted_ls 
from datetime import datetime
from math import ceil

def main():
    base_path = os.path.dirname(os.path.abspath('__file__'))
    cfg = ReadConfig(os.path.join(base_path, 'config.yaml'))

    env = Environment(loader=FileSystemLoader('templates'))
    index_template = env.get_template(cfg._config['theme'] + '/index.html')
    post_template = env.get_template(cfg._config['theme'] + '/post.html')
    pagination_template = env.get_template(cfg._config['theme'] + '/pagination.html')

    # list_file: list all the file names in directory `content`
    list_file = sorted_ls(base_path + '/content')

    # info_list: used to store all the infomartion that contains config info and posts info
    posts_info_list = []

    delete_file_folder(base_path+"/public")

    # pagination
    pagination_list = []
    pagination_info = {}

    per_page = cfg._config['per_page']
    page = ceil(len(list_file) / per_page)
    for _ in range(1, page+1):
        pagination_info['page'] = _
        pagination_info['file'] = list_file[(_-1)*per_page:_*per_page]
        pagination_list.append(pagination_info.copy())

    print('generating')
    for file in list_file:
        # instance of File
        f = File(file)
        if not f.is_hidden_file():
            for _ in pagination_list:
                if file in _['file']:
                    p = _['page']

            file_info_list = ['page_'+str(p), f.year, f.month, f.day, f.title]
            full_path = base_path + "/public/" + "/".join(file_info_list)

            try:
                os.makedirs(full_path)
                os.mknod(full_path + '/index.html')
            except FileExistsError:
                delete_file_folder(full_path)
                os.makedirs(full_path)
                os.mknod(full_path + '/index.html')
                print('File exists')

            with open(base_path + '/content/' + file, 'r') as markdown_file:
                md_f = markdown_file.read()
                generate_markdown = GenerateMarkdown(md_f)

            posts_dict = {}
            posts_dict['file_name'] = file
            posts_dict['title'] = f.title
            posts_dict['body'] = generate_markdown.output
            posts_dict['src'] = os.path.join('page_'+str(p), f.year, f.month, f.day, f.title, 'index.html')
            post_datetime = datetime(int(f.year), int(f.month), int(f.day))
            posts_dict['time'] = post_datetime.strftime('%d %b %y')
            posts_info_list.append(posts_dict)


            keys_list = cfg.get_config_keys()
            for key in keys_list:
                cfg.key = cfg._config[key]

            output_post_template = post_template.render(post=posts_dict, _=cfg._config, )

            with open(full_path + '/index.html', 'w+') as output_post_file:
                output_post_file.write(output_post_template)

    print('done')

    # copy folders from parchment/templates/yourtheme/ to /parchment/public/
    cp_folders(os.path.join(base_path, 'templates', cfg._config['theme']), os.path.join(base_path, 'public'))

    index_page = []
    for index, pl in enumerate(pagination_list):
        pagination_posts_info_list = []
        for p in posts_info_list:
            if p['file_name'] in pl['file']:
                p['src'] = os.path.join(f.year, f.month, f.day, f.title, 'index.html')
                pagination_posts_info_list.append(p)
        if index == 0:
            index_page = pagination_posts_info_list
    
        pagination_index_template = pagination_template.render(posts=pagination_posts_info_list, _=cfg._config, pagination=pagination_list)
        with open(base_path + '/public/' + 'page_' + str(pl['page']) + '/index.html', 'w+') as pagination_index_file:
            pagination_index_file.write(pagination_index_template)

    output_index_template = index_template.render(posts=index_page, _=cfg._config, pagination=pagination_list)
    with open(base_path + '/public/' + 'index.html', 'w+') as output_index_file:
        output_index_file.write(output_index_template)
