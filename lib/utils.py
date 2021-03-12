import uuid
from django.utils.http import int_to_base36

LENGTH_OF_ID = 24

# generate unique ids of length 12
def gen_uuid() -> str:
  return int_to_base36(uuid.uuid4().int)[:LENGTH_OF_ID]