---
layout: publications-overview
title: "Publications"
permalink: /publications/
author_profile: true
---

{% include base_path %}

See below for list of publications sorted on the type of venue where the work has been published. If
you have any questions do not hesitate to contact me.

Journal papers
========
{% for post in site.publications reversed %}
  {% if post.type == "Journal" %}
    {% include slim-pub.html %}
  {% endif %}
{% endfor %}

Conference papers
========

{% for post in site.publications reversed %}
  {% if post.type == "Conference" %}
    {% include slim-pub.html %}
  {% endif %}
{% endfor %}

Thesis
=========
{% for post in site.publications reversed %}
  {% if post.type == "Thesis" %}
    {% include slim-pub.html %}
  {% endif %}
{% endfor %}

Workshop papers
======

{% for post in site.publications reversed %}
  {% if post.type == "Workshop" %}
    {% include slim-pub.html %}
  {% endif %}
{% endfor %}
