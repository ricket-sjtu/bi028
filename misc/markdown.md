# This is the title

![An image link](http://mouapp.com/Mou_128.png)

## This is the second-level title

Besides **Bold Text**,  we can also use *italic text* to emphasize the text.

### This is the third-level title

#### Strong and Emphasize

**strong** or __strong__
*emphasize* or _emphasize_

**Sometimes, I want a lot of text to be bold.
Like, seriously, a _LOT_ of text**

#### Blockquotes
> Right angle brackets $>$ are used for block quotes.

#### Links and Email

An email <example@example.com> link.

Simple inline link <http://chemluois.com>, another inline link 
[Smaller](http://smallerapp.com), one more inline link with title
[Resize](http://resizesafari.com "a Safari extension").

A [reference style][id] link. Input id, then anywhere in the doc,
define the link with corresponding id:

[id]:http://mouapp.com "Markdown editor on Mac OS X"

### Code
We can use backquote to enclose the inline code: `printf("%12d", x);`.

Or we can use triple backquote to enclose the multiple line code:
```python
def function():
	return
```

### Equations

For inline equation, use a pair of dollars to enclose the equation:
$c^2 = a^2 + b^2$.

For a large equation, use a pair of double dollars to enclose the equation:
$$
f(x) = \frac{1}{\sqrt{2\pi} \sigma} e^{\frac{-(x-\mu)^2}{\sigma}}
$$ 

Titles ( or called tool tips ) in the links are optional.

#### Images

An inline image ![Smaller icon](http://smallerapp.com/favicon.ico "Title here"), title is optional.

A ![Resize icon][2] reference style image.

[2]: http://resizesafari.com/favicon.ico "Title"

#### Inline code and Block code

An inline code should be enclosed by a pair of backquotes.

`chmod u+x file` can change the executable permission for `file`.

While an block code should be enclosed by triple backquotes:

```bash
for i in `seq 10`; do
	echo $i
done
```
