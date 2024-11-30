---
title: Beom-Jun Kim
layout: post
categories: [Typography, Markdown]
image: /assets/img/rose.jpg
description: "Welcome to Beom-Jun Kim page."
---
## Topic

There are a few things I've been thinking about lately.

- **1. Is CI/CD really necessary?**  
Don’t get me wrong, I think I need it too.  
CI? It really need for version control, efficient development, quick feedback, etc.
CD also need. But what if the distribution target is not clear? Well, isn’t it meaningless in that situation to begin with?

- **1-2. Even if the project is a Python project?**  
I think this is a little ambiguous. Deploying a Python script rather than a container?  
Unless there are a very large number of distribution targets, I think there is no need to use it. 

- **2. Is Kubernetes really useful?**  
It's user friendly. Easy version management, auto clustering, etc.
However, since it is a bit more convenient than Docker but is a lot heavier, it seems necessary to review its use.

## About me
I am just an ordinary passerby with some experience in setting up background environments.  
It's called engineering, but it might need more accounting. Don't come.  
The three things mentioned above? Honestly, if you can afford it, it's all good, but if the scale becomes even a little bigger, it becomes expensive. You have to be mindful of performance and cost. 

LOL I'm about to run away.  
Just kidding :)


  
  
Reference: [GitHub flavored Markdown](https://help.github.com/en/github/writing-on-github).

* random line to make it work. This will be removed.
{:toc}



## Styling text
**bold**
{% highlight markdown %}
**bold**
{% endhighlight %}

*italic*
{% highlight markdown %}
 *italic*
{% endhighlight %}

~~strikethrough~~
{% highlight markdown %}
~~strikethrough~~
{% endhighlight %}

***bold and italic***
{% highlight markdown %}
***bold and italic***
{% endhighlight %}

## Quotes
>This is a quote
{% highlight markdown %}
>This is a quote
{% endhighlight %}

>This is a quote with author  
><cite><a href="#">The author</a></cite>

{% highlight markdown %}
>This is a quote with author  
><cite><a href="#">The author</a></cite>
{% endhighlight %}

## Links
Theme designed by [Alessio Franceschi](https://alessiofranceschi.me).
{% highlight markdown %}
Theme designed by [Alessio Franceschi](https://alessiofranceschi.me).
{% endhighlight %}

Links can also be relative. [Like this one](/contact.html).
{% highlight markdown %}
Links can also be relative. [Like this one](/contact.html).
{% endhighlight %}

## Lists
Unordered:
- this
- is
- unordered
{% highlight markdown %}
- this
- is
- unordered
{% endhighlight %}  

Ordered:
1. but
2. this
3. is
4. ordered
{% highlight markdown %}
1. but
2. this
3. is
4. ordered
{% endhighlight %}  

Nested:
1. First point
    - but also this
    - and also this
        - and this one too
2. Second point
{% highlight markdown %}
1. First point
    - but also this
    - and also this
        - and this one too
2. Second point
{% endhighlight %}  


## Task Lists
- [x] Write some CSS 
- [ ] Fix bugs
- [ ] Add related posts
{% highlight markdown %}
- [x] Write some CSS 
- [ ] Fix bugs
- [ ] Add related posts
{% endhighlight %}  

## Syntax Highlighting
[Read here](/2020/05/19/special-formatting.html#code-highlight).

## MathJAX and LaTeX
[Read here](/2020/05/19/special-formatting.html#mathjax-and-latex).

## Alerts
[Read here](/2020/05/19/special-formatting.html#alerts).

## Table of Contents
[Read here](/2020/05/19/special-formatting.html#table-of-contents).

## Headings

# The largest heading
## The second largest heading
###### The smallest heading


{% highlight markdown %}
# The largest heading
## The second largest heading
###### The smallest heading
{% endhighlight %}
