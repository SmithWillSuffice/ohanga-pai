## Inserting Images

1. Make a PNG copy, tick it in `HUGO_ROOT/static/images/`
2. Write a html shortcode for it in `HUGO_ROOT/layou/shortcodes/`
3. Use a nice scale in the <img> tag, like 600px wide, retian the aspect ratio. See the existing examples.
4. In your markdown file use the syntax:
```
{{< Foo >}}
```
where "Foo" is the basename of the shortcode file, it'd be "foo.html".
