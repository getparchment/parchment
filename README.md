# parchment

parchment is a simple static site generator written in Python

![parchment](http://ww2.sinaimg.cn/large/005BlYP6gw1ex5nm4d2a7j3074074q3e.jpg)
icon designed by [Mirella](http://mirella-gabriele.deviantart.com/), thanks for the work. 

Note: `parchment` now only support Python3.x

## install

#### download from pypi:

```
wget https://pypi.python.org/packages/source/p/parchment/parchment-0.1.0.tar.gz
tar -xvf parchment-0.1.0.tar.gz && cd parchment-0.1.0
python setup.py install
```

or

#### clone from repository
```
git clone https://github.com/gaotongfei/parchment.git
virtualenv -p python3 venv
source venv/bin/activate
python setup.py install
```

## quick start

```
parchment/
    src/
    content/
    public/
    templates/
    venv/
    config.yaml
    ...
```

run command **parchment_init**, this command will create two empty folders: `content` and `public`

open folder `content`

create a markdown file named `YYYY-MM-DD-title.md`, for example `2015-10-19-parchment is a simple static site generator.md`

edit it by using your favourite editor, then save it

run command **parchment_g** or **parchment_generate**, you will see your markdown files have been generated to html files in folder `public`

**Note: make sure run `parchment_g` or `parchment_generate` command in `parchment` directory**

then create a repository named `yourusername.github.io` on github

```
cd public
git init
git add .
git commit -m "first commit"
git remote add origin https://github.com/yourusername/yourusername.github.io.git
git push -u origin master
```

visit http://yourusername.github.io a few minutes later

