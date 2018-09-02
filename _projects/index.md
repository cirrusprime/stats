---
layout: page
title: Index
permalink: /projects/index/
---
<ul>
    {% for item in site.projects %}
        {% if item.title != 'Index' %}
            <!-- <h2>{{ item.title }}</h2> -->
            <!-- <p>{{ item.description }}</p> -->
            <li><a href="{{ item.url }}">{{ item.title }}</a></li>
        {% endif %}
    {% endfor %}
</ul>