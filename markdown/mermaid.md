- https://support.typora.io/

# Draw Diagrams With Markdown

August 15, 2016 by typora.io

- Sequence Diagrams
  - [Sequence Diagrams Options](https://support.typora.io/Draw-Diagrams-With-Markdown/#sequence-diagrams-options)
- [Flowcharts](https://support.typora.io/Draw-Diagrams-With-Markdown/#flowcharts)
- Mermaid
  - [Sequence Diagrams](https://support.typora.io/Draw-Diagrams-With-Markdown/#sequence-diagrams-1)
  - [Flowcharts](https://support.typora.io/Draw-Diagrams-With-Markdown/#flowcharts-1)
  - [Gantt Charts](https://support.typora.io/Draw-Diagrams-With-Markdown/#gantt-charts)
  - [Class Diagrams](https://support.typora.io/Draw-Diagrams-With-Markdown/#class-diagrams)
  - [State Diagrams](https://support.typora.io/Draw-Diagrams-With-Markdown/#state-diagrams)
  - [Pie Charts](https://support.typora.io/Draw-Diagrams-With-Markdown/#pie-charts)
  - Mermaid Options
    - [Overview](https://support.typora.io/Draw-Diagrams-With-Markdown/#overview)
    - [Mermaid Theme](https://support.typora.io/Draw-Diagrams-With-Markdown/#mermaid-theme)
    - [Auto Numbering](https://support.typora.io/Draw-Diagrams-With-Markdown/#auto-numbering)
    - [Flowchart Curve](https://support.typora.io/Draw-Diagrams-With-Markdown/#flowchart-curve)
    - [Gantt Padding](https://support.typora.io/Draw-Diagrams-With-Markdown/#gantt-padding)

Typora supports some Markdown extensions for diagrams, once they are enabled from preference panel.

When exporting as HTML, PDF, epub, docx, those rendered diagrams will also be included, but diagrams features are not supported when exporting markdown into other file formats in current version. Besides, you should also notice that diagrams is not supported by standard Markdown, CommonMark or GFM. Therefore, we still recommend you to insert an image of these diagrams instead of write them in Markdown directly.

# Sequence Diagrams

This feature uses [js-sequence](https://bramp.github.io/js-sequence-diagrams/), which turns the following code block into a rendered diagram:

```sequence
Alice->Bob: Hello Bob, how are you?
Note right of Bob: Bob thinks
Bob-->Alice: I am good thanks!
```


For more details, please see [this syntax explanation](https://bramp.github.io/js-sequence-diagrams/#syntax).

### Sequence Diagrams Options

You could change CSS variable `--sequence-theme` to set theme for sequence diagrams, supported value are `simple` (default) and `hand`. For example, add following CSS in [Custom CSS](https://support.typora.io/Add-Custom-CSS/), and you will get:


# Flowcharts

This feature uses [flowchart.js](http://flowchart.js.org/), which turns the following code block into a rendered diagram:

```flow
st=>start: Start
op=>operation: Your Operation
cond=>condition: Yes or No?
e=>end

st->op->cond
cond(yes)->e
cond(no)->op
```

# Mermaid

Typora also has integration with [mermaid](https://mermaid-js.github.io/mermaid/#/), which supports sequence diagrams, flowcharts, Gantt charts, class and state diagrams, and pie charts.

## Sequence Diagrams

For more details see [these instructions](https://mermaid-js.github.io/mermaid/#/sequenceDiagram).

~~~mermaid
%% Example of sequence diagram
  sequenceDiagram
    Alice->>Bob: Hello Bob, how are you?
    alt is sick
    Bob->>Alice: Not so good :(
    else is well
    Bob->>Alice: Feeling fresh like a daisy
    end
    opt Extra response
    Bob->>Alice: Thanks for asking
    end
~~~



## Flowcharts

For more details see [these instructions](https://mermaid-js.github.io/mermaid/#/flowchart).

```mermaid
graph LR
A[Hard edge] -->B(Round edge)
    B --> C{Decision}
    C -->|One| D[Result one]
    C -->|Two| E[Result two]
```

## Gantt Charts

For more details see [these instructions](https://mermaid-js.github.io/mermaid/#gantt).

```mermaid
%% Example with selection of syntaxes
        gantt
        dateFormat  YYYY-MM-DD
        title Adding GANTT diagram functionality to mermaid

        section A section
        Completed task            :done,    des1, 2014-01-06,2014-01-08
        Active task               :active,  des2, 2014-01-09, 3d
        Future task               :         des3, after des2, 5d
        Future task2               :         des4, after des3, 5d

        section Critical tasks
        Completed task in the critical line :crit, done, 2014-01-06,24h
        Implement parser and jison          :crit, done, after des1, 2d
        Create tests for parser             :crit, active, 3d
        Future task in critical line        :crit, 5d
        Create tests for renderer           :2d
        Add to mermaid                      :1d

        section Documentation
        Describe gantt syntax               :active, a1, after des1, 3d
        Add gantt diagram to demo page      :after a1  , 20h
        Add another diagram to demo page    :doc1, after a1  , 48h

        section Last section
        Describe gantt syntax               :after doc1, 3d
        Add gantt diagram to demo page      : 20h
        Add another diagram to demo page    : 48h
```

## Class Diagrams

For more details see [these instructions](https://mermaid-js.github.io/mermaid/#/classDiagram).

```mermaid
classDiagram
      Animal <|-- Duck
      Animal <|-- Fish
      Animal <|-- Zebra
      Animal : +int age
      Animal : +String gender
      Animal: +isMammal()
      Animal: +mate()
      class Duck{
          +String beakColor
          +swim()
          +quack()
      }
      class Fish{
          -int sizeInFeet
          -canEat()
      }
      class Zebra{
          +bool is_wild
          +run()
      }
```

![class-diagram](https://support.typora.io/media/new-80/class-diagram.png)

## State Diagrams

For more details see [these instructions](https://mermaidjs.github.io/#/stateDiagram).

```mermaid
stateDiagram
    [*] --> Still
    Still --> [*]

    Still --> Moving
    Moving --> Still
    Moving --> Crash
    Crash --> [*]
```

## Pie Charts

```mermaid
pie
    title Pie Chart
    "Dogs" : 386
    "Cats" : 85
    "Rats" : 150 
```


## Mermaid Options

### Overview

You can change Mermaid options by adding [Custom CSS](https://support.typora.io/Add-Custom-CSS/), supported options include:

```
:root {
  --mermaid-theme: default; /*or base, dark, forest, neutral, night */
  --mermaid-font-family: "trebuchet ms", verdana, arial, sans-serif;
  --mermaid-sequence-numbers: off; /* or "on", see https://mermaid-js.github.io/mermaid/#/sequenceDiagram?id=sequencenumbers*/
  --mermaid-flowchart-curve: linear /* or "basis", see https://github.com/typora/typora-issues/issues/1632*/;
  --mermaid--gantt-left-padding: 75; /* see https://github.com/typora/typora-issues/issues/1665*/
}
```

Please note that if you export document with other themes than currently used one, some mermaid options will not be applied to exported HTML / PDF / Image. For example, if you currently use them Github, but while export to PDF, you set theme YYY for PDF export, and YYY.css defines `--mermaid-sequence-numbers: on`, then the `--mermaid-sequence-numbers: on` would not be applied to exported PDF.

### Mermaid Theme

Added `--mermaid-theme` css variable to quickly define a mermaid theme that fits your theme, the value can be `base`, `default`, `dark`, `forest`, `neutral`, `night` (the one used in night theme), for example:

| CSS                                | Mermaid Demo                                                 |
| ---------------------------------- | ------------------------------------------------------------ |
| `:root {--mermaid-theme:dark;}`    | ![Screen Shot 2020-12-05 at 17.08.46](https://support.typora.io/media/new-97/Screen%20Shot%202020-12-05%20at%2017.08.46.png) |
| `:root {--mermaid-theme:forest;}`  | ![Screen Shot 2020-12-05 at 17.09.42](https://support.typora.io/media/new-97/Screen%20Shot%202020-12-05%20at%2017.09.42.png) |
| `:root {--mermaid-theme:neutral;}` | ![Screen Shot 2020-12-05 at 17.10.11](https://support.typora.io/media/new-97/Screen%20Shot%202020-12-05%20at%2017.10.11.png) |

### Auto Numbering

Add `--mermaid-sequence-numbers: on;` in [Custom CSS](https://support.typora.io/Add-Custom-CSS/) will enable auto numbering for sequence in mermaid:

| –mermaid-sequence-numbers:off                                | –mermaid-sequence-numbers:on                                 |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| ![Screen Shot 2021-04-05 at 23.08.37](https://support.typora.io/media/new-10/Screen%20Shot%202021-04-05%20at%2023.08.37.png) | ![Screen Shot 2021-04-05 at 23.20.31](https://support.typora.io/media/new-10/Screen%20Shot%202021-04-05%20at%2023.20.31.png) |

### Flowchart Curve

Add `--mermaid-flowchart-curve: basis` to get other type of curves.

| –mermaid-flowchart-curve: linear;                            | –mermaid-flowchart-curve: basis                              | –mermaid-flowchart-curve: natural;                           | –mermaid-flowchart-curve: step;                              |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| ![Screen Shot 2021-04-05 at 23.25.41](https://support.typora.io/media/new-10/Screen%20Shot%202021-04-05%20at%2023.25.41.png) | ![Screen Shot 2021-04-05 at 23.30.11](https://support.typora.io/media/new-10/Screen%20Shot%202021-04-05%20at%2023.30.11.png) | ![Screen Shot 2021-04-05 at 23.28.06](https://support.typora.io/media/new-10/Screen%20Shot%202021-04-05%20at%2023.28.06.png) | ![Screen Shot 2021-04-05 at 23.28.52](https://support.typora.io/media/new-10/Screen%20Shot%202021-04-05%20at%2023.28.52.png) |

### Gantt Padding

| –mermaid–gantt-left-padding:75                               | –mermaid–gantt-left-padding:200                              |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| ![Screen Shot 2021-04-05 at 23.33.31](https://support.typora.io/media/new-10/Screen%20Shot%202021-04-05%20at%2023.33.31.png) | ![Screen Shot 2021-04-05 at 23.33.00](https://support.typora.io/media/new-10/Screen%20Shot%202021-04-05%20at%2023.33.00.png) |

hosted on [Github](https://github.com/typora/wiki-website).

<iframe id="_atssh5" title="AddThis utility frame" src="https://s7.addthis.com/static/sh.f48a1a04fe8dbf021b4cda1d.html#rand=0.5220032811364911&amp;iit=1620462178776&amp;tmr=load%3D1620462178743%26core%3D1620462178770%26main%3D1620462178773%26ifr%3D1620462178779&amp;cb=0&amp;cdn=0&amp;md=0&amp;kw=&amp;ab=-&amp;dh=support.typora.io&amp;dr=&amp;du=https%3A%2F%2Fsupport.typora.io%2FDraw-Diagrams-With-Markdown%2F&amp;href=https%3A%2F%2Fsupport.typora.io%2FDraw-Diagrams-With-Markdown%2F&amp;dt=Draw%20Diagrams%20With%20Markdown&amp;dbg=0&amp;cap=tc%3D0%26ab%3D0&amp;inst=1&amp;jsl=0&amp;prod=undefined&amp;lng=zh-tw&amp;ogt=image%2Cdescription%2Ctitle%2Curl&amp;pc=men&amp;pub=ra-5ed23a5bcf8c017f&amp;ssl=1&amp;sid=60964a62e46e20cf&amp;srf=0.01&amp;ver=300&amp;xck=0&amp;xtr=0&amp;og=url%3D%252FDraw-Diagrams-With-Markdown%252F%26title%3DDraw%2520Diagrams%2520With%2520Markdown%26description%3DSequence%2520Diagrams%2520Sequence%2520Diagrams%2520Options%2520Flowcharts%2520Mermaid%2520Sequence%2520Diagrams%2520Flowcharts%2520Gantt%2520Charts%2520Class%2520Diagrams%2520State%2520Diagrams%2520Pie%2520Charts%2520Mermaid%2520Options%2520Overview%2520Mermaid%2520Theme%2520Auto%2520Numbering%2520Flowchart%2520Curve%2520Gantt%2520Padding%2520Typora%2520supports%2520some%2520Markdown%2520extensions%2520for%2520diagrams%252C%2520once%2520they%2520are%2520enabled%2520from%2520preference%2520panel.%2520When%2520exporting%2520as%2520HTML%252C%2520PDF%252C%2520epub%252C%2520docx%252C%2520those%2520rendered%2520diagrams%2520will%2520also%2520be%2520included%252C%2520but%2520diagrams%2520features%2520are%2520not%2520supported%2520when%2520exporting%2520markdown%2520into%2520other%2520file%2520formats%2520in%2520current%2520version.%2520Besides%252C%2520you%2520should%2520also%2520notice%2520that%2520diagrams%2520is%2520not%2520supported%2520by%2520standard%2520Markdown%252C%2520CommonMark%2520or%2520GFM.%2520Therefore%252C%2520we%2520still%2520recommend%2520you%2520to%2520insert%2520an%2520image%2520of%2520these...%26image%3Dhttp%253A%252F%252Ftypora.io%252Fimg%252Ftwitter-sum.png&amp;csi=undefined&amp;rev=v8.28.8-wp&amp;ct=1&amp;xld=1&amp;xd=1" style="height: 1px; width: 1px; position: absolute; top: 0px; z-index: 100000; border: 0px; left: 0px;"></iframe>