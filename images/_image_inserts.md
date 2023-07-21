## Inserting Images

1. Make a PNG copy, tick it in `HUGO_ROOT/static/images/`
2. Write a html shortcode for it in `HUGO_ROOT/layout/shortcodes/`
3. Use a nice scale in the <img> tag, like 600px wide, retain the aspect ratio. See the existing examples.
4. In your markdown file use the syntax:
```
{{< Foo >}}
```
where "Foo" is the basename of the shortcode file, it'd be "foo.html".


## Links to PDF

You can stick them under the post folder, or ../static/pdf/ but I couldn't get it working.

So instead, put the PDF in the pages folder,
```
cp ~/LaTeX/Economics/Mosler_1998_fullemployment.pdf content/questions/pdf/
```
The in the post `foo.md`:
```
[Mosler 1998](../pdf/Mosler_1998_fullemployment.pdf)
```
