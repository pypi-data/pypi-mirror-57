# sitech-notifier
[![CircleCI](https://circleci.com/gh/sitmena/sitech-notifier.svg?style=svg&circle-token=0c83c133f3336982a42c563eb9a29ef21608bdb1)](https://circleci.com/gh/sitmena/sitech-notifier)

Official supported notification library for real-time, sms and email with notifications center.

---
### Requirements
* Python (3.6, 3.7, 3.8)
* Django (2.0, 2.1, 2.2, 3.0)
* Celery

### Installation

1. Install with `pip`:
   ```
   pip install git+https://github.com/sitmena/sitech-notifier.git
   ```
   If you want to enable real time notifications:
   ```
   pip install git+https://github.com/sitmena/sitech-notifier.git#egg=sitech_notifier[realtime]
   ```
   If needed to be installed in docker image, contact 
   [norbert@ulam.io](mailto:norbert@ulam.io) for docker deploy key and use docker 
   multi-stage builds to keep the key private.
   
   Details: https://vsupalov.com/build-docker-image-clone-private-repo-ssh-key/
2. Modify your `settings.py`:
   ```python
   INSTALLED_APPS = [
       ...,
       'sitech_notifier',
   ]
   ```
3. Run `python manage.py migrate`

---
## Basic Usage

### Setup

First, you have to set up delivery backends in your `settings.py`, for example:
```python
SITECH_NOTIFIER_DELIVERY_BACKENDS = [
    'sitech_notifier.delivery.backends.EmailDeliveryBackends',  # default
    'sitech_notifier.delivery.backends.PusherBackend',
    'your_app.backends.CustomDeliveryBackend'
]
```
For list of built-in delivery backends, go to [Delivery backends](#delivery-backends)

#### Custom delivery backend
Often you'll need custom delivery backend, for example for SMS notifications, or if you
want allow users to disable some delivery backends.

To create custom delivery backend, you can subclass `NotificationDeliveryBackend`.
Overriding `perform_send` is required, `notification_enabled` is optional.

Example:
```python
class ConcreteSMSBackend(BaseSMSDeliveryBackend):
    def notification_enabled(self, notification):
        return notification.user.profile.sms_notifications_enabled

    def perform_send(self, notification):
        mobile_number = notification.user.profile.mobile_number
        requests.post(SMS_GATEWAY_URL, {
            'api_key': SMS_GATEWAY_API_KEY,
            'mobile_number': mobile_number,
            'message': notification.full_body_text
        })
```

### Defining notifications
Suppose you want to create a notification  on a new comment on your blog post. First,
you have to define a subclass of `BaseNotification`:
```python
from sitech_notifier.core import BaseNotification

class BlogPostCommentNotification(BaseNotification):
    template_name = 'notifications/blog_post_comment.html'
    description = 'New comment on a blog post'
    notification_type = 'blog_post_comment'
```

Check all notification customization options in [notification factories](#notification-factories)

Then, create file `your_app/templates/notifications/blog_post_comment.html` with
such content:
```html
{% block subject %}New comment on a post blog{% endblock subject %}
{% block short_body %}
    There is a new comment on your blog post "{{ post.title }}".
{% endblock short_body %}
{% block text_body %}
    Hello, there is a new comment on your blog post "{{ post.title }}".
{% endblock text_body %}
{% block html_body %}
<h4>Hello,</h4>
<p>
There is a new comment on your blog post "{{ post.title }}".
</p>
{% endblock html_body %}
```

Then you have to define an event which will fire the notification, see [events](#events-app) 
for the details.

### Enabling Pusher notifications
You can also want to enable real-time notifications which would appear in application.

At first, you have to set up Pusher application (visit https://pusher.com)

Then you have to add `PusherDeliveryBackend` to `SITECH_NOTIFIER_DELIVERY_BACKENDS`
and configure your app settings
```python
SITECH_NOTIFIER_DELIVERY_BACKENDS = [
    ...,
    'sitech_notifier.delivery.backends.PusherDeliveryBackends',
]

PUSHER_APP_ID = 'app_id'
PUSHER_KEY = 'pusher_key'
PUSHER_SECRET = 'secret'
PUSHER_CLUSTER = 'if-other-than-default-us-east-1'
```

Then you have to edit your base template, for example `index.html`:
```html
{% load sitech_notifier %}
...
<script>
    const NOTIFICATION_CALLBACK = data => {
        alert(data.message)
    };
</script>
{% enable_pusher_notifications %}
```

`NOTIFICATION_CALLBACK` is JS function which is being called when notification
comes to the user's private channel. Here we used standard JS `alert`, but in practice
you will want to use more advanced JS notification like [toastr](https://github.com/CodeSeven/toastr):
```javascript
toastr.info(data.message, "", {
    onclick: function() {
      window.location = data.link;
    }
});
```

## Documentation

### Models

 #### AbstractNotification
 Source: `sitech_notifier.models.AbstractNotification`
   
 Base model for notifications, subclass
 this if you need any custom fields and extra data.
 
 **Fields**:
 * `user` - `settings.AUTH_USER_MODEL` foreign key, recipient of the notification
 * `subject` - notification subject, used for email notifications
 * `short_body` - short message of the notification, can be used for real-time in-app
 notifications or inbox page
 * `full_body_txt` - *(optional)* long notification body in plain text. Mainly used for email 
 notifications
 * `full_body_html` - *(optional)* long notification body in HTML. Mainly used for email
 notifications
 * `link` - *(optional)* URL to the resource related to the notification.  
 Example use: Notification on new blog post, include blog post URL in the notification
 * `is_new` - Boolean indicating if notification is new. `True` by default.
 
 #### Notification
 Source: `sitech_notifier.models.Notification`
 
 Subclass of `AbstractNotification` with `created_at`, `modified_at` fields and default
 ordering `(-created_at,)`. Use this model if you don't need any custom data.
 
 #### Custom notifications
 If you want to create custom notification model, subclass `AbstractNotification` 
 and add to `settings.py`:
 ```python
SITECH_NOTIFIER_NOTIFICATION_MODEL = 'your_app.CustomNotification'
```
 
### Notification factories
Notification factories are subclasses of `sitech_notifier.notifications.BaseNotification`
class. They are used to define specific notification in the application. Calling such
subclass creates a notification with all needed data and sends it with Celery
via configured delivery backends.

Notification signature: `SpecificNotification(user, event)`  
`user` and `event` are saved as attributes and accessible through `self`.
`Event` is an instance of `Event` model.

Notifications should not be called manually, process of sending the notifications
is handled by events. 
Notifications are sent by emitting an event which registered the notification as callback. See
[Events](#events-app) for the details.

Notification has to override following attributes:
* `template_name` - path to the template, see [notification templates](#notification-template)
* `description` - description what causes the notification, for example:
"New comment on a blog post"
* `get_context_from_event(event)` (static method) - get context from `Event` object.

If notification does not override these attributes and methods, it will be treated as abstract,
and therefore not be registered in `notification_types`

Optional attributes:
* `notification_type` - notification type code, for example: `new_blog_post`. Notification
type has to be unique, if not defined, it will evaluate to lowercased class name. If
notification of such type already exists, `DuplicateNotificationType` will be raised.

Methods (all optional):
* `get_notification_link(self)` -  get URL linked to the notification, for example:
`return kwargs['blog_post'].get_absolute_url()`


* `get_notification_language(self)` - get language in which notification should be
rendered, for example: `return self.user.profile.language`. Defaults to 
`settings.LANGUAGE_CODE`

* `transform_html_body(self, html_body)` - transform HTML body before sending,
override this if you want for example add CSS to your emails with library such as `premailer`

Helper functions:
* `sitech_notifier.notifications.get_notification_types()` - get all registered
notifications

* `sitech_notifier.notifications.get_notification_description(notification_type)` - get
description of a notification with given type

#### Notification template
Notification template has to look like this, blocks `subject` and `short_body`
are required.
```html
{% block subject %}{% endblock %}
{% block short_body %}{% endblock %}
{% block text_body %}{% endblock %}
{% block html_body %}{% endblock %}
```

### Delivery backends
Delivery backends are subclasses of `NotificationDeliveryBackend` abstract class with
overridden method `perform_send`.

#### Email backend
Source: `sitech_notifier.delivery.backends.EmailDeliveryBackend`

Sends notification to the user via email, `DEFAULT_FROM_EMAIL` setting is required.

#### SMS backend
Source: `sitech_notifier.delivery.backends.BaseSMSDeliveryBackend`

This backend does NOT work out of the box. It needs to be subclassed and `perform_send`
method must be provided.

[Example](#custom-delivery-backend)

#### Pusher delivery backend
Source: `sitech_notifier.delivery.backends.PusherDeliveryBackend`

Sends notification to the user's Pusher private channel, making it possible to enable
real time in-app notifications.

Library also supplies `enable_pusher_notifications` templatetag which should be included
in the base template. Before using the templatetag, JS function `NOTIFICATION_CALLBACK`
has to be defined.

Required settings:
 * `PUSHER_APP_ID`
 * `PUSHER_KEY`
 * `PUSHER_SECRET`

Optional settings:
 * `PUSHER_CLUSTER` - if other than default `us-east-1`
 * `PUSHER_OPTIONS` - other `kwargs` for `Pusher` instance
 
 Pusher docs: <https://pusher.com/docs/channels>
 
 ## Events
 
 `sitech-notifier` package also ships with events library, which can be used to simplify 
 the process of sending notifications. 
 
 ### Basic Usage
 
 #### Events
 
 Create `events.py` file in your app and define events:
 
To connect notification to the events, use `register_notification` decorator. Decorated function
should return a `User` or iterable of users.
 ```python
from sitech_notifier.core import BaseEvent

class NewBlogPost(BaseEvent):
    name = 'new-blog-post'

    @register_notification(NewBlogPostNotification)
    def notify_new_blog_post(self):
        post = self.target
        return post.blog.followers

    @register_notification(PostSubmittedNoification)
    def notify_post_submitted(self):
        post = self.target
        return post.author
```
Note that your notification has to override `get_context_from_event` static method.  
Example:
```python
class NewBlogPostNotification(BaseNotification):
    ...
    @staticmethod
    def get_context_from_event(event):
        return {
            'post': event.target
        }
```

Now, every time `NewBlogPost` is emitted, a notification is sent to all blog `followers`,
with `post=post` as a keyword argument.

#### Emitting events

Events can be emitted with two arguments:
  * `target` (required) - django `Model` instance which is the target of the self, for example
  when there is a new post on a blog, blog is the target
  * `actor` (optional) - django `User` (built-in or custom) instance who fired the 
  notification. Following the example, post author could be the actor, but it's
  possible to retrieve him directly from the target, so it can be skipped.
  
Events are emitted with following call:
```python
Event(target, actor=None).emit()
```

#### Side effects

Events can also handle actions which are not related to the notifications. For this purpose,
override `side_effects` static method of Event's class

```python
class CustomEvent(BaseEvent):
    @staticmethod
    def side_effects(self):
        some_side_effect(self)
```
