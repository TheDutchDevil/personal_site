---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

Conferences
========

{% for post in site.publications reversed %}
  {% if post.type == "Conference" %}
    {% include archive-single.html %}
  {% endif %}
{% endfor %}

Workshops
======

{% for post in site.publications reversed %}
  {% if post.type == "Workshop" %}
    {% include archive-single.html %}
  {% endif %}
{% endfor %}
