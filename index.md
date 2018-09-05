---
layout: page
title: Stats-y stuffs galore
---
I'm attempting to get as much statistical stuff in here as possible, in an easily-comprehensible format for my own reference (as and when I inevitably forget something simple but necessary).  And ideally it might be useful to someone else out there with similar needs.  We shall see.

The main textbook I'm working through at the moment is Andy Field's *Discovering statistics with...*.  I have both the R and SPSS versions, but am aiming to use R (because freeee) as much as possible.  So I'm grabbing key phrases and the shiniest, most important points from there to squidge in here.

<div>
{% assign collections_list = site.collections | where: "label", "collections_list" | first %}
{% for collection in site.collections %}
    <h2><a href="{{ collection.url }}">{{ collection.label | capitalize }}</a></h2>
{% endfor %}
</div>
<!-- <a class="sidebar-nav-item{% if page.url == node.url %} active{% endif %}" href="{{ site.baseurl }}{{ node.url  | remove_first: '/' }}/index/">{{ node.title }}</a> -->
