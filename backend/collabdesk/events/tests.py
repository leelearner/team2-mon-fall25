import uuid
import datetime

from django.utils import timezone
from django.test import TestCase
from .models import Event
from workspaces.models import Workspace
from django.contrib.auth import get_user_model

def createEvent(title, description, start_time, end_time, 
                  event_type, location, created_by, workspace_id, created_at, updated_at):
    e_uuid = uuid.uuid4()
    event = Event.objects.create(
        event_id = e_uuid,
        title = title,
        description = description,
        start_time = start_time,
        end_time = end_time,
        event_type = event_type,
        location = location,
        created_by = created_by,
        workspace_id = workspace_id,
        created_at = created_at,
        updated_at = updated_at,
    )

    return event
    
class EventModelTests(TestCase):
    def test_create_event_and_str_method(self):
        
        User = get_user_model()
        user = User.objects.create()

        workspace = Workspace.objects.create(
            name="CollabDesk Workspace",
            description="Main workspace for CollabDesk project",
            created_by = user,
        )
        created_at = timezone.now()
        updated_at = created_at
        start_time = created_at + datetime.timedelta(hours=1)
        end_time = start_time + datetime.timedelta(hours=1)
        event_type = "GROUP"
        location = "School"
        event = createEvent(
            title="Meeting",
            description="Zoom Meeting",
            start_time=start_time,
            end_time=end_time,
            event_type=event_type,
            location=location,
            created_by=user,
            workspace_id=workspace,
            created_at=created_at,
            updated_at=updated_at,
        )

        self.assertEqual(str(event), event.title)

class BasicTestCase(TestCase):
    """A simple sanity check to verify test setup."""

    def test_addition(self):
        print("Running basic test case for Events...")
        self.assertEqual(1 + 1, 2)
