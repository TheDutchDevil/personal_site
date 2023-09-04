---
layout: archive
title: "Recognition"
permalink: /recognition/
author_profile: true
---

{% include base_path %}

I'm very grateful to have received the following recognition for my work:

{% for award in site.awards %}
    {% include slim-award.html %}
{% endfor %}

