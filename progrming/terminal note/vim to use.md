

## vim note basic

  #### 開檔案清單 (terminal) 
```bash
vim .
```
  #### 分頁指令:
  ```bash
  :tabe {file name}
  :tabe.
  g t #next
  g T #previos
  
  ```

#### 光標

```bash
hjkl
G #end
gg #home
control d #halfpgup
control u #halfpgdown
control f #pgdown
control b #pgup
control e #next line
control y #prev line
zz zt zb  #file mid home end
H L # screen home end
: {line} {line}G #go to [line]
/{word} #find(word) n N switch 
$ 0  #line home end
w e b # next word 1 end # prev word1
W E B # space switch
f t F T # find word
ex : 6fa # next a
; #find again
```

#### inser mode

``` bash
i I#insert     #line home
a A#append     #line end append
o O#nextline   #prev line
s #replace char choosen
c {situate} #change
c w #word
c \$ C #cursor to end replace
c f" # cursor to first "
esc Control[
```

basic

```bash
x X#delete char    #prev char
r{word} R # replace word #replace insert mode
dd # cut
de #delete a word
y$ #paste end
yt" #拷貝到引號前
yy #copy
p P #paste prevline paste
. #repeat
u U#undo 
control r #redo
control a #遞增
control x #遞減
v i w #theword
v a w #the word with ""
v 2 i () #第二層小括號範圍
v i t # tag
V #line
>> 縮排
```

register

```
"q 3yy #copy
Qyy #apend to q
mq #mark sit to q
`q #定位
mQ #跨檔案標記
`` #prev sit

```

聚集

```
q{any key}q
qq #錄製到q
qq0"{esc}A",{esc}0jq
q{}q #錄製
＠q #執行
＠20q
Q ＃追加錄製
```

command

```
s/{old}/{new}/g
#可搭配Ｖ選取範圍
：r file.txt
:6t. ＃複製第六行至此
:6,8t. #複製地678行
:{lineNo}m # 某行移至此
:6,8m.
set path : {}
find **/md.md
```

