---
layout: archive
title: "Awards"
permalink: /awards/
author_profile: true
---

{% include base_path %}

I"m very grateful to have received the following rewards:

{% for award in site.awards %}
    {% include slim-award.html %}
{% endfor %}

