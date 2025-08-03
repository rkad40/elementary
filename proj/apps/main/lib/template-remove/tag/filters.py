from django import template
from django.template.defaultfilters import stringfilter
from django.conf import settings
from cronos import Time, epoch

register = template.Library()

MESSAGE = {
        'success': dict(label='SUCCESS', type='success',   img='site/img/message/success.png'),
        'error':   dict(label='ERROR',   type='danger',    img='site/img/message/error.png'),
        'warning': dict(label='WARNING', type='warning',   img='site/img/message/warning.png'),
        'info':    dict(label='NOTE',    type='info',      img='site/img/message/info.png'),
        'debug':   dict(label='NOTE',    type='secondary', img='site/img/message/debug.png'),
    }

@register.filter(name='alert')
@stringfilter
def alert(value, arg):
    r'''
    ## Description
    Defines an `alert` filter for use with template tags.  This filter is used convert message.tags into a label, 
    Bootstrap alert type and image.  Using the template syntax `{% for message in messages %}...{% endfor %}`, 
    `message.tags` will be one of "success", "error", "warning", "info" or "debug".  For example, if `message.tags` is
    "error":

    - `{{ message.tags|alert:'label' }}` = "ERROR" 
    - `{{ message.tags|alert:'type' }}` = "danger"
    - `{{ message.tags|alert:'img' }}` = "main/img/misc/error.png"
    
    Here is an example of how to use it:

    ```html
    {% load static %}
    {% load main_tags %}
    {% get_static_prefix as STATIC_PREFIX %}

    {% if messages %}
    <div class="flash messages" style="padding: 0;">
        {% for message in messages %}
        <div class="flash messages" style="padding: 0; margin: 0;">
            <div class="alert alert-{{ message.tags|alert:'type' }} alert-dismissible fade show" style="width: 100%; margin: 0 0 5px 0;" role="alert">
                <button type="button" class="close" data-dismiss="alert" aria-label="Close">
                    <span aria-hidden="true">&times;</span>
                </button>
                <img src="{{ STATIC_PREFIX }}{{ message.tags|alert:'img' }}" style="position: relative; left: -3px; top: -1px;}">
                <strong>{{ message.tags|alert:'label' }}</strong>: {{ message }}
            </div>
        </div>
        {% endfor %}
    </div>
    {% endif %}	
    ```
    '''
    if value not in MESSAGE: value = 'info'
    return MESSAGE[value][arg]

