# Numerical_Analysis
为正常生成参考文献，一定要用biber命令运行，需要在编译文档的主目录下包含这四个文件gb7714-2015.bbx, gb7714-2015ay.bbx, gb7714-2015.cbx, gb7714-2015ay.cbx。  
运行代码顺序必须为
```
xelatex document.tex
biber document
xelatex document.tex
xelatex document.tex
```
关于参考文献问题，可查看[这里](https://github.com/hushidong/biblatex-gb7714-2015#jumptotutorial)。
