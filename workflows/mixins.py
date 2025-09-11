from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect
from django.contrib import messages

class ProjectManagerRequiredMixin(AccessMixin):

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or request.user.position.name != "project_manager":
            messages.error(request, "Tylko project manager ma dostęp do tej strony.")
            return redirect("workflows:home-view")
        return super().dispatch(request, *args, **kwargs)