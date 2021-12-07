from flask import url_for
from jinja2.utils import urlize
from flask_login import current_user

from flaskr.utils.template_filters import replace_newline

def make_message_format(user, messages):
    message_tag = ''
    for message in messages:
        message_tag += '<div class="speech-bubble-dest col-md-7 mb-3 offset-md-4 py-2 col-8 offset-2">'
        for splitted_message in replace_newline(message.message):
            message_tag += f'<p>{ urlize(splitted_message) }</p>'
        message_tag += '''
        </div>
        <div class="col-md-1 col-2 d-flex flex-column justify-content-center">
        '''
        if user.picture_path:
            message_tag += f'<img \
                src="{ url_for("static", filename=user.picture_path) }" \
                alt="" \
                class="img-fluid">'
        message_tag += f'''
            <p>{ user.username }</p>
        </div>
        '''
    return message_tag

def make_old_message_format(user, messages):
    message_tag = ''
    for message in messages[::-1]:
        if message.from_user_id == int(current_user.get_id()):
            message_tag += '<div class="col-md-1 col-3 d-flex flex-column justify-content-center">'
            if current_user.picture_path:
                message_tag += f'<img \
                src={ url_for("static", filename=current_user.picture_path) } \
                alt="" \
                class="img-fluid">'
            message_tag += f'<p class="text-center">{ current_user.username }</p>'
            message_tag += '</div>'
            message_tag += '<div class="speech-bubble-self col-md-7 mb-3 py-2 col-7">'
            for splitted_message in replace_newline(message.message):
                message_tag += f'<p>{urlize(splitted_message)}</p>'
            message_tag += '</div>'
            message_tag += f'<div id="self-message-tag-{ message.id }" class="col-md-1 col-2 d-flex align-items-end">'
            if message.is_checked:
                message_tag += '<p class="small">既読</p>'
            message_tag += '</div>'
            message_tag += '<div class="col-md-3"></div>'
        else:
            message_tag += '<div class="speech-bubble-dest col-md-7 mb-3 offset-md-4 py-2 col-8 offset-2">'
            for splitted_message in replace_newline(message.message):
                message_tag += f'<p>{ urlize(splitted_message) }</p>'
            message_tag += '''
            </div>
            <div class="col-md-1 col-2 d-flex flex-column justify-content-center">
            '''
            if user.picture_path:
                message_tag += f'<img \
                    src="{ url_for("static", filename=user.picture_path) }" \
                    alt="" \
                    class="img-fluid">'
            message_tag += f'''
                <p>{ user.username }</p>
            </div>
            '''
    return message_tag
