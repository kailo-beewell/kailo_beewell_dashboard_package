# CSS

The dashboards are customised using CSS. This page explains some of the basics about HTML and CSS, and provides a glossary to some of the elements used for the dashboard.

## What is HTML?

HTML is the standard language for webpages.

Content is structured in elements. Elements have a start tag, content, and end tag. Example: `<p>This is a paragraph element.</p>`

All elements can have attributes. These are specified in the start tag and are structured as name='value'. Example: `<p style='color:red;'>This is a red paragraph.</p>`

## What is CSS?

CSS is a style sheet language used to format HTML documents.
It controls the layout, appearance and style of multiple HTML elements at once.
It allows for seperation of content (HTML) and style (CSS) of webpages.

There are three ways to add CSS to a HTML document:
* Inline - inside element - e.g. `<h1 style='color:blue;'>A Blue Heading</h1>`
* Internal - in head section - e.g. `<style> body {color: red;} </style>`
* External - in .css file, linked to in head section

## Glossary

### Elements

* h1 h2 h3 h4 h5 h6 (e.g. `<h1></h1>`) = creates headlines
* p (`<p></p>`) = creates a paragraph
* div (`<div></div>`) = used to format block content
* ul (`<ul></ul>`) = creates an unordered list
* li (`<li></li>`) = encompasses each item in a list
* label (`<label></label>`) = used to define a label for an `<input>` element
* details (`<details></details>`) = creates disclosure widget where information is  only visible when widgit is "open"
* summary (`<summary></summary>`) = label for details widgit
* span (`<span></span>`) = used to group elements for styling purposes

### Attributes and other code

* `class` = class of HTML elements, multiple elements can have the same class
* `data-*` = allows us to store extra information on HTML elements 
* `data-testid` = custom attribute added to HTML elements to identify them for testing purposes
* `data-baseweb` = might be utilising frontend framework/library like BaseWeb (which is a UI framework for React)
* `role` = describes role of element (e.g. 'option' role identifies selectable choices of a listbox)
* `first-child` = first element in a group of sibling elements - i.e. first element immediately inside another element
* `!important` = declaration that overrides any other conflicting files
* `rem` = root em, a unit of measurement representing the font size of the root element, and 1rem is 1*font size (e.g. if font size is 16px, then 16px)
* `calc()` = perform calculation when specifying a value
* `@media` = media query, apply style based on characteristics of device or screen (e.g. it's width or height)