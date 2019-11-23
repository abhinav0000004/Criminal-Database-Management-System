import asyncio, io, glob, os, sys, time, uuid, requests
from urllib.parse import urlparse
from io import BytesIO
from PIL import Image, ImageDraw
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.face.models import TrainingStatusType, Person, SnapshotObjectType, OperationStatusType


# Set the FACE_SUBSCRIPTION_KEY environment variable with your key as the value.
# This key will serve all examples in this document.
KEY = os.environ['COGNITIVE_SERVICE_KEY']

# Set the FACE_ENDPOINT environment variable with the endpoint from your Face service in Azure.
# This endpoint will be used in all examples in this quickstart.
ENDPOINT = os.environ['FACE_ENDPOINT']

# Used in the Person Group Operations,  Snapshot Operations, and Delete Person Group examples.
# You can call list_person_groups to print a list of preexisting PersonGroups.
# SOURCE_PERSON_GROUP_ID should be all lowercase and alphanumeric. For example, 'mygroupname' (dashes are OK).
PERSON_GROUP_ID = 'criminaldb'
# Used for the Snapshot and Delete Person Group examples.
#TARGET_PERSON_GROUP_ID = str(uuid.uuid4()) # assign a random ID (or name it anything)

'''
Authenticate
All examples use the same client, except for Snapshot Operations.
'''
# <snippet_auth>
# Create an authenticated FaceClient.
face_client = FaceClient(ENDPOINT, CognitiveServicesCredentials(KEY))
# </snippet_auth>
'''
END - Authenticate
'''

'''
Identify a face against a defined PersonGroup
'''

# Reference image for testing against
group_photo = 'test2.jpg'
IMAGES_FOLDER = os.path.join(os.path.dirname(os.path.realpath(__file__)))

# Get test image
test_image_array = glob.glob(os.path.join(IMAGES_FOLDER, group_photo))
image = open(test_image_array[0], 'r+b')

# Detect faces
face_ids = []
faces = face_client.face.detect_with_stream(image)
for face in faces:
    face_ids.append(face.face_id)
# </snippet_identify_testimage>

# <snippet_identify>
# Identify faces
results = face_client.face.identify(face_ids, PERSON_GROUP_ID)
print (results)
print('Identifying faces in {}')
if not results:
    print('No person identified in the person group for faces from the {}.'.format(os.path.basename(image.name)))
for person in results:
    print(person.candidates)
    if person.candidates:
        print('Person for face ID {} is identified in {} with a confidence of {}.'.format(person.face_id, os.path.basename(image.name), person.candidates[0])) # Get topmost confidence score
        
    else:
        print('No one identified in the person group for faces from the {}.'.format(os.path.basename(image.name)))
# </snippet_identify>
'''
END - Create/Train/Detect/Identify Person Group example
'''
