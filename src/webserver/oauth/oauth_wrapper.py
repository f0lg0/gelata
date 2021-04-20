from authlib.integrations.flask_client import OAuth
import os


class OAuthWrapper:
    def __init__(self, flask_app):
        self.oauth = OAuth(flask_app)
        self.google = self.oauth.register(
            name="google",
            client_id=os.getenv("GOOGLE_CLIENT_ID"),
            client_secret=os.getenv("GOOGLE_CLIENT_SECRET"),
            access_token_url='https://accounts.google.com/o/oauth2/token',
            access_token_params=None,
            authorize_url='https://accounts.google.com/o/oauth2/auth',
            authorize_params=None,
            api_base_url='https://www.googleapis.com/oauth2/v1/',
            # This is only needed if using openId to fetch user info
            userinfo_endpoint='https://openidconnect.googleapis.com/v1/userinfo',
            client_kwargs={'scope': 'openid email profile'},
        )

    def get_auth_object(self):
        return [self.oauth, self.google]
