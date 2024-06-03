from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model

# Retrieve the User model
User = get_user_model()

class EmailBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        """
        Authenticate a user based on email and password.
        
        Args:
            request: The HttpRequest object.
            email: The email of the user trying to authenticate.
            password: The password of the user trying to authenticate.
            kwargs: Additional keyword arguments.
        
        Returns:
            The authenticated user object if authentication is successful, otherwise None.
        """
        if email is None or password is None:
            return None
        try:
            # Try to retrieve the user by email
            user = User.objects.get(email=email)
            # Check the password
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            # Return None if the user does not exist
            return None

    def get_user(self, user_id):
        """
        Retrieve a user by their ID.
        
        Args:
            user_id: The ID of the user to retrieve.
        
        Returns:
            The User object if found, otherwise None.
        """
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
