# parchment

parchment is a simple static site generator written in Python

![parchment](http://ww2.sinaimg.cn/large/005BlYP6gw1ex5nm4d2a7j3074074q3e.jpg)

icon designed by [Mirella](http://mirella-gabriele.deviantart.com/), thanks for the work. 

Note: `parchment` now only support Python3.x and Linux

## install

#### clone from repository
```
git clone https://github.com/gaotongfei/parchment.git
cd parchment/
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

run command **parchment init**, this command will create two empty folders: `content` and `public`

open folder `content`

create a markdown file named `YYYY-MM-DD-title.md`, for example `2015-10-19-parchment is a simple static site generator.md`

edit it and then make a little change in the config file `config.yaml`

run command **parchment generate**, you will see your markdown files have been generated to html files in folder `public`

**Note: make sure run `parchment generate` command in `parchment` directory**

then create a repository named `yourusername.github.io` on github

```
cd public
git init
git add .
git commit -m "first commit"
git remote add origin https://github.com/yourusername/yourusername.github.io.git # Change `yourusername` with your username
git push -u origin master
```

visit http://yourusername.github.io a few minutes later

## FAQ

Q: How to solve `error: Setup script exited with error: command 'x86_64-linux-gnu-gcc' failed with exit status 1`?
A: run `sudo apt-get install python3-dev` on Debian/Ubuntu, if still get that error see <a href="http://stackoverflow.com/a/30279877/4144064">stackoverflow</a>.
