---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

{% include base_path %}

See below for list of publications sorted on the type of venue where the work has been published. If
you have any questions do not hesitate to contact me.

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
