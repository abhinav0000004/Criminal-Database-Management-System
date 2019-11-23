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
Create the PersonGroup

# Create empty Person Group. Person Group ID must be lower case, alphanumeric, and/or with '-', '_'.
print('Person group:', PERSON_GROUP_ID)
face_client.person_group.create(person_group_id=PERSON_GROUP_ID, name=PERSON_GROUP_ID)
'''

# Define hardik
hardik = face_client.person_group_person.create(PERSON_GROUP_ID, "Hardik Jaroli")
# Define abhi
abhi = face_client.person_group_person.create(PERSON_GROUP_ID, "Abhinav Chaudary")
# Define gopal
gopal = face_client.person_group_person.create(PERSON_GROUP_ID, "Gopal Gupta")
# </snippet_persongroup_create>

# <snippet_persongroup_assign>


'''
Detect faces and register to correct person
'''
# Find all jpeg images of friends in working directory
hardik_images = [file for file in glob.glob('*.jpg') if file.startswith("hardik")]
abhi_images = [file for file in glob.glob('*.jpg') if file.startswith("abhi")]
gopal_images = [file for file in glob.glob('*.jpg') if file.startswith("gopal")]

# Add to a hardik person
for image in hardik_images:
    w = open(image, 'r+b')
    face_client.person_group_person.add_face_from_stream(PERSON_GROUP_ID, hardik.person_id, w)

# Add to a abhi person
for image in abhi_images:
    m = open(image, 'r+b')
    face_client.person_group_person.add_face_from_stream(PERSON_GROUP_ID, abhi.person_id, m)

# Add to a gopal person
for image in gopal_images:
    ch = open(image, 'r+b')
    face_client.person_group_person.add_face_from_stream(PERSON_GROUP_ID, gopal.person_id, ch)
# </snippet_persongroup_assign>

# <snippet_persongroup_train>

dictn = {"Hardik Jaroli":hardik.person_id,"Abhinav Chaudary":abhi.person_id,"Gopal Gupta":gopal.person_id}
print(dictn)


'''
Train PersonGroup
'''
print()
print('Training the person group...')
# Train the person group
face_client.person_group.train(PERSON_GROUP_ID)

while (True):
    training_status = face_client.person_group.get_training_status(PERSON_GROUP_ID)
    print("Training status: {}.".format(training_status.status))
    print()
    if (training_status.status is TrainingStatusType.succeeded):
        break
    elif (training_status.status is TrainingStatusType.failed):
        sys.exit('Training the person group has failed.')
    time.sleep(5)
# </snippet_persongroup_train>

# <snippet_identify_testimage>






