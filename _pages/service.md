---
layout: service-overview
title: "Service"
permalink: /service/
author_profile: true
---

{% include base_path %}



Conferences 
========
{% for post in site.service reversed %}
  {% if post.type == "Conference Organization" %}
    {% include slim-pub.html %}
  {% endif %}
{% endfor %}

Program Committees
========

{% for post in site.service reversed %}
  {% if post.type == "Program Committee" %}
    {% include slim-pub.html %}
  {% endif %}
{% endfor %}
