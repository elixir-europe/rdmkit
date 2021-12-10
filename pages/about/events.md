---
title: Events
sidebar: about
---


<div class="events upcoming-events">
    <h2 class="mt-5">Upcoming events</h2>
    {%- assign events = site.data.events %}
    <ul class="list-unstyled mt-3">
        {%- for event in events %}
        <li class='upcoming-event' data-start='{{ event.startDate}}'>
          <span class="title mb-1">{{ event.name | escape }}</span>
          <p class="text-muted mb-0"><i class="far fa-calendar me-2"></i><time datetime="{{ event.startDate | date: '%e %B, %Y %H:%M' }}">{{ event.startDate | date_to_long_string }} {{event.startTime}}</time>
          {% if event.endDate or event.endTime %} - <time datetime="{{ event.endDate | date: '%e %B, %Y %H:%M %Z' }}">{{ event.endDate | date_to_long_string }} {{event.endTime}}</time>{% endif %}</p> 
          {%- if event.location %}
          <p class="text-muted mb-0"><i class="fas fa-map-marker-alt me-2"></i>{{ event.location }}</p> 
          {%- endif %}
          {%- if event.description %}
          <p class="text-muted">{{ event.description }}</p>
          {%- endif %}
        </li>
        {%- endfor %}
    </ul>
</div>

<div class="events past-events">
    <h2 class="mt-5">Past events</h2>
    {%- assign events = site.data.events %}
    <ul class="list-unstyled mt-3">
        {%- for event in events %}
        <li class='past-event' data-start='{{ event.startDate}}'>
          <span class="title mb-1">{{ event.name | escape }}</span>
          <p class="text-muted mb-0"><i class="far fa-calendar me-2"></i><time datetime="{{ event.startDate | date: '%e %B, %Y %H:%M' }}">{{ event.startDate | date_to_long_string }} {{event.startTime}}</time>
          {% if event.endDate or event.endTime %} - <time datetime="{{ event.endDate | date: '%e %B, %Y %H:%M %Z' }}">{{ event.endDate | date_to_long_string }} {{event.endTime}}</time>{% endif %}</p> 
          {%- if event.location %}
          <p class="text-muted mb-0"><i class="fas fa-map-marker-alt me-2"></i>{{ event.location }}</p> 
          {%- endif %}
          {%- if event.description %}
          <p class="text-muted">{{ event.description }}</p>
          {%- endif %}
        </li>
        {%- endfor %}
    </ul>
</div>
<script>
  $(document).ready(function() {
    showPastEvents();
    showUpcomingEvents();
  });
</script>

