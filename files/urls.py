from django.urls import re_path

from files.views import AttachmentCreateView, AttachmentDeleteView, \
    AttachmentDetailView, AttachmentDownloadView, AttachmentEditView

urlpatterns = [
    re_path(r"^add/$", view=AttachmentCreateView.as_view(), name="add-attachment"),
    re_path(r"^view/(?P<slug>[-\w]+)/$", view=AttachmentDetailView.as_view(), name="view-attachment"),
    re_path(r"^edit/(?P<slug>[-\w]+)/$", view=AttachmentEditView.as_view(), name="edit-attachment"),
    re_path(r"^delete/(?P<slug>[-\w]+)/$", view=AttachmentDeleteView.as_view(), name="delete-attachment"),
    re_path(r"^download/(?P<slug>[-\w]+)/$", view=AttachmentDownloadView.as_view(), name="download-attachment"),
]
